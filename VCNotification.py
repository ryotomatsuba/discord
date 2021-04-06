import discord
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(member, before, after):
    if (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(828806453920792596)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} {member.mention} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} {member.mention} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

client.run("ODI4ODI2MDEwMjg3NjAzNzMy.YGvOXw.MLQPptS6rfOom-AK7X1Dsu7p1fU")