from time import perf_counter


@Pichu.interactions(is_global=True)
async def ping(client, event):
    """pong!!!"""
    start = perf_counter()
    yield
    delay = (perf_counter()-start)*1000.0
    yield f"{delay:.0f} ms"


@Pichu.commands
async def ping(client, message):
    start = perf_counter()
    await client.typing(message.channel)
    delay = (perf_counter()-start)*1000.0
    return f"{delay:.0f} ms"

