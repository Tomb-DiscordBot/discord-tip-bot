from discord.ext import commands
import discord

def handle_invalid_token():
    embed = discord.Embed(title="Command Error", color=0xE50000)
    embed.description = '''This token is not supported\n
                See `$tokens` for a list of supported tokens'''

    return embed

def handle_deposit(error):
    embed = discord.Embed(title="Command Error", color=0xE50000)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.description = '''You need to include a token code (FTM, TOMB, \
                etc.)\n\ne.g. `$deposit FTM`'''
    else:
        embed.description = "Unknown error occurred. Try again."

    return embed

def handle_invalid_address():
    embed = discord.Embed(title="Invalid Address", color=0xE50000)
    embed.description = "The address you provided is invalid."
    return embed

def handle_insufficient_balance(amount, token, balance):
    token = token.upper()
    embed = discord.Embed(title="Insufficient Balance", color=0xE50000)
    embed.add_field(name="Your balance", value=f"**{balance} {token}**")

    return embed

def handle_no_funds(token):
    token = token.upper()
    embed = discord.Embed(title="Insufficient Balance", color=0xE50000)
    embed.description = f'''You don't have any **{token}**. Please deposit some \
            using the `$deposit` command.'''

    return embed

def handle_withdrawal(error):
    embed = discord.Embed(title="Command Error", color=0xE50000)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.description = '''You need to include a token code (FTM, TOMB, \
                etc.)\n\ne.g. `$withdraw FTM`'''
    elif isinstance(error, commands.CommandInvokeError):
        embed.description = "Make sure you have enough funds to cover for gas."
    else:
        embed.description = "Unknown error occurred. Try again."

    return embed

def handle_balance(error):
    embed = discord.Embed(title="Command Error", color=0xE50000)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.description = '''You need to include a token code (FTM, TOMB, \
                etc.)\n\ne.g. `$balance FTM`'''
    else:
        embed.description = "Unknown error occurred. Try again."

    return embed

def handle_tipping(error):
    embed = discord.Embed(title="Command Error", color=0xE50000)
    if isinstance(error, commands.MissingRequiredArgument):
        embed.description = '''Usage: `$tip @user <amount> <token>`\
                \n\ne.g. `$tip @0xKalakaua 1 FTM`'''
    elif isinstance(error, commands.CommandInvokeError):
        embed.description = "Make sure you have enough funds to cover for gas."
    else:
        embed.description = "Unknown error occurred. Try again."

    return embed