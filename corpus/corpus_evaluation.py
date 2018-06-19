from interpreter_luis import Interpreter
import json

interpreter = Interpreter('../keys.json')

with open("../rasa-nlu/data/data.json", "r", encoding='utf-8') as f:
    data = json.load(f)

examples = data["rasa_nlu_data"]["common_examples"]
tp_scores = {}
fp_scores = {}
for example in examples:
    #print("Intent: " + example['intent'])
    #print("Utterance: " + example['text'])

    intent = example['intent']
    utterance = example['text']
    resp = json.loads((interpreter.send_api_request(utterance)).decode('utf-8'))

    resp_intent = resp["topScoringIntent"]["intent"]
    resp_conf_score = resp["topScoringIntent"]["score"]

    print(resp_intent)
    if resp_intent == intent:
        if example['intent'] in tp_scores.keys():
            tp_scores[example['intent']] += 1
        else:
            tp_scores[example['intent']] = 1
    else:
        if example['intent'] in fp_scores.keys():
            fp_scores[example['intent']] += 1
        else:
            fp_scores[example['intent']] = 1


# evaluate scores
for intent, score in tp_scores.items():
    if intent in fp_scores.keys():
        fp_score = fp_scores[intent]
    else:
        fp_score = 0

    print("Score for {} {}".format(intent, (score / (score + fp_score))*100))