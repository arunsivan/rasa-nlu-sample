from rasa_core.actions import Action
from rasa_core.actions.forms import EntityFormField,FormAction
from rasa_core.events import SlotSet

class ActionSearch(FormAction):

    RANDOMIZE = False

    @staticmethod
    def required_fields():
        return [
            EntityFormField("purpose", "purpose"),
            EntityFormField("purpose_sub", "purpose_sub"),
            EntityFormField("recoil", "recoil"),
            EntityFormField("category", "category"),
            EntityFormField("manufacturer", "manufacturer")
        ]

    def name(self):
        return 'action_search'

    def submit(self, dispatcher, tracker, domain):
        results = RestaurantAPI().search(
            tracker.get_slot("purpose"),
            tracker.get_slot("purpose_sub"),
            tracker.get_slot("recoil"),
            tracker.get_slot("category"),
            tracker.get_slot("manufacturer"))
        return [SlotSet("search_results", results)]
