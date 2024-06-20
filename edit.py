import counter

class EditDictionary():
  def __init__(self, word_dict):
    self.__word_dict = word_dict
    self.__removed_letters = []
    self.__required_letters = []

  def remove_words(self, removable_words):
    for word in removable_words:
      self.__word_dict.pop(word)
    
  def remove_letter(self, letter):
      if letter in self.__required_letters:
        self.__removed_letters.append(letter)
        words_to_remove = []
        for word in self.__word_dict:
          if word.count(letter) > self.__removed_letters.count(letter):
            words_to_remove.append(word)
      else:
        self.__removed_letters.append(letter)
        words_to_remove = [word for word in self.__word_dict if letter in word]
      
      self.remove_words(words_to_remove)
  
  def require_correct_location(self, letter, location):
    self.__required_letters.append(letter)
    words_to_remove = []
    for word in self.__word_dict:
      if word[location] != letter:
        words_to_remove.append(word)
      elif letter not in word:
         words_to_remove.append(word) 
    
    self.remove_words(words_to_remove)


  def require_wrong_location(self, letter, location):
    self.__required_letters.append(letter)
    words_to_remove = []
    for word in self.__word_dict:
      if word[location] == letter:
        words_to_remove.append(word)
      elif letter not in word:
          words_to_remove.append(word) 
    
    self.remove_words(words_to_remove)

  def return_dict(self):
    return self.__word_dict
  
  def return_removed_letters(self):
     return self.__removed_letters
  
  def best_word(self):
    if self.__word_dict:
      return next(iter(self.__word_dict))
    else: return None

  def update(self, tuple_list):
    """
    The tuple list is a list of the inputs where the color of the letter space
    is first and the letter is second.
    Example: l = [('b', 'c', 0), ('b', 'o', 1), ('g', 'a', 2), ('g', 'c', 3), 
    ('y', 'h', 4)]. Where the word is 'coach' and the colors by letters are: 
    black, black, green, green, yellow and the numbers represent the 0-based
    indexes of the letter locations in the word.
    """
    sorted_tuple_list = sorted(tuple_list, key=lambda x: x[0], reverse=True)

    word = ''
    for _, letter, _ in tuple_list:
      word += letter

    for i in range(5):
      color = sorted_tuple_list[i][0]
      letter = sorted_tuple_list[i][1]
      index = sorted_tuple_list[i][2]
      if (color.lower() == 'green') or (color.lower() == 'g'):
        self.require_correct_location(letter, index)
      elif (color.lower() == 'yellow') or (color.lower() == 'y'):
        self.require_wrong_location(letter, index)
      elif (color.lower() == 'black') or (color.lower() == 'b'):
        if letter not in self.__removed_letters:
          self.remove_letter(letter)               