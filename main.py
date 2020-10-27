import discord
from discord.ext import commands
import os
from datetime import datetime

bot = commands.Bot("학교봇 ")
token = ""
with open("discordtoken.txt", "r") as tk:
    token = tk.read()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="도움말을 보시려면 \"학교봇 도움말\"을 이용해주세요!"))

@bot.command(name="급식")
async def _sayFood(ctx, school: str, foodtype: str):
    os.system(f"python food.py {school} {foodtype}")
    with open(f"{school} {datetime.today().strftime('%Y%m%d')} food.txt", "r") as f:
        foodie = f.read()
        await check(foodie, ctx)

@bot.command(name="학사일정")
async def _saySchedule(ctx, school: str):
    os.system("python schedule.py {}".format(school))
    with open(f"{school} {datetime.today().strftime('%Y%m%d')} schedule.txt") as f:
        schedule = f.read()
        await check(schedule, ctx)

@bot.command(name="도움말")
async def _help(ctx):
    with open("help.md", "r") as f:
        await ctx.send(f.read())

@bot.command(name="시간표")
async def _sayTimetable(ctx, schtype: str, school: str, grade: int, classnm: int):
    sctype = "his"
    if schtype == "초등학교":
        sctype = "els"
    elif schtype == "중학교":
        sctype = "mis"
    os.system(f"python timetable.py {school} {grade} {classnm} {sctype} 0")
    with open(f"{school} {datetime.today().strftime('%Y%m%d')} timetable.txt", "r") as f:
        timetable = f.read()
        await check(timetable, ctx)

@bot.command(name="특수시간표")
async def _saySpecialTimetable(ctx, schtype: str, school: str, grade: int, classnm: int):
    os.system(f"python timetable.py {school} {grade} {classnm} {schtype} 1")
    with open(f"{school} {datetime.today().strftime('%Y%m%d')} timetable.txt", "r") as f:
        timetable = f.read()
        await check(timetable, ctx)

async def check(check: str, ctx):
    if not check:
        await ctx.send("ERROR!")
    else:
        await ctx.send(check)

bot.run(token)


