import discord
import sys, os
from CONSTS import *

# discord client
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    sys.stdout.flush()

# vc in/out action
@client.event
async def on_voice_state_update(member, before, after):
    
    if (before.channel != after.channel):
        alert_channel = client.get_channel(VC_NOTIFICATION_ID)
        member_name=member.nick if member.nick else member.name
        if before.channel is None: 
            msg = f'{member_name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)

        elif after.channel is None: 
            msg = f'{member_name} が {before.channel.name} から退出しました。'
            await alert_channel.send(msg)

# message action
async def on_message(message):
    pass

# main
if __name__ == '__main__':
    # discord token
    token = os.environ['DISCORD_API_TOKEN']
    # discord login
    client.run(token)