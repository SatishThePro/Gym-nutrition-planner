 Gym and Nutrition Planner Application (Terminal Based)

$ Course
Object Oriented Programming

$ Team Members
- Satish Thakur (78985)
- Aayrish Sandhu (78986)

---

$ Project Topic
Gym and Nutrition Planner Application

---

$ Project Description
This project is a terminal-based Python application developed as part of the Object Oriented Programming course.  
The application helps users plan their gym workouts and daily nutrition based on personal fitness data such as age, height, weight, fitness goal, training days per week, training environment (Home or Gym), and workout difficulty level.

The program recommends:
- workout splits,
- exercises with sets, reps, rest time, and form instructions,
- daily calorie requirements,
- simple meal suggestions.

The user profile can also be saved to a file and loaded again.

---

$ Project Assumptions
- The project topic and functionality list were selected by the team and implemented according to course requirements.
- The application is terminal-based (no GUI) to keep the logic clear and beginner-friendly.
- User inputs are validated to avoid incorrect data.
- The program uses Object Oriented Programming concepts.
- The project is developed collaboratively using GitHub with separate contributions from each team member.
- The program compiles and runs using Python 3.

---

$ How to Run the Project
$$$ Requirements
- Python 3 installed on the system

$$ Steps to Run
1. Open terminal or command prompt in the project folder.
2. Run the following command: python main.py


---

$ Program Functionality (Menu Options)
When the program runs, the following menu is shown:

1) Create / Update Profile  
- Takes user input: name, age, gender, height, weight, goal, training days, environment, difficulty  
- Validates all inputs  

2) Show Workout Plan  
- Recommends workout split based on training days per week  
- Filters exercises based on environment and difficulty  
- Displays sets, reps range, and rest time  

3) Exercise Details  
- Shows list of exercises  
- User selects an exercise  
- Displays form instructions  

4) Calories & Meals  
- Calculates daily calorie requirement  
- Displays simple meal recommendations  

5) Save Profile  
- Saves user profile to a JSON file  

6) Load Profile  
- Loads user profile from a JSON file  

0) Exit  
- Exits the program  

---

$ Functionalities Implemented (Course Requirements)
- F1: User profile creation and management  
- F2: Terminal input handling and output display  
- F3: Daily calorie requirement calculation  
- F4: Workout split recommendation based on training days  
- F6: Training environment selection (Home / Gym)  
- F7: Difficulty levels (Beginner / Intermediate / Advanced)  
- F8: Exercise details including sets, reps, rest, and form instructions  
- F9: Meal and food recommendations based on calorie needs  
- F10: Data persistence (saving and loading user profile using JSON)

The project implements more than the minimum required number of functionalities.

---

$ Object Oriented Programming Concepts Used
- **Classes and Objects**  
Used to model user profiles, exercises, meals, and logic handlers.
- **Encapsulation**  
User and exercise data are stored inside classes.
- **Abstraction**  
Calorie calculation, meal selection, and workout generation are handled by separate classes and functions.
- **Exception Handling**  
Invalid inputs and errors are handled using try/except blocks.

---

$ File Structure
- `main.py`  
Main entry point, menu handling, module integration, save/load logic.
- `satish_module.py`  
Workout split logic, exercise database, difficulty handling, exercise details.
- `aayrish_module.py`  
User profile, validation, calorie calculation, nutrition logic.
- `data/profile.json`  
Created automatically when saving profile.

---

$ Division of Work
$$ Aayrish Sandhu
- User profile creation and validation (F1)
- Calorie calculation logic (F3)
- Nutrition and meal recommendation logic (F9)
- CLI helper functions for profile input and output (F2)

$$ Satish Thakur
- Workout split recommendation (F4)
- Exercise database and environment filtering (F6)
- Difficulty logic for workouts (F7)
- Exercise details viewer (F8)
- Main program integration and data persistence (F10)

Work was divided approximately equally between team members.

---

$ GitHub Usage
- The project was developed using GitHub.
- Separate branches were used for individual contributions.
- Commits were made over time to show development progress.
- Final code is merged into the main branch.

---

$ Compilation and Execution
- The program compiles and runs successfully using Python 3.
- No external libraries are required.
- The program starts correctly using: python main.py

---

$ Notes
- This is a beginner-level academic project.
- The application is terminal-based to focus on OOP concepts rather than GUI complexity.
- Input validation is implemented to prevent crashes.

---

$ Deliverables
- Source code uploaded to Moodle and GitHub
- Project description (this README)
- Video $1: Project overview and working demonstration
- Video $2: Code explanation and discussion


