import nltk
#To tokenize the string 
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')
check_List=[]
Interests=input("Which stream , or technology are you interested in persuing a career")
my_Token=word_tokenize(Interests)
print("\...Tokens are ...", my_Token )
port_Stem=PorterStemmer()
# Printing the stem and the words generted by tokenizer
for my_w in my_Token:
    print("\n..word is..",my_w)
    my_Stem=port_Stem.stem(my_w)
    print("...stem is ...", my_Stem)
    check_List.append(my_Stem)
print("\n.. generated list is :",check_List)
f = open("make_new_Facts.pl",'w')
if "career" in check_List:
    if "app" in check_List:
        if "develop" in check_List:
            f.write("check(appdevelopment).")
    if "ai" in check_List:    
        f.write("check(ai).")
    # interested in biology, so we generate a fact on biology.
    if "biolog" in check_List:
        f.write("check(biology).")

f.close()


