import sqlite3
connection = sqlite3.connect('ChatbotDatabase.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE if not exists Shifts ( venue text NOT NULL, shiftDate text NOT NULL, shiftTime text NOT NULL, paymentPerHour text NOT NULL, PRIMARY KEY (venue)) ''')
cursor.execute("INSERT INTO Shifts VALUES ('Sainsbury','1/12/2022', '10:00 am to 2:00 pm', '10.5 GBP')")
cursor.execute("INSERT INTO Shifts VALUES ('Tesco','12/12/2022', '10:00 am to 2:00 pm', '11.5 GBP')")
cursor.execute("INSERT INTO Shifts VALUES ('ALDI','14/12/2022', '10:00 am to 2:00 pm', '8.5 GBP')")
cursor.execute("INSERT INTO Shifts VALUES ('Poundland','17/12/2022', '10:00 am to 2:00 pm', '9.5 GBP')")
cursor.execute("INSERT INTO Shifts VALUES ('ASDA','21/12/2022', '10:00 am to 2:00 pm', '13.5 GBP')")
cursor.execute("INSERT INTO Shifts VALUES ('WaitRose','21/12/2022', '10:00 am to 2:00 pm', '12.5 GBP')")
cursor.execute("INSERT INTO Shifts VALUES ('M&S','21/12/2022', '10:00 am to 2:00 pm', '14.5 GBP')")
cursor.execute("INSERT INTO Shifts VALUES ('RoyalMail','21/12/2022', '10:00 am to 2:00 pm', '14.5 GBP')")

cursor.execute('''CREATE TABLE if not exists Students (firstName text NOT NULL, lastName text NOT NULL, DOB text , city text, NINumber text NOT NULL UNIQUE, shareCode text UNIQUE, studentId int NOT NULL UNIQUE, universityName text NOT NULL, PRIMARY KEY (firstName) ) ''')
cursor.execute("INSERT INTO Students VALUES ('Mukul', 'Madgundi', '24/04/1996', 'Nottingham', '365BHJ36TJ', '34HJBVJHV', '20438457', 'University of Nottingham') ")
cursor.execute("INSERT INTO Students VALUES ('Rahul', 'Mall', '03/03/1998', 'Nottingham', '365BHH6TJ', '34HjkVJHV', '20423967', 'University of Nottingham' ) ")
cursor.execute("INSERT INTO Students VALUES ('Shwetali', 'Palsande','17/10/1998', 'Nottingham', '365Bkl6TJ', '34HWEVJHV', '20412967', 'University of Nottingham' ) ")
cursor.execute("INSERT INTO Students VALUES ('Krupa', 'Murthy','09/11/1998', 'Nottingham', '365BHH6TP', '34HjkV9HV', '20128967', 'University of Nottingham' ) ")
cursor.execute("INSERT INTO Students VALUES ('Mahima', 'Harchandani','07/01/1996', 'Nottingham', '365GHH6TJ', '34HH7VJHV', '20908967', 'University of Nottingham' ) ")
cursor.execute("INSERT INTO Students VALUES ('Ashwini', 'Doke', '07/03/1998', 'Nottingham', '365BHHERJ', '34Hjk6JHV', '20438900', 'University of Nottingham' ) ")
cursor.execute("INSERT INTO Students VALUES ('Sushil', 'Kulkarni', '06/11/1998', 'London', '785BHH6TJ', '33HjkVJHV', '20438007', 'University of Brunel' ) ")
cursor.execute("INSERT INTO Students VALUES ('Shivani', 'Mengade', '17/04/1999', 'Nottingham', '458BHH6TJ', '30HjkVJHV', '20638967', 'University of Nottingham' ) ")

cursor.execute('''CREATE TABLE if not exists Bookings ( firstName text, venue text , shiftDate text , shiftTime text, paymentPerHour text, FOREIGN KEY (firstName) references Workers(firstName), FOREIGN KEY (venue) references Shifts(venue)) ''')

