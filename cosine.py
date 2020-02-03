from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 



file1=open("C:/Users/Admin/Documents/a1.txt",'r')
file2=open("C:/Users/Admin/Documents/a2.txt",'r')
file3=open("C:/Users/Admin/Documents/a3.txt",'r')
 
# tokenization 
x = word_tokenize(file1.read())  
y = word_tokenize(file2.read()) 
z = word_tokenize(file3.read())
  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[];l3=[] 
  
# remove stop words from string 
a = {w for w in x if not w in sw}  
b = {w for w in y if not w in sw}
c = {w for w in z if not w in sw}
  
# form a set containing keywords of both strings  
rvector = a.union(b.union(c))  
for w in rvector: 
    if w in a: 
        l1.append(1) # create a vector 
    else: 
        l1.append(0) 
    if w in b: 
        l2.append(1) 
    else: 
        l2.append(0)
    if w in c: 
        l3.append(1) 
    else: 
        l3.append(0)
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i]*l3[i] 
cosine = c / float((sum(l1)*sum(l2)*sum(l3))**0.5) 
print("Cosine similarity: ", cosine)