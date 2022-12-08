import hikari
import lightbulb
import datetime
from datetime import timedelta
import time
import asyncio
from bot_config import bot


default_enabled_guilds=(1006722736074264677)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started')

@bot.listen(hikari.ReactionAddEvent) 
async def get_reaction_user(event):
    pass
    #if not event.is_for_emoji('U+1F4B0'):
        
@bot.command()
@lightbulb.option('cookie','enter your cookie',type=str)
@lightbulb.command('setcookie', 'sets roblox security cookie')
@lightbulb.implements(lightbulb.SlashCommand)
def set_cookie(ctx):
    cookie = ctx.options.cookie
    bot.rest.send(1006722737668104325,"Cookie Successfully Set!")
    return cookie


@bot.command()
@lightbulb.option('amount','how much robux?',type=int, min_value= 500)
@lightbulb.option('time','how many minutes?',type=int, min_value= 1)
@lightbulb.command('startrain', 'starts giveaway (make sure your cookie is set with /setcookie)')
@lightbulb.implements(lightbulb.SlashCommand)
async def start_rain(message):
    
    rbux_val= message.options.amount  # robux amount
    rain_start = datetime.datetime.now() # datetime start time
    rain_end = rain_start + timedelta(minutes=message.options.time) #datetime end time
    endtime_int = int(rain_end.strftime("%Y%m%d%H%M%S")) #end time in secs
    

#Initialize Embed
    embed = hikari.Embed(title="💸 Enter the ROBUX rain! 💸",  #initialize embed
                        description="**RAIN AMOUNT:** " + str(rbux_val) +
                                 "\n**RAIN ENDS: **" + "<t:"+ str(int((time.mktime(rain_end.timetuple()))))+ ":R>" +
                                 "\n\nReact to enter the rain!",
                        color='#FFFF00'
    ) 
                    
    embed.set_footer("ROBUX RAIN started by" + " " + message.author.username) # set footer

    sent_embed = await message.respond(embed) # message object

    embed_msg = await sent_embed.message()

    await asyncio.sleep(endtime_int) # wait for the end of a timer(endtime_int)

    users = await bot.rest.fetch_reactions_for_emoji(1006722737668104325, embed_msg, "💰") # collect users reactions to message object with moneybag emoji
    print(users)
    for user in users: #loop thru users
        await user.send('Thanks for reacting!') #send dm to each user who reacted

bot.run()

