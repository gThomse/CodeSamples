import sqlite3
from vid_data import Video

db = "YouTube py lite.db"
tbl_skip_keys = "[skip tbl]"
tblVids = "[Python videos]"
tblKeyWords = "keywords"

# SQL Lite DB connection
# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(db)
c = conn.cursor()

# Query to a list
skip_words = []

#  All good code commented out below KEEP

# str_fetch = "select key_word from TableName; ".replace("TableName", tbl_skip_keys)
# c.execute(str_fetch)
# print(str_fetch)
#
# row = c.fetchone()
# print("***********   Skip    ****************")
# while row is not None:
#     for _ in row:
#         skip_words.append(_)
#         # print(_)
#     row = c.fetchone()
#
# print(skip_words)
#
# print("*********** Keywords ****************")

str_fetch2 = "select distinct key_word from TableName order by key_word ; ".replace("TableName", tblKeyWords)
c.execute(str_fetch2)

row = c.fetchone()
line = 0
while row is not None:
    line += 1
    # for _ in row:
    #     print ("{:140}, ".format(_))
    # print("")
    if line >= 14:
        print("{} ".format(row[0]))
        line = 0
    else:
        print("{}{} ".format(row[0], ","), end="")

    # print(row)
    row = c.fetchone()
#
# print("***********  Videos  ****************")
#
# # str_fetch3 = "select playlist, owner, title, playlist_lnk, owner_lnk, title_lnk from TableName;" \
# str_fetch3 = "select * from TableName;" \
#         .replace("TableName", tblVids)
# c.execute(str_fetch3)
#
# row = c.fetchone()
# while row is not None:
#     # for _ in row:
#     #     skip_words.append(_)
#     # print(row)
#     print ("{:100} {:80}\n{:100} {:80}\n{:100} {:80}\n\n".format(row[2] + " :", row[5] + " :",row[0] + " :", row[3], row[1], row[4]))
#     row = c.fetchone()
#

searchfor = input("\n\nEnter search keyword: ")
print("\n")

try:
    str_fetch4 = "select * from T1 INNER JOIN T2 on T1.title = T2.title where T2.key_word = '"\
        .replace("T2", tblKeyWords).replace("T1", tblVids)
    str_fetch4 = str_fetch4 + searchfor.lower() + "' ;"
    # print("\n", str_fetch4)
    c.execute(str_fetch4)

    row = c.fetchone()
    while row is not None:
        # print(row)
        print ("{:100} {:80}\n{:100} {:80}\n{:100} {:80}\n\n".format(row[2] + " :", row[5] + " :",row[0] + " :", row[3], row[1], row[4]))
        row = c.fetchone()

except:
    print("Try again, your entry of '{}' wasn't valid or found".format(searchfor))

