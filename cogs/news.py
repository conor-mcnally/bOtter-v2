import discord
from discord.ext import commands
from discord import Embed
import requests
import datetime


class news(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def news(self, ctx):   
        url = ('https://newsapi.org/v2/top-headlines?'
            'country=gb&'
            'apiKey=d906b1dcaed249cf872e26268205e8b1')
        response = requests.get(url)
        json_data = response.json()
        headlines = []
        for article in json_data['articles']:
            headlines.append(article['title'])
        #Return first 5 entries
        top5 = headlines[:5]
        top5 = '\n\n'.join(top5)
        now = datetime.datetime.now().strftime('%d/%m/%Y')
        try:
            embed = Embed()
            embed = discord.Embed(title='News', colour=discord.Colour.dark_green())
            embed.set_footer(text=now)
            embed.set_thumbnail(url='https://i2.wp.com/grin2b.com/wp-content/uploads/2017/01/Grin2B_icon_NEWS.png?fit=675%2C675')
            embed.add_field(name = 'Top Headlines', value = top5)
            
            await ctx.channel.send(embed=embed)
        except:
            print("Error printing embed")

def setup(bot):
    bot.add_cog(news(bot))