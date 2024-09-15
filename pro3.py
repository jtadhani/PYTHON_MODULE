# defin a function
def printrec(mylist): 
    
    if mylist == []:                       
        print() 
        return 
    
    print(mylist[0], '', end='')
    printrec(mylist[1:]) 
          
  
printrec([0, 1, 2, 3, 4]) 