

import sqlite3 #using sqlit3


conn = sqlite3.connect('db_assignment.db')#connects to database file


with conn:
    cur = conn.cursor()     #create table with incrementing id value and row for string value
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_info( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")


    fileList = ['information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg'] #name files to iterate through in for loop

    for txt in fileList: #variable name containing files and new variable (txt)
        if txt.endswith(".txt"):#finds files ending with txt
            print(txt)#prints variable txt
            cur.execute("INSERT INTO tbl_info ( \
            file_name) VALUES (?)", (txt,))#inserts 'wildcard' into string value section of database, txt is being plugged in for that

    conn.commit()
conn.close()
            


