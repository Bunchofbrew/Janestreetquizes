import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

# Replace with your bot token (wrap it in quotes!)
TOKEN = "MTUwMTA4NDg1OTc4NjA2Nzk5OA.GjxWBV.qtMJ70oaY_l3GIBkjb0rQaE8YRt1ydE_Ased0E"

# Define intents
intents = discord.Intents.default()
intents.message_content = True   # Needed so the bot can read messages

bot = commands.Bot(command_prefix="!", intents=intents)

def get_latest_puzzle():
    url = "https://www.janestreet.com/puzzles/current-puzzle/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Extract puzzle title and description safely
    title_tag = soup.find("h1")
    content_tag = soup.find("div", class_="puzzle-content")

    title = title_tag.text.strip() if title_tag else "No title found"
    content = content_tag.text.strip() if content_tag else "No content found"

    return title, content, url

@bot.command(aliases=["quiz"])   # you can call !puzzle or !quiz
async def puzzle(ctx):
    title, content, link = get_latest_puzzle()
    await ctx.send(f"**{title}**\n{content}\nRead more: {link}")

# Archive command
@bot.command()
async def archive(ctx):
    archive_url = "https://www.janestreet.com/puzzles/archive/"
    await ctx.send(f"📚 Explore past puzzles here: {archive_url}")

# 2026 puzzle command
@bot.command(name="2026")
async def puzzle2026(ctx):
    puzzle_url = "https://www.janestreet.com/puzzles/sum-of-squares-index/"
    await ctx.send(f"🧮 2026 Puzzle: Sum of Squares Index\nRead more: {puzzle_url}")

# Simple ping command to test bot is alive
@bot.command()
async def ping(ctx):
    await ctx.send("Bot is online and ready!")

# Run the bot
bot.run(TOKEN)

