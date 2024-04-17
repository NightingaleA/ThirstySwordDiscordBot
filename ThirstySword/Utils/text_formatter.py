class Text_Formatter:
  def __init__(self):
    self.normal =self.__get_as_is_format__()
    self.bold = self.__get_bold_format__()
    self.bold_italics = self.__get_bold_italics_format__()
    self.bold_underline = self.__get_bold_underline_format__()
    self.bold_strikeout = self.__get_bold_striketout_format__()
    self.italics = self.__get_italics_format__()
    self.italics_inderline = self.__get_italics_underline_format__()
    self.italics_strikeout = self.__get_italics_strikeout_format__()
    self.underline = self.__get_underline_format__()
    self.strikethrough = self.__get_strikeout_format__()
    self.newline = self.__get_newline_format__()
    self.quote = self.__get_quote_symbol__()
    self.notation = self.__get_notation_symbol__()
  
  def __get_as_is_format__(self):
    return "{}"
    
  def __get_bold_format__(self):
    return "**{}**"

  def __get_bold_italics_format__(self):
    return "***{}***"

  def __get_bold_underline_format__(self):
    return "**__  {}  __**"
  
  def __get_bold_striketout_format__(self):
    return "**~~  {}  ~~**"
  
  def __get_italics_format__(self):
    return "*{}*"

  def __get_italics_underline_format__(self):
    return "__  {}  __"
  
  def __get_italics_strikeout_format__(self):
    return "~~  {}  ~~"
  
  def __get_underline_format__(self):
    return "__  {}  __"
  
  def __get_strikeout_format__(self):
    return "~~  {}  ~~"
  
  def __get_newline_format__(self):
    return "\n"

  def __get_quote_symbol__(self):
    return "> "
  
  def __get_notation_symbol__(self):
    return "^"
  

  

  
  

