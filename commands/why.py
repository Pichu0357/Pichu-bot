BASE_URL = 'https://nekos.life/api/v2'
HTTP = Pichu.http


@Pichu.interactions(is_global=True)
async def why(client, event):
    """why are you using this commands?"""
    try:
        async with HTTP.get(BASE_URL+'/why') as response:
            if response.status != 200:
                return "Couldn't contact the API right now... WHY?"
            data = await response.json()
        return data['why']
    except (OSError, ConnectionError):
        return None


@Pichu.commands
async def why(client, message):
    try:
        async with HTTP.get(BASE_URL+'/why') as response:
            if response.status != 200:
                return "Couldn't contact the API right now... WHY?"
            data = await response.json()
        return data['why']
    except (OSError, ConnectionError):
        return None

