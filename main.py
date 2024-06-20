import database
import edit
import counter

import sqlite3

words_dict = counter.final_word_dict

words_dict = edit.EditDictionary(words_dict)

def check_win(color_list):
  color_set = set(color_list)
  return (len(color_set) == 1) and (color_set.pop() == 'green' or 'g')

def iterate_dict(words_dict, word, removed_letters):
  color_list = []
  tuple_list = []
  for i in range(5):
    n = i + 1
    print("Valid Options: \'Green\' (G), \'Yellow\' (Y), or \'Black\' (B)")
    color = input(f'Letter {n} Color Results: ')
    tup = (color, word[i], i)
    tuple_list.append(tup)
    if (color.lower() == 'green') or (color.lower() == 'g'):
      color_list.append(color.lower())
    elif (color.lower() == 'yellow') or (color.lower() == 'y'):
      color_list.append(color.lower())
    elif (color.lower() == 'black') or (color.lower() == 'b'):
      color_list.append(color.lower())

  words_dict.update(tuple_list)
  return check_win(color_list)
  

  
if __name__ == '__main__':
  print('\nHello and welcome to WordleBot!\n')
  best_word = words_dict.best_word()
  print(f'The best first word is: {best_word}\n')

  game_over = False
  i = 0
  while (game_over is False) or (i == 6):
    i += 1
    removed_letters = words_dict.return_removed_letters()
    best_word = words_dict.best_word()
    print('Now, please input the results.\n')
    game_over = iterate_dict(words_dict, best_word, removed_letters)
    if game_over:
      print(f'\n\n\n***** Congrats on getting the wordle in {i}! *****')
    else:
      print('\n\n\nThe next best word is: ', words_dict.best_word())
    
  print('\n\nThank you for using WordleBot!')
