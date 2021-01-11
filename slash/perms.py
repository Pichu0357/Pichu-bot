from hata import Embed


@Pichu.interactions(guild=TEST_GUILD)
async def perms(client, event):
    """Shows your permissions."""
    user_permissions = event.user_permissions
    if user_permissions:
        description = '\n'.join(permission_name.replace('_', '-') for permission_name in user_permissions)
    else:
        description = '*none*'

    user = event.user
    return Embed('Permissions', description).add_author(user.avatar_url, user.full_name)