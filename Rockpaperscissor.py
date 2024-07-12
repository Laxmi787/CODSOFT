import random
l=["rock","scissor","paper"]
'''
rock vs paper-> paper wins
rock vs scissors-> rock wins
paper vs scissors-> scissor wins

'''
while True:
    ccount = 0
    ucount = 0
    user_choice = int(input('''
    Game Start....
    1.Yes
    2.No | Exit
                   '''))
    
    if user_choice == 1:
        for a in range(1,6):
            userInput=int(input('''
1.Rock
2.Scissor
3.Paper
                                '''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            Cchoice =random.choice(l)
            #print(uchoice)
            #print(Cchoice)
            if Cchoice == uchoice:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Game Draw")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and Cchoice == "scissor") or(
                uchoice == "paper" and Cchoice == 'rock') or (
                uchoice == "scissor" and Cchoice == "paper"):
                    print("Computer Value", Cchoice)
                    print("User Value", uchoice)
                    print("You Win")
                    ucount += 1
            else:
                print("Computer Value", Cchoice)
                print("User Value", uchoice)
                print("Computer Win")
                ccount += 1
        if ucount == ccount:
            print("Final Game Draw....")   
            print("User Score", ucount) 
            print("Computer Score", ccount)  
        elif ucount>ccount:
            print("Final You Win The Game....")   
            print("User Score", ucount) 
            print("Computer Score", ccount)   
        else:
            print("Final Computer Win The Game....")   
            print("User Score", ucount) 
            print("Computer Score", ccount) 
             
            
            
    else:
        break
feedback=input("Give your valuable feedback:")
print(feedback)
