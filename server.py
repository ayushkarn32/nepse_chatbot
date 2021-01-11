from bot import telegram_chatbot
import sharebot

bot = telegram_chatbot("config.cfg")

def make_reply(msg,f_name):
    reply = None
    if msg == "":
        reply =  "Hello {}, Welcome to My Telegram Bot. Enter -- /help -- for help".format(f_name)
    elif msg == "/help":
        reply = "I can help you please enter the tradecompany's symbol ex: ebl for Everest Bank limited  \n "
        #reply = "hello {}".format(f_name)
    else:
        reply=sharebot.marketvalue(msg)
    return reply

update_id = None
fl = True
pName = {""}
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
                f_name=str(item["message"]["from"]["first_name"])
            except:
                message = None
                f_name=None
            from_ = item["message"]["from"]["id"]
            if(pName == "" or f_name not in pName):
                reply = make_reply("",f_name)
                bot.send_message(reply,from_)
                pName.add(f_name)
            else:
                reply = make_reply(message,f_name)
                bot.send_message(reply,from_)
  

