import os
from discord.ext import commands
from discord_slash import SlashCommand
import json

os.makedirs("./cogs", exist_ok=True)

client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)

f = open('config.json', 'r')
json_dict = json.load(f)
f.close()

""" config.json
  "section":{
    "name": "name"", <- この名前でコマンドが定義されます（また、cogsの中にこの名前でpythonファイルが生成されます）
    "description": "description", <- この名前がコマンドの説明になります
    "contents": "contents" <- これが送信されます
  }
"""
for x in json_dict:
    name = json_dict[x]['name']
    description = json_dict[x]['description']
    contents = json_dict[x]['contents']
    f = open('./cogs/{}.py'.format(name), 'w')
    text = """from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

class Slash(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="{}", description="{}")
    async def _test(self, ctx: SlashContext):
        await ctx.send("{}")

def setup(bot: Bot):
    bot.add_cog(Slash(bot))
    """.format(name, description, contents)
    f.write(text)
    f.close()
    print(name, description, contents)
    client.load_extension(f"cogs.{name}")

client.run(os.environ['DISCORD_TOKEN'])
