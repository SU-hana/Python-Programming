""" WRITE A PYTHON PROGRAM TO READ A FILE LINE BY LINE AND STORE IT INTO A LIST """

with open("text.txt") as f:
 content=f.readlines()
 li=[x.strip() for x in content]
print(li)