\# Gym and Nutrition Planner Application (Terminal Based)



\## Course

Object Oriented Programming



\## Authors

\- Satish Thakur (78985)

\- Aayrish Sandhu (78986)



---



\## Project Overview

This is a terminal-based Python application that helps users plan gym workouts and daily nutrition.  

The user creates a fitness profile and the program recommends workouts, exercises, and meals based on the user’s goal, training days, environment, and difficulty level.



The application also allows saving and loading the user profile.



---



\## Project Files

\- main.py → Main menu and program execution

\- satish\_module.py → Workout logic, exercises, splits, difficulty handling

\- aayrish\_module.py → User profile, validation, calorie calculation, nutrition logic



---



\## How to Run the Program

\### Requirements

\- Python 3 installed



\### Steps

1\. Open terminal / command prompt in the project folder

2\. Run:



\# python main.py





---



\## Program Menu Options

After running the program, the following menu appears:



1\) Create / Update Profile  

\- Takes user input (name, age, gender, height, weight, goal, training days, environment, difficulty)

\- Validates inputs



2\) Show Workout Plan  

\- Recommends workout split based on training days

\- Shows exercises based on environment and difficulty

\- Displays sets, reps, and rest time



3\) Exercise Details  

\- Shows list of exercises

\- User selects an exercise

\- Displays form instructions



4\) Calories \& Meals  

\- Calculates daily calorie requirement

\- Displays simple meal recommendations



5\) Save Profile  

\- Saves user profile to a JSON file



6\) Load Profile  

\- Loads user profile from a JSON file



0\) Exit  

\- Closes the program



---



\## Functionalities Implemented

\- F1: User profile creation and validation  

\- F2: Terminal input and output handling  

\- F3: Daily calorie calculation  

\- F4: Workout split recommendation  

\- F6: Environment-based exercise selection (Home / Gym)  

\- F7: Difficulty levels (Beginner / Intermediate / Advanced)  

\- F8: Exercise details with form instructions  

\- F9: Meal and nutrition recommendations  

\- F10: Data persistence using JSON (Save / Load profile)



---



\## OOP Concepts Used

\- Classes and Objects (UserProfile, Exercise, MealItem)

\- Encapsulation (data stored inside classes)

\- Abstraction (separate classes for calories, meals, workouts)

\- Exception Handling (validation errors and invalid input handling)



---



\## Division of Work

\### Aayrish Sandhu

\- User profile and validation (F1)

\- Calorie calculation logic (F3)

\- Nutrition and meal recommendation (F9)

\- CLI helpers for profile input and output (F2)



\### Satish Thakur

\- Workout split logic (F4)

\- Exercise database and environment filtering (F6)

\- Difficulty logic for workouts (F7)

\- Exercise details viewer (F8)

\- Main program integration and save/load feature (F10)



---



\## Data Storage

\- User profile is saved in:

\- If no file exists, loading profile shows a message instead of crashing.



---



\## Notes

\- This is a beginner-level project created for learning Object Oriented Programming.

\- The application is terminal-based for simplicity.







