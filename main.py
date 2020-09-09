import discord
from discord.ext import commands, tasks
from discord.ext.commands import bot
import datetime
import random
import asyncio
import praw

# reddit data shit
reddit = praw.Reddit(client_id="pmVr1EokJ8Z8hQ",
                     client_secret="jD3-CSBysApJEMg0-cjam5FULYA",
                     username="jamescoloum",
                     password="14millie1#",
                     user_agent="python")

from asyncio import sleep

# other crap that isnt important ( It is important)
client = commands.Bot(command_prefix="n!")
# rules
f = open("idk shit/rules.txt", "r")
rules = f.readlines()
ab = ('your mum on a pole, LMAO!')
ac = ('you die!')
ad = 'you!'
ae = 'porn!'
af = 'your dad!'
ag = 'pokimane since i am a simp!'
ah = 'Linus Tech tips!'
ai = 'your friends!'
aj = 'you, watching me!?'
ak = 'children!'
al = 'anime.....thighs'
am = 'your dad in your mum, LOL!'
an = 'tizzards harams!'
# images
dumbmemes = ["https://imgur.com/t/meme_dump/OrQYwWm",
             "https://imgur.com/t/meme_dump/HGe6t26",
             "https://imgur.com/t/meme_dump/UuZM7nx",
             "https://imgur.com/t/meme_dump/vglTJqH",
             "https://imgur.com/gallery/f1o0x",
             "https://imgur.com/gallery/BJqXV",
             "https://imgur.com/gallery/IoQwV",
             "https://imgur.com/gallery/KU679",
             "https://imgur.com/gallery/8ep3G",
             "https://imgur.com/gallery/H3Ddh",
             "https://imgur.com/t/dank_memes/CtbMBef",
             "https://imgur.com/t/dank_memes/oTWQb71",
             "https://imgur.com/t/dank_memes/8U4jK4A",
             "https://imgur.com/t/dank_memes/zXWKSqb",
             "https://imgur.com/t/dank_memes/b5IdI1I",
             "https://imgur.com/t/dank_memes/afoAguu",
             "https://imgur.com/t/dank_memes/aKiEBkx",
             "https://imgur.com/t/dank_memes/eSsiHVn",
             "https://imgur.com/t/dank_memes/pxuqRJ2",
             "https://imgur.com/t/dank_memes/LJQTSxH",
             "https://imgur.com/t/dank_memes/o4UR43E",
             "https://imgur.com/t/dank_memes/7eRVybj"  # add more when u want to
             ]

# list of words that are not allowed
filtered_words = ["nigga", "nigger", "child-fucker", "child fucker", "jesus christ", "jesus christjesus christ",
                  "christ", "coon", "niggernigger", "child fuckerchild fucker"]

# removed commands
discord.ext.commands.HelpCommand(show_hidden=True)


# Ready/start

@client.event
async def on_ready():
    print('working')

    print('the error does not matter')

    while not client.is_closed():

        rb = 1
        rnb = random.randint(0, 11)
        rb += rnb
        print(rb)
        if rb == 1:
            activity = discord.Activity(name=ab, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)
        elif rb == 2:
            activity = discord.Activity(name=ac, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)

        elif rb == 3:
            activity = discord.Activity(name=ad, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)

        elif rb == 4:
            activity = discord.Activity(name=ae, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)

        elif rb == 5:
            activity = discord.Activity(name=af, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)

        elif rb == 6:
            activity = discord.Activity(name=ag, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)
        elif rb == 7:
            activity = discord.Activity(name=ah, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)

        elif rb == 8:
            activity = discord.Activity(name=ai, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)
        elif rb == 9:
            activity = discord.Activity(name=aj, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)
        elif rb == 10:
            activity = discord.Activity(name=ak, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)
        elif rb == 11:
            activity = discord.Activity(name=al, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)
        elif rb == 12:
            activity = discord.Activity(name=am, type=discord.ActivityType.watching)
            await client.change_presence(activity=activity)
            await asyncio.sleep(3600)


# await bot.change_presence(game=discord.Game(name='1Hentai'))
# auto mod
@client.event
@commands.Cog.listener()
async def on_message(msg, ):
    for word in filtered_words:
        if word in (msg.content.lower()):
            print('message deleted')
            await msg.delete()
    await client.process_commands(msg)


# error control
@client.event
async def on_command_error(ctx, error, ):
    if isinstance(error, commands.MissingPermissions):
        await ctx.message.delete()
        await ctx.send(f":no_entry_sign:  Your not allowed to run that command! :no_entry_sign: ")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        await ctx.send(':pencil2: Check that you have all the required aruguments! :pencil2:')
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.message.delete()
        await ctx.send(":pencil2: Check that the command exists and that you have spelt it correctly! :pencil2: ")
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.message.delete()
        await ctx.send(":pencil2: Check that the arguement is correct and that you have spelt it correctly! :pencil2: ")
    else:
        raise error


# commands

# rules
@client.command(aliases=['r'])
async def rule(ctx, *, number):
    await ctx.send(rules[int(number)])
    print(f"Rule: {number} sent!")


# nuke
@client.command(aliases=['n'])
@commands.has_permissions(manage_messages=True)
async def nuke(ctx):
    await ctx.channel.purge(limit=100000000000)
    await asyncio.sleep(1)
    await ctx.send('Channel has been nuked!  https://tenor.com/view/explosion-nuke-boom-nuclear-gif-5791468')


# clear messages
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


# kick
@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Reason not provided!"):
    try:
        await member.send(f"Bitch you got kicked because: {reason}. https://discord.gg/AnXpYst")
        await kick(reason=reason)
        await ctx.send(f'The bitch that got kicked was {member}. What a dumb bitch!')
    except:
        await member.kick(reason=reason)
        await ctx.send(f'The bitch that got kicked was {member}. What a dumb bitch!')


# ban
@client.command(aliases=['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="Reason not provided!"):
    try:
        await member.send(f"Bitch you got banned because: {reason}. To appeal: https://discord.gg/bsVkbHZ")
        await member.ban(reason=reason)
        await ctx.send(f'The bitch that got banned was {member}. What a dumb bitch!')
    except:
        await member.ban(reason=reason)
        await ctx.send(f'The bitch that got banned was {member}. What a dumb bitch!')


# un-ban
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):  # unban then the tag
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split("#")
    for banned_entry in banned_users:
        user = banned_entry.user
        if (user.name, user.discriminator) == (member_name, member_disc):
            await member.unban(user)
            await ctx.send(f"This nerd: {member_name} has been unbanned like a good child")
            return
    await ctx.send(f"{member} was not found")


@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, reason='No reason specified'):
    muted_role = ctx.guild.get_role(746662255898263612)
    member_role = ctx.guild.get_role(746662045419569192)
    await ctx.channel.purge(limit=1)
    await member.add_roles(muted_role)
    await member.remove_roles(member_role)
    await ctx.send(f':mute: {member.mention} has been muted for: {reason} :mute:')


# unmute
@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(746662255898263612)
    member_role = ctx.guild.get_role(746662045419569192)
    await ctx.channel.purge(limit=1)
    await member.remove_roles(muted_role)
    await member.add_roles(member_role)
    await ctx.send(f':speaker: {member.mention} has been unmuted for being a good child! :speaker: ')


# whois???
@client.command(aliases=['user', 'info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(title=member.name, description=member.mention, colour=discord.Colour.blue())
    embed.add_field(name="id", value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"requested by {ctx.author.name}")
    await ctx.send(embed=embed)


# idk
# memes idk
@client.command()
async def srp(ctx, subred="memes"):
    subreddit = reddit.subreddit(subred)
    all_subs = []
    top_posts = subreddit.top(limit=50)
    for submission in top_posts:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url

    embed = discord.Embed(title=name, colour=discord.Colour.gold())
    embed.set_image(url=url)
    await ctx.send(embed=embed)


# dont change passed here
client.loop.create_task(on_ready())
client.run("NzUyMTQ2MjgxNTM5MDQzMzQ5.X1TYzw.KwUG68YA6QnUdQRYTz1SxsIZrM4")