import random
menu=True
while menu:
    print("""
1.Flip A Coin 100 Times
2.Fortune Cookie
3.Pocket Color
4.Number Of Hot Dogs
5.Exit/Quit
""")
    menu=input("What Would You Like To Do? ")
    if menu=="1":
           
        heads = 0
        tails = 0
        rounds = 0
        while rounds < 100:
            coin = random.randint(1, 2)
            if coin == 1:
                heads += 1
                rounds += 1
            elif coin == 2:
                tails += 1
                rounds += 1
        print("You Flipped Heads {} Times!".format(heads))
        print("You Flipped Tails {} Times!".format(tails))
      
    elif menu=="2":
        fortune = random.randint(1, 5)
        if fortune == 1:
            print ("A beautiful, smart, and loving person will be coming into your life.")
        
        elif fortune == 2:
            print ("A dubious friend may be an enemy in camouflage.")
        
        elif fortune == 3:
            print ("A feather in the hand is better than a bird in the air.")
        
        elif fortune == 4:
            print ("A fresh start will put you on your way.")
        
        elif fortune == 5:
            print ("A friend asks only for your time not your money.")

    elif menu=="3":
        num_people = int(input("Enter number that people will attend: "))
        dogs_per_people = int(input("Enter number of dogs each person wants: "))
        
        total_dogs = num_people * dogs_per_people
        if total_dogs % 10 == 0:
            print("Buy {} bags of dogs".format(total_dogs//10))
        else:
            x_dogs = total_dogs//10
            print("Buy {} bads of dogs".format((x_dogs) + 1))
        
        if total_dogs % 8 == 0:
            print("Buy {} bags of buns".format(total_dogs//8))
        else:
            x_buns = total_dogs//8
            print("Buy {} bads of buns".format((x_buns) + 1))
            
    elif menu=="4":
        num = int(input("Enter a number between 1 and 36: "))
        if num > 18:
            if num % 2 == 0:
                print("black")
            else:
                print("Blue")
        elif num > 10:
            print("Red")
        else:
            print("Orange")
        
    elif menu=="5":
        print("Goodbye")
        menu = None
    else:
        print("Not Valid Choice Try again")