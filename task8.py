# Python function to multiply all the numbers in a list.


def multiplyLst(myList) : 
	
	# Multiply elements one by one 
	result = 1
	for x in myList: 
		result = result * x 
	return result 
	

list1 = [1, 2, 3] 
list2 = [3, 2, 4] 
print(multiplyLst(list1)) 
print(multiplyLst(list2)) 
