###### this is the second .py file ###########

####### write your code here ##########


print "Welcome to the Game!"


#matrix = "\n".join([" ".join(["0" for x in range(3)]) for x in range(3)])

#list1 = list(matrix)

player1 = [1,3,5,7,9]
player2 = [2,4,6,8]


list1 = [0,0,0,0,0,0,0,0,0]



def play_game(lst):
	flag = "True"
	rem = lst[0]%2
	#rem2 = lst2[0]%2
	if(rem!=0):
		print "Player 1's chance"
	else:
		print "Player 2's chance"
	
	print "Enter the position and number to be entered:"
	x,y = map(int, raw_input().split(','))
	if(x>=1 and x<=9):
		if(y>=1 and y<=9):
			list1[x-1]=y
			lst.remove(y)

	for i in xrange(0,9,3):
		print (str(list1[i])).ljust(2)+(str(list1[i+1])).ljust(2)+(str(list1[i+2])).ljust(2)

	h1 = list1[0]+list1[1]+list1[2]
	h2 = list1[3]+list1[4]+list1[5]
	h3 = list1[6]+list1[7]+list1[8]

	v1 = list1[0]+list1[3]+list1[6]
	v2 = list1[1]+list1[4]+list1[7]
	v3 = list1[2]+list1[5]+list1[8]

	d1 = list1[0]+list1[4]+list1[8]
	d2 = list1[2]+list1[4]+list1[6]

	summ = [h1,h2,h3,v1,v2,v3,d1,d2]
	for i in range(len(summ)):
		if(summ[i]>=15):
			print summ
			flag="False"
			break

	return flag





flag = "True"
while(flag=="True"):
	
	flag = play_game(player1)
	print flag
        flag = play_game(player2)
	print flag


print "Want to play another game"

resp = raw_input()

if(resp=="yes"):
	
	while(flag=="True"):
	
		flag = play_game(player1)
		print flag
		flag = play_game(player2)
		print flag


#for i in range(3):
#	print (str(list1[i])).ljust(2)+(str(list1[i+1])).ljust(2)+(str(list1[i+2])).ljust(2)

