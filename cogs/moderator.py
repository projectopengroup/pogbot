import sqlite3
import discord
import base64
import os
import asyncio
from discord.ext import commands


class Moderator(commands.Cog, name="moderator"):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Moderator(bot))
