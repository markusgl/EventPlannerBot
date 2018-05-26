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
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
    
## story 1 no location, no time
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "nürnberg"}
    - utter_ask_time
* search_event{"datetime": "morgen"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
        
## story 2 no time
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "location": "nürnberg"}
    - utter_ask_time
* search_event{"datetime": "morgen"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
    
## story 3 
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "location": "nürnberg", "relativedate": "heute"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
    
    
## story 2.0 no activity, no location, no relativedate
* greet
    - utter_ask_howcanhelp
* search_event
    - utter_ask_activity
* search_event{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "berlin"}
    - utter_ask_time
* search_event{"relativedate": "morgen"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
    
## story 2.1 no location, no time
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "nürnberg"}
    - utter_ask_time
* search_event{"relativedate": "morgen"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
        
## story 2.2 no time
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "location": "nürnberg"}
    - utter_ask_time
* search_event{"relativedate": "morgen"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
    
## story 2.3 
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "location": "nürnberg", "relativedate": "heute"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots

## story 2.3 
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "relativedate": "heute"}
    - utter_ask_location
* search_event{"activity": "kino", "relativedate": "heute", "location": "berlin"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
    
    
## story 3.0 no activity, no location, no dateperiod
* greet
    - utter_ask_howcanhelp
* search_event
    - utter_ask_activity
* search_event{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "berlin"}
    - utter_ask_time
* search_event{"dateperiod": "die nächsten Tage"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - action_clear_slots
    - utter_goodbye    
    
## story 3.1 no location, no time
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "nürnberg"}
    - utter_ask_time
* search_event{"dateperiod": "nächste Woche"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - action_clear_slots
    - utter_goodbye    
        
## story 3.2 no time
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "location": "nürnberg"}
    - utter_ask_time
* search_event{"dateperiod": "am Wochenende"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
    
## story 3.3 
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "location": "nürnberg", "dateperiod": "am Wochenende"}
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    - action_clear_slots
    
## GENERATED STORIES ##

## Generated Story 4786450448284027413
* greet
    - utter_ask_howcanhelp
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - utter_ask_location
* search_event{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.datetime": "1", "builtin.number": "1"}
    - utter_ask_invite
* selection
    - action_clear_slots
    - utter_goodbye
## Generated Story 4786450448284027413
* greet
    - utter_ask_howcanhelp
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - utter_ask_location
* search_event{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.datetime": "1", "builtin.number": "1"}
    - utter_ask_invite
* selection
    - action_clear_slots
    - utter_goodbye
  
## Generated Story 2820955377654008137
* greet
    - utter_ask_howcanhelp
* search_event{"activity": "kino", "relativedate": "heute"}
    - slot{"activity": "kino"}
    - slot{"relativedate": "heute"}
    - utter_ask_location
* search_event{"location": "n\u00fcrnberg"}
    - slot{"location": "n\u00fcrnberg"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.number": "2"}
    - utter_ask_invite
* selection
    - utter_goodbye
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
* goodbye
    - action_clear_slots
    - utter_goodbye
