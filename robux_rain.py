import hikari
import lightbulb
import datetime
from datetime import timedelta
import time
import asyncio
import requests
import winners
from rblx_api import rbx_request, session


bot = lightbulb.BotApp(token='your token goes here',intents=hikari.Intents.DM_MESSAGES, default_enabled_guilds=(guild_id))


@bot.command()
@lightbulb.command('version', 'responds with current version')
@lightbulb.implements(lightbulb.SlashCommand)
async def version(ctx):
    await ctx.respond("Robux Rain version: 1.3 **ALPHA**")

@bot.command()
@lightbulb.option('amount','how much robux?',type=int, min_value= 1)
@lightbulb.option('time','how many minutes?',type=float, min_value= .5)
@lightbulb.option('cookie','enter your cookie',type=str)
@lightbulb.option('groupid','enter your groups ID',type=str)
@lightbulb.command('startrain', 'starts giveaway')
@lightbulb.implements(lightbulb.SlashCommand)
async def start_rain(message):

    #Prepare Unique Parameters (winner count, dm listening, prize pool, giveaway endtime)
    counter = 0 
    listen_list = []
    rbux_val = message.options.amount
    rain_end = datetime.datetime.now() + timedelta(minutes=message.options.time) 
    endtime_int = (message.options.time * 60)
    

    #Prep with API calls and convert json into {user, id} dict
    new_recipients = []
    payload = { 
    "PayoutType": "FixedAmount",
    "Recipients": []
              }
    
    session.cookies[".ROBLOSECURITY"] = message.options.cookie 
    auth_req = rbx_request("POST", "https://auth.roblox.com/") # authenticate roblox login with cookie
    member_req = rbx_request("GET", f"https://groups.roblox.com/v1/groups/{message.options.groupid}/users") # api call for members
    member_data = member_req.json() # turn request into json
    member_data.pop("nextPageCursor") #remove kv pairs for clean dict comphrehension
    member_data.pop("previousPageCursor")
    member_list = {item['user']['username'] : item['user']['userId'] for item in member_data['data']} # create user:id pairs
    member_names = {item['user']['username'] for item in member_data['data']} # users 
    group_req = rbx_request("GET", f"https://groups.roblox.com/v1/groups/{message.options.groupid}")
    group_info = group_req.json()



#Initialize Embed
    start_embed = hikari.Embed(title="💸 Enter the ROBUX rain! 💸",  
                        description="**RAIN AMOUNT:** " + str(rbux_val) +
                                 "\n**RAIN ENDS: **" + "<t:"+ str(int((time.mktime(rain_end.timetuple()))))+ ":R>" +
                                 "\n\nReact to enter the rain!",
                        color='#FFFF00'
    ) 
    start_embed.set_footer("ROBUX RAIN started by" + " " + message.author.username) 
    sent_embed = await message.respond(start_embed) 
    embed_msg = await sent_embed.message()
    await bot.rest.add_reaction(message.channel_id, embed_msg, "💰")
    await asyncio.sleep(endtime_int) # wait for the end of a timer(endtime_int)
    users = await bot.rest.fetch_reactions_for_emoji(message.channel_id, embed_msg, "💰") # collect users reactions to message object with moneybag emoji
    winner_list = [] 
    for user in users:
        if user.is_bot == False:
            winner_list.append(user.mention) # add mentions to the winner list
    winner_group = winners.split_prize_pool(rbux_val,winner_list) # split prize pool randomly among winners
    winner_dict = winners.dictize(winner_group) # turn winner prize pairs into dict
    window_end = datetime.datetime.now() + timedelta(seconds=45)
    end_embed = hikari.Embed(title="💸💸💸WINNERS!!!💸💸💸",
                             description=winner_group + "\n **Claim Window Ends In: ** <t:"+ str(int((time.mktime(window_end.timetuple()))))+ ":R>",
                             color="#4ef500"
    )
    end_embed.set_footer("CHECK YOUR DM FOR INSTUCTIONS")
    await message.respond(embed=end_embed,user_mentions=True) 
    for user in users: #loop thru users
        if user.is_bot == False:
            await user.send('Respond with your **ROBLOX USERNAME ONLY** ') #send dm to each user who reacted
            counter +=1 
            listen_list.append(user.id)
   
    
    #Listen for responses and add to payload for POST request
    @bot.listen(hikari.DMMessageCreateEvent)
    async def get_reply(event): # Listen for reply to dm
        nonlocal counter # make counter usable in nested function
        nonlocal new_recipients
        run = True

        if window_end < datetime.datetime.now(): # If timer already ran out
            await event.message.author.send("Sorry, claim window is closed")
            print("Done listening!")
            await message.respond("Giveaway Complete!")
            bot.unsubscribe(hikari.DMMessageCreateEvent, get_reply) # Stop listening for responses
            run = False

        if run:    
            if event.message.author.id in listen_list: # if author of message is a winner
                try:
                    new_recipients.append({'recipientId': member_list[event.message.content], # recip id is the value of the user key from the member list
                                            'recipientType': 'User',
                                            'amount': int(winner_dict[str(event.message.author.id)]) # reward amt is the value of the key that reps the replier disc id
                                            }) # add robux recipient to list to use to extend recipient payload
                    
                except KeyError:
                    await event.message.author.send("Username is spelled incorrectly. Try again.")
                    await event.message.author.send(f'Alternatively, if you **are not** in the group, **"{group_info["name"]}"** enter one of these users: \n {member_names}')

                else:
                    await event.message.author.send("Successfully recieved username!")
                    listen_list.remove(event.message.author.id) # remove them from winner list
                    counter -= 1
                    payload["Recipients"].extend(new_recipients) #Add winners to payload
                    payout = rbx_request("POST",f"https://groups.roblox.com/v1/groups/{message.options.groupid}/payouts",json=payload) #payout robux
                    if payout.status_code == 400:
                        await event.message.author.send("This user is ineligible for payout.")
                    else:
                        await event.message.author.send("Successfully paid out robux!")
                    new_recipients = []
                    payload["Recipients"] = []
                    

                if counter == 0 or window_end < datetime.datetime.now(): # If everyone responds or timer ran out
                    bot.unsubscribe(hikari.DMMessageCreateEvent, get_reply) # Stop listening for responses
                    await message.respond("Giveaway Complete!")

bot.run()
                

