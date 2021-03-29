#Write a program that takes in numbers from the user and adds them to a list. When the user types ‘stop’ the program takes the average of the list of numbers and prints it to the console.


num_list = []

def take_average():
  total = 0
  for num in num_list:
    total += num
  average = total/len(num_list)
  print("The avarage is {}." .format(average))




while True:
  answer = input('Enter a number, type "stop" to take the avarage:')
  if (answer == 'stop'):
    take_average()
    break
  else:
    num_list.append(int(answer))