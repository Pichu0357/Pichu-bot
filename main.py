from hata import Client
from hata.ext.commands import setup_ext_commands
from hata.ext.slash import setup_ext_slash
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.environ.get('Token')
Pichu = Client(Token)
setup_ext_commands(Pichu, '$')
setup_ext_slash(Pichu, immediate_sync= True)

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

for commands in os.listdir("./commands/"):
    if (file.endswith('.py')):
        with open(f'commands/{commands}') as rk:
            exec(rk.read())

Pichu.start()
