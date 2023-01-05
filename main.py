"""Import modules"""
import discord
import json
import requests

"""Define bot"""
bot = discord.Bot()


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.command(description = "Input Url")
async def url(ctx, url):
    response = requests.get(f"https://traffic1s.com/get-codes?hostname={url}", headers = {"Origin": f"https://{url}"})
    result = json.loads(response.text)
    await ctx.respond(result["html"])

@bot.command(description = "Help")
async def help(ctx):
    await ctx.respond(file = discord.File("help.mp4"))


if __name__ == "__main__":
    bot.run(f"{token}")
