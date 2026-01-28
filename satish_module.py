from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Exercise:
    name: str
    muscle: str
    env: str        # "Home", "Gym", "Both"
    level: str      # "Beginner", "Intermediate", "Advanced"
    instructions: str


EXERCISE_DB = [
    Exercise("Push-ups", "Chest", "Home", "Beginner", "Body straight, lower chest, push up."),
    Exercise("Dumbbell Bench Press", "Chest", "Gym", "Beginner", "Press up, control down, wrists neutral."),
    Exercise("Barbell Bench Press", "Chest", "Gym", "Intermediate", "Tight back, bar to chest, press steadily."),
    Exercise("Band Row", "Back", "Home", "Beginner", "Pull elbows back, squeeze shoulder blades."),
    Exercise("Lat Pulldown", "Back", "Gym", "Beginner", "Pull to upper chest, avoid momentum."),
    Exercise("Barbell Row", "Back", "Gym", "Intermediate", "Hinge, neutral spine, row to ribs."),
    Exercise("Bodyweight Squat", "Legs", "Home", "Beginner", "Hips back, knees track toes, stand tall."),
    Exercise("Leg Press", "Legs", "Gym", "Beginner", "Control down, push up, don’t lock knees hard."),
    Exercise("Back Squat", "Legs", "Gym", "Advanced", "Brace core, squat safely, drive up strong."),
    Exercise("Pike Push-ups", "Shoulders", "Home", "Intermediate", "Hips high, press up."),
    Exercise("DB Shoulder Press", "Shoulders", "Gym", "Beginner", "Press overhead, avoid arch."),
    Exercise("Chair Dips", "Arms", "Home", "Beginner", "Lower controlled, press up."),
    Exercise("DB Curl", "Arms", "Gym", "Beginner", "Curl up, control down, no swinging."),
    Exercise("Plank", "Core", "Both", "Beginner", "Brace core, straight line, breathe."),
    Exercise("Hanging Leg Raise", "Core", "Gym", "Advanced", "Control up/down, avoid swinging."),
]


def level_order(level: str) -> int:
    return {"Beginner": 1, "Intermediate": 2, "Advanced": 3}.get(level, 1)


def recommend_split(days: int) -> Tuple[str, List[List[str]]]:
    if days == 1:
        return "Full Body", [["Chest", "Back", "Legs", "Shoulders", "Arms", "Core"]]
    if days == 2:
        return "Upper/Lower", [["Chest", "Back", "Shoulders", "Arms"], ["Legs", "Core"]]
    if days == 3:
        return "Full Body (3)", [["Chest", "Back", "Legs"], ["Shoulders", "Arms", "Core"], ["Chest", "Back", "Legs", "Core"]]
    if days == 4:
        return "Upper/Lower (4)", [["Chest", "Back", "Shoulders", "Arms"], ["Legs", "Core"], ["Chest", "Back", "Shoulders", "Arms"], ["Legs", "Core"]]
    base = [["Chest", "Shoulders", "Arms"], ["Back", "Arms"], ["Legs", "Core"]]
    out = []
    i = 0
    while len(out) < days:
        out.append(base[i % 3])
        i += 1
    return "PPL", out


def workout_params(difficulty: str) -> Tuple[int, str, int]:
    if difficulty == "Beginner":
        return 3, "10-12", 120
    if difficulty == "Intermediate":
        return 4, "8-12", 90
    return 5, "6-10", 75


def allowed_exercise(profile, ex: Exercise) -> bool:
    if level_order(ex.level) > level_order(profile.difficulty):
        return False
    if ex.env == "Both":
        return True
    return ex.env == profile.environment


def generate_workout(profile, muscles: List[str], per_muscle: int = 2):
    sets, reps, rest = workout_params(profile.difficulty)
    planned = []
    for m in muscles:
        picked = 0
        for ex in EXERCISE_DB:
            if ex.muscle != m:
                continue
            if not allowed_exercise(profile, ex):
                continue
            planned.append((ex, sets, reps, rest))
            picked += 1
            if picked >= per_muscle:
                break
    return planned


def show_exercise_details():
    print("\n--- Exercise Details ---")
    for i, ex in enumerate(EXERCISE_DB, 1):
        print(f"{i}) {ex.name} ({ex.muscle}) [{ex.env}, {ex.level}]")
    try:
        idx = int(input("Pick number: ").strip())
        if 1 <= idx <= len(EXERCISE_DB):
            ex = EXERCISE_DB[idx - 1]
            print("\n" + ex.name)
            print(ex.instructions + "\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Invalid input.\n")
def _level_rank(level):
    order = {
        "Beginner": 1,
        "Intermediate": 2,
        "Advanced": 3
    }
    return order.get(level, 1)


def workout_parameters(difficulty):
    if difficulty == "Beginner":
        return 3, "10-12", 120
    if difficulty == "Intermediate":
        return 4, "8-12", 90
    return 5, "6-10", 75


def recommend_split(days):
    if days <= 1:
        return "Full Body", [
            ["Chest", "Back", "Legs", "Shoulders", "Arms", "Core"]
        ]

    if days == 2:
        return "Upper / Lower", [
            ["Chest", "Back", "Shoulders", "Arms"],
            ["Legs", "Core"]
        ]

    if days == 3:
        return "Push / Pull / Legs", [
            ["Chest", "Shoulders", "Arms"],
            ["Back", "Arms"],
            ["Legs", "Core"]
        ]

    if days == 4:
        return "Upper / Lower (4)", [
            ["Chest", "Back", "Shoulders", "Arms"],
            ["Legs", "Core"],
            ["Chest", "Back", "Shoulders", "Arms"],
            ["Legs", "Core"]
        ]

    return "Custom Split", [
        ["Chest", "Back"],
        ["Legs"],
        ["Shoulders", "Arms"],
        ["Core"]
    ]


def _exercise_allowed(profile, exercise):
    if _level_rank(exercise.difficulty) > _level_rank(profile.difficulty):
        return False

    if exercise.environment == "Both":
        return True

    return exercise.environment == profile.environment


def generate_workout(profile, muscles, per_muscle=2):
    sets, reps, rest = workout_parameters(profile.difficulty)
    workout = []

    for muscle in muscles:
        count = 0
        for ex in EXERCISE_DB:
            if ex.muscle != muscle:
                continue
            if not _exercise_allowed(profile, ex):
                continue

            workout.append((ex, sets, reps, rest))
            count += 1

            if count >= per_muscle:
                break

    return workout
