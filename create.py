import requests
import string
from bs4 import BeautifulSoup
import database

url = "https://wordunscrambler.me/wordle-words-starting-with/a"
wordle_db = database.WordleDatabase()

def scrape_wordle_words (url, word_list):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  for li in soup.find_all('li'):
      a_tag = li.find('a')
      if a_tag:
          word = a_tag.get('data-word')
          if word:
              word_list.append(word)

word_dictionary = []
all_letters = list(string.ascii_lowercase)

for letter in all_letters:
    url = "https://wordunscrambler.me/wordle-words-starting-with/" + letter
    scrape_wordle_words(url, word_dictionary)

check_list = []
for word in word_dictionary:
    if len(word) == 5:
        check_list.append(word)

assert len(check_list) == len(word_dictionary)