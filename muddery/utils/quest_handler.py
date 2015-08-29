"""
QuestHandler
"""

import re
from muddery.utils import defines
from muddery.utils.builder import build_object
from django.conf import settings
from django.db.models.loading import get_model
from evennia.utils import logger


class QuestHandler(object):
    """
    """
    def __init__(self, character):
        """
        Initialize handler
        """
        self.character = character


    def accept(self, quest):
        """
        Accept a quest.
        """
        if quest in self.character.db.current_quests:
            return

        new_quest = build_object(quest)
        if not new_quest:
            return

        self.character.db.current_quests[quest] = new_quest
        self.show_quests()


    def is_finished(self, quest):
        """
        Whether the character finished this quest.
        """
        return quest in self.character.db.finished_quests


    def is_in_progress(self, quest):
        """
        Whether the character is doing this quest.
        """
        return quest in self.character.db.current_quests


    def is_available(self, quest):
        """
        """
        if quest in self.character.db.finished_quests:
            return False

        return True


    def show_quests(self):
        """
        Send quests to player.
        """
        quests = self.return_quests()
        self.character.msg({"quests": quests})


    def return_quests(self):
        """
        Get quests' data.
        """
        quests = []
        for key in self.character.db.current_quests:
            quest = self.character.db.current_quests[key]
            info = {"dbref": quest.dbref,
                    "name": quest.name,
                    "desc": quest.db.desc}
            quests.append(info)

        return quests


    def at_character_move_in(self, location):
        """
        """
        pass


    def at_character_move_out(self):
        """
        """
        pass
