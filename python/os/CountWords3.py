#!/usr/bin/python3
import string
class Words(object):

	paragraph="The quick brown fox jumps over the lazy dog. "
	paragraph+="Now is the time for all good men to come to the aide of their country. "
	paragraph+="Peter picked a pack of pickled paper. "
	paragraph+="The Python programming language was created by" 
	punctuation=string.punctuation+string.whitespace
	

	def input_word(self):
		word=str(input("Please input word to search: "))
		return word
		
	def search_word(self,word):
		l=len(self.paragraph)
		lw=len(word)
		print ("The word is : %s" % word)
		for i in range(l-lw+1):
			current_word=self.paragraph[i:i+lw]
			if current_word.lower() == word.lower():
				if self.is_word(current_word,i):
					print ("Word found: %s at %d" % (current_word,i))
		return
		
	def is_word(self,word,start):

		if start>0:
			if self.paragraph[start-1] in self.punctuation:
				isword=True
			else:
				isword=False
		else:
			isword=True


		if isword:
		
			if len(self.paragraph)>start+len(word):
				if self.paragraph[start+len(word)] in self.punctuation:
					isword=True
				else:
					isword=False

		return isword


	def display_word(self):
		l=len(self.paragraph)
		print ("Length : %d " % l)
		while l>0:
			print (self.paragraph[-l]),
			l-=1
		return

if __name__=="__main__":
	x=Words()
	print (x.paragraph)
	x.search_word(x.input_word())

