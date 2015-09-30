import string

class Viginere(object):

	characters=string.ascii_lowercase

	def get_message(self):
		message=str(input("Please input message: "))
		return message
		
	def get_key(self):
		key=str(input("Please input key: "))
		return key
		
	def expand_key(self,message,key):
		while len(key)<len(message):
			key += key
		return key
		
	def get_shift(self):
	
		shift=int(input("Please input number of shifts: "))
		
		return shift
		
	def encrypt(self,plain,key,shift):
		encrypted=""
		l=len(self.characters)
		lenplain=len(plain)
		for i in range(lenplain):
			position_plain=(self.characters.find(plain[i])+shift)
			position_key=(self.characters.find(key[i])    +shift)
			post = (position_plain + position_key) % l
			encrypted+=self.characters[post]
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

	c=Viginere()
	message=c.get_message()
	key=c.get_key()
	shift=c.get_shift()
	key2=c.expand_key(message,key)
	encrypted=c.encrypt(message,key2,shift)
	decrypted=c.decrypt(encrypted,key2,shift)
	
	print ("Key: ",key2)
	print ("Message: ",message)
	print ("Encrypted: ",encrypted)
	print ("Decrypted: ",decrypted)
	

		
main()
	
	
