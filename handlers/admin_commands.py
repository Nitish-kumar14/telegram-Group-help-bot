from telegram import Update, ChatPermissions
from telegram.ext import CallbackContext

def ban(update: Update, context: CallbackContext) -> None:
    if not update.message.reply_to_message:
        update.message.reply_text('Reply to the user you want to ban.')
        return
    user_id = update.message.reply_to_message.from_user.id
    context.bot.ban_chat_member(update.message.chat_id, user_id)
    update.message.reply_text('User banned.')

def unban(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 1:
        update.message.reply_text('Usage: /unban <user_id>')
        return
    user_id = context.args[0]
    context.bot.unban_chat_member(update.message.chat_id, user_id)
    update.message.reply_text('User unbanned.')

def kick(update: Update, context: CallbackContext) -> None:
    if not update.message.reply_to_message:
        update.message.reply_text('Reply to the user you want to kick.')
        return
    user_id = update.message.reply_to_message.from_user.id
    context.bot.kick_chat_member(update.message.chat_id, user_id)
    update.message.reply_text('User kicked.')

def mute(update: Update, context: CallbackContext) -> None:
    if not update.message.reply_to_message:
        update.message.reply_text('Reply to the user you want to mute.')
        return
    user_id = update.message.reply_to_message.from_user.id
    context.bot.restrict_chat_member(update.message.chat_id, user_id, permissions=ChatPermissions(can_send_messages=False))
    update.message.reply_text('User muted.')

def unmute(update: Update, context: CallbackContext) -> None:
    if not update.message.reply_to_message:
        update.message.reply_text('Reply to the user you want to unmute.')
        return
    user_id = update.message.reply_to_message.from_user.id
    context.bot.restrict_chat_member(update.message.chat_id, user_id, permissions=ChatPermissions(can_send_messages=True))
    update.message.reply_text('User unmuted.')
