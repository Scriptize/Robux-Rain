import hikari
import lightbulb


bot = lightbulb.BotApp(token='MTAwNjcxNzU1NzAwNjQwOTc4OQ.GpzEJD.U-nE7MFddrROwwRm1zZPXyq-NzeXmsEhlZnTF0', default_enabled_guilds=(1006722736074264677))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started')

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


@bot.command
@lightbulb.command('group','This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass
@my_group.child
@lightbulb.command('subcommand','This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand')

@bot.command
@lightbulb.option('num2','The second number',type=int)
@lightbulb.option('num1','The first number',type=int)
@lightbulb.command('add','Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

bot.run()