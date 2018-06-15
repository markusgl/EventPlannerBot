## story 0
* greet
    - utter_greet
* introduce{"name": "max"}
    - action_add_me
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_clear_slots
    
## story 1
* greet
    - utter_greet
* introduce
    - utter_name_not_understood    
* introduce{"name": "sabrina"}
    - action_add_me
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_clear_slots

## Generated Story -1143961169235137103
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_add_me
    - export
    
## Generated Story -1143961169235137103
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_add_me
    - export
  
## Generated Story -8067309347047915342
* greet
    - utter_greet
* introduce
    - action_add_me
    - utter_ask_howcanhelp
* introduce
    - utter_name_not_understood
* introduce{"firstname": "max"}
    - slot{"firstname": "max"}
    - action_add_me
    - utter_ask_howcanhelp
    - export
    
## Generated Story 647496038402761424
* greet
    - utter_greet
* introduce{"firstname": "max"}
    - slot{"firstname": "max"}
    - action_add_me
* get_to_know
    - utter_introduce
    - export

## Generated Story -8191107739883788886
* greet
    - utter_greet
* introduce{"firstname": "luis"}
    - slot{"firstname": "luis"}
    - action_add_me
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - export

## Generated Story -8191107739883788886
* greet
    - utter_greet
* introduce{"firstname": "luis"}
    - slot{"firstname": "luis"}
    - action_add_me
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - export

## Generated Story -38057090118977811
* greet
    - utter_greet
* introduce{"firstname": "dieter"}
    - slot{"firstname": "dieter"}
    - action_add_me
    - utter_ask_howcanhelp
    - export

## Generated Story -6170250799943936569
* greet
    - utter_greet
* introduce{"firstname": "dieter"}
    - slot{"firstname": "dieter"}
    - action_add_me
    - utter_ask_howcanhelp
    - export