import discord
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

github_repo_url = 'https://api.github.com/repos/MaximumPigs/docker_deploy/dispatches'
github_token = os.getenv("GITHUB_TOKEN")
headers = { 'Accept': 'application/vnd.github+json',
            'Authorization':'Bearer ' + github_token}

actions = [ "start", "stop", "store" ]
games = [ "palworld", "enshrouded" ]

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print(f"Sucessfully logged in as {bot.user}\nType !get_help for help")


@bot.command()
async def get_help(ctx):

    await ctx.send(
        f"{ctx.author.mention}\n\n"
        f'Syntax\n```'
        "> !game [ action ] [ game ]```\n"
        'Example "!game start palworld"\n\n'
        'Available actions:\n```'
        "> start  - start game server\n"
        "> stop   - stop game server\n"
        "> store  - copy files down from server and store them (runs automatically on stop action)```\n"
        'Available games:\n```'
        "> palworld\n"
        "> enshrouded```"
    )

@bot.command()
async def game(ctx, action="null", game="null"):

    if action != "null" and game != "null":

        if game in games:
            await ctx.send(
                f"{ctx.author.mention}\n"
                f"Running {action.lower()} on {game.capitalize()} server"
            )

            json_data = '{"event_type":"' + action.lower() + '","client_payload":{ "game":"' +game.lower() + '" }}'

            print(github_repo_url)
            print(headers)
            print(json_data)

            response = requests.post( github_repo_url, headers=headers, data=json_data )
            print(response.status_code)
            print(response.reason)

        else:
            await ctx.send(
                f"{ctx.author.mention}\n"
                f"Action {action.upper()} or Game {game.upper()} doesn't exist - for a list of actions and games type !get_help"
            )
    else:

        await ctx.send(
            f"{ctx.author.mention}\n\n"
            f"Action or game not specified.\n\n"
            'Syntax:\n```'
            "!game [action] [game]```\n\n"
            "Type !get_help for more info"
        )

bot.run(os.getenv("DISCORD_TOKEN"))