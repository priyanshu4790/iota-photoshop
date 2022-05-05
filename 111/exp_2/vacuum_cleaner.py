def func():
    goal_state = {'A':0,'B':0} 
    # 0 for clean and 1 for dirty
    location_input = input("Enter location of vacuum(A/B): ")
    status_input = input("Enter the status of" + location_input + "(0/1) : ")
    nextroom_status_input = input("Enter status of other room : ")
    
    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'
            print("Location A is cleaned")
            if nextroom_status_input == '1':
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                goal_state['B'] = '0'
            else:
                print("Location B is already cleaned")
    
        if status_input == '0':
            print("Location A is already clean ")
            if nextroom_status_input == '1':
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B. ")
                goal_state['B'] = '0'
                print("Location B has been Cleaned. ")
            else:
                print("Location B is already clean.")
    
                
    else:
        print("Vacuum is placed in Loaction B")
        if status_input == '1':
            print("Loaction B is dirty")
            goal_state['B'] = '0'
            print("Location B has been cleaned.")
            if nextroom_status_input == '1':
                print("Location A is dirty.")
                print("Moving left to the location A")
                goal_state['A'] = 0
                print("Location A has been cleaned.")
        else:
            print("loaction B is already clean.")
            if nextroom_status_input == '1':
                print("Location A is dirty.")
                print("Moving left to the location A.")
                goal_state["A"] = 0
                print("Location A has been cleaned.")
            else:
                print("location A is already cleaned.")
    print("Goal State: ")
    print(goal_state)

func()
