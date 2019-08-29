import json

flag = True
load_data = []
while flag:
    user = input("Enter U for update , Enter C for create , Enter D for delete , Enter Q for quit")
    if user == "Q":
        flag = False

    if user == "C":
        data = [{"firstname": input("Enter name: "),
                "lastname": (input("Enter Father's Name: ")),
                "age": int(input("Enter Age: "))}]

        print("Data Posted Successfully")

        with open("SDMS.json", 'a') as f:
            json.dump(data, f)
            f.close()

    if user == "U":
        data = [{"firstname": input("Enter name: ").lower(),
                "lastname": (input("Enter Father's Name: ")).lower(),
                "age": int(input("Enter Age: "))}]
        print("Data Updated Successfully")

        with open("SDMS.json", 'w+') as f:
            json.dump(data, f)
            f.close()


    if user == "D":
    
        for jsonFile in :
            with open(jsonFile) as f:
                data = f.read()
                jsondata = json.loads(data)



        with open("SDMS.json","r") as f:
            another = json.load(f)
            for i in another:
                for keys in i:
                    print(keys)






