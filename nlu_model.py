from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
# from __future__ import unicode_literals

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'cct-bot-nlu')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/cct-bot-nlu')
	print(interpreter.parse(u'i need a gun for personal protection'))
	
if __name__ == '__main__':
	#train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	run_nlu()
