import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree
whitelisted_users = set()

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message_delete(message):
    if message.mentions and not message.author.bot and message.author.id not in whitelisted_users:
        for user in message.mentions:
            reply_ping = message.reference is not None

            embed = discord.Embed(
                title="Ghost Ping Alert",
                description=f"Author: {message.author.mention}\nContent: {message.content}",
                color=discord.Color.red()
            )
            embed.set_footer(text=f"Reply Ping = {reply_ping}")

            alert_message = await message.channel.send(f"{user.mention}", embed=embed)
            await alert_message.delete(delay=10)

@bot.event
async def on_message_edit(before, after):
    if before.mentions and not before.author.bot and before.author.id not in whitelisted_users:
        if not after.mentions:
            for user in before.mentions:
                reply_ping = before.reference is not None

                embed = discord.Embed(
                    title="Ghost Ping Alert",
                    description=f"Author: {before.author.mention}\nOriginal Content: {before.content}",
                    color=discord.Color.red()
                )
                embed.set_footer(text=f"Reply Ping = {reply_ping}")

                alert_message = await before.channel.send(f"{user.mention}", embed=embed)
                await alert_message.delete(delay=10)

@tree.command(name="whitelist", description="Adds or removes a user from the whitelist")
async def whitelist(interaction: discord.Interaction, action: str, user: discord.User):
    if action.lower() == "add":
        whitelisted_users.add(user.id)
        await interaction.response.send_message(f"{user.mention} has been whitelisted from ghost ping alerts.", ephemeral=True)
    elif action.lower() == "remove":
        whitelisted_users.discard(user.id)
        await interaction.response.send_message(f"{user.mention} has been removed from the whitelist.", ephemeral=True)
    else:
        await interaction.response.send_message("Invalid action. Use 'add' or 'remove'.", ephemeral=True)

bot.run(os.getenv("DISCORD_TOKEN"))
