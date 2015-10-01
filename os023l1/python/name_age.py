
def get_number():
	number=int(raw_input("Please input a number: "))
	return number 

def odd_or_even(n):
	if n % 2 == 0:
		return "Even"
	else:
		return "Odd"

def for_loop1(n):
	sum = 0
	for x in range (1,n+1):
		sum += x
	return sum

	
def for_loop2(n):
	sum = 0
	for x in xrange (1,n+1):
		sum += x
	return sum

def for_loop3(n):
	sum = 0
	for x in xrange (n,0,-1):
		sum += x
	return sum

def while_loop1(n):
	sum = 0
	while n>0:
		sum += n
		n -= 1

	return sum

def recur(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return n+recur(n-1)

def input_name():
	name = raw_input("Please enter your name: ")
	age  = int(raw_input("Please input your age: "))
	print "Hi %s, you're young at %d" % (name,age)

def evaluate_number():
	number = get_number()
	print "The number is : ", number
	print "The number is : ",odd_or_even(number)
	print "Arithmetic sum is for loop1 : ",for_loop1(number)
	print "Arithmetic sum is for loop2 : ",for_loop2(number)
	print "Arithmetic sum is for loop3 : ",for_loop3(number)
	print "Arithmetic sum is while     : ",while_loop1(number)
	print "Arithmetic sum is recursion : ",recur(number)


def main():
	evaluate_number()

if __name__ == "__main__":
	main()
