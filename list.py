# a="kaka"
# b="kalanguka namutendereza athieno"
# identity=[a,b]
# print identity[1]
# length=len(b)
# print ("length of b: {0}".format(length))
# c=b.split(" ")
# print(c)


# first_str=c[1]
# print("split string {0}".format(first_str))
# i=0
# # s is for strings not splits
# for s in c:
# 	i=i+1
# 	upper=s.upper()
# 	print("upper case string: "+upper)



#how to read files while using open.txt
# file=open("C:/Users/ProBook/Documents/python-tutorials/open.txt","r")
# data=file.readlines()
# print(data)
# for item in data:
#  print(item) 

# file=open("C:/Users/ProBook/Documents/python-tutorials/text.txt","r")
# data=file.readlines()
# print(data)

# for item in data:
#  print(item) 


# #  # how to read file using text.txt
# for item in data:
# 	content=item.split(" ")
#  	# print(content)
#  	name=content[0]
#  	age=content[1]
#  	print("name: "+name)
#  	print("age: "+age)

# function that opens a file and returns data with in that file
# def opens_a_file():
# 	file=open("C:/Users/ProBook/Documents/python-tutorials/text.txt","r")
# 	data=file.readlines()
# 	print(data)
# 	return data

# d=opens_a_file()
# print (d)

# or....you can give it an argument as below
file_location="C:/Users/ProBook/Documents/python-tutorials/text.txt"
file_location1="C:/Users/ProBook/Documents/python-tutorials/open.txt"
files=[file_location,file_location1]


def opens_a_file(file_name):
	file=open(file_name,"r")
	data=file.readlines()
	print(data)
	return data



i=0
for i in range(0,2):
	current_file=files[i]
	d=opens_a_file(current_file)
	i=i+1
	print (d)












