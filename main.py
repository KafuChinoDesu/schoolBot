import discord
from discord.ext import commands
import os
from datetime import datetime

bot = commands.Bot("학교봇 ")
tk = open("discordtoken.txt", "r")
token = tk.read()
tk.close()
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="도움말을 보시려면 \"학교봇 도움말\"을 이용해주세요!"))

@bot.command(pass_context=True, name="급식")
async def _sayfood(ctx, school: str, foodtype: str):
    os.system("python food.py {} {}".format(school, foodtype))
    f = open("{} {} food.txt".format(school, datetime.today().strftime("%Y%m%d")), "r")
    foodie = f.read()
    if foodie is "":
        await ctx.send("ERROR!")
    else:
        await ctx.send(foodie)
    f.close()

@bot.command(pass_context=True, name="학사일정")
async def _sayschedule(ctx, school: str):
    os.system("python schedule.py {}".format(school))
    f = open("{} {} schedule.txt".format(school, datetime.today().strftime("%Y%m%d")))
    schedule = f.read()
    if schedule == "":
        await ctx.send("ERROR!")
    else:
        await ctx.send(schedule)
    f.close()

@bot.command(pass_context=True, name="도움말")
async def _help(ctx):
    await ctx.send("학교봇 도움말:\n학교봇 급식 (학교명) (중식/석식): 오늘의 급식을 출력합니다.\n학교봇 학사일정 (학교명) : 오늘의 학사일정을 출력합니다.\n학교봇 시간표 (학교 종류) (학교명) (학년) (반) : 시간표를 출력합니다. 대부분의 경우에는 데이터가 없기 떄문에 결과값이 나오지 않습니다.\n학교 종류: 초등학교 중학교 고등학교")
    await ctx.send("예시:\n학교봇 급식 초당고 중식\n학교봇 시간표 고등학교 백현고 3 1\n학교봇 학사일정 동백고")

@bot.command(pass_context=True, name="시간표")
async def _saytimetable(ctx, schtype: str, school: str, grade: int, classnm: int):
    sctype = "his"
    if schtype == "초등학교":
        sctype = "els"
    elif schtype == "중학교":
        sctype = "mis"
    os.system("python timetable.py {} {} {} {}".format(school, grade, classnm, sctype))
    f = open("{} {} timetable.txt".format(school, datetime.today().strftime("%Y%m%d")), "r")
    timetable = f.read()
    if timetable is "":
        await ctx.send("ERROR!")
    else:
        await ctx.send(timetable)
    f.close()

bot.run(token)


