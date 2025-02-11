import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")  # Railway 환경 변수에서 가져옴

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"? 로그인 성공: {bot.user}")

@bot.command()
async def 계정생성(ctx):
    await ctx.author.send("?? **계정을 생성하려면** `/계정 ID 비밀번호` **형식으로 입력하세요.**")
    await ctx.send("?? **DM(개인 메시지)로 안내를 보냈습니다!**")

bot.run(TOKEN)
