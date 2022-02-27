from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

class Slash(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="name", description="description")
    async def _test(self, ctx: SlashContext):
        await ctx.send("contents")

def setup(bot: Bot):
    bot.add_cog(Slash(bot))
    