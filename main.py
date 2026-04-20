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

client = TelegramClient('sessao/telegram_deal_monitor', api_id, api_hash)

def enviar_notificacao(texto):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, json={'chat_id': chat_id, 'text': texto})

group_list = [
      -1001610005189,
      -1001409539217,
      -1001871700299,
      -1002149012596,
      -1001903791112,
      -5270931373
]

pecas_alvo = [
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

filtro_regex = f"(?i)({ '|'.join(pecas_alvo) })"

print(f"Monitorando {len(group_list)} grupos...")

@client.on(events.NewMessage(chats=group_list))
async def handler(event):
    texto = event.message.text
    if texto and re.search(filtro_regex, texto):
        print(f"Mensagem recebida de: {event.chat_id} - {texto}")
        enviar_notificacao(f"Promoção encontrada!\n\n{texto}")

with client:
      print("Programa rodando!")
      client.run_until_disconnected()
