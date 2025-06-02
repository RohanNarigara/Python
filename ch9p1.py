f = open("poem.txt", "r")
content = f.read()
if("twinkle" in content):
    print("The word exits in the file")
else:
    print("Sorry, i couldn\'t find the Word!")
f.close()