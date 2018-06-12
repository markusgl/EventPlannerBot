## story 0
* greet
    - utter_introduce
* introduce{"name": "max"}
    - action_add_me
* goodbye
    - utter_goodbye
    - action_clear_slots
    
## story 1
* greet
    - utter_introduce
* introduce
    - utter_name_not_understood    
* introduce{"name": "sabrina"}
    - action_add_me
* goodbye
    - utter_goodbye
    - action_clear_slots

## Generated Story -1143961169235137103
* greet
    - utter_ask_howcanhelp
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_add_me
    - export
    
## Generated Story -1143961169235137103
* greet
    - utter_ask_howcanhelp
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_add_me
    - export
