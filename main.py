from modules.dictionary_generator.index import WordGen
import modules.fileWriter.index as fs

try:
    length = int(input("What should be the length of each word?"))
    filename = input("Please type any filename for saving all these words : ")
    activate = input("Activate stop words(respond with either true or false):")
    activate = activate.lower()
    if(activate=="true"):
        wordgen = WordGen(length,True)
    else:
        wordgen = WordGen(length)

    case_sensitive = input("Uppercase?(please respond with either true or false):")
    case_sensitive = case_sensitive.lower()
    words = wordgen.words
    if case_sensitive == "true":
        words = words.upper()
    fs.save(filename,words)
except Exception as e:
    print(e)

