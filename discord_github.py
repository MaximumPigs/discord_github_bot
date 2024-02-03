import discord
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

github_token = os.getenv("GITHUB_TOKEN")
headers = { 'Accept': 'application/vnd.github+json',
            'Authorization':'token ' + github_token,
            'Content-Type' : 'application/json' }
data = '{"ref":"main"}'

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print(f"Sucessfully logged in as {bot.user}\nType !get_help for help")


@bot.command()
async def generate(ctx):
    options = ["a", "b", "c", "d"]
    already_sent_res = None  # Safe to remove, used for demo

    await ctx.send(
        f"{ctx.author.mention}\n"
        f'Sample question: (**Important**: Type a "!" in front):\n```'
        "> A\n> B\n> C\n> D```"
    )

    def check(m):
        return (
            m.content.startswith("!")
            and m.content.lower()[1:] in options
            and m.channel.id == ctx.channel.id
        )

    while True:
        msg = await bot.wait_for("message", check=check)
        # msg.content now contains the option. You may now proceed to code here
        # The below code from here are used for demonstration and can be safely removed
        if already_sent_res is None:
            sent_message = await ctx.send(
                f"**{str(msg.author.name)}** has chosen option **{str(msg.content).upper()[1:]}**"
            )
            already_sent_res = not None
        else:
            await sent_message.edit(
                f"**{str(msg.author.name)}** has chosen option **{str(msg.content).upper()[1:]}**"
            )

@bot.command()
async def get_help(ctx):

    await ctx.send(
        f"{ctx.author.mention}\n"
        f'Send one of the following messagesType !start to start server\n```'
        "> !start - Start Server\n> !stop - Stop Server\n> !fetch - Fetch and store game files```"
    )


@bot.command()
async def start(ctx):

    await ctx.send(
        f"{ctx.author.mention}\n"
        f"Starting Palworld Server"
    )

    github_url = 'https://api.github.com/repos/MaximumPigs/Docker_Deploy/actions/workflows/51003280/dispatches'

    response = requests.post( github_url, headers=headers, data=data )
    print(response.status_code)

@bot.command()
async def fetch(ctx):

    await ctx.send(
        f"{ctx.author.mention}\n"
        f"Fetching and storing Game Files - will run automatically on server shutdown"
    )

    github_url = 'https://api.github.com/repos/MaximumPigs/Docker_Deploy/actions/workflows/84425606/dispatches'

    response = requests.post( github_url, headers=headers, data=data )
    print(response.status_code)

@bot.command()
async def stop(ctx):

    await ctx.send(
        f"{ctx.author.mention}\n"
        f"Stopping"
    )

    github_url = 'https://api.github.com/repos/MaximumPigs/Docker_Deploy/actions/workflows/51003282/dispatches'

    response = requests.post( github_url, headers=headers, data=data )
    print(response.status_code)

bot.run(os.getenv("DISCORD_TOKEN"))