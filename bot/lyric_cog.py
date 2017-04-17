from discord.ext.commands import command
from .cog import Cog
from tswift import Song
from markovify import NewlineText

try:
    with open('all.txt', 'rt') as tmg:
        text = NewlineText(tmg.read(), state_size=2)
except FileNotFoundError:
    text = None

class Lyrics(Cog):
    @command(aliases=['lyrics', 'lyric'])
    async def get_lyrics(self, song_name):
        """only mountain goats songs, duh"""
        song = Song.find_song(song_name+" The mountain goats")
        if song:
            lyrics = f'```\n{song.title} - {song.artist}\n{song.lyrics}\n```'
            await self.bot.say(lyrics)
        else:
            await self.bot.reply("Sorry, couldn't find that song")

    @command(aliases=['sing'])
    async def make_lyric(self):
        """Generates Mountain Goats lyrics."""
        if text:
            await self.bot.say(text.make_sentence())
        else:
            await self.bot.say("No text file found for generation.")
