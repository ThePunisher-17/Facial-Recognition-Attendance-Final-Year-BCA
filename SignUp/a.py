import re 
name = "John Smith" 
match = re.search(r"^[A-Z][a-z]+(\s[A-Z][a-z]+)*$", name) 
if match:
    print("Valid name") 
else:
    print("Invalid name")