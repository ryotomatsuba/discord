import discord
from datetime import datetime, timedelta
import pytz
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from CONSTS import *

# discord client
client = discord.Client()
# google calendar 
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
service = build('calendar', 'v3', credentials=creds)
join_time={}
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(member, before, after):
    
    if (before.channel != after.channel):
        now = datetime.now(pytz.timezone('Asia/Tokyo')).isoformat()
        alert_channel = client.get_channel(VC_NOTIFICATION_ID)
        if member.nick:
            member_name=member.nick
        else:
            member_name=member.name
        lounge_event=LOUNGE_EVENT_TEMPLATE.copy()
        if before.channel is None: 
            msg = f'{member_name} が {after.channel.name} に参加しました。'
            await alert_channel.send(msg)
            join_time[member_name]=now

        elif after.channel is None: 
            msg = f'{member_name} が {before.channel.name} から退出しました。'
            lounge_event['summary']=member_name
            lounge_event['start']['dateTime']=join_time[member_name]       
            lounge_event['end']['dateTime']=now
            service.events().insert(calendarId=CALENDAR_ID, body=lounge_event).execute()
            await alert_channel.send(msg)

async def on_message(message):
    pass

client.run("ODI4ODI2MDEwMjg3NjAzNzMy.YGvOXw.MLQPptS6rfOom-AK7X1Dsu7p1fU")