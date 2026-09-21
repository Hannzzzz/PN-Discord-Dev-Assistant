import discord
from discord.ext import commands


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_member_join(self, member):

        channel = discord.utils.get(
            member.guild.text_channels,
            name="general"
)

        if channel :
            file = discord.File("welcome.png", filename="welcome.png")

            member_count= member.guild.member_count

            embed = discord.Embed(
                title = "🎉 SELAMAT DATANG!",
                description=(
                f"Welcome {member.mention}! 👋\n "
                f"Selamat datang di\n"
                f"**{member.guild.name}**\n\n"
                f" Kamu adalah member ke-{member_count}\n"
                f"Semoga betah disini dan enjoy yak!\n"
            )
        )

            embed.add_field(
             name="📌 START HERE",

            value=(
            "📖 Baca rules di <#CHANNEL_ID>\n"
            "💬 Ngobrol di <#CHANNEL_ID>\n"
            "🎮 Cari teman mabar\n"
            "🤝 Kenalan sama member lain"
            
             ),
            inline=False
        )

            embed.set_thumbnail(
                url=member.display_avatar.url
        )

            embed.set_image(
                url="attachment://welcome.png"
        )

            embed.set_footer(
                text="Code. Learn. Build. Together"
        )

            await channel.send(
                embed=embed,
                file=file
        )
    