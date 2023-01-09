import discord
import datetime

from discord.ext import commands

class EventsCog(commands.Cog, name="Events Cog"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    #Listener for Events in specific channels

    pass

async def setup(bot):
    await bot.add_cog(EventsCog(bot))