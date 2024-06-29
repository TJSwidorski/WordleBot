import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import simulate
import counter
from database import *

class WordleGraph():
  def __init__(self, simulation_results):
    self.__simulation_results = simulation_results
    self.__score_list = [score for _, score in simulation_results.values()]
    self.__turn_list = [turn for turn, _ in simulation_results.values()]

  def scatter(self):
    plt.scatter(self.__score_list, self.__turn_list)
    plt.xlabel('Word Score')
    plt.ylabel('Turns to Solve')
    plt.title('Scatter Plot')
    plt.show(block=True)
  
  def flip_scatter(self):
    plt.scatter(self.__turn_list, self.__score_list)
    plt.xlabel('Turns to solve')
    plt.ylabel('Word Score')
    plt.title('Flipped Scatter Plot')
    plt.show(block=True)

  def histogram(self):
    median = np.median(self.__turn_list)
    mean = np.mean(self.__turn_list)
    std = np.std(self.__turn_list)
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    y = norm.pdf(x, mean, std)
    plt.hist(self.__turn_list, bins=9, density=True, alpha=0.5, label='Histogram', edgecolor='black')
    plt.plot(x, y, 'r-', label='Bell Curve')
    plt.axvline(median, color='g', linestyle='dashed', label='Median')
    plt.xlabel('Turns to Solve')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.legend()
    plt.show()
  

CONN = sqlite3.connect('WordleDictionary.db')

words_list = WordleDatabase.retrieve_list(CONN, 'Words List')

average_dict = counter.final_word_dict
letter_dict = counter.stand_word_score
location_dict = counter.loc_word_score

if __name__ == '__main__':
  average_dict_sum = simulate.WordleSimulation(words_list, average_dict)
  average_dict_sum.simulate()
  average_graph = WordleGraph(average_dict_sum.get_sim_results())
  average_graph.scatter()
  average_graph.flip_scatter()
  average_graph.histogram()

  letter_dict_sum = simulate.WordleSimulation(words_list, letter_dict)
  letter_dict_sum.simulate()
  letter_graph = WordleGraph(letter_dict_sum.get_sim_results())
  letter_graph.scatter()
  letter_graph.flip_scatter()
  letter_graph.histogram()

  location_dict_sum = simulate.WordleSimulation(words_list, letter_dict)
  location_dict_sum.simulate()
  location_graph = WordleGraph(average_dict_sum.get_sim_results())
  location_graph.scatter()
  location_graph.flip_scatter()
  location_graph.histogram()