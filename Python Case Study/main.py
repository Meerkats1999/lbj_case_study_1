import os
import pandas as pd
from college import College

if __name__ == "__main__":

    if os.path.exists("colleges.csv"):
        collegeDf = pd.read_csv("colleges.csv")
    else:
        collegeDf = pd.DataFrame(columns=["collegeId", "collegeName", "courseType", "city", "fees", "pinCode"])
        print(collegeDf)
        collegeDf.to_csv('colleges.csv', index=False)

    colleges = College(collegeDf)

    while(1):

        print("1: Register, 2: Display, 3: Remove, 4: Quit")
        option = int(input())
        if(option == 1):
            print("Enter College details to be entered")
            collegeId = input("College Id: ")
            collegeName = input("College Name: ")
            courseType = input("Course Type: ")
            city = input("City: ")
            fees = input("Fees: ")
            pinCode = input("Pin Code: ")
            colleges.registerNew(collegeId, collegeName, courseType, city, fees, pinCode)

        elif(option == 2):
            collegeDf = pd.read_csv("colleges.csv")
            colleges = College(collegeDf)
            courseType = input("Enter name of course: ")
            city = input("Enter name of city: ")
            colleges.Display(courseType, city)

        elif(option == 3):
            collegeDf = pd.read_csv("colleges.csv")
            colleges = College(collegeDf)
            print("Enter college ID of college to be removed")
            collegeId = input()
            colleges.Remove(collegeId)

        elif(option == 4):
            break

        else:
            print("Wrong Option, Please try again")
