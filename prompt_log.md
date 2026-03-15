I used claude code and a few autocompletions from antigravity to create this habit tracker.

Prompts:

"I want to develop a CLI habit tracker app using an SQLite database. It should be able to use create, read, update, and delete for each of the habits. Let's get the core database operations working and start with the create function."

"We'll use python. How do I test it in the command line myself?"

"Now let's implement the read function. From here on out, help me understand how I'd code it myself, so I become familiar with SQLite. Teach me hands-on how to develop the rest of the functions."

"What is the significance of the connections and conn commands?"

"Ok, I did it. Now guide me through an update function"

"How do I test if the update command works"

"I received this error: usage: habit_tracker.py [-h] {create,list} ... habit_tracker.py: error: argument command: invalid choice: 'update' (choose from create, list)"

"Ok, it worked, but the output doesn't show the description of '20 min' or '10 min session' at all, is there an issue with my command line output?"

"It seems like the description is still None. How would I change the description from None to anything I want without having to delete everything?"

"How can I implement a delete all function"

"How can I prevent the habits from reading as 'Successfully updated' even when I update a nonexistent habit? I want to develop a query to list all habits of any frequency, so I can see a list of daily habits, weekly, and monthly separately. How can I implement it? Guide me through the process but don't write any code."

"How can I create a main menu interface to perform the different operations?"

"Yes, convert it to that style."