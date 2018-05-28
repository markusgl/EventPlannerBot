from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import json

from rasa_core.agent import Agent
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.telegram import TelegramInput
#from interpreter import Interpreter
from interpreter_dialogflow import Interpreter

logger = logging.getLogger(__name__)


def run_cli_bot(serve_forever=True):
    interpreter = Interpreter()
    agent = Agent.load('./models/dialogue', interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
        
    return agent


def run_telegram_bot():
    with open('keys.json') as f:
        data = json.load(f)
    telegram_api_key = data['telegram-api-key']

    interpreter = Interpreter()
    agent = Agent.load('./models/dialogue', interpreter)

    input_channel = (TelegramInput(access_token=telegram_api_key,
                                   verify='event123_bot',
                                   webhook_url='4c276b10.ngrok.io/app/webhoook',
                                   debug_mode=True))

    agent.handle_channel(HttpInputChannel(5004, '/app', input_channel))


if __name__ == '__main__':
    run_cli_bot()
    #run_telegram_bot()
