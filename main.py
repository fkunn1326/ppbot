import os
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from server import keep_alive
import json

Client = commands.Bot(command_prefix="!")
slash = SlashCommand(Client, sync_commands=True)

json_open = open('config.json', 'r')
json_load = json.load(json_open)

@slash.slash(name="test", description="test command")
async def test(ctx):
    await ctx.send("pong!")


keep_alive()

Client.run(os.environ['DISCORD_TOKEN'])
