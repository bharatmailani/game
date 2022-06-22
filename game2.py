import random
l=["rock","scissor","paper"]
'''
rock vs paper-> paper wins
rock vs scissor-> rock wins
paper vs scissor-> scissor wins
'''

while True:
    ccount=0
    ucount=0
    uc=int(input('''
    Game start....
    1 Yes
    2 No | Exit    
    '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
            1 Rock
            2 Scissor
            3 paper              
            '''))
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="scissor"
            elif userinput==3:
                uchoice="paper"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Game draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and Cchoice=="scissor") or ( uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Computer Win")
                ccount=ccount+1
            if ucount==ccount:
                print("Computer Score",ccount)
                print("User Score",ucount)
            elif ucount>ccount:
                print("User score",ucount)
                print("Computer Score",ccount)
            else:
                print("User Score",ccount)
                print("Computer Score",ccount)

    else:
        break