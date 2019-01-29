import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater,MessageHandler,CommandHandler,RegexHandler,CallbackQueryHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					filename='logging.txt',
					level=logging.INFO)

logger = logging.getLogger(__name__)

class card():
	def __int__(self,name,cost):
		self.name = name
		self.cost = 0

def create(bot,update):
	keyboard = [[]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	keyboard.append([InlineKeyboardButton('Village', callback_data="Village")])
	keyboard.append([InlineKeyboardButton('Silver', callback_data="Silver")])
	update.message.reply_text('Please Select:',reply_markup=reply_markup)

def button(bot,update):
	query = update.callback_query
	global Village
	if query.data == 'Village':
		Village = card()
		Village.name = 'Village'
		Village.cost = 3
		query.message.reply_text('You have created a Card name :' + str(Village.name) + '\nAnd it costs:' + str(Village.cost))
		
def start(bot,update):
	update.message.reply_text('normal')

def info(bot,update):
	global Village
	update.message.reply_text(str(str(Village.name) + str(Village.cost)))


def main():
	updater = Updater('688735688:AAG3tfiPI_6bHSBzYhZ69K-DmQltNfoH4jQ')
	test = updater.dispatcher
	test.add_handler(CommandHandler('create',create))
	test.add_handler(CommandHandler('start',start))
	test.add_handler(CommandHandler('info',info))
	test.add_handler(CallbackQueryHandler(button))
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()
	
	
	
	
	
	
	