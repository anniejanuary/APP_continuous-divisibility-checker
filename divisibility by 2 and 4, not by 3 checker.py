#czy liczba jest podzielna przez 2, przez 4, nie jest podzielna przez 3 (wszystkie jednocześnie)

while True:
    
    print("Enter a number: ")
    number=int(input())
    
    if number%2 == 0 and number%4==0 and number%3!=0:
        print(True)
        
        print("Do you want to continue? Y/N: ")
        decision=input()
        
        if decision=="N":
            break
    else:
        print(False)
        
        print("Do you want to continue? Y/N: ")
        decision=input()
        
        if decision=="N":
            break
