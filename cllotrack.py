print("hi")


a, b = 1, 2


a = a+b
b = a-b
a = a-b



a = a, b


firstfile.pyc

__pycache__

gcc

a = [1,2,3,4,1,2,3]

x = []
for each in a:
	if(a.count(each)>1):
  	x.append(each)
x = list(set(a))


person = { "Name" : "Farhaan"}
person["Age"] = 23

name = person.get("Name")

word = "MOM"

for i in range(len(word)):
	if (word[i] != word[len(word)-i-1]):  	
  	print("Its is not a plindrome")
    break

if(word == word[::-1])
  
  
  word[0:1]
  word[::-1]
  

sentence = "Farhaan was here"

list_of_words = sentence.split(" ")
rev_list = list_of_words.reverse()
rev_list = list_of_words[::-1]
list_to_string = " ".join(rev_list)


def str_to_file(filename,input_string):
	with open(filename,"w+") as f_obj:
    f_obj.writeline(input_string)

frequency_dict = {}
count = 1
for each in list_of_words:
  if not frequency_dict.get(each):
    frequency_dict[each] = count
  else:
    c = frequency_dict[each]
    frequency_dict[each] = c+1

  
  
  
  
  
  











