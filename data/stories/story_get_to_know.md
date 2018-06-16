## story 0
* greet
    - utter_greet
* introduce{"name": "max"}
    - action_search_me
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
    - action_search_me
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_clear_slots

## story 2
* greet
    - utter_greet
* introduce{"name": "markus"}
    - action_search_me
* decline
    - action_add_me
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_clear_slots

## story 2
* greet
    - utter_greet
* introduce{"name": "markus"}
    - action_search_me
* agree
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - action_clear_slots
      
## Generated Story -1143961169235137103
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_search_me
    - export
    
## Generated Story -1143961169235137103
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_search_me
    - export
  
## Generated Story -8067309347047915342
* greet
    - utter_greet
* introduce
    - action_search_me
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
    - action_search_me
* get_to_know
    - utter_introduce
    - export

## Generated Story -8191107739883788886
* greet
    - utter_greet
* introduce{"firstname": "luis"}
    - slot{"firstname": "luis"}
    - action_search_me
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - export

## Generated Story -8191107739883788886
* greet
    - utter_greet
* introduce{"firstname": "luis"}
    - slot{"firstname": "luis"}
    - action_search_me
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - export

## Generated Story -38057090118977811
* greet
    - utter_greet
* introduce{"firstname": "dieter"}
    - slot{"firstname": "dieter"}
    - action_search_me
    - utter_ask_howcanhelp
    - export

## Generated Story -6170250799943936569
* greet
    - utter_greet
* introduce{"firstname": "dieter"}
    - slot{"firstname": "dieter"}
    - action_search_me
    - utter_ask_howcanhelp
    - export

## Generated Story -7272174495735342007
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_search_me
* decline
    - action_add_me
    - utter_ask_howcanhelp
    
## Generated Story -4728680521305444966
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_search_me
* decline
    - action_add_me
    - slot{"me_name": "markus"}
    - utter_ask_howcanhelp
    - export
    
## Generated Story 4937872231076660150
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_search_me
* agree
    - utter_ask_howcanhelp
* goodbye
    - utter_goodbye
    - export

## Generated Story 631808384204120259
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_search_me
* decline
    - action_add_me
    - slot{"me_name": "markus"}
    - utter_ask_howcanhelp
    - export
