import discord
import datetime
import sys
import traceback

from discord.ext import commands
from discord import app_commands

class LeaveofAbsenceModal(discord.ui.Modal, title="Leave of Absence Form"):

    startdate = discord.ui.TextInput(
        label="What is the start of your leave of absence?",
        style=discord.TextStyle.short,
        placeholder="Enter the start date here...",
        required=True
    )

    enddate = discord.ui.TextInput(
        label="What is the end of your leave of absence?",
        style=discord.TextStyle.short,
        placeholder="Enter the estimated end date here...",
        required=True
    )

    reason = discord.ui.TextInput(
        label="What is the reason for your leave of absence?",
        style=discord.TextStyle.long,
        placeholder="Enter the reason here...",
        required=True
    )

    rank = discord.ui.TextInput(
        label="What is your current rank?",
        style=discord.TextStyle.short,
        placeholder="Enter your rank here...",
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        channel = self.bot.get_channel(1067586821116153886)
        embed = discord.Embed(
            title="Leave of Absence Request",
            colour=discord.Color.dark_blue()
        )
        embed.add_field(name="Start Date", value=self.startdate.value, inline=True)
        embed.add_field(name="Estimated End Date", value=self.enddate.value, inline=True)
        embed.add_field(name="Reason", value=self.reason.value, inline=False)
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)
        embed.set_footer(text=f"ID: {interaction.user.id}")
        embed.timestamp = datetime.datetime.now()
        await channel.send("<@997717072001900624>", embed=embed)
        await interaction.response.send_message(f"Your leave of absence has been submitted. You will be notified when it has been approved or denied.", ephemeral=True)
        pass

    async def on_error(self, error, interaction: discord.Interaction):
        await interaction.response.send_message(f"An error occurred while processing your leave of absence request. Please try again later.", ephemeral=True)
        print("Ignoring exception in modal {}:".format(self), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        pass

    pass

class EmployeeCog(commands.Cog, name="Employee Commands"):
    def __init__(self, bot):
        self.bot = bot

    group = app_commands.Group(name="loa", description="Leave of Absence Commands")

    @group.command(name="submit", description="Request a Leave of Absence")
    @app_commands.checks.has_role(997272837205282917)
    async def submit(self, interaction: discord.Interaction):
        await interaction.response.send_modal(LeaveofAbsenceModal())
        pass

    @group.command(name="approve", description="Approve a Leave of Absence")
    @app_commands.checks.has_role(997717072001900624)
    async def approve(self, interaction: discord.Interaction, member: discord.Member):
        await member.send(f"Hello {member.display_name},\n\nYour leave of absence has been approved. Please contact a member of command if you have any questions.\n\n*I am a bot contacting you on behalf of {interaction.user.mention}. Any responses sent here will not be delivered.*")
        await interaction.response.send_message(f"Leave of absence for {member.mention} has been approved.", ephemeral=True)
        pass

    @group.command(name="deny", description="Deny a Leave of Absence")
    @app_commands.checks.has_role(997717072001900624)
    async def deny(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        await member.send(f"Hello {member.display_name},\n\nYour leave of absence has been denied for the following reason:\n\n{reason}\n\nPlease contact a member of command if you have any questions.\n\n*I am a bot contacting you on behalf of {interaction.user.mention}. Any responses sent here will not be delivered.*")
        await interaction.response.send_message(f"Leave of absence for {member.mention} has been denied.", ephemeral=True)
        pass

    pass

async def setup(bot):
    await bot.add_cog(EmployeeCog(bot))