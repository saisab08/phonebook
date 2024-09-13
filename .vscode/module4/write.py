#write,#read,#append 
text = "hellow world"
with open("myfile.txt","+w") as file:
    file.write(text)
print("writing success")