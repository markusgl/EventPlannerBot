from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Interpreter

def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)

    # output directory for the trained model
    trainer.persist(model_dir, fixed_model_name="eventplannernlu")


def test_nlu(text):
    interpreter = Interpreter.load('models/rasa-nlu/default/eventplannernlu')
    print(interpreter.parse(text))


if __name__ == '__main__':
    #train_nlu('validation_set/validation_set.json', 'config_rasa-nlu.yml', 'models/rasa-nlu')
    test_nlu(u"Ich will was unternehmen")