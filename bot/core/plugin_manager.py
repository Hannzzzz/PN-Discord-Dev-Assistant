from plugins.welcome.welcome import Welcome


async def load_plugins(bot):
    await bot.add_cog(Welcome(bot))