from enum import Enum

COMMAND_STATUS= Enum('COMMAND_STATUS', 'added WIP wait_list')

class Command:
  def __init__(self, id, en, es, type, status):
    self.id = id
    self.languages = {
      "english": en,
      "español": es
    }
    self.type = type
    self.status = status
    self.active_language = None