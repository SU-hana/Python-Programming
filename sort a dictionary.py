""" SORT DICTIONARItem IN ASCENDING AND DESECNDING ORDER """

Item = {'Carl':40,'Alan':2,'Bob':1,'Dann':3}
l = list(Item.items())
dict=dict(l)
print("Dictionary Item: ",dict)
l.sort()
print('Ascending order is: ',l)
l=list(Item.items())
l.sort(reverse=True)
print('Descending order is: ',l)
print("\n")