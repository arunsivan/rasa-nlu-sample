from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel

agent = Agent.load("../models/dialogue", interpreter=RasaNLUInterpreter("../models/nlu/default/cct-bot-nlu"))
agent.handle_channel(ConsoleInputChannel())