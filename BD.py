from time import sleep
import mysql.connector


class Connector():
    while True:
        try:
            db = mysql.connector.connect(
                    host="db",
                    user="root",
                    passwd = "digo12",
                    database = "bancodeteste"  ##mycursor.execute("CREATE DATABASE bancodeteste")
                )
            mycursor = db.cursor()
            break
        except:
            print("error. no database")
            sleep(3)
    

    def __init__(self):
        

        #Deleting All Tables
        try:
            self.mycursor.execute("DROP TABLE Vinculations")
        except:
            print("ok")
        try:
            self.mycursor.execute("DROP TABLE Course")
            self.mycursor.execute("DROP TABLE Subject")
            self.db.commit()
        except:
            print("ok")

        # #Creating Tables
        self.mycursor.execute("""
        CREATE TABLE Course (
            course_id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(50),
            type VARCHAR(20),
            PRIMARY KEY (course_id)
            )""")
        self.mycursor.execute("""
        CREATE TABLE Subject (
            subject_id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(50),
            PRIMARY KEY (subject_id)
            )""")
        self.mycursor.execute("""
        CREATE TABLE Vinculations (
            course_id INT NOT NULL,
            subject_id INT NOT NULL,
            FOREIGN KEY (course_id)
                REFERENCES Course(course_id)
                ON DELETE CASCADE,
            FOREIGN KEY (subject_id)
                REFERENCES Subject(subject_id)
                ON DELETE CASCADE   
            )""")
        self.db.commit()

    #Deleting All Elements
    # mycursor.execute("TRUNCATE TABLE Course")
    # mycursor.execute("TRUNCATE TABLE Vinculations")
    # mycursor.execute("TRUNCATE TABLE Subject")



    #Deleting All Tables
    # mycursor.execute("DROP TABLE Course")
    # mycursor.execute("DROP TABLE Vinculations")
    # mycursor.execute("DROP TABLE Subject")
    #mycursor.execute("DESCRIBE Course")


    # for x in mycursor:
    #     print(x)


    #mycursor.execute("INSERT INTO Course(name, tipo) VALUES (%s,%s)", ("Direito", "GRADUACAO"))
    # db.commit() #used to confirm changes in database


    #mycursor.execute("INSERT INTO Course(name, tipo) VALUES ({},{})".format("Engenharia", "GRADUACAO"))