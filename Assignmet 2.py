# ----------------- Createing.
createList = ['5', '7', 'aiquest', 'Studymart']
print(createList)
createList = ['5', '7', 'aiquest', 'Studymart']
while True:
    create_list = input("What do you want? Enter Choice : read / add / update / delete /quite:")
    if create_list == "quite ":
        print("You exist from program")
        break  
    else:
        print("Please enter ringht comman.")
        break

#--------------------- Reading

createList = ['5', '7', 'aiquest', 'Studymart']
while True:
    create_list = input("What do you want? Enter Choice : read / add / update / delete /quite:")
    # read your List
    if create_list == "read":
        print("Congragulation! This is your list : ", createList)
        break
    else:
        print("Please enter ringht comman.")
        break

#--------------------- Updating

createList = ['5', '7', 'aiquest', 'Studymart']
while True:
    create_list = input("What do you want? Enter Choice : read / add / update / delete /quite:")

# update element from your List
    if create_list == "update":
        up_wrong = input("Enter wrong item: ", )
        up_right = input("Enter right item: ", )
        if up_wrong in createList:
            wr = createList.index(up_wrong)
            createList [wr] = up_right
            print("his is your update list: ", createList)
        else:
            print("Not matched item")
            
        break
    else:
        print("Please enter ringht comman.")
        break

#--------------------- Deleting
createList = ['5', '7', 'aiquest', 'Studymart']
print(createList)
while True:
    create_list = input("What do you want? Enter Choice : read / add / update / delete /quite:")
    if create_list == "delete":
        dl = input("Enter deleted item: ", )
        if dl in createList:
            createList.remove(dl)
        else:
            print("Not matched item")            
        print("This is your deleted list", createList)
        break  
    else:
        print("Please enter ringht comman.")
        break