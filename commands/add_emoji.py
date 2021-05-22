from hata import Permission
from hata.ext.commands import checks


async def PERMISSION_CHECK_HANDLER(client, message, command, check):
    permission_names = ' '. join(permission_name.replace('_', ' ') for permission_name in check.permissions)
    text = f'You must have {permission_names} permission to invoke `{command.display_name}` command.'
    await client.message_create(message, text, allowed_mentions='!replied_user')


CHECK_MANAGE_EMOJIS = checks.has_guild_permissions(
        Permission().update_by_keys(manage_emojis=True),
        handler=PERMISSION_CHECK_HANDLER,
        )


@Pichu.commands(checks=CHECK_MANAGE_EMOJIS)
async def add_emoji(client, message, emoji: 'emoji', emoji_name: str = None):
    guild = message.guild
    
    if guild is None:
        return
    
    if emoji.is_unicode_emoji():
        return "That's an unicode emoji, cannot add it."

    normal_static, normal_animated, managed_static, managed_animated = guild.emoji_counts
    if (normal_animated if emoji.animated else normal_static) >= guild.emoji_limit:
        return 'Cannot add more emojis to the guild, limit reached.'

    if emoji_name is None:
        emoji_name = emoji.name

    emoji_icon = await client.download_url(emoji.url)
    added_emoji = await client.emoji_create(guild, emoji_name, emoji_icon)

    return f'{added_emoji} has been added.'
