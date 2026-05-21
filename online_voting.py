# Online Voting System Project (Python + SQLite)

# Project Overview



# Python Code (main.py)

import sqlite3

conn = sqlite3.connect("voting.db")
cursor = conn.cursor()

# Create voters table
cursor.execute('''
CREATE TABLE IF NOT EXISTS voters(
    voter_id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    voted INTEGER DEFAULT 0
)
''')

# Create candidates table
cursor.execute('''
CREATE TABLE IF NOT EXISTS candidates(
    candidate_id INTEGER PRIMARY KEY,
    candidate_name TEXT,
    votes INTEGER DEFAULT 0
)
''')

conn.commit()


# Insert sample candidates
cursor.execute("SELECT * FROM candidates")

if len(cursor.fetchall()) == 0:

    cursor.execute(
        "INSERT INTO candidates VALUES (1,'Alice',0)"
    )

    cursor.execute(
        "INSERT INTO candidates VALUES (2,'Bob',0)"
    )

    conn.commit()


class VotingSystem:

    def register(self):

        voter_id = int(input("Enter Voter ID: "))
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        cursor.execute(
            "INSERT INTO voters(voter_id,username,password) VALUES(?,?,?)",
            (voter_id, username, password)
        )

        conn.commit()

        print("Registration Successful\\n")


    def login(self):

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        cursor.execute(
            "SELECT * FROM voters WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        if user:

            print("Login Successful\\n")

            if user[3] == 1:
                print("You have already voted\\n")

            else:
                self.vote(user[0])

        else:
            print("Invalid Credentials\\n")


    def vote(self, voter_id):

        print("Candidates")
        print("1. Alice")
        print("2. Bob")

        choice = int(input("Enter Candidate Number: "))

        if choice == 1:

            cursor.execute(
                "UPDATE candidates SET votes = votes + 1 WHERE candidate_id = 1"
            )

        elif choice == 2:

            cursor.execute(
                "UPDATE candidates SET votes = votes + 1 WHERE candidate_id = 2"
            )

        else:
            print("Invalid Choice")
            return

        cursor.execute(
            "UPDATE voters SET voted = 1 WHERE voter_id=?",
            (voter_id,)
        )

        conn.commit()

        print("Vote Cast Successfully\\n")


    def show_results(self):

        cursor.execute("SELECT * FROM candidates")

        results = cursor.fetchall()

        print("\\nElection Results")
        print("---------------------")

        for row in results:

            print(f"{row[1]} : {row[2]} votes")


obj = VotingSystem()

while True:

    print("===== Online Voting System =====")
    print("1. Register")
    print("2. Login and Vote")
    print("3. Show Results")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        obj.register()

    elif choice == 2:
        obj.login()

    elif choice == 3:
        obj.show_results()

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")


conn.close()


