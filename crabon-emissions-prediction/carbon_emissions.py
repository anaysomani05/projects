print("MENU")
print("SELECT YOUR CHOICE....")
print("1. SHOW PREDICTED EMISSIONS WITH GRAPH")
print("2. SHOW PREDICTED EMISSIONS WITHOUT GRAPH")

import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dubai@#123",database = "csproject")
mycursor = mydb.cursor()

mycursor.execute("SELECT REGION,YEAR_2020,YEAR_2025,YEAR_2030,YEAR_2035,YEAR_2040,YEAR_2045,YEAR_2050 FROM PRED_EMISSIONS")
myresult = mycursor.fetchall()

REGIONS = []
YEAR_2020 = []
YEAR_2025 = []
YEAR_2030 = []
YEAR_2035 = []
YEAR_2040 = []
YEAR_2045 = []
YEAR_2050 = []

for i in myresult:
     REGIONS.append(i[0])
     YEAR_2020.append(i[1])
     YEAR_2025.append(i[2])
     YEAR_2030.append(i[3])
     YEAR_2035.append(i[4])
     YEAR_2040.append(i[5])
     YEAR_2045.append(i[6])
     YEAR_2050.append(i[7])
        

x = int(input("Enter your choice(1-2): "))

if x==1:
    print("Regions   :- ",REGIONS)
    print("Year 2020 :- ",YEAR_2020)
    print("Year 2025 :- ",YEAR_2025)
    print("Year 2030 :- ",YEAR_2030)
    print("Year 2035 :- ",YEAR_2035)
    print("Year 2040 :- ",YEAR_2040)
    print("Year 2045 :- ",YEAR_2045)
    print("Year 2050 :- ",YEAR_2050)

    X=["AFRICA","ASIA-PACIFIC","CIS","EUROPE","LATIN AMERICA","MIDDLE-EAST","NORTH-AMERICA"]
    X_axis=np.arange(len(X))
    plt.bar(X_axis-0.3,YEAR_2020,0.1,label=2020)
    plt.bar(X_axis-0.2,YEAR_2025,0.1,label=2025)
    plt.bar(X_axis-0.1,YEAR_2030,0.1,label=2030)
    plt.bar(X_axis-0.0,YEAR_2035,0.1,label=2035)
    plt.bar(X_axis+0.1,YEAR_2040,0.1,label=2040)
    plt.bar(X_axis+0.2,YEAR_2045,0.1,label=2045)
    plt.bar(X_axis+0.3,YEAR_2050,0.1,label=2050)

    plt.xticks(X_axis,X)
    plt.xlabel("Regions")
    plt.ylabel("CO2 EMISSIONS (in million metric tons)")
    plt.title("Prediction of CO2 Emissions")
    plt.legend()
    plt.show()

if x==2:
    print("Regions   :- ",REGIONS)
    y = input("Enter a Region: ")
    
    if y == "AFRICA":
         mycursor.execute("select *from pred_emissions where REGION='AFRICA'")
         myresult=mycursor.fetchall()
         for row in myresult:
              print(row)
              
    elif y == "ASIA-PACIFIC":
         mycursor.execute("select *from pred_emissions where REGION='ASIA-PACIFIC'")
         myresult=mycursor.fetchall()
         for row in myresult:
              print(row)
              
    elif y == "CIS":
          mycursor.execute("select *from pred_emissions where REGION='CIS'")
          myresult=mycursor.fetchall()
          for row in myresult:
               print(row)
             
    elif y == "EUROPE":
          mycursor.execute("select *from pred_emissions where REGION='EUROPE'")
          myresult=mycursor.fetchall()
          for row in myresult:
               print(row)

    elif y == "LATIN AMERICA":
          mycursor.execute("select *from pred_emissions where REGION='LATIN AMERICA'")
          myresult=mycursor.fetchall()
          for row in myresult:
               print(row)
               
    elif y == "MIDDLE-EAST":
          mycursor.execute("select *from pred_emissions where REGION='MIDDLE-EAST'")
          myresult=mycursor.fetchall()
          for row in myresult:
               print(row)
               
    elif y == "NORTH-AMERICA":
          mycursor.execute("select *from pred_emissions where REGION='NORTH-AMERICA'")
          myresult=mycursor.fetchall()
          for row in myresult:
               print(row)
                    
    print("** All the values are in 'million metric tons' **")