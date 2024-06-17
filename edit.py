class EditDictionary():
  def __init__(self, word_dict):
    self.word_dict = word_dict
    
  def remove_letter(self, letter):
      words_to_remove = [word for word in self.word_dict if letter in word]
      for word in words_to_remove:
          self.word_dict.pop(word)
  
  def require_correct_location(self, letter, location):
    words_to_remove = []
    for word in self.word_dict:
      if word[location - 1] != letter:
        words_to_remove.append(word)
      elif letter not in word:
         words_to_remove.append(word) 
    
    for word in words_to_remove:
       self.word_dict.pop(word)


  def require_wrong_location(self, letter, location):
    words_to_remove = []
    for word in self.word_dict:
      if word[location - 1] == letter:
        words_to_remove.append(word)
      elif letter not in word:
          words_to_remove.append(word) 
    
    for word in words_to_remove:
        self.word_dict.pop(word)

  def return_dict(self):
    return self.word_dict
  
  def best_word(self):
    word_list = list(self.word_dict)
    return word_list[0]


