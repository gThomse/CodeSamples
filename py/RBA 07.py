'''

Author : Shaun Thomsen
Date   : 20200501

Observation :   Snapshot needs to be run at the same time every day.
                RBA changes the file on the web around 5pm
                This means if you run the file at 6 pm one day and before 5 pm the next you will
                get duplicates, and if the nxt day its run later than 5 pm, you might manage to miss a day.. of data.

                This was fun to write..
'''

import os
import sys
import pyodbc
import requests
import datetime
from xml.etree import ElementTree as ET

class Error (Exception):
    pass

class BoundaryException(Error):
    pass

def line_no(no):
    local_no = no
    print(f'line no is {local_no}')
    local_no += 1
    return(local_no)

def main(file_text_as_string, cursor_sub,l_date, rate_hist):
    myroot = ET.fromstring(file_text_as_string)

    dateEx =  myroot[2][3].text
    dateEx_l = dateEx.split('T')
    # valC  = myroot[2][6][3][1][1].text
    # baseC = myroot[2][6][3][2].text
    # targetC = myroot[2][6][3][3].text
    # print (f'Contents of the first row {dateEx_l[0]}, {baseC}, {valC}, {targetC}')

    # print (dateEx_l[0], rate_hist)
    if dateEx_l[0] not in rate_hist:
        print('Processing new data file... ')
        for i in range(2,40):
            try:
                # print (i, myroot[i].tag)
                dateEx = myroot[i][3].text
                dateEx_l = dateEx.split('T')  # List with Date and time
                valC = myroot[i][6][3][1][1].text  # Exchange rate
                baseC = myroot[i][6][3][2].text  # Our Country Abbreviation
                targetC = myroot[i][6][3][3].text  # Target Country Abbreviation

                # print(f'On the {dateEx_l[0]}: $1 {baseC}  = {valC} {targetC}')
                strUpdate = "INSERT INTO [Rate History] ( Rate_Date, [Base Currency], ExchangeRate, [Foreign Currency],Snapshot) "
                strUpdate = strUpdate + " SELECT '" + dateEx_l[0] + "' AS Expr1, '" + baseC
                strUpdate = strUpdate + "' AS Expr2, " + valC + " AS Expr3, '" + targetC + "' AS Expr4, "
                strUpdate = strUpdate + "'" + l_date + "';"
                # print(strUpdate)
                cursor_sub.execute(strUpdate)
                conn.commit()
            except:
                print ('.', end='')
    else:
        print (f'{rate_hist[0]} data already loaded :)')

# Main body...
if __name__ == '__main__' :

    # Confirm database before proceeding
    try:
        # Return absolute path for file :
        path_db = os.path.abspath("RBA ExchRatesHistory.accdb")
        print(path_db)
        # print(path_db)

        # Inital path check..
        # print(path_db)
        # Set up Access Connection:
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + path_db)
        cursor = conn.cursor()

        # Date check.. :)
        strMaxDate = "SELECT Max(CDate([Rate_Date])) FROM [Rate History];"
        cursor.execute(strMaxDate)
        # print(strMaxDate)

        rate_hist = []
        # Retrieve last 'Max Rate Date' from DB
        for row in cursor.fetchall():
            rate_hist.append(str(row[0]).split(' ')[0])
            print(f'Last maximum access date : {rate_hist[0]} ')
        l_date = str(datetime.datetime.now()).split(' ')[0]

        try:
            # New date so new data should be available...
            # Then look for the RBA rate XML file...
            # file_name = 'rss-cb-exchange-rates.xml'  # This line used when testing was local. .. :)
            url_file_name = 'https://www.rba.gov.au/rss/rss-cb-exchange-rates.xml'
            print (f'Retrieving source {url_file_name}')
            page = requests.get(url_file_name)
            # print (page.text)
            main(page.text,cursor,l_date, rate_hist)
        except:
            print ('Issues detected retrieving the file... \nPlease check the link\n{url_file_name}\n\nHave a nice day')
    except:
        print('Main try failed.')

    conn.close()