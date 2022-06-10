
from commands import main_start_handler, start_handler , get_text_one , get_text_two , info , setting , setting_seter
from telegram.ext import Updater, CommandHandler , CallbackQueryHandler,ConversationHandler ,MessageHandler
from telegram.ext.filters import Filters
from bot_text import dict_msg

# 0 , 1 , 2 , 3 for conversation handling
FIRST , SECOND , THIRD , FOURTH= range(4)


def main ():
    #token
    
    updater = Updater(" YOUR TOKEN ")

    #addcommand
    

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("start",main_start_handler)],
        states={

            FIRST: [CallbackQueryHandler(get_text_one, pattern="^translate$"),
                    CallbackQueryHandler(info, pattern="^info$"),
                    CallbackQueryHandler(setting,  pattern="^setting$")
                    ],
            SECOND: [MessageHandler(Filters.regex(dict_msg["user_msg"]),get_text_two),
                    CallbackQueryHandler(start_handler, pattern="^back$"),
                    CallbackQueryHandler(info, pattern="^info$")],

            THIRD : [CallbackQueryHandler(setting_seter, pattern = "^fa$")
                    ,CallbackQueryHandler(setting_seter, pattern = "^en$"),
                    CallbackQueryHandler(setting_seter, pattern = "^ar$"),
                    CallbackQueryHandler(setting_seter, pattern = "^ru$")
                    ,CallbackQueryHandler(setting_seter, pattern = "^fr$"),
                    CallbackQueryHandler(setting_seter, pattern = "^it$"),
                    CallbackQueryHandler(setting_seter, pattern = "^zh-CN$"),
                    CallbackQueryHandler(setting_seter, pattern = "^de$"),
                    CallbackQueryHandler(setting_seter, pattern = "^es$"),
                    CallbackQueryHandler(start_handler, pattern="^back$"),
                    CallbackQueryHandler(info, pattern="^info$")],

            FOURTH: [CallbackQueryHandler(start_handler, pattern="^back$")]
  
        },
        fallbacks=[CommandHandler("start",main_start_handler)],
        allow_reentry=False,
    )

    updater.dispatcher.add_handler(conversation_handler)


    #start

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()