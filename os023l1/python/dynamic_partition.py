
def main():

	partitions=100,500,200,300,600
	partitions[6]=700
	print ("**** using lists ****")
	for p in partitions:
		print "Partition: ", p

	print ("**** using arrays **** and for-loop")
	print ("Note: start with 0, and end the number of elements")
	for i in range(0,5):
		print "Partition: ", partitions[i]
	return


if __name__ == "__main__":
	main()

