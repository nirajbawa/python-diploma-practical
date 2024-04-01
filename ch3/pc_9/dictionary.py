
# creating dictionary
print("\n\ncreating dictionary : \n\n")
d = {"name":"niraj", "class":"ty-co"}

# accessing dictionary
print(d["name"])
print(d["class"])

# pringing all dictionary elements
print("\n\npringing all dictionary elements: \n\n")
for key, val in d.items():
    print(key, " : ", val)
    
# updaing dictinary elements
print("\n\nupdating dictionary elements : \n\n")
d["name"] = "bava"

d.update({"class": "sy-co"})
d.update({"school": "jamia"})

print(d)

# deleing dictionary elemetns
print("\n\ndeleing dictionary elemetns : \n\n")
del d["name"]
print(d)

print(d.pop('class'))
print(d.popitem())
print(d)

del d
try:
    print(d)
except Exception as e:
    print(e)

    
    

