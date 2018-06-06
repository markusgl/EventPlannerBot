## Story 1
* find_appointment{"relativedate": "heute"}    
    - slot{"relativedate": "heute"}
    - action_search_appointment
    - utter_goodbye
    
## Story 2
* greet
    - utter_ask_howcanhelp
* find_appointment
    - utter_ask_time
    - action_search_appointment
    
## Story 3
* greet
    - utter_ask_howcanhelp
* find_appointment{"datetime": "06.05.2018"}
    - utter_ask_time
    - action_search_appointment
    
## Story 4
* find_appointment
    - utter_ask_time
    - action_search_appointment
    
## Generated Story -2253719340681464826
* greet
    - utter_ask_howcanhelp
* find_appointment{"relativedate": "heute"}
    - slot{"relativedate": "heute"}

## Generated Story 984826086781566823
* greet
    - utter_ask_howcanhelp
* find_appointment{"appointment": "termine", "relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - action_search_appointment
    
## Generated Story 6999645622301093630
* find_appointment{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - action_search_appointment
