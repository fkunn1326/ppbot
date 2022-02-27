from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext

class Slash(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @cog_ext.cog_slash(name="きのこは正義", description="きのこ")
    async def _test(self, ctx: SlashContext):
        await ctx.send("きのこ！！！！")

def setup(bot: Bot):
    bot.add_cog(Slash(bot))
    