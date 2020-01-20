i = 0
numbers = []

increment = int(input("Enter the increment value: "))
initial_count_value = int(input("Enter the starting value: "))
max_value = int(input("Enter the maximum value: "))

def loop_function(counter,max,list_var, increment_value):
    print("counter is %d" % counter
    )
    while counter < (max + 1):
     print("At the top counter is %d" % counter)
     list_var.append(counter)

     counter = counter + increment_value

     print("numbers now: " , list_var)
     print("At the bottom counter is %d" % counter)

loop_function(initial_count_value,max_value, numbers, increment)

print("The numbers: ")
for num in numbers:
  print(num)
