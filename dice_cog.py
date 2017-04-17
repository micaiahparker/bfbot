import random
import re
import operator

from discord.ext.commands import command
from .cog import Cog

dice_match = re.compile(r'(\d+)d(\d+)(\+|-|\*)?(\d+)?')

ops = {'*': operator.mul, '+': operator.add, '-': operator.sub}

class Dice(Cog):
    @command()
    async def roll(self, roll):
        rolls = dice_match.findall(roll)
        for times, size, op, bonus in rolls:
            result = self.roll_die(int(size), int(times))
            if op:
                result = ops[op](result, int(bonus))
            await self.bot.reply(f"{roll}: "+str(result))

    @command()
    async def hi(self):
        await self.bot.reply('hi')

    @command()
    async def stats(self):
        stats = {}
        for stat in ['Strength', 'Intelligence', 'Wisdom', 'Dexterity', 'Constitution', 'Charisma']:
            stats[stat] = self.stat_roll()
        reply = "Stats\n"
        for key, stat in stats.items():
            reply+=f'\t{key}: {stat}\n'
        await self.bot.reply(reply)

    @classmethod
    def stat_roll(cls):
        return sum(sorted([random.randint(1, 6) for _ in range(4)])[1:])

    @staticmethod
    def roll_die(size, times):
        return sum(random.randint(1, size) for _ in range(times))
