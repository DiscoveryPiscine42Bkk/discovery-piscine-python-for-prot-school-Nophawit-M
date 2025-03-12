def parametmat(Nopphawit_M) :
    if num_paramet != 1 :
        print("none")
        
    else:
        
        word = input("What was the parameter? : ")
        if word == Nopphawit_M :
            print("Good job!")
            
        else:
            print("Nope sorry...")
num_paramet = parametmat.__code__.co_argcount
            
parametmat('Hello')