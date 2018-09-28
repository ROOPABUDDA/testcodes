"""
version 1.0.0
date: 9/18/2018
author ROOPA BT
"""

"""
The below code is to return the highest tweeter in ascending order
CASE-1
SAMPLE INPUT:
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

SAMPLE OUTPUT
sachin 3

CASE-2
SAMPLE INPUT
1
6
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
kohli tweet_id_5
kohli tweet_id_6

SAMPLE OUTPUT
kohli 2
sachin 2
sehwag 2

CASE-3
SAMPLE INPUT:
2
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sehwag tweet_id_4
5
dhoni tweet_id_10
dhoni tweet_id_11
kohli tweet_id_12
dhoni tweet_id_13
dhoni tweet_id_14

SAMPLE OUTPUT:
sachin 2
sehwag 2
dhoni 4
"""


def tweet_count(userlist):	
	user_unique = set(userlist)
	userdict = {each:userlist.count(each) for each in user_unique}
	max_value = max(userdict.values())
	max_keys = [k for k, v in userdict.items() if v == max_value]
	for each in sorted(max_keys):
		print(each, max_value)


T = int(input())
for test_case in range(T):
	tweets = int(input())
	l = [input().split() for tweet in range(tweets)]
	userlist = [each[0] for each in l]
	tweet_count(userlist)
