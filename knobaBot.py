# Инициализация бота с использованием его токена
bot = telebot.TeleBot("")


# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=['name'])
def send_name(message):
    bot.reply_to(message, 'Привет! Меня зовут knoba!')


# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)


# Запуск бота
bot.polling()
