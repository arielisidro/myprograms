import string

class PlayFair(object):

	characters=string.ascii_lowercase

	def get_message(self):
		message=str(input("Please input message: "))
		return message
		
	def get_key(self):
		key=str(input("Please input key: "))
		return key
		
	def construct_matrix(self,key):
		m=key
		exclude='i'
		for c in self.characters:
			if c in m:
				pass
			elif c != exclude:
				m += c
				
		matrix=[[0 for x in range(5)] for x in range(5)]
		for i in range(5):
			for j in range(5):
				matrix[i][j]=m[i*5+j]
										
		return matrix
		
	def reconstruct_message(self,message):
		new_message=""
		prev_char=""
		for c in message:
			if c==prev_char:
				new_message += prev_char + "x"
			else:
				new_message += prev_char 
			prev_char=c
		new_message += prev_char
		
		return new_message
		
	def print_matrix(self,matrix):
		for i in range(5):
			print (matrix[i])
		
		
	def encrypt(self,message,matrix):
		encrypted=""
		print (message)
		l=len(message)
		i=0
		while i<l:
			c2=message[i:i+2]
			#check row
			for i in range(5):
				if c2[0] in matrix[i] and c2[1] in matrix[i]:
					encrypted += 
			
			print (message[i:i+2])
			i += 2
		
		return encrypted
		
	def decrypt(self,cipher,key,shift):
		decrypted=""
		l=len(self.characters)
		lencipher=len(cipher)
		for i in range(lencipher):
			position_cipher=(self.characters.find(cipher[i]))
			position_key=(self.characters.find(key[i])      )
			post = ((position_cipher - shift) - position_key - shift ) % l
			decrypted+=self.characters[post]
		return decrypted
		
		
def main():

	c=PlayFair()
	message=c.get_message()
	key=c.get_key()
	matrix=c.construct_matrix(key)
	c.print_matrix(matrix)
	new_message=c.reconstruct_message(message)
	
	encrypted=c.encrypt(new_message,matrix)
	#decrypted=c.decrypt(encrypted,key2,shift)
	
	#print ("Key: ",key2)
	#print ("Message: ",message)
	#print ("Encrypted: ",encrypted)
	#print ("Decrypted: ",decrypted)
	

		
main()
	
	
