import discord
import praw
from discord.ext import commands

class RandomCopyPastaCog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def copypasta(self):
        """Put the ID of your spem channel here"""
        spamChannel = "Put_A_Channel_ID_Here"
        
        """This is the actual code"""
        channel = ctx.message.channel.id
        if spamChannel = "Put_A_Channel_ID_Here":
            self.bot.say("Please open the cog's scrypt and change the varriable \'spamChannel\' to the ID of your server's spam channel!")
        else:
            if channel = spamChannel:
                reddit = praw.Reddit(client_id='zQ1s57VSHEE3mg',
                         client_secret="wpiRxlMiwUNB1gxktbqAVG9mvgw",
                         user_agent='Gets Copypasta from r/copypasta/random')
                sub = reddit.subreddit('copypasta')
                post = sub.random()
                self.bot.say(post.selftext)
            else:
                self.bot.say("Please take this to the spam channel for the sanity of other users. Thanks!!")
def setup(bot):
    bot.add_cog(RandomCopyPastaCog(bot))
