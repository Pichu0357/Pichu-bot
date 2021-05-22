from hata import Color, Embed, Emoji
import os


CAT_FISH = Emoji.precreate(os.environ.get('CAT_FISH'))
CAT_COLOR = Color.from_html('#000000')

BASE_URL = 'https://nekos.life/api/v2'
HTTP = Pichu.http


@Pichu.interactions(is_global=True)
async def cat(client, event):
    """I will be good neko! moo!"""
    try:
        async with HTTP.get(BASE_URL+'/img/meow') as response:
            if response.status != 200:
                return "Couldn't contact the API right now..."
            data = await response.json()
        return Embed(f"Here is your cat {CAT_FISH:e}", color=CAT_COLOR).\
            add_image(data['url'])
    except (OSError, ConnectionError):
        return None


@Pichu.commands
async def cat(client, message):
    try:
        async with HTTP.get(BASE_URL+'/img/meow') as response:
            if response.status != 200:
                return "Couldn't contact the API right now..."
            data = await response.json()
        return Embed(f"Here is your cat {CAT_FISH:e}", color=CAT_COLOR).\
            add_image(data['url'])
    except (OSError, ConnectionError):
        return None

