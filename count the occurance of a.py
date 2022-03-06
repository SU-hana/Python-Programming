""" STORE A LIST OF FIRST NAMES.COUNT THE OCCURRENCES OF ‘a’ WITHIN THE LIST """

Words = ['able', 'table', 'cable', 'label', 'stable', 'fable']
a_count = 0
for word in Words:
    for char in word:
        if char == 'a':
            a_count = a_count + 1

print (a_count)