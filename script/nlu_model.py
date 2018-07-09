from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import shutil
import os
# from __future__ import unicode_literals
#commit h
def train_nlu(data, configs, model_dir):
	if os.path.exists("../models"):
		shutil.rmtree("../models")
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'cct-bot-nlu')

def run_nlu():
	interpreter = Interpreter.load('../models/nlu/default/cct-bot-nlu')
	print(interpreter.parse(u'coconut'))

if __name__ == '__main__':
	train_nlu('../data/data.json', '../config/config_spacy.yml', '../models/nlu')
	# run_nlu()
