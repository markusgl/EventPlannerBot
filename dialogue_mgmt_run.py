from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.telegram import TelegramInput
from interpreter import Interpreter

logger = logging.getLogger(__name__)
TELEGRAM_API_KEY = '590846089:AAHppWEHq_AlVPjCfDLP8nB4cMNbL6scPws'


def run_cli_bot(serve_forever=True):
    interpreter = Interpreter()
    agent = Agent.load('./models/dialogue', interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
        
    return agent


def run_telegram_bot():
    interpreter = Interpreter()
    agent = Agent.load('./models/dialogue', interpreter)

    input_channel = (TelegramInput(access_token=TELEGRAM_API_KEY,
                                   verify='event123_bot',
                                   webhook_url='3f667559.ngrok.io/app/webhoook',
                                   debug_mode=True))

    agent.handle_channel(HttpInputChannel(5004, '/app', input_channel))


if __name__ == '__main__':
    #run_cli_bot()
    run_telegram_bot()