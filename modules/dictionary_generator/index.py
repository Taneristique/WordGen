import random
class WordGen: 
    def __init__(self, length,sw = False):
        if length <= 2 or length > 64:
            raise ValueError("Length should be between 2 and 65!")
        self.count= 100000
        self.c ='' # it will store the words of the dictionary 
        if(sw == True):
            self.c = [chr(i) for i in range(97,123)] + [str(j) for j in range(10)]+['?','.','!','*']
        else:
            self.c = [chr(i) for i in range(97,123)] + [str(j) for j in range(10)]
        self.length = length # character length
        self.words = self.generate()
    def generate(self):
        words = ""
        for _ in range(self.count):
            for _ in range(self.length):
                words += self.c[random.randint(0,len(self.c)-1)]
            words+="\n"
        return words
