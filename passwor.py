import re
pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}")
string = "123456790."
a = pattern.fullmatch(string)
print(a)
if pattern.fullmatch(string):
    print("Password usable")
break
else:
    print("Not a usable passowrd")  


