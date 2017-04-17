import os
import sys

from discord.ext.commands import Bot
from .config import Config


class DiceBot(Bot):
    config = Config()

    def __init__(self, *args, command_prefix='!',**kwargs):
        super().__init__(*args, command_prefix=command_prefix, **kwargs)

    def run(self, *args, **kwargs):
        super().run(self.config.BOT_TOKEN, *args, **kwargs)

    async def restart(self):
        """Restarts the bot. Used for debugging purposes."""
        await self.logout()
        os.system('python -m bfbot')
        sys.exit(0)
