""" Custom Actions for API calls etc """
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from knowledge_base.neo_4_j_graph import KnowledgeGraph

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset, Restarted


class ActionSearchContact(Action):
    def name(self):
        return 'action_search_contact'

    def run(self, dispatcher, tracker, domain):

        kg = KnowledgeGraph()
        contact_name = tracker.get_slot('firstname')
        relation_ship = tracker.get_slot('relationship')
        #print(contact_name)
        #print(relation_ship)

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

        print("Current slot-values %s" % tracker.current_slot_values())
        print("Current state %s" % tracker.current_state())

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