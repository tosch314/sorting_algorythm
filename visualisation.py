import matplotlib.pyplot as plt
import numpy as np
import itertools 

  
def get_permutation_list(listA):
  perm= itertools.permutations(listA)
  listB = list(perm)
  return listB


def plot_bar_x(label_list, data_list):
    # this is for plotting purpose
    index = np.arange(len(label_list))
    plt.bar(index, data_list)
    plt.xlabel('Permutations', fontsize=5)
    plt.ylabel('Counts', fontsize=5)
    plt.xticks(index, label_list, fontsize=5)
    plt.show()


def listOflistToString(listA):
    new_list = []
    for lists in listA:
        string_element = ""
        for ele in lists:
            string_element += ele
        new_list.append(string_element)
    return new_list


label_list = ['A', 'B', 'C']
test_list = [1,2,3,4,5,6]



plot_bar_x(listOflistToString(get_permutation_list(label_list)), test_list)

        
