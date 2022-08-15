import time
import os
import linecache
import requests

fileDir = os.getcwd()
customPrompts = open(fileDir + "\customprompts.txt")
getLines = customPrompts.read().splitlines() 
response = requests.get("https://api.github.com/repos/necrosis000/necrosis-customizable-madlibs/releases/latest")
customResults = open(fileDir + "\customresults.txt")
getCustomResultLines = customResults.read().splitlines() 

print("Version Number: " + response.json()["name"])
print(" ")

prompt1 = input(getLines[0] + " ")
prompt2 = input(getLines[1] + " ")
prompt3 = input(getLines[2] + " ")
prompt4 = input(getLines[3] + " ")
prompt5 = input(getLines[4] + " ")

print("")
print("-------------------------------")
print("RESULTS")
print("-------------------------------")
print(getCustomResultLines[0] + " " + prompt1)
print("")
print(getCustomResultLines[1] + " " + prompt2)
print("")
print(getCustomResultLines[2] + " " + prompt3)
print("")
print(getCustomResultLines[3] + " " + prompt4)
print("")
print(getCustomResultLines[4] + " " + prompt5)
print("-------------------------------")
print("")
print("Thank you for using my program. More updates soon! \n \n This program will close automatically in 1 minute")
time.sleep(60)