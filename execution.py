from sorting_algorythm import random_sort
import random


# this function creates a list of length a, with random numbers in the range from b to c
def create_list(a,b,c):
  random_list = []
  for i in range(0,a):
    n = random.randint(b,c)
    random_list.append(n)
  return random_list


test_list = [2,3,1]

def collect_data(data_points):
  a,b,c,d,e,f = 0
  for i < data_points:
    random_sort(test_list)
    if test_list == [1,2,3]:
      

print(test_list)
