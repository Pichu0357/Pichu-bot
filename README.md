# Pichu-bot
We are making a Discord bot using Hata API Wrapper


## About-Hata

Hata is an async Discord API wrapper written in Python named after Hata no Kokoro.

If naming a Discord API wrapper after a Touhou character is not enough to convince you to try it, it has got some
real stuff:

- Fast and simple asynchronous framework to write concurrent code using async/await syntax, but also great for
    embedding into a threaded system.
- Running more clients from the same instance.
- Shared entity cache between shards and clients.
- Feature rich API for common use cases.
- Fast rate limit handling.
- No member objects associated with guilds. Hata uses guild -> user -> guild relation enabling implementing
    cross-guild features more easily.
- Optimized dispatch event parsers depending on intents, client count and on handled events as well.
- Option to disable user presences or even user caching, although disabling user cache is not recommended.
- Command and extension loader extension.
- Audio sending and receiving.
- Can interacting with the Discord API without gateway connection.
- Switching between api version with environmental variable.


## Requirements
- [Hata](https://github.com/HuyaneMatsu/hata)
- [dotenv](https://pypi.org/project/python-dotenv/) 
- Python >= 3.9
