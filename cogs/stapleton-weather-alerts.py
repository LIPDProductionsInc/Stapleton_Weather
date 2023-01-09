import discord
import datetime
import typing

from discord.ext import commands
from discord import app_commands
from typing import Literal

class WeatherAlertsCog(commands.Cog, name="Weather Alert Commands"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(name="issue", description="Issue a weather alert for the county")
    @commands.check_any(commands.is_owner(), commands.has_any_role(997257519347024002, 997257499340177578, 997256700232994938, 997256680616251563))
    @app_commands.describe(alert_type="The type of alert to issue", message="The message to send")
    async def issue(self, ctx, alert_type:Literal["Advisory", "Watch", "Warning"], message:str):
        channel = ctx.bot.get_channel(997711440867758170)
        log = ctx.bot.get_channel(1061871530201595904)
        if alert_type == "Advisory":
            embed = discord.Embed(
                title="Weather Advisory",
                colour=discord.Color(0xe1eb00),
                description=message
            )
            embed.set_footer(text=f"Stapleton County Weather Service | Issued by {ctx.author.name}", icon_url=ctx.author.avatar)
            embed.timestamp = datetime.datetime.utcnow()
            logembed = discord.Embed(
                colour=discord.Color.dark_orange(),
                description=f"**Issued by:** {ctx.author.mention}"
            )
            logembed.set_author(name="Weather Advisory Issued", icon_url=ctx.author.avatar)
            logembed.set_footer(text=f"ID: {ctx.author.id}")
            logembed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            await log.send(embed=logembed)
        elif alert_type == "Watch":
            embed = discord.Embed(
                title="Weather Watch",
                colour=discord.Color(0xe1eb00),
                description=message
            )
            embed.set_footer(text=f"Stapleton County Weather Service | Issued by {ctx.author.name}", icon_url=ctx.author.avatar)
            embed.timestamp = datetime.datetime.utcnow()
            logembed = discord.Embed(
                colour=discord.Color.dark_orange(),
                description=f"**Issued by:** {ctx.author.mention}"
            )
            logembed.set_author(name="Weather Watch Issued", icon_url=ctx.author.avatar)
            logembed.set_footer(text=f"ID: {ctx.author.id}")
            logembed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            await log.send(embed=logembed)
        elif alert_type == "Warning":
            embed = discord.Embed(
                title="Weather Warning",
                colour=discord.Color(0xff0000),
                description=message
            )
            embed.set_footer(text=f"Stapleton County Weather Service | Issued by {ctx.author.name}", icon_url=ctx.author.avatar)
            embed.timestamp = datetime.datetime.utcnow()
            logembed = discord.Embed(
                colour=discord.Color.dark_orange(),
                description=f"**Issued by:** {ctx.author.mention}"
            )
            logembed.set_author(name="Weather Warning Issued", icon_url=ctx.author.avatar)
            logembed.set_footer(text=f"ID: {ctx.author.id}")
            logembed.timestamp = datetime.datetime.now()
            await channel.send(embed=embed)
            await log.send(embed=logembed)
            pass
        pass

    pass

async def setup(bot):
    await bot.add_cog(WeatherAlertsCog(bot))