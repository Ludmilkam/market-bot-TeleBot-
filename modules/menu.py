import telebot
import modules.button as bt
list_items = []
menu_bar = telebot.types.ReplyKeyboardMarkup()

menu_bar.add(bt.bt1)
menu_bar.add(bt.bt2)
menu_bar.add(bt.bt3)
