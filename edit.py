class EditDictionary():
  def __init__(self, word_dict):
    self.__word_dict = word_dict
    self.__removed_letters = []
    self.__required_letters = []
    
  def remove_letter(self, letter):
      if letter in self.__required_letters:
        print("Duplicate Letter")
      else:
        self.__removed_letters.append(letter)
        words_to_remove = [word for word in self.__word_dict if letter in word]
        for word in words_to_remove:
          self.__word_dict.pop(word)
  
  def require_correct_location(self, letter, location):
    self.__required_letters.append(letter)
    words_to_remove = []
    for word in self.__word_dict:
      if word[location] != letter:
        words_to_remove.append(word)
      elif letter not in word:
         words_to_remove.append(word) 
    
    for word in words_to_remove:
       self.__word_dict.pop(word)


  def require_wrong_location(self, letter, location):
    self.__required_letters.append(letter)
    words_to_remove = []
    for word in self.__word_dict:
      if word[location] == letter:
        words_to_remove.append(word)
      elif letter not in word:
          words_to_remove.append(word) 
    
    for word in words_to_remove:
        self.__word_dict.pop(word)

  def return_dict(self):
    return self.__word_dict
  
  def return_removed_letters(self):
     return self.__removed_letters
  
  def best_word(self):
    if self.__word_dict:
      return next(iter(self.__word_dict))
    else: return None