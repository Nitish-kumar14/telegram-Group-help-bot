import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from utils.user_utils import get_all_usernames


def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_photo(update.effective_chat.id, photo=open('images/image.jpg', 'rb'))
    keyboard = [
        [
            InlineKeyboardButton("Add 𝐀𝐍𝐈𝐌𝐄𝐕𝐄𝐑𝐒𝐄 To Your Group", url="https://t.me/YOUR_BOT_USERNAME?startgroup=true"),
        ],
        [
            InlineKeyboardButton("Support", url= "https://t.me/ANIMEVERSEDD"),
            InlineKeyboardButton("Update", url= "https://t.me/ANIMEVERSEDD"),
        ],
        [
            InlineKeyboardButton("Help & Commands", callback_data='help_commands')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f'Hi, {update.effective_user.first_name}!\nI am Your ANIMEVERSE bot  I am a group help bot and ', reply_markup=reply_markup)


def couple(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    bot_username = context.bot.username
    usernames = get_all_usernames(context.bot, chat_id, bot_username)
    
    if len(usernames) < 2:
        update.message.reply_text('Not enough users to form a couple.')
        return
    
    couple = random.sample(usernames, 2)
    
    # Path to your background image
    background_image_path = 'images/couple.jpg'
    
    # Send the background image with the couple's names
    with open(background_image_path, 'rb') as image:
        context.bot.send_photo(chat_id=chat_id, photo=image, caption=f'The couple is: {couple[0]} and {couple[1]}')

def show_help(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Available Commands:\n"
        "/start - Start the bot\n"
        "/ban - Ban a user\n"
        "/unban - Unban a user\n"
        "/kick - Kick a user\n"
        "/mute - Mute a user\n"
        "/unmute - Unmute a user\n"
    )
    update.edit_message_text(text=help_text)