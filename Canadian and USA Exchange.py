import os
# import sys
import pyodbc
# import requests
import datetime
# import numpy
# import tkinter
import matplotlib.pyplot as plt
import matplotlib.style
import statistics

# SELECT RH.ID, RH.Rate_Date, RH.[Base Currency], RH.ExchangeRate, RH.[Foreign Currency], RH.Snapshot
# FROM [Rate History] AS RH
# WHERE (((RH.[Foreign Currency])="NZD" Or (RH.[Foreign Currency])="USD"));

def retrieve_data(dte, cs , plot_data):
    path_db = os.path.abspath("RBA ExchRatesHistory.accdb")

    print(path_db)

    # Set up Access Connections:
    conn1 = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path_db)
    conn2 = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path_db)
    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()

    # Check date isn't today

    # Working Countries Entries is defined in Access

    # ****************************************************
    # Pulling Reference Data for plotting and Query sqlCMD
    # ****************************************************
    # sqlCRef is short for SQL Country Reference

    sqlCRef = "Select [Foreign Currency], [Colour], [Description] from [Country Ref] where [Description] IS NOT Null;"
    # print ("2nd Qry")
    print (sqlCRef)

    try:
        cursor2.execute(sqlCRef)
    except:
        print ("Error in second cursor")

    # Country set is used in sql
    country_set = " ( "
    #  c is used to build a 2 dim list of country ids and data
    c = []
    try:
        index_of = -1
        for row in cursor2.fetchall():
            plot_data.append(row)
            index_of += 1
            if index_of == 0:
                country_set = country_set + chr(39) + row[0] +chr(39)
                c.append(row[0])
            elif index_of > 0:
                country_set =country_set + chr(44) + chr(39) + row[0] +chr(39)
                c.append(row[0])
        country_set = country_set + " ) "
    except:
        print ("Error in for loop print ***")

    conn2.close

    sqlCMD = "SELECT h.id, h.Rate_Date, h.[Base Currency], h.ExchangeRate, h.[Foreign Currency], h.snapshot "
    sqlCMD = sqlCMD + "    FROM[Rate History] AS h, [Rate History] AS datesfilter "
    sqlCMD = sqlCMD + "where "
    sqlCMD = sqlCMD + "    h.[Foreign Currency] in " + country_set + " and "
    sqlCMD = sqlCMD + "    h.Rate_Date = datesfilter.Rate_Date and "
    sqlCMD = sqlCMD + "    datesfilter.[Foreign Currency]= " + chr(39) + "USD" + chr(39) + " "
    sqlCMD = sqlCMD + "Order By h.Rate_Date "

    print (sqlCMD)
    cursor1.execute(sqlCMD)

    # cs is the start of the 2 dimensional data array
    # cs = []
    for e in c:
        # print(e)
        s = []
        s.append(e)
        s.append([])
        cs.append(s)

    try:
        # step = -1
        for row in cursor1.fetchall():
            # print (row)

            if row[4] == cs[0][0]:
                dte.append(datetime.date.fromisoformat(row[1]))
                cs[0][1].append(float(row[3]))
            else:
                for index_step in range(1,len(cs)):
                    if row[4] == cs[index_step][0]:
                        cs[index_step][1].append(float(row[3]))

    except:
        print ("Function " + chr(34) + "retrieve_data " + chr(34) + ", cursor fetchall FAILED.")

    conn1.close()

    return (dte, cs, plot_data)

def pnt_i(i):
    print (i)
    i += 1
    return(i)

def plot_data_fn(dte,cs, plot_data):
    # The next line must preceed the plt.plot() command.
    fig, ax = plt.subplots()

    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # blue, green, red, cyan, magenta, yellow, black
    # Data
    # plt.style.use("seaborn-v0_8")
    plt.style.use ("fast")

    eur = []
    for _ in cs[0]:
                # print(_, "\n")
        eur.append(_)

    # For Fill Between.... separating out USD
    usd = []
    for _ in cs[3]:
                # print(_, "\n")
        usd.append(_)

    usd_median = statistics.median(usd[1])

    print(usd_median)
    # print("^^ ", usd_min)
    try:
        for i in range(len(plot_data)):

            # print (plot_data[i][0]," Colour of ",plot_data[i][1], "Description of ", plot_data[i][2])

            # 14/7/2023
            #  0 'EUR'
            #  1 'GBP'
            #  2 'NZD'
            #  3 'USD'
            if i > 0 and i < 3:
                plt.plot(dte, cs[i][1], color=plot_data[i][1], label=plot_data[i][2])
            else:
                if i < 1:
                    plt.plot(dte, eur[1], color=plot_data[i][1], label=plot_data[i][2] )
                else:
                    plt.plot(dte, usd[1], color=plot_data[i][1], label=plot_data[i][2] )
    except:
        print ("Error sizing plot_data")

    plt.title("1 Australian $ buys (Exchange Rates)")

    plt.grid(True)
    plt.legend()

    plt.xlabel("Dates")
    # Orientation of labels on dte array (x axis)
    fig.autofmt_xdate()
    plt.ylabel("Exchange Rate")
    # usd = cs[3]

    plt.fill_between(dte, usd[1], eur[1],
                     # alpha = 0.25, label='USD > EUR')
                     # where=(usd[1] > eur[1]),
                     # interpolate = True,
                     alpha = 0.25
                      )

    plt.tight_layout()
    plt.show()

    return
 
# Main body...
# print(__name__)
if __name__ == '__main__' :

    # Initialising arrays for plotting
    dte = []
    cs = []
    plot_data = []
    country_no = 2

    # From Database
    # print ("Hello")
    retrieve_data(dte, cs , plot_data)

    try:
        plot_data_fn(dte, cs, plot_data)

    except:
        print("Plotting Error")

