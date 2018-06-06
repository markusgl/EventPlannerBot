""" Custom Actions for API calls etc """
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from knowledge_base.neo_4_j_graph import KnowledgeGraph

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset, Restarted
from datetime import timedelta
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import logging
logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)


class ActionSearchContact(Action):
    def name(self):
        return 'action_search_contact'

    def run(self, dispatcher, tracker, domain):
        kg = KnowledgeGraph()
        contact_name = tracker.get_slot('firstname')
        relation_ship = tracker.get_slot('relationship')

        if contact_name:
            relationship = kg.search_relationship_by_contactname(contact_name)
            if relationship is None:
                dispatcher.utter_message("Ich kenne "+ str(contact_name).title() + " nicht. Willst du mir sagen wer das ist?")
            else:
                SlotSet("relationship", relationship)
                dispatcher.utter_message("Deine(n) "+relationship+" "+contact_name+"?")
        elif relation_ship:
            contact = kg.search_contactname_by_relationship(relation_ship)
            if contact is None:
                if relation_ship == "vater" or relation_ship == "bruder" or relation_ship == "onkel":
                    dispatcher.utter_message("Ich kenne deinen " + str(relation_ship) + " leider nicht. "
                                                                                   "Willst du mir sagen wie er heißt?")
                elif relation_ship == "mutter" or relation_ship == "schwester" or relation_ship == "tante":
                    dispatcher.utter_message("Ich kenne deine " + str(relation_ship) + " leider."
                                                                                  "Willst du mir sagen wie sie heißt?")
                else:
                    dispatcher.utter_message("Ich kenne " + str(relation_ship) + " nicht.")
            else:
                SlotSet("contactname", contact)
                dispatcher.utter_message("Meinst du "+contact+"?")
        else:
            dispatcher.utter_message("Leider hab ich dich nicht ganz verstanden. Wen willst du mitnehmen?")

        return []


class ActionAddContact(Action):
    def name(self):
        return 'action_add_contact'

    def run(self, dispatcher, tracker, domain):
        kg = KnowledgeGraph()
        contact_name = tracker.get_slot('firstname')
        relation_ship = tracker.get_slot('relationship')

        kg.add_contact(contact_name=contact_name, relationship=relation_ship)
        dispatcher.utter_message("Danke, jetzt kenn ich auch "+ str(contact_name) +"!")


class ActionSearchEvents(Action):
    """
    Searches eveent recommendations in the area and suggests contacts to join
    """
    def name(self):
        return 'action_search_events'

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('location')

        if tracker.get_slot('datetime'):
            time = tracker.get_slot('datetime')
        elif tracker.get_slot('relativedate'):
            time = tracker.get_slot('relativedate')
            if time == 'morgen':
                tomorrow = datetime.datetime.now() + timedelta(days=1)
                event_time = tomorrow.isoformat() + 'Z'

        elif tracker.get_slot('dateperiod'):
            time = tracker.get_slot('dateperiod')

            #TODO convert to date
        else:
            event_time = None

        dispatcher.utter_message("Ich versuche Veranstaltungen in deiner Umgebung zu finden")

        #activity = tracker.get_slot('activity')
        print("Current slot-values %s" % tracker.current_slot_values())
        print("Current state %s" % tracker.current_state())

        return []


class ActionSearchAppointment(Action):
    """
    Searches appointments on the google calendar depending on given time or time period
    """
    def name(self):
        return 'action_search_appointment'

    def run(self, dispatcher, tracker, domain):
        # check if time was given by the user and convert relative dates and time periods
        if tracker.get_slot('datetime'):
            appointment_time = tracker.get_slot('datetime')
        elif tracker.get_slot('relativedate'):
            given_time = tracker.get_slot('relativedate')
            if given_time == 'heute':
                today = datetime.datetime.now()
                appointment_time = today.isoformat() + 'Z'
            elif given_time == 'morgen':
                tomorrow = datetime.datetime.now() + timedelta(days=1)
                appointment_time = tomorrow.isoformat() + 'Z'
            elif given_time == 'übermorgen':
                after_tomorrow = datetime.datetime.now() + timedelta(days=2)
                appointment_time = after_tomorrow.isoformat() + 'Z'
            else:
                appointment_time = ""
        elif tracker.get_slot('dateperiod'):
            given_time = tracker.get_slot('dateperiod')
            appointment_time = ""
        else:
            appointment_time = ""

        print(appointment_time)

        if appointment_time:
            events = self.search_google_calendar(appointment_time)
            print(events)
            if not events:
                dispatcher.utter_message("Du hast heute keine Termine.")
            for event in events:
                dispatcher.utter_message("Ich konnte folgende Termin finden:")
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])


    def search_google_calendar(self, event_time):
        # Setup the Calendar API
        SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))

        # Call the Calendar API
        events_result = service.events().list(calendarId='primary', timeMin=event_time,
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return None
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

        return events

    if __name__ == "__main__":
        tomorrow = datetime.datetime.now() + timedelta(days=1)
        event_time = tomorrow.isoformat() + 'Z'
        print(event_time)

        events = search_google_calendar(event_time)
        print(events)


class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Ich konnte folgendes finden")
        count = 1
        for match in tracker.get_slot("matches"):
            dispatcher.utter_message(str(count) + " " + match)
            count += 1
        dispatcher.utter_message("Wie ist deine Wahl?")
        dispatcher.utter_button_message("Tippe die entprechende Zahl ein", buttons=[{"1":"eins", "2":"zwei", "3":"drei"}])

        return []


class ActionClearSlots(Action):
    def name(self):
        return 'action_clear_slots'

    def run(self, dispatcher, tracker, domain):
        tracker.clear_follow_up_action()

        print("Current slot-values %s" % tracker.current_slot_values())
        print("Current state %s" % tracker.current_state())

        return [AllSlotsReset()]


class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'

    def run(self, dispatcher, tracker, domain):
        return[Restarted()]

