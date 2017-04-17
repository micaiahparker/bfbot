from .dicebot import DiceBot

bot = DiceBot(description="Rolls dice and kicks ass.")

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name} {bot.user.id}')

@bot.command(aliases=['reset'])
async def restart():
    await bot.say('Restarting...')
    await bot.restart()
