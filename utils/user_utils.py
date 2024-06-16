from telegram import Bot
from telegram.error import BadRequest

def get_all_usernames(bot: Bot, chat_id: int, bot_username: str) -> list:
    usernames = []
    try:
        # Fetch chat administrators instead of members
        members = bot.get_chat_administrators(chat_id)
        for member in members:
            user = member.user
            if user.username and user.username != bot_username:
                usernames.append(f"@{user.username}")
            elif user.username != bot_username:
                usernames.append(user.first_name)
    except BadRequest:
        pass
    return usernames
