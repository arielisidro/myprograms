def get_number():
	number=int(raw_input("Please input a number: "))
	return number

def check_number(number):
	if number>10:
		print "Number is greater than 10"
	else:
		print "Number is less than or equal to 10"
	
def r(n):
	if n==1:
		return 1
	else:
		return n+r(n-1)


def main():

	number=get_number()
	check_number(number)
	print "Arithmetic sum : %d " % r(number)

if __name__ == "__main__":
	main()
