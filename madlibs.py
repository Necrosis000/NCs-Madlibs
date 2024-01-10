import PySimpleGUI as sg
import os 
import webbrowser
import datetime
from scripts import madlibsbuilder
import json


fileDir = os.getcwd()
customPrompts = json.load(open(fileDir + "\\saves\\samplesave.json"))["questions"]
selected_theme = 'Dark Grey 8'
sg.theme(selected_theme)
menu_def = [['&File', ['New','Load']],
                ['&Help', ['&Github page']] ]


filenum = 0


layout = [ [sg.Menu(menu_def)],
            [sg.Text("Necrosis MadLibs (Version: 1.1)")],
           # [sg.Text("Choose a file: "), ],
            #[sg.OptionMenu(values=Options_list)]
            [sg.Text(customPrompts["question1"] ,key="enter0"), sg.InputText(key='question1enter')],
            [sg.Text(customPrompts["question2"], key="enter1"), sg.InputText(key='question2enter')],
            [sg.Text(customPrompts["question3"], key="enter2"), sg.InputText(key='question3enter')],
            [sg.Text(customPrompts["question4"], key="enter3"), sg.InputText(key='question4enter')],
            [sg.Text(customPrompts["question5"], key="enter4"), sg.InputText(key='question5enter')],
            [sg.Text(customPrompts["question6"], key="enter5"), sg.InputText(key='question6enter')],
            [sg.Text(customPrompts["question7"], key="enter6"), sg.InputText(key='question7enter')],
            [sg.Text("Results:")],
            [sg.Text("Hi my name is ", visible=False, key="resultquestion1"), sg.Text(size=(50,1), key='result1')],
            [sg.Text("My hobby is ", visible=False, key="resultquestion2"), sg.Text(size=(50,1), key='result2')],
            [sg.Text("And When i grow up i want to be a ", visible=False, key="resultquestion3"), sg.Text(size=(50,1), key='result3')],
            [sg.Text("I also use ", visible=False, key="resultquestion4"), sg.Text(size=(50,1), key='result4')],
            [sg.Text("My favourite food is ", visible=False, key="resultquestion5"), sg.Text(size=(50,1), key='result5')],
            [sg.Text("Also i have a fear of ", visible=False, key="resultquestion6"), sg.Text(size=(50,1), key='result6')],
            [sg.Text("I have a friend named ", visible=False, key="resultquestion7"), sg.Text(size=(50,1), key='result7')],
            [sg.Button("Generate"), sg.Button("Close")]]

window = sg.Window('Necrosis MadLibs (Version: 1.1)', layout)   

while True:             
    event, values = window.read()
    #print(f"Event: {event}, Values: {values}")
    if event in (sg.WIN_CLOSED, 'Close'):
        break
    elif event == "Generate":
        question1 = values['question1enter']
        question2 = values['question2enter']
        question3 = values['question3enter']
        question4 = values['question4enter']
        question5 = values['question5enter']
        question6 = values['question6enter']
        question7 = values['question7enter']

        # everything invisible so only the specific ones are visible
        if window['enter0'].visible == True:
            window['result1'].update(f"{window['resultquestion1'].get()} {values['question1enter']}", visible=True)
        if window['enter1'].visible == True:
            window['result2'].update(f"{window['resultquestion2'].get()} {values['question2enter']}",visible=True)
        if window['enter2'].visible == True:    
            window['result3'].update(f"{window['resultquestion3'].get()} {values['question3enter']}",visible=True)
        if window['enter3'].visible == True:
            window['result4'].update(f"{window['resultquestion4'].get()} {values['question4enter']}",visible=True)
        if window['enter4'].visible == True:
            window['result5'].update(f"{window['resultquestion5'].get()} {values['question5enter']}",visible=True)
        if window['enter5'].visible == True:
            window['result6'].update(f"{window['resultquestion6'].get()} {values['question6enter']}",visible=True)
        if window['enter6'].visible == True:
            window['result7'].update(f"{window['resultquestion7'].get()} {values['question7enter']}",visible=True)
    
    elif event == "Load":
        #file_types=".txt"
        answer = sg.popup_yes_no("Load new save? \n (any unsaved progress will be lost)")

        if answer == "Yes":
            # make everything invisible (lol)
            window['result1'].update(visible=False)
            window['result2'].update(visible=False)
            window['result3'].update(visible=False)
            window['result4'].update(visible=False)
            window['result5'].update(visible=False)
            window['result6'].update(visible=False)
            window['result7'].update(visible=False)

            # input boxes
            window['question1enter'].update(visible=False)
            window['question2enter'].update(visible=False)
            window['question3enter'].update(visible=False)
            window['question4enter'].update(visible=False)
            window['question5enter'].update(visible=False)
            window['question6enter'].update(visible=False)
            window['question7enter'].update(visible=False)

            #labels
            window['enter0'].update(visible=False)
            window['enter1'].update(visible=False)
            window['enter2'].update(visible=False)
            window['enter3'].update(visible=False)
            window['enter4'].update(visible=False)
            window['enter5'].update(visible=False)
            window['enter6'].update(visible=False)


            getsave = sg.popup_get_file("get file", no_window=True, file_types=(("json file", "*.json"),), initial_folder=fileDir + "\\saves")
            savedgotten = open(getsave)
            jsonsavedgotten = json.load(savedgotten)

            if jsonsavedgotten["totalquestions"] == 1:
                window['enter0'].update(jsonsavedgotten["questions"]["question1"], visible=True)
                window['resultquestion1'].update(jsonsavedgotten['responses']['response1'], visible=False)
                window['resultquestion2'].update(visible=False)
                window['resultquestion3'].update(visible=False)
                window['resultquestion4'].update(visible=False)
                window['resultquestion5'].update(visible=False)
                window['resultquestion6'].update(visible=False)
                window['resultquestion7'].update(visible=False)
                window['question1enter'].update(visible=True)

            elif jsonsavedgotten["totalquestions"] == 2:
                window['enter0'].update(jsonsavedgotten["questions"]["question1"], visible=True)
                window['enter1'].update(jsonsavedgotten["questions"]["question2"], visible=True)
                window['resultquestion1'].update(jsonsavedgotten['responses']['response1'], visible=False)
                window['resultquestion2'].update(jsonsavedgotten['responses']['response2'], visible=False)
                window['resultquestion3'].update(visible=False)
                window['resultquestion4'].update(visible=False)
                window['resultquestion5'].update(visible=False)
                window['resultquestion6'].update(visible=False)
                window['resultquestion7'].update(visible=False)
                window['question1enter'].update(visible=True)
                window['question2enter'].update(visible=True)

            elif jsonsavedgotten["totalquestions"] == 3:            
                window['enter0'].update(jsonsavedgotten["questions"]["question1"], visible=True)
                window['enter1'].update(jsonsavedgotten["questions"]["question2"], visible=True)
                window['enter2'].update(jsonsavedgotten["questions"]["question3"], visible=True)
                window['resultquestion1'].update(jsonsavedgotten['responses']['response1'], visible=False)
                window['resultquestion2'].update(jsonsavedgotten['responses']['response2'], visible=False)
                window['resultquestion3'].update(jsonsavedgotten['responses']['response3'], visible=False)
                window['resultquestion4'].update(visible=False)
                window['resultquestion5'].update(visible=False)
                window['resultquestion6'].update(visible=False)
                window['resultquestion7'].update(visible=False)
                window['question1enter'].update(visible=True)
                window['question2enter'].update(visible=True)
                window['question3enter'].update(visible=True)

            elif jsonsavedgotten["totalquestions"] == 4:            
                window['enter0'].update(jsonsavedgotten["questions"]["question1"], visible=True)
                window['enter1'].update(jsonsavedgotten["questions"]["question2"], visible=True)
                window['enter2'].update(jsonsavedgotten["questions"]["question3"], visible=True)
                window['enter3'].update(jsonsavedgotten["questions"]["question4"], visible=True)
                window['resultquestion1'].update(jsonsavedgotten['responses']['response1'], visible=False)
                window['resultquestion2'].update(jsonsavedgotten['responses']['response2'], visible=False)
                window['resultquestion3'].update(jsonsavedgotten['responses']['response3'], visible=False)
                window['resultquestion4'].update(jsonsavedgotten['responses']['response4'], visible=False)
                window['resultquestion5'].update(visible=False)
                window['resultquestion6'].update(visible=False)
                window['resultquestion7'].update(visible=False)
                window['question1enter'].update(visible=True)
                window['question2enter'].update(visible=True)
                window['question3enter'].update(visible=True)
                window['question4enter'].update(visible=True)

            elif jsonsavedgotten["totalquestions"] == 5:            
                window['enter0'].update(jsonsavedgotten["questions"]["question1"], visible=True)
                window['enter1'].update(jsonsavedgotten["questions"]["question2"], visible=True)
                window['enter2'].update(jsonsavedgotten["questions"]["question3"], visible=True)
                window['enter3'].update(jsonsavedgotten["questions"]["question4"], visible=True)
                window['enter4'].update(jsonsavedgotten["questions"]["question5"], visible=True)
                window['resultquestion1'].update(jsonsavedgotten['responses']['response1'], visible=False)
                window['resultquestion2'].update(jsonsavedgotten['responses']['response2'], visible=False)
                window['resultquestion3'].update(jsonsavedgotten['responses']['response3'], visible=False)
                window['resultquestion4'].update(jsonsavedgotten['responses']['response4'], visible=False)
                window['resultquestion5'].update(jsonsavedgotten['responses']['response5'], visible=False)
                window['resultquestion6'].update(visible=False)
                window['resultquestion7'].update(visible=False)
                window['question1enter'].update(visible=True)
                window['question2enter'].update(visible=True) 
                window['question3enter'].update(visible=True)
                window['question4enter'].update(visible=True)
                window['question5enter'].update(visible=True)
            
            elif jsonsavedgotten["totalquestions"] == 6:            
                window['enter0'].update(jsonsavedgotten["questions"]["question1"], visible=True)
                window['enter1'].update(jsonsavedgotten["questions"]["question2"], visible=True)
                window['enter2'].update(jsonsavedgotten["questions"]["question3"], visible=True)
                window['enter3'].update(jsonsavedgotten["questions"]["question4"], visible=True)
                window['enter4'].update(jsonsavedgotten["questions"]["question5"], visible=True)
                window['enter5'].update(jsonsavedgotten["questions"]["question6"], visible=True)
                window['resultquestion1'].update(jsonsavedgotten['responses']['response1'], visible=False)
                window['resultquestion2'].update(jsonsavedgotten['responses']['response2'], visible=False)
                window['resultquestion3'].update(jsonsavedgotten['responses']['response3'], visible=False)
                window['resultquestion4'].update(jsonsavedgotten['responses']['response4'], visible=False)
                window['resultquestion5'].update(jsonsavedgotten['responses']['response5'], visible=False)
                window['resultquestion6'].update(jsonsavedgotten['responses']['response6'], visible=False)
                window['resultquestion7'].update(visible=False)
                window['question1enter'].update(visible=True)
                window['question2enter'].update(visible=True)
                window['question3enter'].update(visible=True)
                window['question4enter'].update(visible=True)
                window['question5enter'].update(visible=True)
                window['question6enter'].update(visible=True)

            elif jsonsavedgotten["totalquestions"] == 7:            
                window['enter0'].update(jsonsavedgotten["questions"]["question1"], visible=True)
                window['enter1'].update(jsonsavedgotten["questions"]["question2"], visible=True)
                window['enter2'].update(jsonsavedgotten["questions"]["question3"], visible=True)
                window['enter3'].update(jsonsavedgotten["questions"]["question4"], visible=True)
                window['enter4'].update(jsonsavedgotten["questions"]["question5"], visible=True)
                window['enter5'].update(jsonsavedgotten["questions"]["question6"], visible=True)
                window['enter6'].update(jsonsavedgotten["questions"]["question7"], visible=True)
                window['resultquestion1'].update(jsonsavedgotten['responses']['response1'], visible=False)
                window['resultquestion2'].update(jsonsavedgotten['responses']['response2'], visible=False)
                window['resultquestion3'].update(jsonsavedgotten['responses']['response3'], visible=False)
                window['resultquestion4'].update(jsonsavedgotten['responses']['response4'], visible=False)
                window['resultquestion5'].update(jsonsavedgotten['responses']['response5'], visible=False)
                window['resultquestion6'].update(jsonsavedgotten['responses']['response6'], visible=False)
                window['resultquestion7'].update(jsonsavedgotten['responses']['response7'], visible=False)
                window['question1enter'].update(visible=True)
                window['question2enter'].update(visible=True)
                window['question3enter'].update(visible=True)
                window['question4enter'].update(visible=True)
                window['question5enter'].update(visible=True)
                window['question6enter'].update(visible=True)
                window['question7enter'].update(visible=True)

                
            #if jsonsavedgotten["questions"]["question1"]:
            #    window['enter0'].update(jsonsavedgotten["questions"]["question1"])
            #    window['resultquestion1'].update(jsonsavedgotten['responses']['response1'])
            #elif jsonsavedgotten["questions"]["question1"] and jsonsavedgotten["questions"]["question2"]:
            #    window['enter1'].update(jsonsavedgotten["questions"]["question2"])
            #    window['resultquestion2'].update(jsonsavedgotten["responses"]["response2"])
            #elif jsonsavedgotten["questions"]["question3"]:
            #    window['enter2'].update(jsonsavedgotten["questions"]["question3"])
            #    window['resultquestion3'].update(jsonsavedgotten["responses"]["response3"])
            #elif jsonsavedgotten["questions"]["question4"]:
            #    window['enter3'].update(jsonsavedgotten["questions"]["question4"])
            #    window['resultquestion4'].update(jsonsavedgotten["responses"]["response4"])
            #elif jsonsavedgotten["questions"]["question5"]:
            #    window['enter4'].update(jsonsavedgotten["questions"]["question5"])
            #    window['resultquestion5'].update(jsonsavedgotten["responses"]["response5"])
            #elif jsonsavedgotten["questions"]["question6"]:
            #    window['enter5'].update(jsonsavedgotten["questions"]["question6"])
            #    window['resultquestion6'].update(jsonsavedgotten["responses"]["response6"])
            #elif jsonsavedgotten["questions"]["question7"]:
            #    window['enter6'].update(jsonsavedgotten["questions"]["question7"])
            #    window['resultquestion7'].update(jsonsavedgotten["responses"]["response7"])
            
            
            
            
            
            
            
            
    elif event == "Github page":
        webbrowser.open("https://github.com/Necrosis000/Necrosis-Customizable-Madlibs")

    elif event == "New":
        madlibsbuilder.newmadlibs()


window.close()
