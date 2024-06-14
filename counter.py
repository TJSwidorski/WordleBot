from database import *
import sqlite3

CONN = sqlite3.connect('WordleDictionary.db')

words_list = WordleDatabase.retrieve_list(CONN, 'Words List')

#Count all letters
letter_totals = {'Total': 0}
letter_probability = {}
word_score = {}

def count_letters(counter, word_list):
  for word in word_list:
    for i in range(len(word)):
      if word[i].upper() in counter:
        counter[str((word[i]).upper())] += 1
      else:
        counter[str((word[i]).upper())] = 1
      counter['Total'] += 1

  sorted_counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
  counter.clear()
  for item in sorted_counter:
    counter[item[0]] = item[1]

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
  sorted_scores = sorted(score_dict.items(), key=lambda item:item[1], reverse=True)
  score_dict.clear()
  for score in sorted_scores:
    score_dict[score[0]] = score[1]

calc_word_score(word_score, letter_probability, words_list)

print(word_score)

#Count letters at each position