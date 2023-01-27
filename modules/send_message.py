import telebot
import modules.bot_creation as m_bot


@m_bot.bot.callback_query_handler(func = lambda callback: callback.data)     
def send_link(callback):
    if callback.data == "замовити":
        m_bot.bot.send_message(callback.message.chat.id, "Замовлення оформлено")
        m_bot.bot.send_message(-695748294, "Хтось зробив замовлення")
    


