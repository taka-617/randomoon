import discord
import random
import asyncio
import os
from dotenv import load_dotenv
from db import participant
from db import stage
from db import weapon
from db import weaponHistory
from db import insiderTheme
from discord import Intents, Client, Embed
from random import randint

#python3 discordbot.py

load_dotenv()

# トークンの値は.envに設定
TOKEN = os.environ['BOT_TOKEN']

JOIN_EMOJI_NAME = os.environ['JOIN_EMOJI_NAME']
LEAEVE_EMOJI_NAME = os.environ['LEAEVE_EMOJI_NAME']

stage_count = stage.countAll()
selected_stages = []

it_numbers = {}

insider_guess_time = 0

insider_game_time_max = 300

is_guess = True

# 接続に必要なオブジェクトを生成
intents: Intents = Intents.default()
client: Client = Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global is_guess
    global insider_game_time_max
    global insider_guess_time
    channel_id = message.channel.id
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '/random': 
        participants = participant.selectAll()
        if len(participants) == 0:
            await message.channel.send('参加者がいないデシ')

            return
        selected_stage = stage.selectRandom(selected_stages)
        selected_stages.append(str(selected_stage[0]))
        if len(selected_stages) == stage_count:
            selected_stages.clear()

        embeds = Embed(title="次のステージ", description="{}".format(selected_stage[1]), inline=False)
        for participant_data in participants:
            id = participant_data[1]
            weapon_data = weapon.selectWeaponRandom()
            weapon_discription = "<@{}>".format(id)
            weapon_discription += "\n{}".format(weapon_data['main_weapon'])
            if weapon_data['main_id'] > weapon_data['sub_id']:
                weapon_discription += "(または{})".format(weapon_data['sub_weapon'])
            embeds.add_field(name="", value="{}".format(weapon_discription), inline=True)
            weaponHistory.insert(weapon_data['main_id'], participant_data[1])

        await client.get_channel(channel_id).send(embed=embeds)
    if message.content == '/random_unique': 
        participants = participant.selectAll()
        if len(participants) == 0:
            await message.channel.send('参加者がいないデシ')

            return
        selected_stage = stage.selectRandom(selected_stages)
        selected_stages.append(str(selected_stage[0]))
        if len(selected_stages) == stage_count:
            selected_stages.clear()

        embeds = Embed(title="次のステージ", description="{}".format(selected_stage[1]), inline=False)
        for participant_data in participants:
            id = participant_data[1]
            weapon_data = weapon.selectWeaponRandomUnique(id)
            weapon_discription = "<@{}>".format(id)
            weapon_discription += "\n{}".format(weapon_data['main_weapon'])
            if weapon_data['main_id'] > weapon_data['sub_id']:
                weapon_discription += "(または{})".format(weapon_data['sub_weapon'])
            embeds.add_field(name="", value="{}".format(weapon_discription), inline=True)
            weaponHistory.insert(weapon_data['main_id'], participant_data[1])

        await client.get_channel(channel_id).send(embed=embeds)
    if message.content == '/start':
        embeds = Embed(description="hello <@1247085866741137418>") 
        msg = await client.get_channel(channel_id).send(embed=embeds)
        print(msg.id)
    if message.content == '/users':
        participants = participant.selectAll()

        description = "今の参加者一覧デシ"
        for participant_data in participants:
            id = participant_data[1]
            description += "\n<@{}>".format(id)

        embeds = Embed(description=description) 
        msg = await client.get_channel(channel_id).send(embed=embeds)
    if message.content == '/reset_user':
        participant.trancate()
        await message.channel.send('参加者をリセットしたデシ')
    if message.content == '/reset_weapon_history':
        weaponHistory.trancate()
        await message.channel.send('ブキの履歴をリセットしたデシ')
    if message.content == '/dm_send':
        await message.author.send('test')
    if message.content == '/it_random':
        participants = participant.selectAll()
        it_numbers = {}
        for participant_data in participants:
            id = participant_data[1]
            is_in = False
            while is_in == False:
                number = random.randint(1,100)
                if number in it_numbers:
                    continue
                else:
                    it_numbers[number] = id
                    is_in = True
            user = await client.fetch_user(id)
            await user.send('あなたの数字は {} デシ'.format(number))
        await message.channel.send('数字を配ったデシ')
    if message.content == '/it_open':
        description = "答え合わせデシ"
        for number, id in it_numbers.items():
            description += "\n<@{}>：{}".format(id, number)
        embeds = Embed(description=description) 
        msg = await client.get_channel(channel_id).send(embed=embeds)

    if message.content == '/insider_ready':
        participants = participant.selectAll()
        list = random.sample(participants, 2)
        master = list[0]
        master_id = master[1]
        user = await client.fetch_user(master_id)
        theme = insiderTheme.selectRandom()
        await user.send('お題は {} デシ'.format(theme['theme']))
        await message.channel.send('<@{}> がマスター デシ'.format(master_id))
        insider = list[1]
        insider_id = insider[1]
        user = await client.fetch_user(insider_id)
        await user.send('お題は {} デシ'.format(theme['theme']))

    if message.content == '/insider_game_start':
        insider_game_time = insider_game_time_max
        description = "お題を当てるデシ"
        description += "\n残り{}秒".format(insider_game_time)
        embeds = Embed(description=description) 
        msg = await client.get_channel(channel_id).send(embed=embeds)
        while is_guess:
            insider_game_time -= 1
            insider_guess_time += 1
            if insider_game_time == 0:
                embeds = Embed(description="終了デシ") 
                await msg.edit(embed=embeds)
                break
            description = "お題を当てるデシ"
            description += "\n残り{}秒".format(insider_game_time)
            embeds = Embed(description=description) 
            await msg.edit(embed=embeds)
            await asyncio.sleep(1)

    if message.content == '/insider_game_finish':
        is_guess = False
        description = "お題が当たったデシ"
        description += "\nインサイダーを当てる時間は{}秒 デシ".format(insider_guess_time)
        embeds = Embed(description=description) 
        msg = await client.get_channel(channel_id).send(embed=embeds)

    if message.content == '/insider_guess_start':
        description = "インサイダーを当てるデシ"
        description += "\n残り{}秒".format(insider_guess_time)
        embeds = Embed(description=description) 
        msg = await client.get_channel(channel_id).send(embed=embeds)
        while True:
            insider_guess_time -= 1
            if insider_guess_time == 0:
                embeds = Embed(description="終了デシ") 
                await msg.edit(embed=embeds)
                break
            description = "インサイダーを当てるデシ"
            description += "\n残り{}秒".format(insider_guess_time)
            embeds = Embed(description=description) 
            await msg.edit(embed=embeds)
            await asyncio.sleep(1)

@client.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == JOIN_EMOJI_NAME :
        part = participant.selectOne(payload.user_id)
        if part is None:
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            embeds = Embed(description="<@{}> が参加するデシ".format(payload.user_id))

            participant.insert(payload.user_id)
            channel_id = message.channel.id
            await client.get_channel(channel_id).send(embed=embeds)
    if payload.emoji.name == LEAEVE_EMOJI_NAME :
        part = participant.selectOne(payload.user_id)
        if part is not None:
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            embeds = Embed(description="<@{}> が参加を取りやめたデシ".format(payload.user_id))

            participant.delete(payload.user_id)
            channel_id = message.channel.id
            await client.get_channel(channel_id).send(embed=embeds)
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)