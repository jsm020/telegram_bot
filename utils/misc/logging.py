import logging

logging.basicConfig(
    format=u'[%(asctime)s] %(message)s',
    level=logging.INFO,
    filename='bot.log',  # write all logs in bot.log
    filemode='w'         # every moment can write again
)
