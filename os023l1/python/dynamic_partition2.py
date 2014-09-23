
def main():

	partitions=(100,500,200,300,600)
	allocations=[]
	dicts={}
	print ("**** using lists ****")
	for p in partitions:
		print "Partition: ", p
		allocations.append(p)
	allocations.append(700)
	print ("allocation")
	#partitions.append(300)
	for a in allocations:
		print "Allocation: ", a

	print ("**** using arrays **** and for-loop")
	print ("Note: start with 0, and end with the number of elements")
	for i in range(0,5):
		print "Partition: ", partitions[i]
		dicts[partitions[i]]=i;

	for i in dicts.keys():
		print ("dicts ",i," = ",dicts[i])

	return

if __name__ == "__main__":
	main()

