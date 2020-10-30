import discord
from discord.ext import commands
from discord.utils import get
import random

class Hallows(commands.Cog):

    trick = [
	'https://i.imgur.com/jn0f2OT.png', 
        'https://i.imgur.com/gS7zNJF.png', 
        'https://i.imgur.com/vR7P6yz.png', 
        'https://i.imgur.com/YY5IJbv.png', 
        'https://i.imgur.com/ozvgxtN.mp4', 
        'https://i.imgur.com/Ymsb3hA.mp4',
        'https://i.imgur.com/c5l8gHn.png',
        'https://i.imgur.com/aRNLbyW.png',
        'https://i.imgur.com/Xdc8x0y.png',
        'https://i.imgur.com/rSYsHgR.png',
        'https://i.imgur.com/ezHJEIU.png',
        'https://i.imgur.com/pldqNrr.png',
        'https://i.imgur.com/sNYXV8P.png', 
        'https://i.imgur.com/l1j8EFU.png',
        'https://i.imgur.com/0IXQyhn.png', 
        'https://i.imgur.com/UQePbsk.jpeg',
        'https://i.imgur.com/1PXgGzG.jpeg',
        'https://i.imgur.com/2r6xkrL.png',
        'https://i.imgur.com/hzhUqou.png', 
        'https://i.imgur.com/7ZGP1Dq.jpeg',
        'https://i.imgur.com/gTeQxFn.png', 
        'https://i.imgur.com/OfypSwv.png',
        'https://i.imgur.com/qRN7Y2u.png',
        'https://i.imgur.com/O3Udcd1.png',
        'https://i.imgur.com/stxWFtL.jpeg',
        'https://i.imgur.com/uX2buv1.jpeg',
        'https://i.imgur.com/y05Dk6M.jpeg',
        'https://i.imgur.com/h9eM5TY.jpeg',
        'https://i.imgur.com/ZWpR5DW.jpeg',
        'https://i.imgur.com/ln2wBD0.jpeg',
        'https://i.imgur.com/PaJFtS2.jpeg',
        'https://i.imgur.com/0AzoBTA.jpeg',
        'https://i.imgur.com/f8q1521.jpeg',
        'https://i.imgur.com/aVM3Zdd.jpeg',
        'https://i.imgur.com/F2p4dDc.jpeg',
        'https://i.imgur.com/yXRYCNb.jpeg',
        'https://i.imgur.com/xpzac4T.png',
        'https://i.imgur.com/N986HVq.jpeg',
        'https://i.imgur.com/8GH5p7p.jpeg',
        'https://i.imgur.com/UrzItpr.jpeg',
        'https://i.imgur.com/1zJ43hO.png',
        'https://i.imgur.com/pCjyzZS.png',
        'https://i.imgur.com/SDLik4Z.jpeg',
        'https://i.imgur.com/rskdEuT.jpeg',
        'https://i.imgur.com/H3P0vMh.jpeg',
        'https://i.imgur.com/taAVvwH.jpeg',
        'https://i.imgur.com/T3Leabb.jpeg',
        'https://cdn.discordapp.com/attachments/765839161830932481/771574671921119242/rowletbbq.png',
        'https://preview.redd.it/i2ec1oluhdn41.png?width=801&auto=webp&s=3596ebdecae42ecd8de3e93f61c7484a1162a016',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Pipa_pipa_whole_body.jpg/500px-Pipa_pipa_whole_body.jpg',
        'Did you know? \n25% of your bones are in your feet.',
        'Did you know? \nCherries can still be sold if 4% of them are found to contain maggots.',
        'Did you know? \nThe average number of skeletons that people have is greater than one.',
    ]

    treat = [
        'https://cdn.discordapp.com/attachments/765839161830932481/766389080871141427/SPOILER_sample-16a23792ca9fe2bb266e936aaae6b172.png',
        'https://i.imgur.com/BjwHe5R.jpeg',
        'https://i.imgur.com/xzRckyo.jpeg',
        'https://i.imgur.com/vuQ6bod.jpeg',
        'https://i.imgur.com/c2daEp4.jpeg',
        'https://i.imgur.com/wQpG42h.jpeg',
        'https://i.imgur.com/EseC8Bu.jpeg',
        'https://i.imgur.com/D1ENxC6.jpeg',
        'https://i.imgur.com/R3f8H7C.jpeg',
        'https://i.imgur.com/BSfhjMa.jpeg',
        'https://i.imgur.com/BQT7Hjr.jpeg',
        'https://i.imgur.com/aagJfYB.jpeg',
        'https://i.imgur.com/EAykhWQ.jpeg',
        'https://i.imgur.com/fcDJJPN.jpeg',
        'https://i.imgur.com/KollfPl.jpeg',
        'https://i.imgur.com/IajjdyD.jpeg',
        'https://i.imgur.com/FUO5J2m.jpeg',
        'https://i.imgur.com/as9BMp6.jpeg',
        'https://i.imgur.com/iJqVDX4.jpeg',
        'https://i.imgur.com/v6RjXNt.jpeg',
        'https://i.imgur.com/WVou4QQ.jpeg',
        'https://i.imgur.com/AbQ2jNF.jpeg',
        'https://i.imgur.com/zI5mNQk.jpeg',
        'https://i.imgur.com/cwO5yDc.jpeg',
        'https://i.imgur.com/IPdpV26.jpeg',
        'https://i.imgur.com/IWwXqkb.jpeg',
        'https://i.imgur.com/7VA424c.jpeg',
        'https://i.imgur.com/aCdOh3p.jpeg',
        'https://i.imgur.com/Pj4qBuM.jpeg',
        'https://i.imgur.com/pDiZZBV.jpeg',
        'https://i.imgur.com/OFkbHUJ.jpeg',
        'https://i.imgur.com/MRYz0G5.jpeg',
        'https://i.imgur.com/BOOkpCc.jpeg',
        'https://i.imgur.com/s43VzhE.jpeg',
        'https://i.imgur.com/wHzMlxn.jpeg',
        'https://i.imgur.com/ZZQ33tI.jpeg',
        'https://i.imgur.com/aFxbSvT.jpeg',
        'https://i.imgur.com/65qxSg8.jpeg',
        'https://i.imgur.com/iOD8vmt.jpeg',
        'https://i.imgur.com/gRrGx0Z.jpeg',
        'https://i.imgur.com/xJmIHzn.jpeg',
        'https://i.imgur.com/yFRLT8b.jpeg',
        'https://i.imgur.com/MvPP1a3.jpeg',
        'https://i.imgur.com/hrHS40Z.jpeg',
        'https://i.imgur.com/1KVdFOf.jpeg',
        'https://i.imgur.com/f6T7kap.jpeg',
        'https://i.imgur.com/4Ayqvqm.jpeg',
        'https://i.imgur.com/5KCGZ7C.jpeg',
        'https://i.imgur.com/CiHcxi5.jpeg',
        'https://i.imgur.com/i6l0sos.jpeg',
        'https://i.imgur.com/KTblyP8.jpeg',
        'https://i.dailymail.co.uk/i/pix/2016/05/19/06/3453F4AD00000578-3598190-image-a-1_1463635913664.jpg',
        'https://cdn.discordapp.com/attachments/675174769515036673/682328607288197171/20200226_1412491.jpg',        
        'Did you know? \nWhile bats are very adept fliers, they do end up running into each other. A lot.',
        "Did you know? \nCanada geese adopt orphan geese from different species into their flocks.",
        'Did you know? \nVampire bats share food.',
        
    ]

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def tot(self, ctx):
        if ctx.message.author.bot:
            return

        message = ''

        if random.random() > 0.5:
            message = random.choice(self.trick)
            print('Trick') 
        else:
            message = random.choice(self.treat)
            print('Treat')

        await ctx.send(message)

def setup(bot):
    bot.add_cog(Hallows(bot))
