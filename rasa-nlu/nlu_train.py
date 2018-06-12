from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Interpreter


def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    # output directory for the trained model
    trainer.persist(model_dir, fixed_model_name="weathernlu")

def run_nlu():
    interpreter = Interpreter.load('./models/nlu/default/weathernlu')
    print(interpreter.parse(u"Wie wird das Wetter in Berlin heute?"))


if __name__ == '__main__':
    print("training started...")
    train_nlu('./rasa-nlu/data/data.json', './rasa-nlu/config_spacy.json', './models/rasa-nlu')
    print("training finished.")