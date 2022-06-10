from telegram.ext import CallbackContext
from telegram import Update, ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
from bot_text import dict_msg
from googletrans import Translator

# 0 , 1 , 2 , 3 for conversation handling
FIRST, SECOND, THIRD, FOURTH = range(4)

# country tags for finding index of user language target
country_tag = ["fa", "en", "ar", "ru", "fr", "it", "zh-CN", "de", "es"]


# names of supported country in country_name list
country_name = ["فارسي-🇮🇷", "انگليسي-🏴󠁧󠁢󠁥󠁮󠁧󠁿", "عربي-🇦🇪", "روسيه-🇷🇺",
                "فرانسوي-🇫🇷", "ايتاليايي-🇮🇹", "چيني-🇨🇳", "آلماني-🇩🇪", "اسپانيايي-🇪🇸"]


# Is the first function to be executed if user send /start command
def main_start_handler(update=Update,  context=CallbackContext):
    # first name of user for saying welcome
    firstname = update.message.chat.first_name
    # For it to send message to user
    chat_id = update.message.chat_id
    # chat action shows typing... in bot
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)

    buttons = [
        [
            InlineKeyboardButton("شروع ترجمه", callback_data="translate")
        ],
        [
            InlineKeyboardButton("تنظیمات", callback_data="setting")
        ],
        [
            InlineKeyboardButton("ارتباط با ما", url="https://t.me/Thiirty"),
            InlineKeyboardButton(
                "گیت هاب", url="https://github.com/amirhoseinG/FATSRAN-telegram-bot"),
            InlineKeyboardButton("راهنما", callback_data="info")
        ]
    ]
    # send message to user
    update.message.reply_text(
        text=dict_msg["start_msg"].format(firstname),
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    # connect to get_text_one  and back , info functions
    return FIRST


# such main_start_handler function but this function run in conversation if user Select back button
def start_handler(update=Update,  context=CallbackContext):

    buttons = [
        [
            InlineKeyboardButton("شروع ترجمه", callback_data="translate")
        ],
        [
            InlineKeyboardButton("تنظیمات", callback_data="setting")
        ],
        [
            InlineKeyboardButton("ارتباط با ما", url="https://t.me/Thiirty"),
            InlineKeyboardButton(
                "گیت هاب", url="https://github.com/amirhoseinG/FATSRAN-telegram-bot"),
            InlineKeyboardButton("راهنما", callback_data="info")
        ]
    ]

    # bot edit message
    context.bot.editMessageText(text=dict_msg["menu"], chat_id=dict_msg["user_chat_id"],
                                message_id=dict_msg["user_msg_id"], reply_markup=InlineKeyboardMarkup(buttons))

    # connect to get_text_one and back , info
    return FIRST



def get_text_one(update=Update,  context=CallbackContext):
    query = update.callback_query

    buttons = [[InlineKeyboardButton("بازگشت", callback_data="back"), InlineKeyboardButton(
        "راهنما", callback_data="info")]]
    dict_msg["user_chat_id"] = query.message.chat_id
    dict_msg["user_msg_id"] = query.message.message_id
    # edit bot message
    context.bot.editMessageText(text=dict_msg["start_msg2"], chat_id=dict_msg["user_chat_id"],
                                message_id=dict_msg["user_msg_id"], reply_markup=InlineKeyboardMarkup(buttons))

    # connect to get_text_two and back , info

    return SECOND


def get_text_two(update=Update,  context=CallbackContext):

    # get user message
    dict_msg["user_msg"] = update.message.text

    # use googletrans library to translate user message
    translator = Translator()

    # get Results 
    result = translator.translate(
        dict_msg["user_msg"], dest=dict_msg["user_to_lang"])

    # retry button    
    button = [[InlineKeyboardButton("شروع مجدد", callback_data="back")]]

    # bot changing text to result
    context.bot.editMessageText(
        text=result.text, chat_id=dict_msg["user_chat_id"], message_id=dict_msg["user_msg_id"], reply_markup=InlineKeyboardMarkup(button))

    # connect to start_handler
    return FOURTH


# info function
def info(update=Update, context=CallbackContext):
    query = update.callback_query
    dict_msg["user_chat_id"] = query.message.chat_id
    dict_msg["user_msg_id"] = query.message.message_id
    context.bot.send_chat_action(dict_msg["user_chat_id"], ChatAction.TYPING)

    buttons = [
        [
            InlineKeyboardButton("بازگشت", callback_data="back")
        ],
        [
            InlineKeyboardButton(
                "گیت هاب", url="https://github.com/amirhoseinG/FATSRAN-telegram-bot"),
            InlineKeyboardButton("ارتباط با ما", url="https://t.me/Thiirty")
        ]]

    # bot edit message gives bot information
    context.bot.editMessageText(text=dict_msg["info_msg"], chat_id=dict_msg["user_chat_id"],
                                message_id=dict_msg["user_msg_id"], reply_markup=InlineKeyboardMarkup(buttons))

    # connect to start_handler
    return FOURTH


    
# getter setting function
def setting(update=Update,  context=CallbackContext):

    # update query data
    query = update.callback_query
    # detect set language for To show in message
    lang_index = country_tag.index(dict_msg["user_to_lang"])
    # set user message and user chat id
    dict_msg["user_chat_id"] = query.message.chat_id
    dict_msg["user_msg_id"] = query.message.message_id

    # edit bot message and show language button for changing target
    context.bot.editMessageText(text=dict_msg["start_msg4"].format(country_name[lang_index]), chat_id=dict_msg["user_chat_id"],
                                message_id=dict_msg["user_msg_id"], reply_markup=InlineKeyboardMarkup(dict_msg["settings_btn"]))

    # connect to setting_seter and back , info functions
    return THIRD


# setter setting function
def setting_seter(update=Update,  context=CallbackContext):

    # update query data
    query = update.callback_query
    # get button data
    data = query.data
    # detect set language for show in message
    data_index = country_tag.index(data)
    # set language target
    dict_msg["user_to_lang"] = data

    # edit bot message
    context.bot.editMessageText(text=dict_msg["change_trans_to"].format(country_name[data_index]), chat_id=dict_msg["user_chat_id"],
                                message_id=dict_msg["user_msg_id"], reply_markup=InlineKeyboardMarkup(dict_msg["settings_btn"]))

    # this function dosent have return
    # END setting
