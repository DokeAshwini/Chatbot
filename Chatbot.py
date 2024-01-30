import numpy as np 
import pandas as pd
import warnings
import sqlite3
warnings.filterwarnings('ignore')
import json 
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance

venueSQL = "Select venue from Shifts"
studentSQL = "Select firstName from Students"
nameQuery = "Please enter your first (name in one word): \n"
locationQuery = "Please enter the location/store name (in one word): \n"

connection = sqlite3.connect('ChatbotDatabase.db')
cursor = connection.cursor()

#please give the location of intents.json file wherever you have stored it.
with open('C:\\Users\\psxad11\\OneDrive - The University of Nottingham\\HAI lab\\Chatbot_20493897\\intents.json') as json_file:
    data = json.load(json_file)
data = data['intents']

dataset = pd.DataFrame(columns=['intent', 'text', 'response'])
for i in data:
    intent = i['intent']
    for t, r in zip(i['text'], i['responses']):
        row = {'intent': intent, 'text': t, 'response':r}
        dataset = dataset.append(row, ignore_index=True)
dataset

def cosine_distance_countvectorizer_method(s1, s2):

    allsentences = [s1 , s2]

    vectorizer = CountVectorizer()
    all_sentences_to_vector = vectorizer.fit_transform(allsentences)
    text_to_vector_v1 = all_sentences_to_vector.toarray()[0].tolist()
    text_to_vector_v2 = all_sentences_to_vector.toarray()[1].tolist()

    cosine = distance.cosine(text_to_vector_v1, text_to_vector_v2)
    return round((1-cosine),2)

def respond(text):
    maximum = float('-inf')
    response = ""
    closest = ""
    for i in dataset.iterrows():
        similarity = cosine_distance_countvectorizer_method(text, i[1]['text'])
        if similarity > maximum:
            maximum = similarity
            response = i[1]['response']
            closest = i[1]['text']

    if maximum < 0.1 :
        response = "Sorry, can you come again? \nI can book/cancel/view a shift for you. Thanks, Jeni"

    if response.lower() == "availableshiftlist":
        cursor.execute("Select distinct * from Shifts")
        records = cursor.fetchall()
        response = 'Following is the list of available shfits with respective dates and time:'
        for rows in records:
            response = response +'\n' + 'Venue = ' + rows[0] +' \t Date = ' + rows[1] + ' \t Time = ' + rows[2] + ' \t Pay per hour= ' + rows[3] + ' GBP'
                
    if response.lower() == "cancelshift":
        name = input(nameQuery)
        try :
            cursor.execute(studentSQL)
            names = cursor.fetchall()
            for n in names :
                if name.lower() == n[0].lower(): 
                    location = input(locationQuery)
                    cursor.execute(venueSQL)
                    locations = cursor.fetchall()          
                    for l in locations :
                        if location.lower() == l[0].lower():
                            sqlCheckShiftBook = "Select * from Bookings where firstname = ? and venue = ?"
                            sqlCancel = "Delete from Bookings where firstname = ? and venue = ?"
                            try :
                                cursor.execute(sqlCheckShiftBook, [(name),(location)])
                                records = cursor.fetchall()
                                if len(records)==0:
                                    response = "Hi "+name+", you were not booked at " + location + " for the shift, please check the details you provided again"
                                    return response
                                else :
                                    cursor.execute(sqlCancel, [(name),(location)])
                                    response= "You have successfully cancelled your shift!"
                                    return response
                            except:
                                response = "Oops! I cannot verify your details, Please check the details you provided again!"
                                return response
        except:
            response = "Oops! I cannot verify your details, Please check the details you provided again!"
            return response
        
    if response.lower() == "bookshift":
        name = input(nameQuery)
        try :
            cursor.execute(studentSQL)
            names = cursor.fetchall()
            for n in names :
                if name.lower() == n[0].lower(): 
                    location = input(locationQuery)
                    cursor.execute(venueSQL)
                    locations = cursor.fetchall()     
                    for l in locations :
                        if location.lower() == l[0].lower():
                            if location.lower() == "sainsbury":
                                date = "1/12/2022"
                                pay = "10.5 GBP"
                            if location.lower() == "tesco":
                                date = "12/12/2022"
                                pay = "11.5 GBP"
                            if location.lower() == "poundland":
                                date = "17/12/2022"
                                pay = "9.5 GBP"
                            if location.lower() == "aldi":
                                date = "14/12/2022"
                                pay = "8.5 GBP"
                            if location.lower() == "asda":
                                date = "21/12/2022"
                                pay = "13.5 GBP"
                            if location.lower() == "waitrose":
                                date = "21/12/2022"
                                pay = "12.5 GBP"
                            if location.lower() == "royalmail":
                                date = "21/12/2022"
                                pay = "14.5 GBP"
                            if location.lower() == "m&s":
                                date = "21/12/2022"
                                pay = "14.5 GBP"
                            confirm = input(f"Could you kindly confirm that you are prepared to make a reservation for the shift at {location} on {date} with a Yes or No? \n")
                            if confirm.lower()=="yes" :
                                try :
                                    sqlBook = "INSERT INTO Bookings VALUES (?, ? , ?, '10:00 am to 2:00 pm', ?)"
                                    cursor.execute(sqlBook, [(name.lower()), (location.lower()), (date), (pay)])
                                    response = 'Congratulations! you have successfully booked your shift'
                                    return response
                                except:
                                    response = "Oops something went wrong, can you please come again."
                                    return response
                            else:
                                response = "I am Sorry, do you want book other shift or exit?"
                                return response
        except:
            response = "Oops! I cannot verify your details, Please check the details you provided again!"
            return response
                
    if response.lower() == "checkmylist":
        name = input(nameQuery)
        cursor.execute("Select distinct * from Bookings where firstName = ?", [(name)])
        records = cursor.fetchall()
        if records == [] :
            response = 'You have no upcoming shifts scheduled with us.'
        else :
            response = 'Following is the list of shifts you booked at respective dates and time:'
            for rows in records:
                response = response +'\n' + 'Student Name = '+ rows[0] +' Venue = ' + rows[1] +' \t Date = ' + rows[2] + ' \t Time = ' + rows[3] + ' \t Pay per hour= ' + rows[4]

    return response

print("\nHello, I'm Jeni, and welcome to JobSeekers! How can I help you today? \nPlease enter 'Quit' or 'Exit' anytime during the chat if you want to discontinue.")

while True:
    text = str(input("You: "))    
    if text.lower() == "exit" or text.lower() == "quit":
        print("Jeni: Thank you for reaching out, looking forward to seeing you again!")
        connection.commit()
        connection.close()
        break
    reply = respond(text)
    if reply.lower() == "quit":
        print("Jeni: Thank you for reaching out, looking forward to seeing you again!")
        connection.commit()
        connection.close()
        break
    print("Jeni:", reply)