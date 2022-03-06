""" GET A STRING FROM AN INPUT STRING WHERE ALL OCCURENCES OF FIRST CHARACTER REPLACED WITH 
‘$’, EXCEPT FIRST CHARACTER."""
 
String=input("Enter a String: ")
print(String[0] + String[1:].replace(String[0],'$'))