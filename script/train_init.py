
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


import logging
import shutil

from rasa_core.agent import Agent
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
	logging.basicConfig(level='INFO')
	training_data_file = '../data/stories.md'
	model_path = '../models/dialogue'
	fallback = FallbackPolicy(fallback_action_name="utter_default",
                          core_threshold=0.3,
                          nlu_threshold=0.2)
	agent = Agent('../domain/cct-chatbot-nlu_domain.yml', policies = [MemoizationPolicy(max_history = 2), KerasPolicy(),fallback])

	agent.train(
			training_data_file,
			epochs = 500,
			batch_size = 10,
			validation_split = 0.2)

	agent.persist(model_path)
