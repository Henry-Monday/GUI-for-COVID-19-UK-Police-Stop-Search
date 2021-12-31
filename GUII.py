from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
import json
import datetime as dt
import requests
import seaborn as sb
from tkinter.ttk import Combobox


root = Tk()
root.title("GUI FOR COVID_19 & POLICE S&S")
root.geometry("1200x700")
root.iconbitmap("pandc.ico")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 10, column = 2, columnspan = 3, padx = 15, pady = 15)

box_value = StringVar()
LocationBox = Combobox(root, textvariable=box_value)
LocationBox['values'] = ("avon-and-somerset", "bedfordshire", "btp", "cambridgeshire", "city-of-london", "cheshire", "cleveland",\
    "cumbria", "derbyshire", "devon-and-cornwall", "dorset", "durham", "dyfed-powys", "essex", "greater-manchester", "gwent", "gloucestershire", \
    "hampshire", "hertfordshire", "humberside", "kent", "lancashire", "leicestershire", "lincolnshire", "merseyside", "metropolitan", "norfolk", "northamptonshire",\
    "northumbria", "north-wales", "north-yorkshire", "nottinghamshire", "south-wales", "south-yorkshire", "staffordshire", "suffolk", "surrey", "sussex", "thames-valley",\
    "warwickshire", "west-mercia", "west-midlands", "west-yorkshire", "wiltshire")
LocationBox.current(2)
LocationBox["state"] = "readonly"
LocationBox.grid(row = 14, column = 4)
#this_value = locationBox.get()
this_value = LocationBox.get()




year_value = StringVar()
YearBox = Combobox(root, textvariable=year_value)
YearBox['values'] = ("2019", "2020", "2021")
YearBox.current(2)
YearBox["state"] = "readonly"
YearBox.grid(row = 14, column = 6)
#y_value = locationBox.get()
y_value = YearBox.get()



month_value = StringVar()
MonthBox = Combobox(root, textvariable=month_value)
MonthBox['values'] = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
MonthBox.current(2)
MonthBox["state"] = "readonly"
MonthBox.grid(row = 14, column = 8)
#m_value = locationBox.get()
m_value = MonthBox.get()




my_Img = ImageTk.PhotoImage(Image.open("TEESSIDE_LOGO.png"))
my_label = Label(image = my_Img)
my_label.grid(row = 5, column = 1)

Info_Query = Label(root, text = "COVID-19 & Police Stop and Search Information Enquiry",padx = 10, pady = 8)
Info_Query.grid(row = 0, column = 1)

COVID_19 = Label(root, text = "COVID-19 Section",padx = 10, pady = 8)
COVID_19.grid(row = 4, column = 0)

STOPS_AND_SEARCHS = Label(root, text = "STOP & SEARCH Section",padx = 10, pady = 8)
STOPS_AND_SEARCHS.grid(row = 4, column = 3)

def covid_19():
    df = pd.read_csv("covid.csv", parse_dates = ["date"])
    # New Columns Classing Different Age Range BySpecimenDate

    df["Infants"] = df["newCasesBySpecimenDate-0_4"] + df["newCasesBySpecimenDate-5_9"]
    df["Teens"] = df["newCasesBySpecimenDate-10_14"] + df["newCasesBySpecimenDate-15_19"] 
    df["Youths"] = df["newCasesBySpecimenDate-20_24"] + df["newCasesBySpecimenDate-25_29"] + df["newCasesBySpecimenDate-30_34"] + df["newCasesBySpecimenDate-35_39"] + df["newCasesBySpecimenDate-40_44"]
    df["Middle_Aged"] = df["newCasesBySpecimenDate-45_49"] + df["newCasesBySpecimenDate-50_54"] + df["newCasesBySpecimenDate-55_59"]
    df["Oldies"] = df["newCasesBySpecimenDate-60_64"] + df["newCasesBySpecimenDate-65_69"] + df["newCasesBySpecimenDate-70_74"] + df["newCasesBySpecimenDate-75_79"] + df["newCasesBySpecimenDate-80_84"] + df["newCasesBySpecimenDate-85_89"] + df["newCasesBySpecimenDate-90+"] 


    # New Columns Classing Different Age Range BySpecimenDateRollingRate

    df["Infants_RR"] = df["newCasesBySpecimenDateRollingRate-0_4"] + df["newCasesBySpecimenDateRollingRate-5_9"]
    df["Teens_RR"] = df["newCasesBySpecimenDateRollingRate-10_14"] + df["newCasesBySpecimenDateRollingRate-15_19"] 
    df["Youths_RR"] = df["newCasesBySpecimenDateRollingRate-20_24"] + df["newCasesBySpecimenDateRollingRate-25_29"] + df["newCasesBySpecimenDateRollingRate-30_34"] + df["newCasesBySpecimenDateRollingRate-35_39"] + df["newCasesBySpecimenDateRollingRate-40_44"]
    df["Middle_Aged_RR"] = df["newCasesBySpecimenDateRollingRate-45_49"] + df["newCasesBySpecimenDateRollingRate-50_54"] + df["newCasesBySpecimenDateRollingRate-55_59"]
    df["Oldies_RR"] = df["newCasesBySpecimenDateRollingRate-60_64"] + df["newCasesBySpecimenDateRollingRate-65_69"] + df["newCasesBySpecimenDateRollingRate-70_74"] + df["newCasesBySpecimenDateRollingRate-75_79"] + df["newCasesBySpecimenDateRollingRate-80_84"] + df["newCasesBySpecimenDateRollingRate-85_89"] + df["newCasesBySpecimenDateRollingRate-90+"] 


    # New Columns Classing Different Age Range BySpecimenDateRollingSum

    df["Infants_RS"] = df["newCasesBySpecimenDateRollingSum-0_4"] + df["newCasesBySpecimenDateRollingSum-5_9"]
    df["Teens_RS"] = df["newCasesBySpecimenDateRollingSum-10_14"] + df["newCasesBySpecimenDateRollingSum-15_19"] 
    df["Youths_RS"] = df["newCasesBySpecimenDateRollingSum-20_24"] + df["newCasesBySpecimenDateRollingSum-25_29"] + df["newCasesBySpecimenDateRollingSum-30_34"] + df["newCasesBySpecimenDateRollingSum-35_39"] + df["newCasesBySpecimenDateRollingSum-40_44"]
    df["Middle_Aged_RS"] = df["newCasesBySpecimenDateRollingSum-45_49"] + df["newCasesBySpecimenDateRollingSum-50_54"] + df["newCasesBySpecimenDateRollingSum-55_59"]
    df["Oldies_RS"] = df["newCasesBySpecimenDateRollingSum-60_64"] + df["newCasesBySpecimenDateRollingSum-65_69"] + df["newCasesBySpecimenDateRollingSum-70_74"] + df["newCasesBySpecimenDateRollingSum-75_79"] + df["newCasesBySpecimenDateRollingSum-80_84"] + df["newCasesBySpecimenDateRollingSum-85_89"] + df["newCasesBySpecimenDateRollingSum-90+"] 


    # Total Number of Cases in each class per day across all AgeRange

    df["Total_Cases"] = df["Infants"] + df["Teens"] + df["Youths"] + df["Middle_Aged"] + df["Oldies"]
    df["Total_Cases_RR"] = df["Infants_RR"] + df["Teens_RR"] + df["Youths_RR"] + df["Middle_Aged_RR"] + df["Oldies_RR"] 
    df["Total_Cases_RS"] = df["Infants_RS"] + df["Teens_RS"] + df["Youths_RS"] + df["Middle_Aged_RS"] + df["Oldies_RS"]

    # Break the Date Column into Weeks & Months

    df["Week"] = df["date"].dt.isocalendar().week

    df["Month"] = df["date"].dt.month_name()

    # Drop All Other Columns After Classification

    df_covid = df[["areaType","areaCode","areaName","date","Week","Month","Infants","Teens","Youths","Middle_Aged","Oldies","Infants_RR","Teens_RR","Youths_RR","Middle_Aged_RR","Oldies_RR",\
                "Infants_RS","Teens_RS","Youths_RS","Middle_Aged_RS","Oldies_RS", "Total_Cases","Total_Cases_RR","Total_Cases_RS"]]


    df_covid.sort_values(by = "date", ascending = True, inplace = True)

    
    df_covid.plot(kind = "line", x = "Month", y = "Total_Cases", title = "Total Monthly Cases")
    df_covid.plot(kind = "line", x = "Week", y = "Total_Cases", title = "Total Weekly Cases")
    df_covid.plot(kind = "line", x = "date", y = "Total_Cases", title = "Total Daily Cases")
    df_covid.plot(kind = "line", x = "areaName", y = "Total_Cases", title = "Total Cases By Area-Name")
    df_covid.plot(kind = "line", x = "areaType", y = "Total_Cases", title = "Total Cases By Area-Type")
    
    # # sb.barplot(x = "Month", y = "Total_Cases", hue="areaType", data=df_covid)
    # # sb.barplot(x = "Week", y = "Total_Cases", hue="areaType", data=df_covid)
    # # sb.barplot(x = "date", y = "Total_Cases", hue="areaType", data=df_covid)
    # sb.barplot(x = "areaType", y = "Total_Cases", data=df_covid)

    
    
    # sb.barplot(x="areaName", y="Total_Cases", data=df_covid)
    plt.show()


covid = Button(root, text = "COVID-19", fg = "green", bg = "black", pady = 10, padx = 10, command = covid_19)
covid.grid(row = 8, column = 0)




def stop_and_search(value, year, month):
    print("value - " + value, "year -" + year, "month -" + month)
    df = pd.read_json("https://data.police.uk/api/stops-force?force="+value+"&date="+year+"-"+month)
    df.sort_values(by = "datetime", ascending = True, inplace = True)
    print(df["age_range"])
    
    Total_Stop_and_Search = str(len(df["involved_person"]))+ " persons were stopped and searched by the "+this_value+" Police in the period "+m_value+"-"+y_value
    
    # output = print(cleveland_SS, \
    #     "persons were stopped and searched by the Cleveland Police in  July 2020.")
    
    # display.insert(END, Total_Stop_and_Search)
    # display.delete(END, Total_Stop_and_Search)



    df["age_range"].value_counts().plot(kind = "bar", title = "Age Range Stopped and Searched in "+value.upper())
    plt.show()
    #my_Label = Label(root, text = display.get()).pack()
    
    #return total
    #total = total.get()
    #display.insert("1.0",total)
    # cleveland_AR = df["age_range"].unique()
    # return ("Cleveland Police department in the month of July", \
    #     "stopped and searched persons in the following age range", cleveland_AR)

# LocationBox.bind("<<ComboboxSelected>>", stop_and_search)
# YearBox.bind("<<ComboboxSelected>>", stop_and_search)
# MonthBox.bind("<<ComboboxSelected>>", stop_and_search)

  
#output_text = StringVar() 
# lbl_output = Label(root, text = output_text).grid()


stop_search = Button(root, text = "Stop and Search", fg = "green", bg = "black", pady = 10, padx = 10, command = lambda: stop_and_search(this_value, y_value, m_value))
stop_search.grid(row = 8, column = 3)


# result = StringVar()
display = Text(root, height = 2, width = 40)
display.grid(row = 11, column = 3, columnspan = 2)




quit = Button(root, text = "QUIT", fg = "green", bg = "black", pady = 10, padx = 10, command = root.quit)
quit.grid(row = 14, column = 3)

root.mainloop()