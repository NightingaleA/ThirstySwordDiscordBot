import discord
from Managers.data_manager import DataManager


class input_handler:

  def __init__(self):
    self.data_manager = DataManager()

  def get_message_to_send(self, message):
    has_command = self.data_manager.message_contains_command(message.content)

    if (has_command):
      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_help_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_help_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_label_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_label.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_condition_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_condition.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_basic_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_basic_move.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_special_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_special_move.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_playbook_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_playbook.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager.localizer, message, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_label_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_label_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_label.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager.localizer, message, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_condition_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_condition_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_condition.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager.localizer, message, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_basic_move_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_basic_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_basic_move.name)
        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager.localizer, message, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_special_move_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_special_move_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_special_move.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager.localizer, message, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_playbook_list.name):
        commands_to_include = []
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_playbook_list.name)
        commands_to_include.append(
          self.data_manager.COMMAND_TYPE.command_playbook.name)

        response = self.data_manager.commands_manager.get_command_list(
          self.data_manager.localizer, message, commands_to_include)
        return response

      if (self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_playbook.name):
          response = self.data_manager.playbooks_manager.do_playbook(self.data_manager, message)
          return response

      if(self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_label.name):
        response = self.data_manager.parse_label( message)
        return response  
      if(self.data_manager.current_command.type ==
          self.data_manager.COMMAND_TYPE.command_condition.name):
        response = self.data_manager.parse_condition( message)
        return response  
      else: 
        response = self.data_manager.moves_manager.do_move(self.data_manager, message)
        return response

      embed = discord.Embed(title=self.data_manager.current_command.languages[self.data_manager.localizer.lang.name], color=0xFF5733)
      embed.add_field(name='**—————————**',
                      value=self.data_manager.localizer.get_utils_with_key(
                        "missing_command"))
      return embed