from modules import *


bot = Application.builder().token(TOKEN).build()

bot.add_handler(MessageHandler(filters.ALL,on_message))

bot.run_polling(allowed_updates=Update.ALL_TYPES)