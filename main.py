import os
from keep_alive import keep_alive
from discord.ext import commands
import discord
from threading import Thread
from libs import *


def collectdata1():
    collectdata(client)


client = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)
client.remove_command('help')

@client.command(aliases=["p"])
async def ping( ctx):
    await ctx.send(round(client.latency * 1000))

@client.event
async def on_ready():  # When the client is ready
    for extension in extensions:
        client.load_extension(extension)  # Loades every extension.
    print("I'm in")
    print(client.user)
    Thread(target=collectdata1).start()


@client.event
async def on_message(msg):

    addletters(msg.content)
    await client.process_commands(msg)


@client.event
async def on_member_join(member):
    dot = load_database()
    channel = client.get_channel(dot["serverchannel"][str(member.guild.id)])
    await channel.send(
        f"<@{member.id}> , Welcome to {member.guild.name} !! Introduce yourself so others can get know you!!"
    )


@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(
        title="***Help***",
        description="Use !help <command> for extended information",
        color=ctx.author.color)
    em.add_field(
        name="***Main features :***",
        value=
        "**invitelink** | **lettercount** |  **ping** |**sourcecode** | **serverstatus** | **clear** | **declarechannel**"
    )
    em.add_field(
        name="***Gambling :***",
        value=
        "**ratemyidea** | **rolladice** | **toosacoin** | **yesorno**")
    await ctx.channel.send(embed=em)


@help.command()
async def invitelink(ctx):
    em = discord.Embed(
        title="***Invite link***",
        description=
        "Get a link of **TEEN PROGRAMMING** server, which you can share to others and let them join you here !!",
        color=ctx.author.color)
    em.add_field(name="**Usage :**", value="`!invitelink`")
    em.add_field(name="**Aliases :**", value="`!il`")
    await ctx.channel.send(embed=em)


@help.command()
async def serverstatus(ctx):
    em = discord.Embed(
        title="***Server status***",
        description=
        "This shows the number members who have been online and offline in the server for a period of time",
        color=ctx.author.color) 
    em.add_field(name="**Usage :**", value="`!serverstatus [online/total]`")
    em.add_field(name="**Aliases :**", value="`!ss`")
    await ctx.channel.send(embed=em)


@help.command()
async def ping(ctx):
    em = discord.Embed(
        title="***Ping***",
        description="Shows the ping of this bot in the server",
        color=ctx.author.color) 
    em.add_field(name="**Usage**", value="`!ping`")
    em.add_field(name="**Aliases**", value="`!p`")
    await ctx.channel.send(embed=em)

@help.command()
async def sourcecode(ctx):
    em = discord.Embed(
        title="***Sourcecode***",
        description="Returns a link for the bot's source code",
        color=ctx.author.color) 
    em.add_field(name="**Usage :**", value="`!sourcecode`")
    em.add_field(name="**Aliases :**", value="`!sc`")
    await ctx.channel.send(embed=em)


@help.command()
async def clear(ctx):
    em = discord.Embed(
        title="***Clear***",
        description=
        "Clears the message in the channel. For this to work you must be an admin or owner",
        color=ctx.author.color)  
    em.add_field(name="**Usage :**", value="`!clear <numberofmessages>`")
    await ctx.channel.send(embed=em)


@help.command()#here
async def declarechannel(ctx):
    em = discord.Embed(
        title="***Declare channel***",
        description=
        "Declares a channel in which bot is allowed send general messages. You must have administrative permissions to use this command ",
        color=ctx.author.color) 
    em.add_field(name="**Usage :**", value="`!declarechannel <channel>`")
    em.add_field(name="**Aliases :**", value="`!dc`")
    await ctx.channel.send(embed=em)

@help.command()
async def ratemyidea(ctx):
    em = discord.Embed(
        title="***Rate my idea***",
        description=
        "gives a star rating for your your idea",
        color=ctx.author.color) 
    em.add_field(name="**Usage :**", value="`!ratemyidea <youridea>`")
    em.add_field(name="**Aliases :**", value="`!rmi` | `!star`")
    await ctx.channel.send(embed=em)

@help.command()
async def rolladice(ctx):
    em = discord.Embed(
        title="***Roll a dice***",
        description=
        "Rolls the dice and gives the result of it . if you want to roll it for muliple times, mention how many times",
        color=ctx.author.color) 
    em.add_field(name="**Usage :**", value="`!rolladice [numberoftimes]`")
    em.add_field(name="**Aliases :**", value="`!rod` | `!dice`")
    await ctx.channel.send(embed=em)

@help.command()
async def toosacoin(ctx):
    em = discord.Embed(
        title="***Toss a coin***",
        description=
        "tosses the coin and show the result of it",
        color=ctx.author.color) 
    em.add_field(name="**Usage :**", value="`!toosacoin`")
    em.add_field(name="**Aliases :**", value="`!tac` | `!toss`")
    await ctx.channel.send(embed=em)

@help.command()
async def yesorno(ctx):
    em = discord.Embed(
        title="***Yes or no***",
        description=
        "says yes or no for what u ask",
        color=ctx.author.color) 
    em.add_field(name="**Usage :**", value="`!yesorno [question]`")
    em.add_field(name="**Aliases :**", value="`!yon` | `!yesno`")
    await ctx.channel.send(embed=em)




extensions = ['cogs.features', 'cogs.gamble']
keep_alive()  # Starts a webserver to be pinged.
client.run(os.getenv('TOKEN'))  # Starts the client
