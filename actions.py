""" Custom Actions for API calls etc """
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class ActionSearchFriends(Action):
    def name(self):
        return 'action_search_people'

    def run(self, dispatcher, tracker, domain):
        # TODO call knowledge base

        friends = ["Maria", "Eva", "Daniel"]

        return [SlotSet("friends", friends)]

class ActionSearchEvents(Action):
    def name(self):
        return 'action_search_events'

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('location')

        if tracker.get_slot('datetime'):
            time = tracker.get_slot('datetime')
        elif tracker.get_slot('relativedate'):
            time = tracker.get_slot('relativedate')
            #TODO convert to date
        elif tracker.get_slot('dateperiod'):
            time = tracker.get_slot('dateperiod')
            #TODO convert to date
        else:
            time = None

        activity = tracker.get_slot('activity')

        dispatcher.utter_message("Ok ich versuche etwas zu finden für {} am {} in {}".format(activity, time, location))
        movies = ["Avengers - Infinity War", "Ready Player One", "Black Panther"] # TODO API Request

        return [SlotSet("matches", movies)]


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
        dispatcher.utter_button_message("Tippe einfach die entprechende Zahl ein", buttons=[{"1":"eins", "2":"zwei", "3":"drei"}])

        return []