#Developed by - Tejas Kapade
#Powerd By - Andro Coder
#Dec-24 / 2020 ( 4.50 pm )
#You Tube - Andro Coder 
#Instagram - @andro_coder

game=[" "," "," "," "," "," "," "," "," "]
state = False
print("Game Board Keys\n")
print( "\n","0"," | " ,"1"," | ","2","\n","_____________\n","3"," | " ,"4"," | ","5","\n","_____________\n","6"," | " ,"7"," | ","8\n"	)
px = 0
def winx():
	if((game[0] == "X" and game[1] == "X" and game[2] == "X") or (game[0] =="X" and game[3] == "X" and game[6] == "X") or (game[1] == "X" and game[4] == "X" and game[7] == "X") or (game[2] == "X" and game[5] == "X" and game[8] == "X") or (game[3] == "X" and game[4] == "X" and game[5]) or (game[6] == "X" and game[7]== "X" and game[8] == "X") or (game[0] == "X" and game[4] == "X" and game[8] == "X") or (game[2] == "X" and game[4] == "X" and game[6] == "X")):
	
		return True
		
def winy():
   if((game[0] == "O" and game[1] == "O" and game[2] == "O") or (game[0] =="O" and game[3] == "O" and game[6] == "O") or (game[1] == "O" and game[4] == "O" and game[7] == "O") or (game[2] == "O" and game[5] == "O" and game[8] == "O") or (game[3] == "O" and game[4] == "O" and game[5]) or (game[6] == "O" and game[7]== "O" and game[8] == "O") or (game[0] == "O" and game[4] == "O" and game[8] == "O") or (game[2] == "O" and game[4] == "O" and game[6] == "O")):
   	return True
   
while(True):
 try:
 	statex = winx()
 	statey = winy()
 	if(statex):
 		print("\nPlayer X , Wins Game !!\n")
 		break
 	if(statey):
 		print("\nPlayer O , Wins Game !!\n")
 		break
 	play1 =  int(input("\nPlayer 1 X input is ___\n"))
 	if(play1 >= 9 ):
 		print("\ninput must not greater than 8 \n")
 		continue
 	if(game[play1] != " "):
 		print("\nAlready Taken , choose another\n")
 		continue
 	else:
 		game[play1] = "X"
 	if(statex):
 		print("\nPlayer X , Wins Game !!\n")
 		break
 	if(statey):
 		print("\nPlayer O , Wins Game !!\n")
 		break
 	print( "\n",game[0]," | " ,game[1]," | ",game[2],"\n","_____________\n",game[3]," | " ,game[4]," | ",game[5],"\n","_____________\n",game[6]," | " ,game[7]," | ",game[8]
	)
	
 	play2 =  int(input("\nPlayer 2 O input is ___\n"))
 	if(statex):
 		print("\nPlayer X , Wins Game !!\n")
 		break
 	if(statey):
 		print("\nPlayer O , Wins Game !!\n")
 		break
 	if(play2 >= 9):
 		print("\n invalid try again\n")
 		continue
 	if(game[play2] != " "):
 		print("\nAlready Taken , choose another\n")
 		continue
 	else:
 		game[play2] = "O"
 	if(statex):
 		print("\nPlayer X , Wins Game !!\n")
 		break
 	if(statey):
 		print("\nPlayer O , Wins Game !!\n")
 		break
 	print( "\n",game[0]," | " ,game[1]," | ",game[2],"\n","_____________\n",game[3]," | " ,game[4]," | ",game[5],"\n","_____________\n",game[6]," | " ,game[7]," | ",game[8]	)
 	
 except ValueError:
 	print("\nInvalid Input Try Again___\n")
	 
