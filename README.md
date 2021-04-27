shire_selections_stock

At CodeClan week 5 is project week so I decided to go with the shop brief: make a web application to be used by shop manager/owner/staff to keep track of their
inventory. As I have recently set-up a small record label (which will be selling vinyl, t-shirts, and other merch) I hope that I personally will be able to use
my own purpose built application in the near future.

FRIDAY
After spending some time considering my project with instructors and fellow cohorts, I eventually decided to scrap my initial idea and go with a straight-forward idea that fits the brief 100%. I used the requirements for the PDA submission as a checklist for my planning; including wireframes, use case and activity diagrams, and class/object/sql_schema diagrams.

SATURDAY
Basically had a day off, however I did create a basic file structure, a database, and looked at previous examples and documentation.

SUNDAY
Completed database set-up with sql schema, ran tests on my models, made basic repositories with C + D, and started writing the console.py file

MONDAY
Finished working on the back end and moved on to the front end. Created html files, linked them up with the controller, and worked on the manufacturers table. Most basic functions are working except for the update function: I have encountered my first big error that I hope to resolve tomorrow. (list index out of range)

TUESDAY
After the stand-up Craig shared with me a lab example with a working update function- "week_04/day_3/one_to_many_solution", after close inspection I realised that my select(id) function in manufacturers_repository.py was missing "result["id"]" in the values list, which would result in my update function (in the controller) returning an updated object with an "id" of none.

As of 3.30pm I have got the add product tab working, now all that is left (in regards to the functions) is to set-up the edit/delete and start work on the styling.