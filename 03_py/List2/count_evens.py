#Using a for loop and an if function to track and count even nums in the list
def count_evens(nums):
  a = 0
  for i in nums:
    if i % 2 == 0:
      a+=1
  return a

print('count_evens([2, 1, 2, 3, 4]):',count_evens([2, 1, 2, 3, 4]))
print('count_evens([2, 2, 0]):',count_evens([2, 2, 0]))
print('count_evens([1, 3, 5]):',count_evens([1, 3, 5]))
print('count_evens([]):',count_evens([]))
print('count_evens([11, 9, 0, 1]):',count_evens([11, 9, 0, 1]))
print('count_evens([2, 11, 9, 0]):',count_evens([2, 11, 9, 0]))
print('count_evens([2]):',count_evens([2]))
print('count_evens([2, 5, 12]):',count_evens([2, 5, 12]))
