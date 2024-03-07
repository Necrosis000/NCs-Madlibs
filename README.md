# NC's Madlibs
A fully customizable madlibs program made in python!

## How to download:
 First go to right and click releases
 
 Find the latest version and click ncsmadlibs1.1.zip and it will auto-download
 
 Now extract the zip and run the .exe and you are good to go!

## How to use:

You can use the base madlibs if you want but to make your own click:

### File
### New
And add your own sections (Max is 7)

It doesnt matter if it's less then 7 it will still work!

Go have some fun and make some funny madlibs!

## Save Format
```json
{
    "totalquestions": 7,
    "questions": {
        "question1": "Enter a name:",
        "question2": "Enter a hobby:",
        "question3": "Enter a job:",
        "question4": "Enter a item:",
        "question5": "Enter a food:",
        "question6": "Enter a fear:",
        "question7": "Enter a second name:"
    },
    "responses": {
        "response1": "Hi my name is ",
        "response2": "My hobby is ",
        "response3": "And When i grow up i want to be a ",
        "response4": "I also use ",
        "response5": "My favourite food is ",
        "response6": "Also i have a fear of ",
        "response7": "i have a friend named "
    }
}
```

NOTE: Manually editing a save is unstable. Please only edit it if you know json well.

"totalquestions" is what tells the script how many questions/responses are in the save.

"questions/responses" is the main strings that tell the script what the questions and responses are that were saved.


## Roadmap
- Add built in save loading system. (so people who dont know loading files well can have an easier time)
