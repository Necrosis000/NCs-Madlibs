import PySimpleGUI as sg
import os 
import json
import time

fileDir = os.getcwd()
selected_theme = 'Dark Grey 8'
sg.theme(selected_theme)


import datetime

def newmadlibs():
    questionmode = True
    sectiontimes = 2
    layout = [
        [sg.Frame('Questions:',[[sg.Text("Section 1: ", key="section1"), sg.InputText(key='section1enter')],], key='-FRAME-')],
        [sg.Frame('Responses:',[[sg.Text("Response 1: ", key="response1"), sg.InputText(key='response1enter')],], key='-RESPONSEFRAME-')],
        [sg.Button("New Section", key="sectionbtn"), sg.Button("Save"), sg.Exit()],
        
        
        
        
        
        ]

    window = sg.Window('Necrosis MadLibs (Version: 1.1)', layout)   


    while True:             
        event, values = window.read()
        print(event)
        if event in (sg.WIN_CLOSED, 'Close'):
            break

        elif event == "Exit"  :
            answer = sg.popup_yes_no("Close? \n (any unsaved progress will be lost)")
            if answer == "Yes":
                break
            if answer == "No":
                print("no")
        elif event == "sectionbtn":
            print(f"section{sectiontimes}")
            if sectiontimes < 8:
                newsection = [[sg.Text(f"Question {sectiontimes}: ", key=f"section{sectiontimes}"), sg.InputText(key=f'section{sectiontimes}enter')]]
                newresponse = [[sg.Text(f"Response {sectiontimes}: ", key=f"response{sectiontimes}"), sg.InputText(key=f'response{sectiontimes}enter')]]
                window.extend_layout(window['-FRAME-'], newsection)
                window.extend_layout(window['-RESPONSEFRAME-'], newresponse)
                sectiontimes = sectiontimes + 1
        elif event == "Save":
            keys = window.key_dict
           # print(keys)
            with open(fileDir + "\\saves\\save_" + str(datetime.datetime.now().year) + "_" + str(datetime.datetime.now().month) + "_" + str(datetime.datetime.now().hour) + "_" + str(datetime.datetime.now().minute) + "_" + str(datetime.datetime.now().second) + "_" + str(datetime.datetime.now().microsecond) + ".json", 'w+') as jfile:
             

             if "section1" in window.AllKeysDict: 
                samplejson = {"totalquestions": 1, "questions": {"question1": window["section1enter"].get()}, "responses":{"response1":window["response1enter"].get()}}
                formattedjson = json.dumps(samplejson, indent=4)
                jfile.write(formattedjson)
                sg.popup("File saved!")

             if "section2" in window.AllKeysDict:
                samplejson = {"totalquestions": 2, "questions": {"question1": window["section1enter"].get(), "question2": window["section2enter"].get()}, "responses":{"response1":window["response1enter"].get(), "response2":window["response2enter"].get()}}
                jfile.close()
                jsonFile = open(f"{jfile.name}", mode="w+")
                jdump = json.dumps(samplejson, indent=4)
                jsonFile.write(jdump)
                jsonFile.close()
               
             
             if "section3" in window.AllKeysDict:
                samplejson = {"totalquestions": 3, "questions": {"question1": window["section1enter"].get(), "question2": window["section2enter"].get(), "question3": window["section3enter"].get()}, "responses":{"response1":window["response1enter"].get(), "response2":window["response2enter"].get(), "response3":window["response3enter"].get()}}
                jfile.close()
                jsonFile = open(f"{jfile.name}", mode="w+")
                jdump = json.dumps(samplejson, indent=4)
                jsonFile.write(jdump)
                jsonFile.close()
             
             if "section4" in window.AllKeysDict:
                samplejson = {"totalquestions": 4, "questions": {"question1": window["section1enter"].get(), "question2": window["section2enter"].get(), "question3": window["section3enter"].get(), "question4": window["section4enter"].get()}, "responses":{"response1":window["response1enter"].get(), "response2":window["response2enter"].get(), "response3":window["response3enter"].get(), "response4":window["response4enter"].get()}}
                jfile.close()
                jsonFile = open(f"{jfile.name}", mode="w+")
                jdump = json.dumps(samplejson, indent=4)
                jsonFile.write(jdump)
                jsonFile.close()
             
             if "section5" in window.AllKeysDict:
                samplejson = {"totalquestions": 5, "questions": {"question1": window["section1enter"].get(), "question2": window["section2enter"].get(), "question3": window["section3enter"].get(), "question4": window["section5enter"].get(), "question5": window["section5enter"].get()}, "responses":{"response1":window["response1enter"].get(), "response2":window["response2enter"].get(), "response3":window["response3enter"].get(), "response4":window["response4enter"].get(), "response4":window["response5enter"].get()}}
                jfile.close()
                jsonFile = open(f"{jfile.name}", mode="w+")
                jdump = json.dumps(samplejson, indent=4)
                jsonFile.write(jdump)
                jsonFile.close()
             
             if "section6" in window.AllKeysDict:
                samplejson = {"totalquestions": 6, "questions": {"question1": window["section1enter"].get(), "question2": window["section2enter"].get(), "question3": window["section3enter"].get(), "question4": window["section4enter"].get(), "question5": window["section5enter"].get(), "question6": window["section5enter"].get()}, "responses":{"response1":window["response1enter"].get(), "response2":window["response2enter"].get(), "response3":window["response3enter"].get(), "response4":window["response4enter"].get(), "response5":window["response5enter"].get(), "response6":window["response6enter"].get()}}
                jfile.close()
                jsonFile = open(f"{jfile.name}", mode="w+")
                jdump = json.dumps(samplejson, indent=4)
                jsonFile.write(jdump)
                jsonFile.close()

             if "section7" in window.AllKeysDict:
                samplejson = {"totalquestions": 7, "questions": {"question1": window["section1enter"].get(), "question2": window["section2enter"].get(), "question3": window["section3enter"].get(), "question4": window["section4enter"].get(), "question5": window["section5enter"].get(), "question6": window["section6enter"].get(), "question7": window["section7enter"].get()}, "responses":{"response1":window["response1enter"].get(), "response2":window["response2enter"].get(), "response3":window["response3enter"].get(), "response4":window["response4enter"].get(), "response5":window["response5enter"].get(), "response6":window["response6enter"].get(), "response7":window["response7enter"].get()}}
                jfile.close()
                jsonFile = open(f"{jfile.name}", mode="w+")
                jdump = json.dumps(samplejson, indent=4)
                jsonFile.write(jdump)
                jsonFile.close()


          
                    
                
                    
    window.close()




































