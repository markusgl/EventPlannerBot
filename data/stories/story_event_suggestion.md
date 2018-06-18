## story 0 no activity, no location, no time
* greet
    - utter_greet
* search_event
    - utter_ask_activity
* search_event{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "berlin"}
    - utter_ask_time
* search_event{"datetime": "morgen"}
    - action_search_events
    - action_suggest
    - utter_ask_invite
    - action_search_contact
* goodbye
    - utter_goodbye
    - action_clear_slots
    
    
## GENERATED STORIES ##

## Generated Story -4205675749258817950
* greet
    - utter_greet
* search_event
    - utter_ask_activity
* search_event{"activity": "kino"}
    - slot{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "n\u00fcrnberg"}
    - slot{"location": "n\u00fcrnberg"}
    - export
 
## Generated Story -3387218605229212631
* greet
    - utter_greet
* introduce{"firstname": "markus"}
    - slot{"firstname": "markus"}
    - action_search_me
    - slot{"me_name": "markus"}
* agree
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "firstname": "lara"}
    - slot{"activity": "kino"}
    - slot{"firstname": "lara"}
    - action_search_contact
* contact_selection{"relationship": "schwester"}
    - slot{"relationship": "schwester"}
    - action_add_contact
    - utter_ask_time
* greet{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - action_search_events
* goodbye
    - export