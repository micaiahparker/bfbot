from .bot import bot
from .dice_cog import Dice
from .lyric_cog import Lyrics

bot.add_cog(Dice(bot))
bot.add_cog(Lyrics(bot))
bot.run()
