import pymongo
from pymongo import MongoClient

from datetime import date, datetime
from typing import Counter

from mutagen.mp3 import MP3
from tkinter import filedialog

import os

# Please Enter Your Connection String Inside The MongoClient To Connect With The Database

Cluster = MongoClient(" ----Please Enter Your Connection String Here---- ")

while True :

    print("Please Select Any One Of The Following :-")
    Upload = ["1 – Upload_Song", "2 – Upload_Podcast", "3 – Upload_Audiobook", "4 - View_QUERY", "5 - Delete_QUERY", "6 - BREAK"]
    for i in Upload :
        print(i)

    Choose_Upload = int(input("Please Choose Any One Of The Above : "))
    
    if Choose_Upload == 1 :
        DB = Cluster["Music_App"]
        Collection = DB["Songs"]
        Date = datetime.now()
        Date = str(Date)
        Bad_Chars = ['-', ':', " ", "."]
        for i in Bad_Chars :
            Date = Date.replace(i, "")
        Data = Date[12::]

        def Convert(Seconds):
            Hours = Seconds // 3600
            Seconds %= 3600
            Minutes = Seconds // 60
            Seconds %= 60
            return Hours, Minutes, Seconds

        File_Name = filedialog.askopenfilename(title="Select A MP3 File", filetypes=[("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")])

        print("Would You Like To Enter The Song Name ?")
        Enter = ["1 - Yes" , "2 - No"]
        for i in Enter :
            print(i)

        Choose_Enter = int(input("Please Choose Either { 1 } Or { 2 } : "))
        if Choose_Enter == 1 :
            Song_Name = input("Please Input The Song Name : ").title()
        else :
            Song_Name = os.path.basename(File_Name)
        
        Audio = MP3(File_Name)
        Audio_Info = Audio.info
        Length_In_Secs = int(Audio_Info.length)
        Hours, Minutes, Seconds = Convert(Length_In_Secs)

        Hours, Minutes, Seconds = str(Hours), str(Minutes), str(Seconds)
        
        for t in Hours :
            if t == "0" :
                Song_Duration = (str(Minutes) + ":" + str(Seconds) + " Or " + str(Length_In_Secs) + " Seconds")
            else :
                Song_Duration = (str(Hours) + ":" + str(Minutes) + ":" + str(Seconds))

        Now = datetime.now()
        Uploading_Time = Now.strftime("%H:%M:%S")

        Post = {"_id": Data, "Song Name": Song_Name, "Song Duration": Song_Duration, "Uploading Time": Uploading_Time}

        Collection.insert_one(Post)

    elif Choose_Upload == 2 :
        DB = Cluster["Music_App"]
        Collection = DB["Podcasts"]
        Date = datetime.now()
        Date = str(Date)
        Bad_Chars = ['-', ':', " ", "."]
        for i in Bad_Chars :
            Date = Date.replace(i, "")
        Data = Date[12::]

        def Convert(Seconds):
            Hours = Seconds // 3600
            Seconds %= 3600
            Minutes = Seconds // 60
            Seconds %= 60
            return Hours, Minutes, Seconds

        File_Name = filedialog.askopenfilename(title="Select A MP3 File", filetypes=[("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")])

        print("Would You Like To Enter The Podcast Name ?")
        Enter = ["1 - Yes" , "2 - No"]
        for i in Enter :
            print(i)

        Choose_Enter = int(input("Please Choose Either { 1 } Or { 2 } : "))
        if Choose_Enter == 1 :
            Podcast_Name = input("Please Input The Podcast Name : ").title()
        else :
            Podcast_Name = os.path.basename(File_Name)
        
        Audio = MP3(File_Name)
        Audio_Info = Audio.info
        Length_In_Secs = int(Audio_Info.length)
        Hours, Minutes, Seconds = Convert(Length_In_Secs)

        Hours, Minutes, Seconds = str(Hours), str(Minutes), str(Seconds)
        
        for t in Hours :
            if t == "0" :
                Podcast_Duration = (str(Minutes) + ":" + str(Seconds) + " Or " + str(Length_In_Secs) + " Seconds")
            else :
                Podcast_Duration = (str(Hours) + ":" + str(Minutes) + ":" + str(Seconds))

        Now = datetime.now()
        Uploading_Time = Now.strftime("%H:%M:%S")

        Host = input("Please Enter The Podcast's Host Name : ").title()

        x = [x for x in input("Please Enter The Participants Names : ").split()]
        x.sort()
        x = str(x)
        Participants = x.title()

        Post = {"_id": Data, "Podcast Name": Podcast_Name, "Podcast Duration": Podcast_Duration, "Uploading Time": Uploading_Time, "Host Name": Host, "Participants Names": Participants}

        Collection.insert_one(Post)

    elif Choose_Upload == 3 :
        DB = Cluster["Music_App"]
        Collection = DB["Audiobooks"]
        Date = datetime.now()
        Date = str(Date)
        Bad_Chars = ['-', ':', " ", "."]
        for i in Bad_Chars :
            Date = Date.replace(i, "")
        Data = Date[12::]

        def Convert(Seconds):
            Hours = Seconds // 3600
            Seconds %= 3600
            Minutes = Seconds // 60
            Seconds %= 60
            return Hours, Minutes, Seconds

        File_Name = filedialog.askopenfilename(title="Select A MP3 File", filetypes=[("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")])

        print("Would You Like To Enter The Audiobook Name ?")
        Enter = ["1 - Yes" , "2 - No"]
        for i in Enter :
            print(i)

        Choose_Enter = int(input("Please Choose Either { 1 } Or { 2 } : "))
        if Choose_Enter == 1 :
            Audiobook_Name = input("Please Input The Audiobook Name : ").title()
        else :
            Audiobook_Name = os.path.basename(File_Name)
        
        Audio = MP3(File_Name)
        Audio_Info = Audio.info
        Length_In_Secs = int(Audio_Info.length)
        Hours, Minutes, Seconds = Convert(Length_In_Secs)

        Hours, Minutes, Seconds = str(Hours), str(Minutes), str(Seconds)
        
        for t in Hours :
            if t == "0" :
                Audiobook_Duration = (str(Minutes) + ":" + str(Seconds) + " Or " + str(Length_In_Secs) + " Seconds")
            else :
                Audiobook_Duration = (str(Hours) + ":" + str(Minutes) + ":" + str(Seconds))

        Now = datetime.now()
        Uploading_Time = Now.strftime("%H:%M:%S")

        Author = input("Please Enter The Author's Name : ").title()
        
        Narrator = input("Please Enter The Narrator's Name : ").title()

        Post = {"_id": Data, "Title": Audiobook_Name, "Author's Name": Author, "Narrator's Name": Narrator, "Audiobook Duration": Audiobook_Duration, "Uploading Time": Uploading_Time}

        Collection.insert_one(Post)

    elif Choose_Upload == 4 :
        View = Collection.find({})
        for x in View :
            print(x)

    elif Choose_Upload == 5 :
        Delete_QUERY = str(input("Please Enter The QUERY _id : "))
        Collection.delete_one({"_id": Delete_QUERY})

    elif Choose_Upload == 6 :
        break