import sqlite3

c = sqlite3.connect("database.db")
cr = c.cursor()

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file: 
        binaryData = file.read()
    return binaryData

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def create():
    cr.execute("CREATE TABLE if not exists gestures(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, photo BLOB NOT NULL)")
    print("created")
    c.commit()
    cr.close()
    c.close()

def insertImage(label,photo):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO gestures
                                  (name, photo) VALUES (?, ?)"""

        gesturePhoto = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (label, gesturePhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)

    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

def readImage(label):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from gestures where name = ?"""
        cursor.execute(sql_fetch_blob_query, (label,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]

            print("Storing photo on disk \n")
            photoPath = "D:\college\Image Processing\ip_paper\images\\" + name + ".jpg"
            writeTofile(photo, photoPath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

# create()
 
# insertImage('mohit', r'E:\imagica\Screenshot_2019-06-04-10-04-50-632.jpeg') # label and image path
# insertImage('m',r'E:\traditional_day_14March2019\me.jpg') 
readImage('mohit')

