import sqlite3
from vid_data import Video

import itertools
import os
import re
import pickle
import pyodbc
# from numba import njit
import CheckChannel as check

# Google's Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import csv

#  If Debuging set this boolean to True
# PLV_Debug = True
PLV_Debug = False

PLV_Debug_Count = 10
# PLV_Debug = False
output_file = 'python videos.csv'
db_videos = "YouTube python.accdb"
db_video_lite = "YouTube py lite.db"
tbl_vidoes = "[python videos]"
tblKeyWords = "keywords"
tblSkip = "[skip tbl]"

# future improvement.. This list should be table driven.


PL_Exclude = \
    [
        'Comedy', 'Microsoft Power Automate', 'Music playlist 1', 'Music playlist 2', 'Old Movies',
        'Old movies', 'PL/SQL', 'Python', 'Stilh', 'Tableau', 'XL', 'YouTube', 'Cartoons'
    ]

PL_Include = ['Python','Git','Sublime Text', 'JavaScript', 'HTML CSS', 'Visual Studio']

# Replaced List with Dictionaey to implement filtering of duplicates with Lists.
# When vid_records works, vid_ids can be deleted, or keep it if I ever want to clean up the duplicates on YouTube.

# vid_ids = []
vid_records = {}


def mergedict(dict1, dict2):
    return dict2.update(dict1)


def print_error(playlist, playlink, title, titlelink, owner, ownerlink):
    print("Playlist  {}".format(playlist))
    print("PlayLink  {}".format(playlink))
    print("Title     {}".format(title))
    print("TitleLink {}".format(titlelink))
    print("Owner     {}".format(owner))
    print("OwnerLink {}".format(ownerlink))


def alpha_numeric_chars_only(string):
    return re.sub('[^0-9a-zA-Z]+', ' ', string).strip("  ")


def extended_ascii(string):
    return re.sub(r'[^\x00-\x7f]', r'', string).strip()


# def checkchannel(channellnk):
#     if channellnk == "https://www.youtube.com/@Выпечкаикулинария.":
#         return "https://www.youtube.com/@user-rw7sk1li6q"
#
#     if channellnk == "https://www.youtube.com/@КулинаримсТаней2.0":
#         return "https://www.youtube.com/@tanja.kulinarim"
#
#     if channellnk == "https://www.youtube.com/@КулинаримсТаней":
#         return "https://www.youtube.com/@kulinarimstanej"
#
#     if channellnk == "https://www.youtube.com/@Cookingtree쿠킹트리":
#         return "https://www.youtube.com/@Cooking_tree"
#
#     if channellnk == "https://www.youtube.com/@ChocolateCacaoチョコレートカカオ":
#         return "https://www.youtube.com/@chocolate_cacao"
#
#     if channellnk == "https://www.youtube.com/@Calorierestaurant칼로리식당":
#         return "https://www.youtube.com/@Calorierestaurant"
#
#     if channellnk == "https://www.youtube.com/@꿀키honeykki":
#         return "https://www.youtube.com/@honeykkicook"
#
#     if channellnk == "https://www.youtube.com/@ChezSucre砂糖の家":
#         return "https://www.youtube.com/watch?v=RYjjLD13RYE"
#
#     if channellnk == "https://www.youtube.com/@조꽁드Jocondesbaking":
#         return "https://www.youtube.com/watch?v=2tq2diJFBm0"
#
#     if channellnk == "https://www.youtube.com/@ТортыиКулинарияCakes&Cooking":
#         return "https://www.youtube.com/@cakescooking"
#
#     if channellnk == "https://www.youtube.com/@식탁일기tablediary":
#         return "https://www.youtube.com/@table_diary"
#
#     if channellnk == "https://www.youtube.com/@BooneBake분베이크":
#         return "https://www.youtube.com/@BooneBake"
#
#     if channellnk == "https://www.youtube.com/@꾸움Kkuume":
#         return "https://www.youtube.com/@Kkuume"
#
#     if channellnk == "https://www.youtube.com/@DerrickSherrill":
#         return "https://www.youtube.com/@derricksherrill3511"
#
#     return channellnk

# @njit (nopython = True)
def playlist_videos(youtube, playlst_str, playlist_id):
    # Working Variable
    set_size = 0
    l_repdict = {}
    # Running total
    c_repdict = {}

    # videos = []
    print("Playlist '{}'".format(playlst_str), end="")

    nextPageToken = None

    n = itertools.count()

    while True:
        request = youtube.playlistItems().list(
            part="contentDetails, snippet",
            # playlistId="PLbVn4f96VrAr3HgyVe1MJtRbYrcq8xlb5",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=nextPageToken
        )

        response = request.execute()

        # print(response)

        lnkPL = "https://www.youtube.com/playlist?list="
        lnk = "https://youtu.be/"

        for item in response['items']:

            # Replaced List with Dictionaey to implement filtering of duplicates with Lists.
            next(n)
            # Dict code

            #  ADD This ***************** Try
            try:
                #  *********** 24/5/2023  12:23
                # video_owner = item['snippet']['videoOwnerChannelTitle']
                video_owner = alpha_numeric_chars_only(extended_ascii(item['snippet']['videoOwnerChannelTitle']))
                video_owner = video_owner if len(video_owner.strip()) > 3 else "Have to Lookup "
            except:
                video_owner = "Look up manually"
                pass

            try:
                channellnk = "https://www.youtube.com/@" + video_owner.replace(" ", "").replace("'", "")
                channellnk = check.channel(channellnk)
            except:
                channellnk = ""
                pass

            l_repdict = {
                playlst_str + "  " + item['snippet']['title']:
                    {
                        "Play List": playlst_str,
                        "Play Link": lnkPL + playlist_id,
                        "Vid Owner": video_owner,
                        "Vid Title": alpha_numeric_chars_only(extended_ascii(item['snippet']['title'])),
                        "Vid Link": lnk + item['contentDetails']['videoId'],
                        "Owner Channel": channellnk
                    }
            }
            # print(video_owner)
            mergedict(l_repdict, c_repdict)

        nextPageToken = response.get('nextPageToken')

        if not nextPageToken:
            if PLV_Debug is True:
                print(" had {} vidoes".format(next(n)))

            # This is where the the data is returned to the calling function.
            mergedict(c_repdict, vid_records)
            break
    set_size = next(n)
    # print(" had {} vidoes".format(set_size))
    return(set_size)

def main():
    path_db = os.getcwd().replace("AppData\Roaming\JetBrains\PyCharmCE2023.1\scratches",
                                  "Documents\code\YouTube Code\py\playlist")
    os.chdir(path_db)
    try:


        # Return absolute path for file:
        path_db = os.path.abspath(db_video_lite)
        print(path_db)

        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()

        run_delete = "DELETE FROM TableName;".replace("TableName", tbl_vidoes)
        cursor.execute(run_delete)
        #  In sqlite ommits are made on the CONN and not the cursor
        conn.commit()

        run_delete = "DELETE FROM TableName;".replace("TableName", tblKeyWords)

        cursor.execute(run_delete)
        conn.commit()

    except:
        print("Connection not made to {}\n Please check if the file exists before proceeding\n\nThen check syntax of code".format(path_db))
        quit()

        # **** Finished Setting Up Database Connection ****

    #  **** Setting up Youtube Credentials ****

    credentials = None

    if PLV_Debug is True:
        print("\n    *** ******** ***\n\n    To do:  ")
        print("    Msg of objective")
        print("\n    *** ******** ***\n")

    # token.pickle stores the user's credentials
    if os.path.exists('token.pickle'):
        print('Loading Credentials From File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            try:
                credentials.refresh(Request())
            except:
                print("Token_Exception: Have to delete 'Token Pickle' File")
                if os.path.exists('token.pickle'):
                    os.remove('token.pickle')
                    print("File deleted, try again")
                quit()
        else:
            try:
                print('Fetching New Tokens...')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json',
                    scopes=[
                        'https://www.googleapis.com/auth/youtube.readonly'
                    ]
                )

                flow.run_local_server(port=8080, prompt='consent',
                                      authorization_prompt_message='')
                credentials = flow.credentials
            except:
                print("Refresh Client Secret file")
                print(
                    "https://console.cloud.google.com/apis/credentials?project=yt-play-lists&supportedpurview=project")
                quit()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)

    youtube_cred = build("youtube", "v3", credentials=credentials)

    # **** Finished Setting Up Database Connection ****
    # **** Finding all Playlists

    nextPageToken = None

    # A mutable list
    my_playlist = []

    # **** Reading Play Lisys ****

    while True:
        # **** Retrieving Play Lists Names ****

        request = youtube_cred.playlists().list(
            part="contentDetails,snippet",
            mine=True,
            maxResults=50,
            pageToken=nextPageToken
        )

        response = request.execute()

        # id = ""
        # title = ""

        for item in response['items']:
            id = item['id']
            title = item['snippet']['title']
            # print("{:30} - link is 'https://www.youtube.com/playlist?list={}".format(title,id, id))
            if title in PL_Include:
                my_playlist.append(
                    {
                        'id': id,
                        'title': title
                    }
                )

        nextPageToken = response.get('nextPageToken')

        if not nextPageToken:
            print(
                "Playlist names extracted\n***************************************************************************************************************\n")
            break

    # **** Finished Retrieving Play Lists Names ****
    # **** Results stored in my_playlist list [] ****

    # Found all Playlist
    # **** Now looping playlists to retrieve video data

    #  First Sort playlists by Title Name
    my_playlist.sort(key=lambda ele: ele['title'])

    c = 0

    for j in my_playlist:
        c += 1
        tle = j['title']

        # **** Building a Dictionary of Videos from each Playlist
        _ = playlist_videos(youtube_cred, tle, j['id'])
        print(" {}, Adjusted Dictionary size = {}".format(_ , len(vid_records)))

        # **** Exception Code for Debug purposes - Ignore if working
        if PLV_Debug is True:
            if c >= PLV_Debug_Count:
                break

    # Finished Looping
    # Built Vid_ids

    # **** Finished looping playlists to retrieve video data

    # Output
    # First to CSV
    # Second to an Access Database

    # CSV Code  to output_file
    field_names = ['PlayList', 'Owner', 'Title', 'Video Link', 'Playlist Link', 'Owner Link']

    if PLV_Debug is True:
        for i in vid_records:
            print(vid_records[i]['Play List'], " ", vid_records[i]['Vid Owner'], " ", vid_records[i]['Vid Title'], " ",
                  vid_records[i]['Vid Link'], " ", vid_records[i]['Play Link'], " ", vid_records[i]['Owner Channel'])

    t_vidoes = itertools.count()
    t_errors = itertools.count()
    t_playlist = itertools.count()

    # Load SkipKeys

    skip_words = []
    str_fetch = "select key_word from TableName;".replace("TableName", tblSkip)
    cursor.execute(str_fetch)

    row = cursor.fetchone()
    while row is not None:
        for _ in row:
            skip_words.append(_)
            # print(_)
        row = cursor.fetchone()

    # OUTPUT
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        print("\nError titles were:\n")

        for i in vid_records:
            playlist = vid_records[i]['Play List']
            vid_owner = vid_records[i]['Vid Owner']
            playlnk = vid_records[i]['Play Link']
            vid_title = vid_records[i]['Vid Title']
            vid_link = vid_records[i]['Vid Link']
            owner_channel = vid_records[i]['Owner Channel']

            next(t_playlist)
            for key_word in vid_title.split(" "):
                if key_word.lower().strip() not in skip_words:

                    str_update = "INSERT INTO [TableName] (title, key_word) ".replace("TableName", tblKeyWords)
                    str_update = str_update + " values ('" + vid_title + "', '" + key_word.lower() + "');"

                    cursor.execute(str_update)
                    conn.commit()

            try:
                #  Skip is TRUE
                #  Don't skip , report is FALSE
                skip_on_screen_excel_feedback = False
                # CSV

                writer.writerow(
                    {
                        'PlayList': playlist,
                        'Owner': vid_owner,
                        'Title': vid_title,
                        'Video Link': vid_link,
                        'Playlist Link': playlnk,
                        'Owner Link': owner_channel
                    })

                #   If The spreadsheet fails NOTHING gets writtent to MSACCESS
                #   Then to an Access Database
                try:

                    str_update = "INSERT INTO TableName (PlayList, Owner, Title, title_lnk, " \
                                 "playlist_lnk, owner_lnk) ".replace("TableName", tbl_vidoes)
                    str_update = str_update + " values ('" + playlist.replace("'", "''")  + "', '" + vid_owner + "', '"
                    str_update = str_update + vid_title + "', '" + vid_link + "', '"
                    str_update = str_update + playlnk + "', '" + owner_channel + "');"

                    # print(str_update)

                    try:
                        cursor.execute(str_update)
                        conn.commit()
                        skip_on_screen_excel_feedback = True
                        next(t_vidoes)
                    except:
                        skip_on_screen_excel_feedback = False

                except:
                    print("Exception")
                    print("Error writing to Access Database {}\n".format(tbl_vidoes))
                    print_error(playlist, playlnk, title, vid_title, vid_owner, owner_channel)

            except:
                pass

            if skip_on_screen_excel_feedback is False:
                print("Shouldn't see this")
                print(
                    "Playlist {:20}{:100}, \nPlaylist Link: {:14}{:100} \nVideo Owner: {:16}{:100}\nTitle: {:22}{:100} \nVideo Link: {:17}{:100}\nOwner Channel: {:14}{:100}\n\n".format
                    (" ", playlist, " ", playlnk, " ", vid_owner, " ", vid_title, " ", vid_link, " ", owner_channel))
                next(t_errors)

    print("\nVidoes number extracted from YouTube was {}".format(t_playlist))
    print("Number written to file was {}".format(t_vidoes))
    print("Number of 'Title issues' / 'write errors' was: {}\n\nFinished".format(t_errors))
    print("\n\nCSV File: '{}'".format(os.path.join(os.getcwd(), output_file)))
    print("MS Access File: '{}'".format(path_db))

    conn.close
    print("Connection Closed")

if __name__ == "__main__":
    main()

#  After finishing the code, I realised that attempting to write
#  to both Excel and MS Access in within 1 loop with
#  nested Try and Exceptions statements was too complex.
#
#  The better approach would have been to make 2 loop passes,
#  The first for Excel - so as to trap and process it's errors
#  and the second for Access for similar reasons.
