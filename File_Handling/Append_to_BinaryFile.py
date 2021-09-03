import pickle
file = open("NewFile.dat","ab")
Subject = []
while(True):
    Subject_1 = input("Enter Subject No. 1 Name")
    Subject_2 = input("Enter Subject No. 2 Name")
    Subject_3 = input("Enter Subject No. 3 Name")
    Subject_4 = input("Enter Subject No. 4 Name")
    data = [Subject_1,Subject_2,Subject_3,Subject_4]
    Subject.append(data)
    Sub = input("Do you want to enter more Subjects? [Y/N]:")
    if(Sub == "N"):
        break
pickle.dump(Subject,file)
file.close()

def read():
    file = open("NewFile.dat","rb")
    data = ''
    try :
        while(data):
            data = pickle.load(file)
            for i in data:
                print(i)
    except:
        print("End of Line")
read()
