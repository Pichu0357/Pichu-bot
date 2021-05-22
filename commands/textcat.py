BASE_URL = 'https://nekos.life/api/v2'
HTTP = Pichu.http


@Pichu.interactions(is_global=True)
async def textcat(client, event):
    """I will send textcats :3"""
    try:
        async with HTTP.get(BASE_URL+'/cat') as response:
            if response.status != 200:
                return "Couldn't contact the API right now... OwO"
            data = await response.json()
        return data['cat']
    except (OSError, ConnectionError):
        return None


@Pichu.commands
async def textcat(client, message):
    try:
        async with HTTP.get(BASE_URL+'/cat') as response:
            if response.status != 200:
                return "Couldn't contact the API right now... OwO"
            data = await response.json()
        return data['cat']
    except (OSError, ConnectionError):
        return None
