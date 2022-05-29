
import pandas as pd
import statistics as st

df = pd.read_csv("StudentsPerformance.csv")

data = df["reading score"].tolist()

mean = st.mean(data)
mode = st.mode(data)
median = st.median(data)
stdev = st.stdev(data)

print("Mean is " , mean)
print("Mode is " , mode)
print("Median is " , median)
print("Stdev is ", stdev)

StdevStart1,StdevEnd1 = (mean - stdev) , (mean + stdev)
StdevStart2,StdevEnd2 = (mean - 2*(stdev)) , (mean + 2*(stdev))
StdevStart3,StdevEnd3 = (mean - 3*(stdev)) , (mean + 3*(stdev))

ListOfStdev1 = [i for i in data if i > StdevStart1 and i < StdevEnd1]
ListOfStdev2 = [i for i in data if i > StdevStart2 and i < StdevEnd2]
ListOfStdev3 = [i for i in data if i > StdevStart3 and i < StdevEnd3]

Total = len(data)

x = len(ListOfStdev1)
y = x*100/Total

x2 = len(ListOfStdev2)
y2 = x2*100/Total

x3 = len(ListOfStdev3)
y3 = x3*100/Total



print(y , "%" , "Data Lies within First Stdev")
print(y2 , "%" , "Data Lies within Second Stdev")
print(y3 , "%" , "Data Lies within Third Stdev")