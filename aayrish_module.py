from dataclasses import dataclass
from typing import List

class ValidationError(Exception):
    pass

@dataclass
class UserProfile:
    name: str
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    goal: str
    training_days: int
    environment: str
    difficulty: str

    def validate(self):
        if not self.name.strip():
            raise ValidationError("Name cannot be empty")
        if self.gender not in ("Male", "Female"):
            raise ValidationError("Gender must be Male or Female")
        if self.goal not in ("Cut", "Maintain", "Bulk"):
            raise ValidationError("Goal must be Cut, Maintain or Bulk")
        if self.environment not in ("Home", "Gym"):
            raise ValidationError("Environment must be Home or Gym")
        if self.difficulty not in ("Beginner", "Intermediate", "Advanced"):
            raise ValidationError("Difficulty must be Beginner, Intermediate or Advanced")
        if not (12 <= self.age <= 90):
            raise ValidationError("Age must be between 12 and 90")
        if not (120 <= self.height_cm <= 220):
            raise ValidationError("Height must be between 120 and 220 cm")
        if not (30 <= self.weight_kg <= 250):
            raise ValidationError("Weight must be between 30 and 250 kg")
        if not (1 <= self.training_days <= 7):
            raise ValidationError("Training days must be between 1 and 7")

class CalorieCalculator:
    @staticmethod
    def bmr(profile):
        if profile.gender == "Male":
            return 10 * profile.weight_kg + 6.25 * profile.height_cm - 5 * profile.age + 5
        return 10 * profile.weight_kg + 6.25 * profile.height_cm - 5 * profile.age - 161

    @staticmethod
    def activity_multiplier(days):
        if days <= 1: return 1.2
        if days == 2: return 1.35
        if days == 3: return 1.45
        if days == 4: return 1.55
        if days == 5: return 1.65
        return 1.75

    @classmethod
    def daily_calories(cls, profile):
        calories = cls.bmr(profile) * cls.activity_multiplier(profile.training_days)
        if profile.goal == "Cut":
            calories -= 400
        elif profile.goal == "Bulk":
            calories += 300
        if profile.gender == "Male" and calories < 1500:
            calories = 1500
        if profile.gender == "Female" and calories < 1200:
            calories = 1200
        return int(calories)

@dataclass
class MealItem:
    name: str
    calories: int
    tag: str

class NutritionRecommender:
    def __init__(self, meals):
        self.meals = meals

    def recommend(self, target):
        bias = (target - 1600) / 1200
        if bias < 0: bias = 0
        if bias > 1: bias = 1

        def pick(tag):
            items = [m for m in self.meals if m.tag == tag]
            items.sort(key=lambda x: x.calories)
            if not items:
                return MealItem("No data", 0, tag)
            index = int(bias * (len(items) - 1))
            return items[index]

        return [
            pick("Breakfast"),
            pick("Lunch"),
            pick("Dinner"),
            pick("Snack")
        ]

MEAL_DB = [
    MealItem("Oats + Milk + Banana", 450, "Breakfast"),
    MealItem("Eggs + Toast + Fruit", 550, "Breakfast"),
    MealItem("Chicken Rice Bowl", 650, "Lunch"),
    MealItem("Paneer Rice Bowl", 700, "Lunch"),
    MealItem("Chicken Curry + Rice", 750, "Dinner"),
    MealItem("Paneer Curry + Rice", 800, "Dinner"),
    MealItem("Whey Shake", 200, "Snack"),
    MealItem("Yogurt + Nuts", 300, "Snack"),
]

class CalorieCalculator:
    @staticmethod
    def bmr(profile):
        w, h, a = profile.weight_kg, profile.height_cm, profile.age
        if profile.gender == "Male":
            return 10*w + 6.25*h - 5*a + 5
        return 10*w + 6.25*h - 5*a - 161

    @staticmethod
    def activity_multiplier(days):
        if days <= 1:
            return 1.2
        if days == 2:
            return 1.35
        if days == 3:
            return 1.45
        if days == 4:
            return 1.55
        if days == 5:
            return 1.65
        return 1.75

    @classmethod
    def daily_calories(cls, profile):
        tdee = cls.bmr(profile) * cls.activity_multiplier(profile.training_days)
        if profile.goal == "Cut":
            tdee -= 400
        elif profile.goal == "Bulk":
            tdee += 300
        return int(tdee)


class MealItem:
    def __init__(self, name, calories, tag):
        self.name = name
        self.calories = calories
        self.tag = tag


MEAL_DB = [
    MealItem("Oats + Milk + Banana", 450, "Breakfast"),
    MealItem("Eggs + Toast", 500, "Breakfast"),
    MealItem("Chicken Rice Bowl", 650, "Lunch"),
    MealItem("Paneer Rice Bowl", 700, "Lunch"),
    MealItem("Chicken Curry + Rice", 750, "Dinner"),
    MealItem("Paneer Curry + Rice", 800, "Dinner"),
    MealItem("Whey Shake", 200, "Snack"),
    MealItem("Yogurt + Nuts", 300, "Snack"),
]


class NutritionRecommender:
    def recommend(self, target):
        selected = []
        total = 0
        for meal in MEAL_DB:
            if total + meal.calories <= target:
                selected.append(meal)
                total += meal.calories
        return selected

def create_or_update_profile_cli(existing=None):
    print("\n--- Create / Update Profile ---")

    name = input("Name: ").strip()
    age = int(input("Age: ").strip())
    gender = input("Gender (Male/Female): ").strip()
    height = float(input("Height (cm): ").strip())
    weight = float(input("Weight (kg): ").strip())
    goal = input("Goal (Cut/Maintain/Bulk): ").strip()
    days = int(input("Training days per week: ").strip())
    environment = input("Environment (Home/Gym): ").strip()
    difficulty = input("Difficulty (Beginner/Intermediate/Advanced): ").strip()

    profile = UserProfile(
        name=name,
        age=age,
        gender=gender,
        height_cm=height,
        weight_kg=weight,
        goal=goal,
        training_days=days,
        environment=environment,
        difficulty=difficulty
    )

    profile.validate()
    return profile


def print_calories_and_meals(profile):
    calories = CalorieCalculator.daily_calories(profile)
    meals = NutritionRecommender().recommend(calories)

    print(f"\nDaily calorie target: {calories} kcal")
    print("-" * 40)

    total = 0
    for meal in meals:
        print(f"{meal.tag}: {meal.name} ({meal.calories} kcal)")
        total += meal.calories

    print(f"Estimated total: {total} kcal\n")


