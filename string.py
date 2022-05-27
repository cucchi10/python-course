myStr = "hello world"

# print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.title())
print(myStr.swapcase())
print(myStr.capitalize())

print (myStr.replace("hello", "bye"))
print (myStr.replace("hello", "bye").upper())

print(myStr.count("l"))

print(myStr.startswith("hello"))
print(myStr.endswith("d"))

print(myStr.split())
print(myStr.split("o"))


print(myStr.find("o")) #busca posicion del caracter
print(len(myStr))

print(myStr.index("e"))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])
print(myStr((0,1,2,3,4)))
print(myStr[-4])

print(f"El tipico texto es {myStr}")
print("El tipico texto es {0}".format(myStr))


