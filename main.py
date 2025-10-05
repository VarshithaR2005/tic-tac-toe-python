def board(xstate,ystate):
    zero='X' if xstate[0] else('O' if ystate[0] else 0)
    one='X' if xstate[1] else('O' if ystate[1] else 1)
    two='X' if xstate[2] else('O' if ystate[2] else 2)
    three='X' if xstate[3] else('O' if ystate[3] else 3)
    four='X' if xstate[4] else('O' if ystate[4] else 4)
    five='X' if xstate[5] else('O' if ystate[5] else 5)
    six='X' if xstate[6] else('O' if ystate[6] else 6)
    seven='X' if xstate[7] else('O' if ystate[7] else 7)
    eight='X' if xstate[8] else('O' if ystate[8] else 8)
    print(f" {zero} | {one} | {two}")
    print("---|---|---")
    print(f" {three} | {four} | {five}")
    print("---|---|---")
    print(f" {six} | {seven} | {eight}")
def check_win(xstate,ystate):
    winner=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in winner:
        if(xstate[win[0]]+xstate[win[1]]+xstate[win[2]]==3):
            board(xstate,ystate)
            print("X won the match")
            print("Game Over")
            return 1
        elif(ystate[win[0]]+ystate[win[1]]+ystate[win[2]]==3):
            board(xstate,ystate)
            print("O won the match")
            print("Game Over")
            return 0
    return -1
def main():
    print("WELCOME TO TIC TAC TOE")
    print("Let's go")
    play="yes"
    while(play=="yes"):
        xstate=[0,0,0,0,0,0,0,0,0]
        ystate=[0,0,0,0,0,0,0,0,0]
        turn=1
        count=0
        while(True):
            board(xstate,ystate)
            if(turn==1):
                print("X's Turn:")
                n=int(input("please enter a number:"))
                xstate[n]=1
                count+=1
            else:
                print("O's Turn:")
                n=int(input("please enter a number:"))
                ystate[n]=1
                count+=1
            result=check_win(xstate,ystate)
            if(count==9):
                board(xstate,ystate)
                print("Match draw")
                print("Game over")
                break
            if(result!=-1):
                break
            turn=1-turn
        play=input("Do you want to play another game??(yes/no):")
if __name__=="__main__":
    main()