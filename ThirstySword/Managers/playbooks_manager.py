import pandas as pd
from Data.playbook import Playbook
class Playbooks_Manager:
  def __init__(self):
    self._playbookDataframe = pd.read_csv(
      "ThirstySword/Data/data_playbooks.csv")
    self._playbookDataframe.set_index("uniqueID",
                                      drop=True,
                                      inplace=True)
    self._playbookDataframe.fillna('-', inplace=True)
    self.dictionary = self._playbookDataframe.to_dict(orient="index")
    self.list = []

    for id, element in self.dictionary.items():
      playbook = Playbook(id, element['command'], element['name'], element['blurb'], element['source'])
      self.list.append(playbook)

  def do_playbook(self, data_manager):
    playbook_to_do = self.get_playbook(data_manager.current_command.id)    

    if(playbook_to_do):
      response = playbook_to_do.parse_playbook(data_manager)  
      return response

  def get_playbook(self, command_id):
    for playbook in self.list:
      if(command_id == playbook.command):
        return playbook
      