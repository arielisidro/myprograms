import string
class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid=guid
        self.title=title
        self.subject=subject
        self.summary=summary
        self.link=link
    def getGuid(self):
        return self.guid
        
    def getTitle(self):
        return self.title
        
    def getSubject(self):
        return self.subject
        
    def getSummary(self):
        return self.summary
        
    def getLink(self):
        return self.link                                                                                                                                                                                                                                                        

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word=word

    def rearrangeText(self,text):
        newText=text.lower()
        for t in string.punctuation:
            if t in newText:
                newText=newText.replace(t,' ')
        return newText                
                
        
    def isWordIn(self,text):
        wordLower=self.word.lower()
        newTextSplit=self.rearrangeText(text).split(' ')
        for t in newTextSplit:
            if t==wordLower:
                return True
        return False                
        

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self,story):
        return Trigger.isWordIn(story.title)
