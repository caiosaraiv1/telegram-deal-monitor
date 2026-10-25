import os
import re
import requests
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

client = TelegramClient('session/telegram_deal_monitor', api_id, api_hash)

def send_notification(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, json={'chat_id': chat_id, 'text': text})

group_list = [
      -1001610005189,
      -1001409539217,
      -1001871700299,
      -1002149012596,
      -1001903791112,
      -5270931373
]

target_parts = [
    r'5700x',
    r'9060\s?xt',
    r'16gb.*ddr4.*cl16',
    r'ssd.*1tb.*nvme',
    r'b550m',
    r'(750w|850w).*gold.*modular',
    r'arct?ic.*p12',
    r'lian\s?li.*a3',
    r'asus.*ap201',
    r'deepcool.*ch260',
    r'27.*(qhd|1440p).*(180|165|170)\s?hz'
]

regex_filter = f"(?i)({ '|'.join(target_parts) })"

print(f"Monitoring {len(group_list)} groups...")

@client.on(events.NewMessage(chats=group_list))
async def handler(event):
    text = event.message.text
    if text and re.search(regex_filter, text):
        print(f"Message received from: {event.chat_id} - {text}")
        send_notification(f"Deal found!\n\n{text}")

with client:
      print("Program running!")
      client.run_until_disconnected()
