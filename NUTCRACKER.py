NUTCRACKER = open("C:\\Users\\User\\.spyder-py3\\EXERCISES\\FOR NUTCRACKER.txt","r")
#Open file located in computer

target = "qwerty123" #Set target password as following

for x in NUTCRACKER: #create a loop that continues until the end of file
    if x.strip() == target: #if password matches target
        print(f"Password: {x}")
        print("Access granted")
        print("")
        break #print following and break loop
    else: #if not
        print(f"Password: {x}")
        print("Access denied")
        print("")
        #print following and continue loop
        
NUTCRACKER.close() #close file to prevent error