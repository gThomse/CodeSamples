import sqlite3
from vid_data import Video

db = "YouTube py lite.db"
tblVids = "[Python videos]"
tblKeyWords = "keywords"
tblSkip = "[skip tbl]"

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(db)
c = conn.cursor()
#
# c.execute("Delete from tablename".replace("tablename", tblVids))
#
# c.execute("DROP TABLE tablename".replace("tablename", tblVids))
# c.execute("""CREATE TABLE tablename (
#             playlist text,
#             owner text,
#             title text,
#             playlist_lnk text,
#             owner_lnk text,
#             title_lnk text
#             )""".replace("tablename", tblVids))

tblVids_idx = tblVids.replace("[","").replace("]","_idx01").replace(" ","_")
print ("drop index " + tblVids_idx + ";")
c.execute ("drop index " + tblVids_idx + ";")
conn.commit()

sql_index = "CREATE INDEX tablename_idx01 ON tablename (fieldname01);".replace("tablename_idx01",tblVids_idx).replace("fieldname01","title").replace("tablename",tblVids)
print(sql_index)
c.execute(sql_index)
conn.commit()

#
# c.execute("DROP TABLE tablename".replace("tablename", tblKeyWords))
# c.execute("""CREATE TABLE tablename  (
#             title text,
#             key_word text
#             )""".replace("tablename", tblKeyWords))


str_idx = "SELECT name FROM sqlite_master WHERE type == 'index' AND tbl_name == 'table_name';".replace("table_name",tblKeyWords)
c.execute(str_idx)
row = c.fetchone()
while row is not None:
    c.execute ("drop index " + row[0] +";")
    row = c.fetchone()

conn.commit()

sql_index = "CREATE INDEX tablename_idx01 ON tablename (fieldname01);".replace("tablename",tblKeyWords).replace("fieldname01","title")
print(sql_index)
c.execute(sql_index)

sql_index = "CREATE INDEX tablename_idx02 ON tablename (fieldname02);".replace("tablename",tblKeyWords).replace("fieldname02","key_word")
print(sql_index)
c.execute(sql_index)

#
# c.execute("DROP TABLE tablename".replace("tablename", tblSkip))
# c.execute("CREATE TABLE tablename (key_word text)".replace("tablename", tblSkip))
#
# # c.execute("INSERT INTO employees VALUES (:keyword)", {'keyword': emp.first})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "how"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "to"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "use"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "them"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "and"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "the"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "you"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "python"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "for"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "a"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "an"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "with"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "get"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "in"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "are"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "tutorial"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "1"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "2"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "3"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "4"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "5"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "6"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "7"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "8"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "9"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "10"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "11"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "12"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "13"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "14"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "15"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "16"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "17"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "18"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "19"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "20"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "2019"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "2020"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "2021"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "2022"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "2023"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "beginners"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "beginner"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "about"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "again"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "basic"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "basics"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "by"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "but"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "can"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "code"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "become"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "better"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "best"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "across"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "along"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "alert"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "benefits"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "do"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "five"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "easy"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "free"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "full"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "had"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "great"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "have"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "here"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "I "})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "is"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "late"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "more"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "most"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "not"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "of"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "old"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "on"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "or"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "our"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "p"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "s"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "tip"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "tips"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "too"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "top"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "two"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "three"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "one"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "using"})
# c.execute("INSERT INTO tablename VALUES (:key_word)".replace("tablename", tblSkip), {'key_word': "vs"})
#
conn.commit()

# Next 2 lines were used for testing.
# c.execute("INSERT INTO [Python videos] (PlayList, Owner, Title, title_lnk, playlist_lnk, owner_lnk)  values ('Python', 'Internet Made Coder', '3 PYTHON AUTOMATION PROJECTS FOR BEGINNERS', 'https://youtu.be/vEQ8CXFWLZU', 'https://www.youtube.com/playlist?list=PLbVn4f96VrAolUpkBwmfy-J7dCHE8iQH5', 'https://www.youtube.com/@InternetMadeCoder');")
# conn.commit()
conn.close()