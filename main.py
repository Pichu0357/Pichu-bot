from hata import Client
from hata.ext.commands import setup_ext_commands
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.environ.get('Token')
Pichu = Client(Token)
setup_ext_commands(Pichu, '$')

@Pichu.events
async def ready(client):
    print(f'{client:f} logged in.')

@Pichu.events
async def message_create(client, message):
    if message.author.is_bot:
        return

    lowercase_conversion = message.content.lower()

    if lowercase_conversion == 'ping':
        await client.message_create(message.channel, 'pong')

Pichu.start()
