from hata import Color, Embed, Emoji
import os


NEKOGIRL_KISS = Emoji.precreate(os.environ.get("NEKOGIRL_KISS"))
NEKOGIRL_COLOR = Color.from_html('#FFB6C1')

@Pichu.interactions(is_global=True)
async def nekogirl(client, event):
    """wanna see nekogirls? OwO"""
    try:
        async with HTTP.get(BASE_URL+'/img/neko') as response:
            if response.status != 200:
                return "Couldn't contact the API right now..."
            data = await response.json()
        return Embed(f"Here is your nekogirl {NEKOGIRL_KISS:e}", color=NEKOGIRL_COLOR).\
            add_image(data['url'])
    except (OSError, ConnectionError):
        return None


@Pichu.commands
async def nekogirl(client, message):
    try:
        async with HTTP.get(BASE_URL+'/img/neko') as response:
            if response.status != 200:
                return "Couldn't contact the API right now..."
            data = await response.json()
        return Embed(f"Here is your nekogirl {NEKOGIRL_KISS:e}", color=NEKOGIRL_COLOR).\
            add_image(data['url'])
    except (OSError, ConnectionError):
        return None

