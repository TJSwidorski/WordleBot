from database import *
import sqlite3

CONN = sqlite3.connect('WordleDictionary.db')

words_list = WordleDatabase.retrieve_list(CONN, 'Words List')

#Count all letters
letter_totals = {'Total': 0}
letter_probability = {}
word_score = {}

#Helper
def order_dict(counter):
  sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
  counter.clear()
  for item in sorted_counter:
    counter[item[0]] = item[1]

#Helper
def dict_counter(counter, word, index):
  if word[index].upper() in counter:
    counter[str((word[index]).upper())] += 1
  else:
    counter[str((word[index]).upper())] = 1
  counter['Total'] += 1

#Worker
def count_letters(counter, word_list):
  for word in word_list:
    for i in range(len(word)):
      dict_counter(counter, word, i)

  order_dict(counter)

count_letters(letter_totals, words_list)

# print(letter_totals)

def letter_percentages(prob_dict, letter_totals):
  for letter in letter_totals:
    prob_dict[letter] = letter_totals[letter] / letter_totals['Total']

letter_percentages(letter_probability, letter_totals)

# print(letter_probability)

def calc_word_score(score_dict, letter_probs, word_list):
  for word in word_list:
    accum = 1
    for i in range(len(word)):
      letter = word[i].upper()
      prob = letter_probs[letter]
      accum *= prob
    score_dict[word] = accum
  
  order_dict(score_dict)

calc_word_score(word_score, letter_probability, words_list)

# print(word_score)

#Count letters at each position
first_total = {'Total': 0}
second_total = {'Total': 0}
third_total = {'Total': 0}
fourth_total = {'Total': 0}
fifth_total = {'Total': 0}

loc_totals = [first_total, second_total, third_total, fourth_total, fifth_total]

def count_positions(list_of_dicts, word_list):
  for word in word_list:
    for i in range(len(word)):
      dict_counter(list_of_dicts[i], word, i)
  
  for dict in list_of_dicts:
    order_dict(dict)

count_positions(loc_totals, words_list)

first_prob = {}
second_prob = {}
third_prob = {}
fourth_prob = {}
fifth_prob = {}

prob_totals = [first_prob, second_prob, third_prob, fourth_prob, fifth_prob]

def location_percentages(prob_list, loc_list):

  totals = zip(prob_list, loc_list)

  for prob, loc in totals:
    letter_percentages(prob, loc)

location_percentages(prob_totals, loc_totals)

loc_word_score = {}

def calc_loc_score(score_dict, probability_list, word_list):
  for word in word_list:
    accum = 1
    for i in range(len(word)):
      letter = word[i].upper()
      prob = probability_list[i][letter]
      accum *= prob
    score_dict[word] = accum
  order_dict(score_dict)

calc_loc_score(loc_word_score, prob_totals, words_list)

# print(loc_word_score)

#Standardize the Dictionary
def standardize_dict(word_dict):
    values = list(word_dict.values())
    mean = sum(values) / len(values)
    stddev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5

    # Standardize the values
    new_dict = {}
    for word, value in word_dict.items():
        standardized_value = (value - mean) / stddev
        new_dict[word] = standardized_value

    order_dict(new_dict)
    return new_dict

stand_word_score = standardize_dict(word_score)
stand_loc_score = standardize_dict(loc_word_score)

# print(stand_loc_score)

#Combine the two

def overall_score(word_dict, loc_dict, word_list):
  """
  Where both dicts have already been standardized.
  """
  final_score = {}
  for word in word_list:
    w_score = word_dict[word]
    loc_score = loc_dict[word]
    mean = (w_score + loc_score) / 2
    final_score[word] = mean

  order_dict(final_score)
  return final_score

final_word_dict = overall_score(stand_word_score, stand_loc_score, words_list)

# print("Complete word score:", list(stand_word_score)[:5])
# print("Letter location score:", list(stand_loc_score)[:5])
# print("Final scoring:", list(final_word_dict)[:5])