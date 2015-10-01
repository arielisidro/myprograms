def recur(n):
	if n==0:
		return 0
	else:
		return n+recur(n-1)

def main():
	
	x=int(raw_input("any number? "))
	print "Summation: %d " % recur(x)

if __name__ == "__main__":
	main()
