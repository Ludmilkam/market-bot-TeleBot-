
import telebot
import modules.button
import modules.menu as menu
import modules.bot_creation as m_bot
import modules.send_message
import modules.pictures.url as url
import modules.inline_keyboard as inline_keyboard
import modules.find_path as find_path
import os
user = m_bot.bot.get_me()

@m_bot.bot.message_handler(commands=["start"])
def bot_start(message):
    m_bot.bot.send_message(message.chat.id, "Оберіть категорію", reply_markup = menu.menu_bar)
    m_bot.bot.register_next_step_handler(message, press_bt_s)
# @m_bot.bot.message_handler(content_types= ["text"])

def press_bt_s(message):
    if message.text == "NEW":
        for i in range(5):
            if i == 0:
                keyboard = inline_keyboard.inline_keyboard1
            if i == 1:
                keyboard = inline_keyboard.inline_keyboard2
            if i == 2:
                keyboard = inline_keyboard.inline_keyboard3
            if i == 3:
                keyboard = inline_keyboard.inline_keyboard4
            if i == 4:
                keyboard = inline_keyboard.inline_keyboard5
            path_image = find_path.find_path()
            path_image = os.path.join(path_image, f"modules/pictures/bt{i + 1}.jpg")
            m_bot.bot.send_photo(
                message.chat.id, 
                open(path_image, "rb"), reply_markup = keyboard)



    if message.text == "SALE":
        for i in range(5):
            if i == 0:
                keyboard = inline_keyboard.inline_keyboard1
            if i == 1:
                keyboard = inline_keyboard.inline_keyboard2
            if i == 2:
                keyboard = inline_keyboard.inline_keyboard3
            if i == 3:
                keyboard = inline_keyboard.inline_keyboard4
            if i == 4:
                keyboard = inline_keyboard.inline_keyboard5
            path_image = find_path.find_path()
            path_image = os.path.join(path_image, f"modules/pictures/bt{i + 1}.jpg")
            m_bot.bot.send_photo(
                message.chat.id, 
                open(path_image, "rb"), reply_markup = keyboard)
        



    if message.text == "DISCOUNTS":
        for i in range(5):
            if i == 0:
                keyboard = inline_keyboard.inline_keyboard1
            if i == 1:
                keyboard = inline_keyboard.inline_keyboard2
            if i == 2:
                keyboard = inline_keyboard.inline_keyboard3
            if i == 3:
                keyboard = inline_keyboard.inline_keyboard4
            if i == 4:
                keyboard = inline_keyboard.inline_keyboard5
            path_image = find_path.find_path()
            path_image = os.path.join(path_image, f"modules/pictures/bt{i + 1}.jpg")
            m_bot.bot.send_photo(
                message.chat.id, 
                open(path_image, "rb"), reply_markup = keyboard)


# @m_bot.bot.callback_query_handler(func = lambda callback: callback.data)     
# def send_link(callback):
#     if callback == "замовити":
#         m_bot.bot.send_message(callback.message.chat.id, "Замовлення оформлено")










m_bot.bot.polling(none_stop = True)
