import string

class PlayFair(object):

	characters=string.ascii_lowercase
	exclude="j"
	monograph="q"

	def get_message(self):
		message=str(input("Please input message: "))
		return message
		
	def get_key(self):
		key=str(input("Please input key: "))
		return key
		
	def construct_matrix(self,message,key):

		m=''

		#for c in self.characters:
		#	if c not in key+message:
		#		self.exclude=c
		#		break

		for c in key+self.characters:
			if c in m:
				pass
			elif c != self.exclude:
				m += c

		print (m)		

		matrix=[[0 for x in range(5)] for x in range(5)]
		for i in range(5):
			for j in range(5):
				matrix[i][j]=m[i*5+j]
										
		return matrix
		
	def reconstruct_message(self,message,key,e_or_d):

		new_message=""
		prev_char=""
		#for c in self.characters:
		#	if c not in key+message and c != self.exclude:
		#		self.monograph=c
		#		break
				 
		print ("monograph: %s, exclude: %s" %(self.monograph,self.exclude))
		
		for c in message:
			if e_or_d==1:
				if c==prev_char:
					new_message += prev_char + self.monograph
				else:
					new_message += prev_char 
				prev_char=c
			else:
				if c != self.monograph:
					new_message += c
		new_message += prev_char
		
		print ("New message: ", new_message)
		
		return new_message
		
	def print_matrix(self,matrix):
		for i in range(5):
			print (matrix[i])
		
	def check_line(self,line,pair,matrix,e_or_d):
	
		#e_or_d: -1 -> decrypt, 1 -> encrypt
		row=col=ix1=ix2=-9
		
		if line=='row':
			ix1=ix2=-9
			for row in range(5):
				if pair[0] in matrix[row] and pair[1] in matrix[row]:
					ix1 = (matrix[row].index(pair[0])+1*e_or_d) % 5
					ix2 = (matrix[row].index(pair[1])+1*e_or_d) % 5
					break
					
		elif line=='col':
		
			for col in range(5):
				ix1=ix2=-9
				column=[]
				for row in range(5):
					column += [matrix[row][col]]

				if pair[0] in column and  pair[1] in column:
					ix1=(column.index(pair[0])+1*e_or_d ) % 5
					ix2=(column.index(pair[1])+1*e_or_d ) % 5
					break

		else:
			#get intersection
			row1=row2=col1=col2=-9
			for row in range(5):
				for col in range(5):
					if pair[0] == matrix[row][col]:
						row1=row
						col1=col
					elif  pair[1]==matrix[row][col]:
						row2=row
						col2=col
							
					if row1 != -9 and row2 != -9:
						break
						
				if row1 != -9 and row2 != -9:
					break
			row=row1
			col=col2
			ix1=row2
			ix2=col1
			
		return row,col,ix1,ix2
		
	def encrypt_decrypt(self,msg,key,e_or_d):


		matrix=self.construct_matrix(msg,key)
		
		self.print_matrix(matrix)
		message=self.reconstruct_message(msg,key,e_or_d)

		encrypted=""
		l=len(message)
		ctr=0
		
		while ctr<l:
		
			pair=message[ctr:ctr+2]

			if len(pair)==1:
				pair=pair+self.monograph
				
			#check row
			row,col,ix1,ix2=self.check_line('row',pair,matrix,e_or_d)
			if ix2 != -9:
				encrypted += matrix[row][ix1]+matrix[row][ix2]
			else:
				#check col
				row,col,ix1,ix2=self.check_line('col',pair,matrix,e_or_d)
				if ix2 != -9:
					print (ix2)
					encrypted += matrix[ix1][col]+matrix[ix2][col]
				else:
					#intersect
					row,col,ix1,ix2=self.check_line('int',pair,matrix,e_or_d)
					encrypted += matrix[row][col]+matrix[ix1][ix2]

			ctr += 2
		
			
		return encrypted
		
	
def main():

	c=PlayFair()
	#message=c.get_message()
	#key=c.get_key()
	#message="hidethegoldinthetreestump"
	#key="playfairexample"
	message="wearediscoveredsaveyourselfx"
	key="monarchy"
	message="hidethegoldinthetreestump"
	key="playfairexample"
	
	
	encrypted=c.encrypt_decrypt(message,key,1)
	decrypted=c.encrypt_decrypt(encrypted,key,-1)
	decrypted=c.reconstruct_message(decrypted,key,-1)
	
	print ("Message: ",message)
	print ("BM OD ZB XD NA BE KU DM UI XM MO UV IF")
	print ("Key: ",key)
	print ("Encrypted: ",encrypted)
	print ("Decrypted: ",decrypted)
	

		
main()
	
	
