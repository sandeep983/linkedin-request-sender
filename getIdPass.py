#get the id and password from text file

def getIdPass(a): 
    match a:
        case 1:
            try:
                with open('sid.txt', mode='r') as file:
                    idpass = file.readlines()
                    return idpass
            except Exception as e:
                print(f'{e}\n"sid.txt" file was not found')
        
        case 2:
            try:
                with open('bid.txt', mode='r') as file:
                    idpass = file.readlines()
                    return idpass
            except Exception as e:
                print(f'{e}\n"bid.txt" file was not found')

        case 3:
            try:
                with open('hid.txt', mode='r') as file:
                    idpass = file.readlines()
                    return idpass
            except Exception as e:
                print(f'{e}\n"hid.txt" file was not found')
            
        case _:
            print("Invalid choice")