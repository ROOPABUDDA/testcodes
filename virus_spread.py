"""
version 1.0.0
date: 9/20/2018
author ROOPA BT
"""

"""[summary]
To get the time taken for files to be infected with virus in that folder
[description]

SAMPLE INPUT:
3
6 5
(2,2)
100 50
(39,5)
44 130
(1,1)

SAMPLE OUTPUT:
4 seconds
1 minute 1 second
2 minutes 9 seconds
"""
import time
T = int(input())

def check_virus(infected):
	"""[summary]
	to check for virus in file with respect t  location and spread the virus
	[description]
	
	Arguments:
		infected {[list]} -- [contains the files that are already infected with virus with non duplicate values]
	"""
	global second	
	for each in infected:		
		i = each[0]
		j = each[1]
		flag = False
		if(mat.count([i-1,j]) == 1) and (infected.count([i-1,j])==0):
			newlist.append(([i-1,j]))
			flag = True
		if(mat.count([i+1,j]) == 1) and (infected.count([i+1,j])==0):
			newlist.append(([i+1,j]))
			flag = True
		if(mat.count([i,j-1]) == 1) and (infected.count([i,j-1])==0):
			newlist.append(([i,j-1]))
			flag = True
		if(mat.count([i,j+1]) == 1) and (infected.count([i,j+1])==0):
			newlist.append(([i,j+1]))
			flag = True
		if(mat.count([i-1,j+1]) == 1) and (infected.count([i-1,j+1])==0):
			newlist.append(([i-1,j+1]))
			flag = True
		if(mat.count([i+1,j-1]) == 1) and (infected.count([i+1,j-1])==0):
			newlist.append(([i+1,j-1]))
			flag = True
		if(mat.count([i-1,j-1]) == 1) and (infected.count([i-1,j-1])==0):
			newlist.append(([i-1,j-1]))
			flag = True
		if(mat.count([i+1,j+1]) == 1) and (infected.count([i+1,j+1]) == 0):
			newlist.append(([i+1,j+1]))
			flag = True
	if(flag):		
		second = second+1


for test_case in range(T):
	matrix = list(map(int,input().split()))
	n = matrix[0] 
	m = matrix[1] 
	mat=  [[row,col] for row in range(1,n+1) for col in range(1,m+1)]
	viruslocation = input().split(",")	
	i = viruslocation[0][1:]
	j = viruslocation[1][:-1]
	
	virus = [int(i),int(j)]
	infected = list([virus])
	second =0 	
	newlist = list([virus])
	start_time = time.time()

	for count in range(max([n,m])):
		infected = sorted((infected +newlist))
		infected = [infected[i] for i in range(len(infected)) if i == 0 or infected[i] != infected[i-1]]
		if(infected != mat):
			check_virus(infected)
		elif(infected == mat):
			break

	min_str = ""
	sec_str = ""
	if(second >59):
		if(second%60 ==0):
			#minute = int(second/60)
			min_str = (str(minute) + " minutes") if int(second/60)>1 else "1 minute"
		else:
			#minute = int(second/60)
			#sec = second%60
			min_str = (str(int(second/60)) + " minutes") if int(second/60)>1 else "1 minute"
			sec_str = (str(sec) + " seconds") if (second%60)>1 else "1 second"
		print(min_str + " " + sec_str)
	elif(second==1):
		print(" 1 second")
	else:
		print(str(second) + " seconds")
	print(time.time() - start_time)
