# -*- coding: utf-8 -*-
import discord
import datetime
import asyncio
import re
import random
import time
import json
from Dtime import Uptime
from discord.utils import get
from discord.ext import tasks

token = "Nzg0NDQ5MTA4OTc4OTU4MzQ2.X8pdKQ.PmQwlJrBb0ZKMQbBjEuPcbc6hEw" #봇 토큰 설정하기
intents = discord.Intents.all()
client = discord.Client(intents=intents) #client 설정하기
Uptime.uptimeset()
@client.event
async def on_ready(): #봇이 준비되었을때
    print("the bot is started.")
    print(client.user)
    print("============================")
    print("봇이 들어가있는 서버")
    import asyncio
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("부팅 중...현재 명령어 사용 불가")
    guild_list = client.guilds
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {}".format(i.id, i.name)) 
    await client.change_presence(status=discord.Status.online, activity=game)
    user = len(client.users)
    server = len(client.guilds)
    message = ["씨퓨를 쓰는 유저 수는 " + str(user) + "명이에요!","씨퓨를 쓰는 서버 수는 " + str(server) + "개에요!","씨퓨야 도움말"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.content == "씨퓨야 ㅗ": 
        await message.channel.send("ㅗㅗ") 
    if message.content == "씨퓨야 흠터": 
        await message.channel.send("레스팅") 
    if message.content == "와": 
        await message.channel.send("칸다포에버") 
    if message.content == "씨퓨야 ㅎㅇ": 
        await message.channel.send("ㅇㅇ ㅎㅇ")
    if message.content == "씨퓨야 ?": 
        await message.channel.send("!") 
    if message.content == "씨퓨야 민초": 
        await message.channel.send("맛있음") 
    if message.content == "씨퓨야 그타": 
        await message.channel.send("망겜") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 파리": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("옵투?") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 옵투": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("날파리") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 심심해": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("그타켜") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 없데이트": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("카요 페리코 습격:12월 15일 GTA 온라인 출시.이제껏 경험해보지 못한 위험에 뛰어들 때입니다. 지금까지 볼링브로크 교도소에서 유죄가 선고된 스파이를 탈출시키고, 병적인 자기중심주의에 빠진 갑부로부터 세상을 구하고, 위험을 무릅쓰고 카지노에서 현금을 빼돌렸다면, 이제는 섬 전체를 상대할 시간입니다.") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 ㅗㅜㅑ": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("ㅗㅜㅑ...:heart:") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "히히": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("희희") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "씨퓨야 시리즈a": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("505,000$") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "씨퓨야 주인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("i7_3700X에요!") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "씨퓨야 둠피임?": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("?") #봇이 "ㅂㅇ" 라고 답한다
    if message.content == "씨퓨야 둠피": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("커여움") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 잘자": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("너도...:heart:") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 안녕": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("안녕하세요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 카습": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("현금:2,326,500$,예술품:2,585,000$,금괴:2,843,456$,다이아몬드:3,618,720$") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 카습 엘리트조건": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("비밀 작전:15분 이내 완료/사망자 없음/해킹 실패 0/발각되지 않음,대사기극:15분 이내 완료/사망자 없음/발각되지 않음,공격 전술:15분 이내 완료/사망자 없음/80명 헤드샷") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 카습 1회보상": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("공격전술:100,000,대 사기극:150,000,비밀 작전:200,000,모든 진입 방식 클리어:300,000,모든 진입 방식 엘리트:350,000,어려움 난이도에서 죽지 않고 완료:250,000") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("왜 불러?") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 카습하자": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("시러") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 보그단": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("보그단 문제의 수입은 1,187,500$에요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 심날": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("심판의 날 습격의 수입은 1,500,000$에요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 플리카": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("플리카 작업의 수입은 143,750$에요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 탈옥": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("탈옥의 수입은 500,000$에요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 휴메인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("휴메인 연구소 습격의 수입은 675,000$에요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 시리즈A": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("시리즈 A의 수입은 505,000$에요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 퍼시픽": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("퍼시픽 스탠다드 습격의 최대 수입은 1,250,000$에요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 정보약탈": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("정보 약탈의 수입은 812,500$에요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 나죽어": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("주거랏:crossed_swords:") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 짖어": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("싫은뎅") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 뒤져": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("시러") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 시리": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("시리보단 클리포드지") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습": #만일 사용자가 "야" 라고 입력했을때
        await message.channel.send("마드라조 파일:1,100,000$ 신시미토 테킬라:900,000$ 루비 목걸이:1,000,000$ 무기명 채권:1,100,000$ 핑크 다이아몬드:1,300,000$ 팬서 조각상:1,900,000$") #봇이 "왜" 라고 답한다.
    if message.content == "씨퓨야 랜덤":
        await message.channel.send(random.randint(1, 10))
    if message.content == "씨퓨야 카습구인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 카습 구인을 하고 있어요!")
    if message.content == "씨퓨야 카습금": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 카습 금 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 카습다이아": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 카습 다이아 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 카습현금": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 카습 현금 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습테킬라": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 신시미토 테킬라 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습루비목걸이": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 루비 목걸이 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습핑크다이아": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 핑크 다이아몬드 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습채권": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 무기명 채권 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습목걸이": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 루비 목걸이 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습조각상": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 팬서 조각상 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습팬서": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 팬서 조각상 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습팬서조각상": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 팬서 조각상 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 페습구인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 페습 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 플리카구인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 플리카 작업 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 탈옥구인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 탈옥 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 휴메인구인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 휴메인 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 시리즈A구인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 시리즈A 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 시리즈a구인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 시리즈A 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 퍼시픽구인": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send(f"@everyone  {message.author.mention}님이 퍼시픽 구인을 하고 있어요!") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 자폭해": #만일 사용자가 "ㅎㅇ" 라고 입력했을때
        await message.channel.send("SYNTAXERROR:invalid syntax - unable to import message.content == '씨퓨야 자폭해': from index.py") #봇이 "ㅂㅇ" 라고 답한다.
    if message.content == "씨퓨야 이민재": #만일 사용자가 "야" 라고 입력했을때
        await message.channel.send("관종") #봇이 "왜" 라고 답한다.
    if message.content == "너밴": #만일 사용자가 "야" 라고 입력했을때
        await message.channel.send("아 잘못했어요") #봇이 "왜" 라고 답한다.
    if message.content == "너밴": #만일 사용자가 "야" 라고 입력했을때
        await message.channel.send("살려줘") #봇이 "왜" 라고 답한다.
    if message.content == "씨퓨야 둠삭필": 
        await message.channel.send("둠피삭제필수") 
    if message.content == "씨퓨야 옵치": 
        await message.channel.send("개망겜") 
    if message.content == "씨퓨야 배그": 
        await message.channel.send("갓겜(이었던것)")
    if message.content == "씨퓨야 레식": 
        await message.channel.send("아니 이게 왜죽어 ㄹㅇ")
    if message.content == "씨퓨야 데가": 
        await message.channel.send("데스티니가디언즈 갓겜")
    if message.content == "씨퓨야 글옵": 
        await message.channel.send("갓겜은 아닌데 망겜도 아님")
    if message.content == "씨퓨야 크시": 
        await message.channel.send("어케만든건지 모르겠어요 ㄹㅇ")
    if message.content == "씨퓨야 하리보": 
        await message.channel.send("예전엔 멀쩡했는데 요즘엔 너무 끊겨요...")
    if message.content == "씨퓨야 히드라": 
        await message.channel.send("낮에는 잘 안끊기고 음질도 좋은데 늦은 밤 되면 너무 끊겨요")
    if message.content == "씨퓨야 프레드봇": 
        await message.channel.send("예전엔 너무 끊겼었는데 요즘엔 괜찮아졌어요")
    if message.content == "씨퓨야 엄준식": 
        await message.channel.send("ㅖ?그게뭐죠 사람이름은 아닐거고 대충 엄마가준비한식사 이런건가")
    if message.content == "씨퓨야 노래": 
        await message.channel.send("ㅖ?")
    if message.content == "씨퓨야 히오스":
        await message.channel.send("응?친구들 아직도 그 갓겜을 해보지 못한거야?")
        await asyncio.sleep(3)
        await message.channel.send("지금 바로 시공의 폭풍에서 전설의 영웅들을 만나보자구~!!")
        await asyncio.sleep(3)
        await message.channel.send("우-와 상상만 해도 떨리는걸?")
        await asyncio.sleep(3)
        await message.channel.send("♚♚히어로즈 오브 더 스☆톰♚♚가입시$$전원 카드팩☜☜뒷면100%증정※ ♜월드오브 워크래프트♜펫 무료증정￥ 특정조건 §§디아블로3§§★공허의유산★초상화획득기회@@ 즉시이동http://kr.battle.net/heroes/ko/ 무료 서비스/레스토랑급 시설/5대5 초이스/정원코스/항만코스/골짜기코스/에이스 매일밤 52명 출연/달콤살벌 노바/귀여운 동생 리리/상큼발랄 제이나/ ★【히오스】★ 24시간 영업 연중무휴") 
    if message.content == "씨퓨야 10초타이머":
        await message.channel.send("째깍째깍째깍...")
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}님 10초가 지났어요!")
    if message.content == "씨퓨야 5초타이머":
        await message.channel.send("째깍째깍째깍...")
        await asyncio.sleep(5)
        await message.channel.send(f"{message.author.mention}님 5초가 지났어요!")
    if message.content == "씨퓨야 15초타이머":
        await message.channel.send("째깍째깍째깍...")
        await asyncio.sleep(15)
        await message.channel.send(f"{message.author.mention}님 15초가 지났어요!")
    if message.content == "20초타이머":
        await message.channel.send("째깍째깍째깍...")
        await asyncio.sleep(20)
        await message.channel.send(f"{message.author.mention}님 20초가 지났어요!")
    if message.content == "25초타이머":
        await message.channel.send("째깍째깍째깍...")
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}님 10초가 지났어요!")
    if message.content == "30초타이머":
        await message.channel.send("째깍째깍째깍...")
        await asyncio.sleep(30)
        await message.channel.send(f"{message.author.mention}님 30초가 지났어요!")
    if message.content == "라면타이머":
        await message.channel.send("째깍째깍째깍...")
        await asyncio.sleep(180)
        await message.channel.send(f"{message.author.mention}님 3분이 지났어요!")
    if message.content == "씨퓨야 ㅋ":
        await message.channel.send(f"{message.author.mention}ㅋ")
    if message.content == "씨퓨야 핑해봐":
        await message.channel.send(f"{message.author.mention}")

    if message.content == '씨퓨야 업타임':
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await message.channel.send(f"{hours}시간 {minitues}분 {seconds}초 동안 씨퓨가 일했어요!")

    if  message.content == "씨퓨야 패치노트":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.green(), title="씨퓨 패치노트", description="이번에 추가된 기능")
        embed.add_field(name="1.내 정보 기능이 추가되었습니다.", value="씨퓨에게 내 정보라고 말해서 자신의 가입일과 id를 알아보세요!")
        embed.add_field(name="2.습격을 추천해주는 기능이 추가되었습니다.", value="무슨 습격을 할 지 모르겠을땐 씨퓨에게 추천습격이라고 말해보세요!")
        embed.add_field(name="3.습격 멤버를 구인할 수 있는 기능이 추가되었습니다.", value="에블핑을 사용하기 때문에 너무 많이 쓰면 사람들이 싫어할 수도 있어요!")
        embed.add_field(name="4.봇의 정보를 볼 수 있는 기능이 생겼습니다.", value="씨퓨에게 봇 정보라고 말해서 봇이 들어가있는 서버 개수를 확인해보세요!")
        embed.add_field(name="5.청소 기능이 추가되었습니다.", value=".청소 명령어를 사용해서 메세지를 청소해보세요!")
        embed.add_field(name="6.찬반투표 기능이 추가되었습니다.", value="씨퓨에게 찬반이라고 말하면 투표를 할 수 있어요!")
        await message.channel.send(embed=embed)
        
    if  message.content == "씨퓨야 도움말":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.green(), title="도움말", description="씨퓨가 할 수 있는 것들")
        embed.add_field(name="씨퓨가 말할 수 있는 말들", value="안녕,ㅎㅇ,민초,그타,둠피,ㄹㅇ,히히,주인,패치노트,내정보,옵투,카습 엘리트조건,핑,내정보,나무위키,업타임,타이머,랜덤,배그,옵치,레식,히오스,둠삭필")
        embed.add_field(name="씨퓨야 추천습격", value="무슨 습격을 할 지 모르겠을땐 씨퓨에게 추천습격이라고 말해보세요!")
        embed.add_field(name="씨퓨야 (습격 이름)", value="습격의 수입을 볼 수 있어요!")
        embed.add_field(name="씨퓨야 (습격 이름)구인", value="습격 멤버를 구인할 수 있어요!")
        embed.add_field(name="씨퓨야 카습(목표물 이름)", value="자신의 목표물이 뭔지 알리면서 구인을 할 수 있어요!")
        embed.add_field(name="씨퓨야 ㅗ", value="ㅗㅗ")
        embed.add_field(name="씨퓨야 패치노트", value="이번에 추가된 기능을 볼 수 있어요!")
        embed.add_field(name="씨퓨야 업타임", value="봇이 실행된 시간을 볼 수 있어요!")
        embed.add_field(name="씨퓨야 핑", value="봇의 지연 시간을 확인할 수 있어요!")
        embed.add_field(name="씨퓨야 차량리뷰", value="그타에 나오는 이동 수단을 추천해줘요!근데 일반 채팅방에서 하면 도배가 될 수 있으니 이 명령어 쓸거면 봇채팅방으로 ㄱㄱ")
        embed.add_field(name="씨퓨야 봇 정보", value="봇이 들어간 서버 개수와 봇을 쓰는 인원을 확인할 수 있어요!")
        await message.channel.send("DM으로 도움말을 보냈어요!")
        if message.author.dm_channel:
            await message.author.dm_channel.send(embed=embed)
        elif message.author.dm_channel is None:
            channel = await message.author.create_dm()
            await channel.send(embed=embed)

    if  message.content == "씨퓨야 차량리뷰":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.green(), title="씨퓨가 타본 이동 수단", description="직접 구매 후 사용해본 이동 수단만 리뷰함")
        embed.add_field(name="1.프로젠 TR4", value="성능은 나쁘지 않은데 이차살돈이면 크리거를 산다.")
        embed.add_field(name="베네팩터 크리거", value="접지력이랑 핸들링,가속력,최고속도까지 다 좋다.돈이 있다면 사는거 추천")
        embed.add_field(name="디클라스 스크램제트", value="부스터 쓸 수 있는 시간도 길고 점프기능도 있는데 부스터쓰다가 어디 부딫혀서 돌면서 날아가면 제어가 안된다.")
        embed.add_field(name="듀바치 바그너", value="가성비 좋다고해서 사봤는데 꺼무위키에 나온거랑은 다르게 접지력은 별로였다.근데 가속력이랑 핸들링은 나쁘진 않았었던걸로 기억함")
        embed.add_field(name="그로티 투리스모 R", value="적당한 슈퍼카 사고싶은데 젠토르노는 별로라고 하면 이거사면된다.성능도 나쁘지 않고 디자인도 예쁨")
        embed.add_field(name="그로티 비질란테", value="습격할때도 좋고 시민차 날릴때도 좋은데 휠베이스가 길어서 핸들링이 별로였다.습격할때 차나 비행기 터트릴거면 토레아도르 쓰는게 나을수도 있다.")
        embed.add_field(name="그로티 퓨리아", value="가변스포일러 달려있고 디자인도 이쁘고 성능도 평타는 치는데 최고속도가 높진 않다.근데 핸들링이랑 접지력이 좋아서 도시 돌아다니는 용도로는 추천함.")
        embed.add_field(name="오셀럿 페네트레이터", value="가격은 88만달러밖에 안하는데 가속력 좋고 접지력도 나쁘지 않다.내가 타봤을땐 나쁘지 않았음.")
        embed.add_field(name="오셀럿 XA-21", value="디자인도 나쁘지 않고 성능 좋고 접지력이랑 핸들링도 좋다.돈 있으면 사는걸 추천.")
        embed.add_field(name="오버플로드 아타크", value="후륜구동이라서 초반에 휠스핀 있는거 빼면 나쁘지 않은 차다.")
        embed.add_field(name="오버플로드 타이런트", value="디자인 이쁘고 핸들링이랑 접지력까지 좋은데 초반에 가속이 답답하다.")
        embed.add_field(name="페가시 젠토르노", value="성능도 좋고 디자인도 이쁘다.가격도 72만달러정도라서 가성비 슈퍼카 찾는거면 이서 사면 된다.")
        embed.add_field(name="페가시 리퍼", value="예쁜 쓰레기")
        embed.add_field(name="페가시 템페스타", value="성능도 나쁘지 않고 디자인도 이쁘다.이쁜 차 사고싶은데 리퍼는 너무 쓰레기라서 사기 싫으면 이거 추천함.")
        embed.add_field(name="테저렉트", value="디자인도 나쁘지 않고 전기차라서 엔진음 조용하고 가속력도 좋다.전기차 단점이었던 최고속도도 높기 때문에 비싸긴 해도 돈값 하는 차다.")
        embed.add_field(name="피스터 811", value="가속력 좋고 디자인 좋은데 접지력이랑 핸들링이 구림.")
        embed.add_field(name="프린시페 디베스트 에이트", value="가속력 좋고 최고속도 높은데 휠베이스가 길어서 핸들링이 별로다.")
        embed.add_field(name="프로젠 이탈리 GTB 커스텀", value="디자인 이쁘고 성능도 나쁘지 않다.커브 돌때 미끄러지긴 하는데 카운터쳐주면 바로 돌아온다.가성비 좋음.")
        embed.add_field(name="프로젠 T20", value="가변스포일러 달려있고 디자인 이쁘다.좀 비싸긴 한데 슈퍼카 살거면 이것도 나쁘지 않음.")
        embed.add_field(name="트루페이드 네로 커스텀", value="이쁘고 성능 좋다.가성비 좋음.")
        embed.add_field(name="트루페이드 트랙스", value="다들 핸들링이 좋다고 하는데 난 별로 못느꼈음.근데 차 성능은 좋다.사도 후회는 안함.")
        await message.channel.send("DM으로 차량 리뷰를 보냈어요!")
        if message.author.dm_channel:
            await message.author.dm_channel.send(embed=embed)
        elif message.author.dm_channel is None:
            channel = await message.author.create_dm()
            await channel.send(embed=embed)

    if message.content == "씨퓨야 핑":
        la = client.latency
        await message.channel.send(f'{str(round(la * 1000))}ms')

    if message.content == "씨퓨야 추천습격":
        r = ["구습", "카습", "페습", "신습"]
        embed=discord.Embed(color=0x000000, title=f"추천습격", description=random.choice(r))
        await message.channel.send(embed=embed)
    if message.content == "씨퓨야 룰렛":
        r = ["룰렛 기능은 지원 중지되었습니다."]
        embed=discord.Embed(color=0x000000, title=f"룰렛 지원 중지됨", description=random.choice(r))
        await message.channel.send(embed=embed)
    if message.content == "씨퓨야 러시안룰렛":
        r = ["철컥","철컥","철컥","철컥","철컥","**탕**"]
        embed=discord.Embed(color=0x000000, title=f"총", description=random.choice(r))
        await message.channel.send(embed=embed)
    if message.content == "씨퓨야 둠피키우기":
        r = ["이런...둠피가 힐을 못받아서 죽었어요", "이런...둠피가 밥을 안먹어서 죽었어요", "이런...둠피가 삭제됐어요", "이런...둠피가 빡빡이라서 죽었어요","이런...둠피가 힐을 못받아서 죽었어요","이런...둠피가 힐을 못받아서 죽었어요","이런...둠피가 힐을 못받아서 죽었어요","이런...둠피가 심장마비로 죽었어요","이런...둠피가 자신의 머리를 보고 너무 밝아서 눈이 멀었어요","둠피가 잘 자라다가 섬난맞고 죽었어요","둠피가 잘 자라다가 너무 잘 자라서 죽었어요","이런...둠피가 둠피스트라서 죽었어요","둠피스트가 그냥 죽었어요","둠피스트가 브론즈라서 죽었어요","둠피스트를 너무 잘해서 자신의 역겨움을 감당하지 못하고 죽었어요","둠피가 밥을 너무 많이 먹어서 죽었어요"]
        embed=discord.Embed(color=0x000000, title=f"둠피키우기", description=random.choice(r))
        await message.channel.send(embed=embed)
    if message.content == "씨퓨야 나무위키":
        r = ["꺼라","씹덕위키"]
        embed=discord.Embed(color=0x000000, title=f"룰렛 지원 중지됨", description=random.choice(r))
        await message.channel.send(embed=embed)

    if message.content == "씨퓨야 카드 줘": 
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.green(), title="카드", description=random.randint(2, 10))
        embed.add_field(name="카드", value=random.randint(2, 10))
        await message.channel.send(embed=embed)
    if message.content == "히트": 
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.green(), title="카드", description=random.randint(2, 10))
        await message.channel.send(embed=embed)
    if message.content == "스탠드":
        await message.channel.send(f"{message.author.mention}님이 스탠드하셨습니다.")

    if message.content == "씨퓨야 블랙잭 도움말": 
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.green(), title="규칙", description="")
        embed.add_field(name="기본적인 규칙", value="카드의 합이 21점이 되면 블랙잭이고 21점에 가장 가깝게 만들면 승리해요!그리고 21을 초과하면 패배해요!")
        embed.add_field(name="카드 설명", value="카드는 2부터 10까지 있고 K나 Q,J는 10으로 계산해요!그리고 A는 1점 또는 11점으로 계산하게 돼요.플레이어가 1로 계산할지 11로 계산할지 정할 수 있어요!")
        embed.add_field(name="블랙잭", value="처음 2장의 카드가 A와 10(J,Q,K를 포함)해서 21점이 된 것을 블랙잭이라고 해요!블랙잭을 가지고 있는 플레이어를 제외한 다른 플레이어는 패배해요!")
        embed.add_field(name="버스트", value="카드의 합이 21을 넘으면 버스트되고 게임에서 패배해요!")
        embed.add_field(name="히트", value="처음 2장의 상태에서 카드를 더 뽑는 것을 히트라고 해요!21이 되지 않는 한 얼마든지 원하는 만큼 카드를 뽑을 수 있어요!")
        await message.channel.send(embed=embed)

    if message.content == "씨퓨야 디엠보내봐":
        if message.author.dm_channel:
            await message.author.dm_channel.send("시러")
        elif message.author.dm_channel is None:
            channel = await message.author.create_dm()
            await channel.send("시러")

    if message.content.startswith("씨퓨야 봇 정보"):
        users = len(client.users)
        servers = len(client.guilds)
        await message.channel.send(f"씨퓨가 있는 서버 수는 {servers}개고 씨퓨를 쓰는 유저 수는 {users}명이에요!")

    if message.content == "현대차" or message.content == "기아차" or message.content == "현기차" or message.content == "씨발" or message.content == "개새끼" or message.content == "새끼" or message.content == "병신" or message.content == "지랄" or message.content == "^^ㅣ발" or message.content == "우짱" or message.content == "수님" or message.content == "신태일" or message.content == "씨1발" or message.content == "시1발" or message.content == "ㅆㅂ" or message.content == "병1신" or message.content == "좇같네" or message.content == "좆같네" or message.content == "혐초":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title=":no_entry_sign:경고!", description=f"{message.author.mention}님 욕하지 마세여!")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
        await message.delete()

    if message.content.startswith(".청소"):
        if message.content == '.청소':
            await message.channel.send(f"{message.author.mention} ,  \n몇 개를 청소할지 적어주세요.")
        else:
            if message.author.guild_permissions.administrator:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(f"{message.author.mention} ,  \n{number}개의 메시지를 삭제했습니다.\n(이 메시지는 잠시 후에 삭제됩니다.)")
                await asyncio.sleep(2)
                await a.delete()
            else:
                await message.channel.send(f"{message.author.mention} ,  \n메세지를 삭제할 수 없습니다.")

    if message.content.startswith("씨퓨야 박제해"):
        a = await message.channel.send('시러')
        await a.pin()

    if message.content == "씨퓨야 서버정보":
        embed=discord.Embed(title=message.guild.name, color=0x000000)
        embed.set_thumbnail(url=message.guild.icon_url) #서버의 아이콘
        embed.add_field(name="서버생성일", value=message.guild.created_at.strftime("20%y년 %m일 %d일".encode('unicode-escape').decode()).encode().decode('unicode-escape'),inline=False) #.strftime 뒤로 안적으로 오우 보기 싫어집니다.
        embed.add_field(name="서버주인", value=message.guild.owner.name, inline=False) #서버의 주인을 불러옵니다.
        embed.add_field(name="상세정보", value="인원수: " + str(len(message.guild.members)) + "명\n" + "역할수: " +str(len(message.guild.roles)) + "개\n 이모티콘 수: " + str(len(message.guild.emojis)) + "개", inline=False) #서버의 인원수, 역할수, 이모티콘수를 불러옵니다.
        await message.channel.send(embed=embed)

    if message.content.startswith('씨퓨야 찬반'):
        subject = message.content [6:]
        embed=discord.Embed(title="찬반투표!", description="찬성은 따봉을 반대는 싫어요 반응을 눌러주세요!", color=0x0088ff)
        embed.add_field(name="주제", value=subject, inline=False)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    if message.content == "씨퓨야 가위" or message.content == "씨퓨야 바위" or message.content == "씨퓨야 보":
        random_ = random.randint(1, 3)

        if random_ == 1:
            if message.content == "씨퓨야 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저도 가위! 비겼습니다.")
            elif message.content == "씨퓨야 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 가위! {message.author.mention}님이 이겼습니다.")   
            elif message.content == "씨퓨야 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 가위! 제가 이겼습니다.")   
        elif random_ == 2:
            if message.content == "씨퓨야 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 바위! 제가 이겼습니다.")
            elif message.content == "씨퓨야 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저도 바위! 비겼습니다.")   
            elif message.content == "씨퓨야 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 바위! {message.author.mention}님이 이겼습니다.")
        elif random_ == 3:
            if message.content == "씨퓨야 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 보! {message.author.mention}님이 이겼습니다.")
            elif message.content == "씨퓨야 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 보! 제가 이겼습니다.")   
            elif message.content == "씨퓨야 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저도 보! 비겼습니다.")
        random_ = random.randint(1, 3)

    if message.content.startswith("씨퓨야 내정보"):
        status = str(message.author.status)
        if status == "online":
            status = "온라인🟢"
        elif status == "dnd":
            status = "방해금지⛔"
        elif status == "idle":
            status = "자리비움🟡"
        else:
            status = "오프라인⚪"
        if message.author.bot == False:
            bot = "유저"
        else:
            bot = "봇"
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f'{message.author.name}의 정보')
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="별명", value=message.author.display_name)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id)
        embed.add_field(name="상태", value=f"{status}", inline=False)
        embed.add_field(name="최상위 역할", value=message.author.top_role.mention, inline=False)
        embed.add_field(name="봇", value=bot)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("씨퓨야 킥"):
        if message.author.guild_permissions.kick_members:
            userid = message.content[3:]
            user_id = re.findall("\d+", userid)
            userkick = message.guild.get_member(int(user_id[0]))
            await message.guild.kick(userkick)
            await message.channel.send(str(userkick) + "님을 추방했어요!")

    if message.content.startswith("씨퓨야 밴"):
        if message.author.guild_permissions.ban_members:
            userid = message.content[3:]
            user_id = re.findall("\d+", userid)
            userban = message.guild.get_member(int(user_id[0]))
            await message.guild.ban(userban)
            await message.channel.send(str(userban) + "님을 차단했어요!")

    if message.content == "씨퓨야 핑 인민들":    
        commander = discord.utils.get(message.guild.roles, name="하찮고 하찮은 불쌍한 인민들")
        await message.channel.send("{} 라는 역할을 가지고 계신 분들!누군가가 여러분들을 불렀어요!".format(commander.mention))
    if message.content == "씨퓨야 핑 수령":    
        commander = discord.utils.get(message.guild.roles, name="위대하신 우리 수령 장군님")
        await message.channel.send("{} 라는 역할을 가지고 계신 분들!누군가가 여러분들을 불렀어요!".format(commander.mention))
    if message.content == "씨퓨야 핑 인민들":    
        commander = discord.utils.get(message.guild.roles, name="하찮고 하찮은 불쌍한 인민들")
        await message.channel.send("{} 라는 역할을 가지고 계신 분들!누군가가 여러분들을 불렀어요!".format(commander.mention))

@client.event
async def on_member_join(member):
    await member.guild.get_channel(797113862092226580).send(member.mention + "님이 서버에 들어왔어요!모두 환영해 주자구요.")
    return

@client.event
async def on_member_remove(member):
    await member.guild.get_channel(797113862092226580).send(member.mention + "님이 서버에서 나갔어요.ㅃ")
    return

@client.event
async def on_member_join(member):
    await member.guild.get_channel(752345407694045286).send(member.mention + "님이 서버에 들어왔어요!모두 환영해 주자구요.")
    return

@client.event
async def on_member_remove(member):
    await member.guild.get_channel(800706052240572447).send(member.mention + "님이 서버에서 나갔어요.ㅃ")
    return

@client.event
async def on_guild_join(server):
    print(server,"서버에 접속했습니다!")

@client.event
async def on_guild_remove(server):
    print(server,"서버에서 연결이 끊겼습니다..") 
 
client.run(token)