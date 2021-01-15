from discord.ext import commands
import random
import asyncio


class Troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        
        if message.author.id == 526302545564663809:
            text = message.content
            text = text.lower()
            replies = ["oh really Mio? you and i-n-noo-c-cent?!", "mio and innocent :eyes:", "imagine you being innocent", "how unholy of you being innocent", "you and innocent *smirks*", "Duoluo zhe, mio", "when i couldn't be innocent, mio thinks she is :eyes: haha!", "you're eons away from being innocent", "humanity would decimate if you're innocent, mio", "an old pervy geezer could be innocent, but you... ", "innocent... someone's high"]
            msgs = ['i am innocent', "i'm innocent", "i'm very innocent", "im very innocent", "im fking innocent", "im fucking innocent", "i am fucking innocent", "i am soo fucking innocent", "i am soo fking innocent", "im soo fking innocent", "me innocent" , "i innocent", "im innocent", "mio is innocent", "mio innocent", "innocent mio", "innocent me"]
            
            for msg in msgs:

                if msg in text:                    
                    x = random.randrange(3, 5)
                    await asyncio.sleep(x)
                    await message.channel.send(f"{random.choice(replies)}")
                    break

def setup(bot):
    bot.add_cog(Troll(bot))