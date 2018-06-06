## story 0 no activity, no location, no time
* greet
    - utter_ask_howcanhelp
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
