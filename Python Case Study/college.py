import pandas as pd

class College:

    def __init__(self, collegeDf):
        self.collegeDf = collegeDf

    def registerNew(self, collegeId, collegeName, courseType, city, fees, pinCode):
        self.collegeDf.loc[len(self.collegeDf.index)] = [collegeId, collegeName, courseType, city, fees, pinCode]
        self.collegeDf.to_csv('colleges.csv', encoding='utf-8', index=False)

    def Display(self, courseType, city):
        rslt_df = self.collegeDf[self.collegeDf['courseType'] == str(courseType)]
        rslt_df1 = rslt_df[rslt_df['city'] == str(city)]
        print(rslt_df1)

    def Remove(self, collegeId):
        self.collegeDf.drop(self.collegeDf[self.collegeDf["collegeId"] == int(collegeId)].index, inplace = True)
        self.collegeDf.to_csv('colleges.csv', encoding='utf-8', index=False)
