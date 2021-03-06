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

for test_case in range(T):
	matrix = list(map(int,input().split()))
	n = matrix[0] 
	m = matrix[1] 
	mat=  [[row,col] for row in range(1,n+1) for col in range(1,m+1)]
	viruslocation = input().split(",")	
	i = int(viruslocation[0][1:])
	j = int(viruslocation[1][:-1])
	second = max((n-i),(m-j))
	start_time = time.time()
	min_str = ""
	sec_str = ""
	if(second >59):
		if(second%60 ==0):			
			min_str = (str(minute) + " minutes") if int(second/60)>1 else "1 minute"
		else:			
			min_str = (str(int(second/60)) + " minutes") if int(second/60)>1 else "1 minute"
			sec_str = (str(second%60) + " seconds") if (second%60)>1 else "1 second"
		print(min_str + " " + sec_str)
	elif(second==1):
		print(" 1 second")
	else:
		print(str(second) + " seconds")
	print(time.time() - start_time)
