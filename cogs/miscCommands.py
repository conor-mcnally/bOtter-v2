import discord
from discord.ext import commands
from discord import Embed
import wikipedia


class miscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        ping = round(self.bot.latency * 1000)
        await ctx.send(f'**{str(ping)}ms**')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)

    # Wikipedia search for terms
    @commands.command(name='wiki', description="Search wikipedia for a term")
    async def wiki(self, ctx, *, query):
        search = wikipedia.summary(query, sentences=3, chars=1000, auto_suggest=True, redirect=True)
        embed = Embed()
        embed = discord.Embed(
            title=f'{query}',
            colour=discord.Colour.dark_blue(),
            description=search
        )
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):

        if member is None:
            embed = discord.Embed(title="This command is used like this: ```+avatar [member]```", colour=0xff0000)
            await ctx.send(embed=embed)
            return

        else:
            embed2 = discord.Embed(title=f"{member}'s Avatar!", colour=0xffffff)
            embed2.set_image(url=member.avatar_url)
            await ctx.send(embed=embed2)

    @commands.command(name="credits", description="Who made the bot")
    async def credits(self, ctx):
        await ctx.send("Made by `McNaldo`")


def setup(bot):
    bot.add_cog(miscCommands(bot))
