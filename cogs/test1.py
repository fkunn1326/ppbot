from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

class Slash(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="test1", description="test!!!!")
    async def _test(self, ctx: SlashContext):
        await ctx.send("test!!!!!")

def setup(bot: Bot):
    bot.add_cog(Slash(bot))
    