# usre input value store
no = int(input("Enter the Number :- "))

# variabla declare
num = no
temp = 0
i = 0

# list variabla declare
b = []

# while loop is start in codiction is check

while 1<no:
    
    i = i + 1
    
    # if codiction is start
    if num % i == 0:
        temp = temp + i
        # i value is append is list varible b 
        b.append(i)
        
    no = no - 1

# join is str in bilt function list value is str value convat
sum_num = ' + '.join(map(str, b))

if (num == temp):
    
    print(f"{sum_num} = {temp} Number is perfact")
else:
    
    print(f"{sum_num} = {temp} Number is note perfact")