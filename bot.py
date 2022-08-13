import hikari

bot = hikari.GatewayBot(token='MTAwNjcxNzU1NzAwNjQwOTc4OQ.GpzEJD.U-nE7MFddrROwwRm1zZPXyq-NzeXmsEhlZnTF0')

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)
bot.run()