import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Load token dari file .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Inisialisasi bot dengan prefix "!"
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Event ketika bot sudah siap
@bot.event
async def on_ready():
    print(f'Bot {bot.user} sudah online!')

# Command !ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Command !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Halo, {ctx.author.mention}!")

# Menjalankan bot
bot.run(TOKEN)
