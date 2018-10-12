'''
from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-421095818547-423731229538-439653236854-390c971007e0cdf0297166d10c7fb9c2', #app verification token
							'xoxb-421095818547-438103386900-mkp2CGNTqjEIf6xYwUuKu9nr', # bot verification token
							'9XUqz59tnc2TCdmWFTaOrbub', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
'''

from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxb-421095818547-438103386900-mkp2CGNTqjEIf6xYwUuKu9nr' # bot user authentication token
                           )

agent.handle_channels([input_channel], 5004, serve_forever=True)