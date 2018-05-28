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
    - action_search_contact
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
    - action_search_contact
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
    - action_search_contact
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
    - action_search_contact
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
    - action_search_contact
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

## Generated Story -4546596856385291886
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - utter_ask_activity
* search_event{"activity": "kino"}
    - slot{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "n\u00fcrnberg"}
    - slot{"location": "n\u00fcrnberg"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.datetime": "1", "builtin.number": "1"}
    - utter_ask_invite
* contact_selection
    - action_search_contact
* contact_selection
    - export
## Generated Story -9090375821377452847
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - utter_ask_location
* search_event{"location": "n\u00fcrnberg"}
    - slot{"location": "n\u00fcrnberg"}
    - utter_ask_activity
* search_event{"activity": "kino"}
    - slot{"activity": "kino"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.number": "1", "builtin.datetime": "1"}
    - utter_ask_invite
* contact_selection
    - action_search_contact
* contact_selection{"builtin.datetime": "ja genau"}
    - utter_goodbye
    - export
## Generated Story -4546596856385291886
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - utter_ask_activity
* search_event{"activity": "kino"}
    - slot{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "n\u00fcrnberg"}
    - slot{"location": "n\u00fcrnberg"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.datetime": "1", "builtin.number": "1"}
    - utter_ask_invite
* contact_selection
    - action_search_contact
* contact_selection
    - export
## Generated Story -9090375821377452847
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - utter_ask_location
* search_event{"location": "n\u00fcrnberg"}
    - slot{"location": "n\u00fcrnberg"}
    - utter_ask_activity
* search_event{"activity": "kino"}
    - slot{"activity": "kino"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.number": "1", "builtin.datetime": "1"}
    - utter_ask_invite
* contact_selection
    - action_search_contact
* contact_selection{"builtin.datetime": "ja genau"}
    - utter_goodbye

## Generated Story -1264619619890341108
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - utter_ask_location
* search_event{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.datetime": "3", "builtin.number": "3"}
    - utter_ask_invite
* contact_selection
    - action_search_contact

## Generated Story 8147637031944812160
* search_event{"location": "berlin", "relativedate": "heute"}
    - slot{"location": "berlin"}
    - slot{"relativedate": "heute"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.number": "2"}
    - utter_ask_invite
* contact_selection
    - action_search_contact
* goodbye
    - export
## Generated Story 4392702703658739764
* search_event{"relativedate": "heute"}
    - slot{"relativedate": "heute"}
    - utter_ask_location
* search_event{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.number": "2"}
    - utter_ask_invite
* contact_selection
    - action_search_contact
* contact_selection{"relationship": "schwester"}
    - slot{"relationship": "schwester"}
    - action_search_contact
* contact_selection
    - utter_confirm

## Generated Story -3282871180467400832
* search_event{"relativedate": "heute", "activity": "kino", "location": "berlin"}
    - slot{"activity": "kino"}
    - slot{"location": "berlin"}
    - slot{"relativedate": "heute"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.number": "3", "builtin.datetime": "3"}
    - utter_ask_invite
* contact_selection{"relationship": "schwester"}
    - slot{"relationship": "schwester"}
    - action_search_contact
* contact_selection
    - utter_confirm_contact_invitation
* goodbye
    - utter_goodbye
    
## Generated Story 4 
* search_event{"relativedate": "heute", "activity": "kino", "firstname": "Max"}
    - slot{"activity": "kino"}    
    - slot{"relativedate": "heute"}
    - slot{"firstname": "Max"}
    - action_search_contact
* contact_selection
    - utter_ask_location
* search_event
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.datetime": "1", "builtin.number": "1"}
    - utter_confirm
    - utter_goodbye
    
## Generated Story 4 
* search_event{"relativedate": "heute", "activity": "kino", "relationship": "Schwester"}
    - slot{"activity": "kino"}    
    - slot{"relativedate": "heute"}
    - slot{"relationship": "schwester"}
    - action_search_contact
* contact_selection
    - utter_ask_location
* search_event
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.datetime": "1", "builtin.number": "1"}
    - utter_confirm
    - utter_goodbye
    
## Generated Story 4 
* search_event{"activity": "kino", "firstname": "lara"}
    - slot{"activity": "kino"}    
    - slot{"firstname": "lara"}
    - action_search_contact
* contact_selection
    - action_add_contact
* search_event{"location": "berlin"}
    - utter_ask_time
* search_event{"datetime": "morgen"}
    - action_search_events
    - slot{"matches": ["Avengers - Infinity War", "Ready Player One", "Black Panther"]}
    - action_suggest
* selection{"builtin.datetime": "1", "builtin.number": "1"}
    - utter_confirm
    - utter_goodbye
    
## Generated Story -141789019633875134
* search_event{"activity": "kino", "firstname": "lara"}
    - slot{"activity": "kino"}
    - slot{"firstname": "lara"}
    - action_search_contact
* contact_selection{"relationship": "schwester"}
    - slot{"relationship": "schwester"}
    - action_add_contact
    - export