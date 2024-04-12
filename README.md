# YANTT: Yet another time tracker

<img src="./clock.png" title="" alt="" width="311">

#### Video Demo: ![https://www.youtube.com/watch?v=FcsZDTlEPo8](https://www.youtube.com/watch?v=FcsZDTlEPo8)

#### Description

**Main Goal**

I have tried a variety of time trackers, but they all are to complex for me to put in use; therefore, I made YANTT.

YANTT isn't just another time tracker - It's more than that. 
In comparison with other time trackers such as Clockify or Toggl Track, YANTT reduces all useless features, and only focuses on one major feature: tracking time.

**Features**

Just as the demo showed, there were only three action you could take in YANTT.

- Create and delete diverse activity labels
- Track time based on different activities
- View all the tracked records

By doing this, users can get used to using YANTT more easily and wouldn't be distracted from pedantries.

#### Understanding

##### File Structure

```
├── .gitignore
├── README.md
├── app.py
├── clock.png
├── helpers.py
├── history.py
├── label.py
├── static
│   ├── clock.ico
│   ├── history.js
│   ├── label.js
│   ├── script.js
│   ├── styles.css
│   ├── time_format.js
│   └── time_tracker.js
├── templates
│   ├── index.html
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   └── stats.html
├── todo.org
├── tracker.db
└── user.py
```

There are several files, but I will only explain some of them that are important.

`app.py`

- The starting point of the program

- Create different routes

- Provide various APIs in order to help Front-end display the webpages

`history.py`

- Create history records after time trackers are finished

`label.py`

It has four main functions:

- Add a new label to the database

- Delete a old label from the database

- Check if a label exist

`user.py`

- Get user id from the database

- Check if the username exist

- Check if the password is correct

- Add a new user to the database

`static/script.js`

- The starting point of all Javascript files

`static/time-tracker.js`

- Display a time tracker

- Create a new time tracker

- Check if there's a time tracker running

- Get the time tracker running

`static/history.js`

- Post a request to the history-creating API

`label.js`

- Display different labels

- Get labels from the label-getting API
