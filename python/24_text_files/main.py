with open("xxx.txt", "w") as text_file:
    text = "Ala ma kota"
    text_file.write(text)


with open("xxx.txt", "r") as xxx:
    print(xxx)
    xxx_contents = xxx.readline()
    print(xxx_contents)


with open("xxx.txt", "a") as text_file:
    text = "\n" + "Ala ma kota"
    text_file.write(text)


with open("xxx.txt", "w") as text_file:
    text = ""
    text_file.write(text)
