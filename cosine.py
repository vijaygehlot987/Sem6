from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
file1=open("C:/Users/Admin/Documents/a1.txt",'r')
file2=open("C:/Users/Admin/Documents/a2.txt",'r')

 
# tokenization 
x = word_tokenize(file1.read())  
y = word_tokenize(file2.read()) 

  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[]
l2 =[]
  
# remove stop words from string 
a = {w for w in x if not w in sw}  
b = {w for w in y if not w in sw}

  
# form a set containing keywords of both strings  
rvector = a.union(b)  
for w in rvector: 
    if w in a: 
        l1.append(1) # create a vector 
    else: 
        l1.append(0) 
    if w in b: 
        l2.append(1) 
    else: 
        l2.append(0)
c=0
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("Cosine similarity: ", cosine)