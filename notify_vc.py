import discord
from datetime import datetime, timedelta
import pytz
import sys, os
from CONSTS import *

# discord client
client = discord.Client()

# # google calendar 
# if os.path.exists('token.json'):
#     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# # If there are no (valid) credentials available, let the user log in.
# if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#         creds.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             'credentials.json', SCOPES)
#         creds = flow.run_local_server(port=0)
#     # Save the credentials for the next run
#     with open('token.json', 'w') as token:
#         token.write(creds.to_json())
# creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# service = build('calendar', 'v3', credentials=creds)

# discord 
join_time={}
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
            # service.events().insert(calendarId=CALENDAR_ID, body=lounge_event).execute()
            await alert_channel.send(msg)

async def on_message(message):
    pass

client.run(os.environ["DISCORD_API_TOKEN"])