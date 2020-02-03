from nltk.tokenize import word_tokenize
file1 =open("C:/Users/admin/Desktop/stopword1.txt",'r')
s1=word_tokenize(file1.read())
print(s1)
file2 =open("C:/Users/admin/Desktop/stopword2.txt",'r')
s2=word_tokenize(file2.read())
print(s2)
a=0
def intersection(s1,s2):
    return list(set(s1) & set(s2))
print(intersection(s1, s2))
print(len(intersection(s1, s2)))
def Union(s1, s2):
    unionlist= list(set(s1)|set(s2))
    return unionlist
print(Union(s1,s2))
print(len(Union(s1,s2)))
jaccard=float(len(intersection(s1, s2))/len(Union(s1,s2)))
print(jaccard)