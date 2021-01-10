import random
@Pichu.commands
async def ping(client, message):
    return 'Pong ' + str(random.randint(10, 200)) + 'ms'