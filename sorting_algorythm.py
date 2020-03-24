import random

def random_sort(nums):
  counter = 0
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(nums)-1):
      if nums[i] > nums[i+1]:
        random.shuffle(nums)
        counter += 1
        swapped = True
  print(counter)
  print(nums)


a = 10
random_list = []
for i in range(0,a):
  n = random.randint(1,30)
  random_list.append(n)



random_sort(sophie_list)

