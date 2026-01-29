import json
import os
import satish_module as sw
import aayrish_module as am
DATA_FILE = "data/profile.json"


def save_profile(profile):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(profile.__dict__, f, indent=2)
    print("Profile saved to file.")


def load_profile():
    if not os.path.exists(DATA_FILE):
        print("No saved profile found.")
        return None

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    profile = am.UserProfile(**data)
    profile.validate()
    print("Profile loaded from file.")
    return profile


def show_menu():
    print("\n=== Gym & Nutrition Planner ===")
    print("1) Create / Update Profile")
    print("2) Show Workout Plan")
    print("3) Exercise Details")
    print("4) Calories & Meals")
    print("5) Save Profile")
    print("6) Load Profile")
    print("0) Exit")


def main():
    profile = None

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                profile = am.create_or_update_profile_cli(profile)
                print("Profile saved in memory.")

            elif choice == "2":
                if not profile:
                    print("Please create a profile first.")
                    continue

                split_name, days = sw.recommend_split(profile.training_days)
                print(f"\nWorkout Split: {split_name}")
                print("-" * 40)

                for i, muscles in enumerate(days, start=1):
                    print(f"\nDay {i}: {', '.join(muscles)}")
                    workout = sw.generate_workout(profile, muscles)

                    if not workout:
                        print("No exercises available.")
                        continue

                    for ex, sets, reps, rest in workout:
                        print(
                            f"- {ex.name}: {sets} sets x {reps} reps (rest {rest}s)")

            elif choice == "3":
                sw.show_exercise_details()

            elif choice == "4":
                if not profile:
                    print("Please create a profile first.")
                    continue
                am.print_calories_and_meals(profile)

            elif choice == "5":
                if not profile:
                    print("No profile to save.")
                else:
                    save_profile(profile)

            elif choice == "6":
                profile = load_profile()

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option.")

        except am.ValidationError as e:
            print("Validation error:", e)
        except ValueError:
            print("Invalid input type.")
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()
