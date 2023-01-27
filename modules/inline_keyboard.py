import telebot 



inline_bt1 = telebot.types.InlineKeyboardButton("Замовити",
                                                callback_data = "замовити"
                                                )
inline_bt2 = telebot.types.InlineKeyboardButton(
                                                "Перейти до сайту",
                                                url  = "https://yabloki.ua/ukr/iphone-14-pro-max-deep-purple-128gb.html"
                                                )
inline_bt3 = telebot.types.InlineKeyboardButton(
                                                "Перейти до сайту",
                                                url = "https://yabloki.ua/ukr/iphone-14-blue-128gb.html"
                                                )
inline_bt4 = telebot.types.InlineKeyboardButton(
                                                "Перейти до сайту",
                                                url = "https://yabloki.ua/ukr/zarjadnaja-stancija-ecoflow-river-mini-210-vt-g-wireless-riverminiwireless.html"
                                                )
inline_bt5 = telebot.types.InlineKeyboardButton(
                                                "Перейти до сайту",
                                                url = "https://yabloki.ua/ukr/macbook-air-13-apple-m2-256gb-starlight-2022-mly23.html"
                                                )
inline_bt6 = telebot.types.InlineKeyboardButton(
                                                "Перейти до сайту",
                                                url = "https://yabloki.ua/ukr/air-pods-pro-2.html"
                                                )
inline_keyboard1 = telebot.types.InlineKeyboardMarkup()
inline_keyboard1.add(inline_bt1)
inline_keyboard1.add(inline_bt2)

inline_keyboard2 = telebot.types.InlineKeyboardMarkup()
inline_keyboard2.add(inline_bt1)
inline_keyboard2.add(inline_bt3)

inline_keyboard3 = telebot.types.InlineKeyboardMarkup()
inline_keyboard3.add(inline_bt1)
inline_keyboard3.add(inline_bt4)

inline_keyboard4 = telebot.types.InlineKeyboardMarkup()
inline_keyboard4.add(inline_bt1)
inline_keyboard4.add(inline_bt5)

inline_keyboard5 = telebot.types.InlineKeyboardMarkup()
inline_keyboard5.add(inline_bt1)
inline_keyboard5.add(inline_bt6)

