# number store is no variable
no = int(input("Enter the positive intejar number :- "))

# variabla declare
i = 0
temp = 'B'
a = 'A'
b = 'B'
print(a,end=" ")

# while loop is start in chek condition
while i < no :
    
    print(temp ,end=" ")
    temp = b + a

    # Update a and b for the next iteration
    a = b
    b = temp
    
    i = i + 1