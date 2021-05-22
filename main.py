from hata import Client, Guild
from hata.ext.commands import setup_ext_commands
from hata.ext.slash import setup_ext_slash
from hata.ext.extension_loader import EXTENSION_LOADER
from dotenv import load_dotenv
import os

# loading the .env file
load_dotenv()

TOKEN = os.environ.get('TOKEN')
GUILD = Guild.precreate(os.environ.get('GUILD_ID'))

Pichu = Client(TOKEN)
setup_ext_commands(Pichu, '$')
setup_ext_slash(Pichu)


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


EXTENSION_LOADER.add_default_variables(Pichu=Pichu)

for command in os.listdir('commands'):
    if command.endswith('.py'):
        EXTENSION_LOADER.add(f'commands.{command[:-3]}', Pichu=Pichu)


EXTENSION_LOADER.load_all()
Pichu.start()
