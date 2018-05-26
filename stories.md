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
    - utter_goodbye
    - export
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
* goodbye
    - export
