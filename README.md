![UnemploymentUpdate-Heroku](thumbnail480x243.jpg?raw=true)

# UnemploymentUpdate-Heroku
A Heroku web app using Flask, PostgreSQL, and D3.js

# Summary
This app uses Flask as the viewer infrastructure, PostgreSQL as the database management system,
and D3.js for data visualization on the platform. There are still some things implement, like
an update feature for old information in the database (changing Pending to Rejected or Affirmative).
Another feature, or rather viewport, to add is the mobile view. There are some issues on just on appearance
that would make it more mobile-user friendly. I also have an SQLite based app for those who want to toy around
with the application [here].

Also, I would like to give credit to Nadieh Bremer for her [Radar Chart], as it was the source of inspiration 
and infrastructure for this single-list structured radar chart. 

# Features
* Upload record individually or use a CSV file with a collection of records. 
* Delete individual records only (no multiple selection tool)
* Dashboard categorizes for pre-determined list of job sectors (edit source code for your case)
* Bar graph counts "Number of Jobs Applied to by Month"
* Circle graph shows proportional size of pending, rejections, and affirmations of responses to a job application



[Radar Chart]: http://bl.ocks.org/nbremer/21746a9668ffdf6d8242
[here]: https://github.com/aflopez314/UnemploymentUpdate-SQLite


Update 3/13/2021
----------------------
* Added update feature for response section
* Circle data growth rate changed
