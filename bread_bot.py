import hikari
import lightbulb
import datetime
from datetime import timedelta
import time
 

bot = lightbulb.BotApp(token='MTAwNjcxNzU1NzAwNjQwOTc4OQ.GpzEJD.U-nE7MFddrROwwRm1zZPXyq-NzeXmsEhlZnTF0', default_enabled_guilds=(1006722736074264677))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started')


@bot.command
@lightbulb.option('amount','how much robux?',type=int, min_value= 500)
@lightbulb.option('time','how many minutes?',type=int, min_value= 2)
@lightbulb.command('startrain', 'starts giveaway')
@lightbulb.implements(lightbulb.SlashCommand)
async def print_embed(ctx):
    
    rbux_val= ctx.options.amount
    rain_start = datetime.datetime.now()
    rain_end = rain_start + timedelta(minutes=ctx.options.time)

#Initialize Embed
    embed = hikari.Embed(title="💸 Enter the ROBUX rain! 💸",
                        description="**RAIN AMOUNT:** " + str(rbux_val) +
                                 "\n**RAIN ENDS: **" + "<t:"+ str(int((time.mktime(rain_end.timetuple()))))+ ":R>" +
                                 "\n\nReact to enter the rain!,",
                        color='#FFFF00'
    ) 
                    
    embed.set_footer("ROBUX RAIN started by" + " " + ctx.author.username)
    await ctx.respond(embed)


#@bot.command
#@lightbulb.command('ping', 'Says pong!')
#@lightbulb.implements(lightbulb.SlashCommand)
#async def ping(ctx):
#    await ctx.respond('```Pong!```')



#@bot.command
#@lightbulb.option('num2','The second number',type=int)
#@lightbulb.option('num1','The first number',type=int)
#@lightbulb.command('add','Add two numbers together')
#@lightbulb.implements(lightbulb.SlashCommand)
#async def add(ctx):
#   await ctx.respond(ctx.options.num1 + ctx.options.num2)




bot.run()

