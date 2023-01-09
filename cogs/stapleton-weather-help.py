import discord
import datetime

from discord.ext import commands
from datetime import timedelta

class HelpCog(commands.Cog, name="Help Cog"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="help")
    async def help(self, ctx, *, command: str = None):
        """Shows help about a command or the bot"""
        embed = discord.Embed(
            title="Help",
            description="Here is a list of commands you can use with Stapleton Weather.",
            color=discord.Color.dark_blue()
            )
        #if discord.utils.get(ctx.author.roles, id=646549329493884929):
        #    embed.add_field(name="Council Commands", value="`propose`, `legal-review`, `charter`, `template`, `documents`", inline=False)
        embed.add_field(name="Commands", value="`help`, `ping`, `serverinfo`, `userinfo`, `avatar`, `council`", inline=False)
        embed.add_field(name="Moderation", value="`ban`, `kick`, `unban`", inline=False)
        embed.set_footer(text=f"Stapleton Weather | Developed by {self.bot.owner}", icon_url=str(self.bot.user.avatar))
        await ctx.send(embed=embed)
        pass

    pass

async def setup(bot):
    await bot.add_cog(HelpCog(bot))