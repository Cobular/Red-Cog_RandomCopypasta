import discord
import praw
from discord.ext import commands

class RandomCopyPastaCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def copypasta(self):
        """This does stuff!"""
        reddit = praw.Reddit(client_id='zQ1s57VSHEE3mg',
                     client_secret="wpiRxlMiwUNB1gxktbqAVG9mvgw",
                     user_agent='Gets Copypasta from r/copypasta/random')
        sub = reddit.subreddit('copypasta')
        post = sub.random()
        self.bot.say(post.selftext)

def setup(bot):
    bot.add_cog(RandomCopyPastaCog(bot))