with open('Codingal.txt', 'w') as file:
    file.write("Hi this text you are reading is typed by code with python to test it")
    file.close()


with open('Codingal.txt', 'r')as file:
    data = file.readlines()
    print("Words in this file are ....")
    for line in data:
        word = line.split()
        print(word)
file.close()