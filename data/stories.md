## story 0 no activity, no location, no time
* greet
    - utter_ask_howcanhelp
* search_event
    - utter_ask_activity
* search_event{"activity": "kino"}
    - utter_ask_location
* search_event{"location": "berlin"}
    - utter_ask_time
* search_event{"datetime": "morgen"}#
    - action_search_events
    - action_suggest
* selection{"number":1}
    - utter_ask_invite
* goodbye
    - utter_goodbye
    
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