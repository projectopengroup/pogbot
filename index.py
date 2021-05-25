# Importing requirements
import discord
from discord.ext import commands

# Request bot token from user input.
BotToken = input("Enter bot token: ")

# Define bot and it's commands prefix.
bot = commands.Bot(command_prefix="!")


@bot.event
# Look for incoming messages in DMs and in Chat.
async def on_message(msg):
    # Check if the message author is a bot.
    if msg.author.bot:
        # if it is a bot then return the code from here, not going any further.
        return
    # Print the server name and channel of the message followed by author name and the message content.
    print(f'(Server: {msg.guild}) [{msg.channel}] {msg.author} : {msg.content}')
    # Ensure that we process our commands, as on_message overrides and stops command execution.
    await bot.process_commands(msg)


@bot.command()
# Look for a command called ping.
async def ping(ctx):
    # Send a message "Pong" when ping has been used.
    await ctx.send("Pong")


@bot.command()
# Look for a command called github.
async def github(ctx):
    # Sends the link to the bot github page when the github command is used.
    await ctx.send("https://github.com/projectopengroup/Pogbot")


@bot.command()
# Look for a command called echo
async def echo(ctx, *, arg):
    # Send an echo of the keyword-only argument.
    await ctx.send(arg)


@bot.command(name='avatar', aliases=['av', 'pfp'])
# Look for a command called avatar and collects optional user parameter, so if no user given, user = None.
async def avatar(ctx, user: discord.Member = None):
    # Checks if user parameter is given. If user = none, that means no user was given so user variable is set to the
    # command author.
    if user is None:
        user = ctx.author
    # Defining pfp from user's avatar_url.
    pfp = user.avatar_url
    # Creating an embed response using an f string to insert the author long name by using our variable 'user'.
    embed = discord.Embed(
        title=f'**{user}**',
        description='**Avatar**',
        color=0x08d5f7
    )
    # Setting the embed's image url property to the one we defined from user.avatar_url
    embed.set_image(url=pfp)
    # Sending the embed message response back.
    await ctx.send(embed=embed)


@bot.command(name='userid', aliases=['id', 'uid'])
# Look for a command called userid and collects optional user parameter, so if no user given, user = None.
async def userid(ctx, user: discord.Member = None):
    # Checks if user parameter is given. If user = none, that means no user was given so user variable is set to the
    # command author.
    if user is None:
        user = ctx.author
    # Creates a discord embed with the elements: title (Which gets the user's tag),
    # description (Which gets the user's id), and color (which is the bot's color).
    idembed = discord.Embed(title=f"**{user}'s ID**", description=f'**{user.id}**', color=0x08d5f7)
    await ctx.send(embed=idembed)


@bot.event
# Check to see if bot is ready.
async def on_ready():
    # Print status to terminal.
    print('Status: Ready.')
    await bot.change_presence(
        activity=discord.Game(name='with discord API'))


@bot.event
# Look for members joining.
async def on_member_join(member):
    print(f'{member} joined.')


@bot.event
# Look for members leaving.
async def on_member_remove(member):
    print(f'{member} left.')


# Run the bot using its token.
bot.run(BotToken)
