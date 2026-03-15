I developed a habit tracker CLI with the ability to create, read, update, filter by frequency, and delete any or all habits.
I chose habit tracking as my project because frequent tracking and updating of habits is a proven method for maintaining good habits and improving oneself. 

My tracker has the following schema:

Field       Type	    Constraints	                 Purpose
id          INTEGER	    Primary key, auto-increment	 Unique identifier for each habit
name        TEXT	    NOT NULL, UNIQUE	         The habit's name (no duplicates allowed)
description TEXT	    (optional)	                 Free-text description of the habit
frequency   TEXT	    NOT NULL, default 'daily'	 How often the habit should be done
created_at  TEXT	    NOT NULL	                 ISO timestamp of when the habit was added


How to run

Call the script from the command line:
python3 habit_tracker.py

Then enter the number of the option you want to perform.

The 4 CRUD operations in my project are creating, reading, updating, and deleting habits. The user performs these using the main menu loop.