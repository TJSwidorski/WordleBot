from database import *
import sqlite3
import counter
import edit
import random
import copy

class WordleSimulation():
  def __init__(self, words_list, words_dict):
    self.__words_list = copy.deepcopy(words_list)
    self.__words_dict = copy.deepcopy(words_dict)
    self.__sim_results = None

  def __recursively_solve(self, words_dict, num, solution):
    wd = words_dict
    edit_dict = edit.EditDictionary(wd)
    best_word = edit_dict.best_word()

    if best_word == solution:
      return num
    else:
      for i in range(5):
        #If Green
        if best_word[i] == solution[i]:
          edit_dict.require_correct_location(best_word[i], i)
        #If Yellow
        elif (best_word[i] != solution[i]) and (best_word[i] in solution):
          edit_dict.require_wrong_location(best_word[i], i)
        #If Black
        else:
          edit_dict.remove_letter(best_word[i])
      wd = edit_dict.return_dict()
      return self.__recursively_solve(wd, num+1, solution)
        

  def __solve(self, solution, words_dict):
    return self.__recursively_solve(words_dict, 1, solution)

  def simulate(self):
    #Don't do any solving work in here
    #Return the number of turns it took to get the answer
    results = {}
    l = len(self.__words_list)
    while l > 0:
      n = random.randrange(0, l)
      sol = self.__words_list[n]
      words_dict_copy = copy.deepcopy(self.__words_dict)
      ans = self.__solve(sol, words_dict_copy)
      #Add the word as the key
      #Add a tuple (Number of turns, Word Score) as the value
      results[sol] = (ans, self.__words_dict[sol])
      self.__words_list.pop(n)

      l = len(self.__words_list)

    self.__sim_results = results

  def get_sim_results(self):
    return self.__sim_results
  
  def average(self):
    turn_vals = [num for num, _ in self.__sim_results.values()]
    return (sum(turn_vals) / len(turn_vals))
      

CONN = sqlite3.connect('WordleDictionary.db')

words_list = WordleDatabase.retrieve_list(CONN, 'Words List')

average_dict = counter.final_word_dict
letter_dict = counter.stand_word_score
location_dict = counter.loc_word_score

if __name__ == '__main__':
  average_dict_sim = WordleSimulation(words_list, average_dict)
  average_dict_sim.simulate()
  ave = average_dict_sim.average()
  print('Average solve length for average scoring system: ', ave)

  letter_dict_sim = WordleSimulation(words_list, letter_dict)
  letter_dict_sim.simulate()
  lett = letter_dict_sim.average()
  print('\nAverage solve length for letter scoring system: ', lett)

  location_dict_sim = WordleSimulation(words_list, location_dict)
  location_dict_sim.simulate()
  loc = location_dict_sim.average()
  print('\nAverage solve length for location scoring system: ', loc)

