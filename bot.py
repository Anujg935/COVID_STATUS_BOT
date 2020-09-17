from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from data_fetch import *
from newsHeadline import *


start_headline = 0 

def start(bot, update):
    chat_id = update.message.chat_id

    s = "<b>Welcome to COVID-19 Status Bot\n I will give you real time update about data as well a news about COVID-19.</b>\n"
    s = s + "You can control me by sending these commands:\n"
    s = s + "/India -gives data of COVID-19 cases in india.\n"
    s = s + "/World -gives data of COVID-19 cases for rest of thw world (top 5).\n"
    s = s + "/newsHeadLines -show top 5 latest news Headlines.\n"
    s = s + "/moreNews  - to get more news updates.\n"
    
    bot.sendMessage(chat_id=chat_id,text=s,parse_mode='HTML')

def hel(bot, update):
    chat_id = update.message.chat_id
    s = s + "<b>You can control me by sending these commands:</b>\n"
    s = s + "/India -gives data of COVID-19 cases in india.\n"
    s = s + "/World -gives data of COVID-19 cases for rest of thw world (top 5).\n"
    s = s + "/newsHeadLines -show top 5 latest news Headlines.\n"
    s = s + "/moreNews  - to get more news updates.\n"
    
    bot.sendMessage(chat_id=chat_id,text=s,parse_mode='HTML')
def India(bot, update):
    chat_id = update.message.chat_id

    total_cases,total_active_cases,deaths = getIndiaData()
    s = "<b>India</b> :\nTotal active cases : "+str(total_active_cases)+"\nDeaths : "+str(deaths)+"\nTotal Cases : "+str(total_cases)

    bot.sendMessage(chat_id=chat_id,text=s,parse_mode='HTML')

def World(bot, update):
    chat_id = update.message.chat_id

    data = getWorldData(5)
    s=""

    for k,v in data.items():
        s = s+"<b>"+k+"</b>\nTotal cases : "+v[0]+"\nDeaths : "+v[1]+"\n"

    bot.sendMessage(chat_id=chat_id,text=s,parse_mode='HTML')

def newsHeadLines(bot,update):
    chat_id = update.message.chat_id
    headlines = getNewsHeadlines()
    
    global start_headline
    start_headline = 0
    s = "<b>Top 5 Headlines on Coronavirus are:</b>\n"
    for i in range(5):
        s = s + headlines[i] +"\n"
        start_headline = start_headline + 1
    bot.sendMessage(chat_id=chat_id,text=s,parse_mode='HTML')


def moreNews(bot,update):
    chat_id = update.message.chat_id
    print(0)
    global start_headline
    
    if(start_headline != 0 ):
        s = "<b>Next 5 Headlines on Coronavirus are:</b>\n"
        headlines = getNewsHeadlines()
        print(len(headlines))
        for i in range(start_headline,start_headline+5):
            s = s + headlines[i] +"\n"
        
        start_headline = start_headline + 5
        bot.sendMessage(chat_id=chat_id,text=s,parse_mode='HTML')
    else:
        bot.sendMessage(chat_id=chat_id,text="First use /newsHeadLines\n",parse_mode='HTML')
  
def main():
    updater = Updater('Your telegram bot API token')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',hel))
    dp.add_handler(CommandHandler('India',India))
    dp.add_handler(CommandHandler('World',World))
    dp.add_handler(CommandHandler('newsHeadLines',newsHeadLines))
    dp.add_handler(CommandHandler('moreNews',moreNews))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()