import string

class CaesarCipher(object):

	characters=string.ascii_letters+" "+"."

	def get_message(self):
		message=raw_input("Please input message: ")
		return message
		
	def get_shift(self):
	
		shift=int(input("Please input number of shifts: "))
		
		return shift
		
	def encrypt(self,m essage,shift):
		encrypted=""
		l=len(self.characters)
		lenmessage=len(message)
		for i in range(lenmessage):
			post=(self.characters.find(message[i])+shift) % l
			encrypted+=self.characters[post]
		return encrypted
		
	def decrypt(self,message,shift):
		decrypted=""
		l=len(self.characters)
		lenmessage=len(message)
		for i in range(lenmessage):
			post=(self.characters.find(message[i])-shift) % l
			decrypted+=self.characters[post]
		return decrypted
		
		
def main():

	c=CaesarCipher()
	message=c.get_message()
	shft=c.get_shift()
	encrypted=c.encrypt(message,shft)
	decrypted=c.decrypt(encrypted,shft)
	
	print ("Message: ",message)
	print ("Encrypted: ",encrypted)
	print ("Decrypted: ",decrypted)
	

		
main()
	
	
