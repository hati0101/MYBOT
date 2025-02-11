import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # Railway ȯ�� �������� ������

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"? �α��� ����: {bot.user}")

@bot.command()
async def ��������(ctx):
    await ctx.author.send("?? **������ �����Ϸ���** `/���� ID ��й�ȣ` **�������� �Է��ϼ���.**")
    await ctx.send("?? **DM(���� �޽���)�� �ȳ��� ���½��ϴ�!**")

bot.run(TOKEN)
