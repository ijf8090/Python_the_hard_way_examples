i = 0
numbers = []
initial_count_value = int(input("Enter the starting value: "))

def loop_function(counter,list_var):
    while counter < 6:
     print("At the top counter is %d" % counter)
     list_var.append(counter)

     counter += 1
     print("numbers now: " , list_var)
     print("At the bottom counter is %d" % counter)

loop_function(initial_count_value,numbers)

print("The numbers: ")
for num in numbers:
  print(num)
