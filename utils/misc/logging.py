import logging

logging.basicConfig(
    format=u'[%(asctime)s] %(message)s',
    level=logging.INFO,
    filename='bot.log',  # Loglarni 'bot.log' fayliga yozish
    filemode='w'         # Har safar faylni qayta yozish
)
