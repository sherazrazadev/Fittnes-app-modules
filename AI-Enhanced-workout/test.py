import random

class Exercise:
    def __init__(self, name, muscle_group, variations, target_reps):
        self.name = name
        self.muscle_group = muscle_group
        self.variations = variations
        self.target_reps = target_reps
        self.current_variation_index = 0

    def adjust_for_difficulty(self, difficulty):
        time_based_exercises = ['running', 'cycling', 'jump rope', 'stair climbing', 'hiit']
        multiplier = 1.5 if difficulty.lower() == 'medium' else 2 if difficulty.lower() == 'hard' else 1
        if self.name.lower() in time_based_exercises:
            multiplier = 1.25 if difficulty.lower() == 'medium' else 1.5 if difficulty.lower() == 'hard' else 1
        self.target_reps = int(self.target_reps * multiplier)

    def get_current_variation(self):
        return self.variations[self.current_variation_index]

    def select_variation(self, easier=True):
        if easier and self.current_variation_index > 0:
            self.current_variation_index -= 1
        elif not easier and self.current_variation_index < len(self.variations) - 1:
            self.current_variation_index += 1

class WorkoutPlan:
    def __init__(self, user):
        self.user = user
        self.current_plan = []

    def generate_workout(self, difficulty, goal):
        exercise_database = create_exercise_database()
        if goal in exercise_database and difficulty in exercise_database[goal]:
            self.current_plan = exercise_database[goal][difficulty]
        else:
            print("No workout plan available for this goal and difficulty.")
            return False

        self.execute_workout()
        return True

    def execute_workout(self):
        print("Starting workout...")
        for exercise in self.current_plan:
            print(f"Performing: {exercise['name']} - Reps: {exercise['reps']} - Sets: {exercise['sets']} - Rest: {exercise['rest']}")
        print("Workout completed!")

    def collect_feedback(self):
        comments = input("Any specific feedback (too hard, too easy)? ")
        # Currently, feedback adjustment not fully implemented because structured plans don't support dynamic adjustments yet

class User:
    def __init__(self, user_id, fitness_level, exercise_history=None):
        self.user_id = user_id
        self.fitness_level = fitness_level
        self.exercise_history = exercise_history if exercise_history else []

def create_exercise_database():
    return {
        'muscle building': {
            'beginner': [
                {"name": "Dumbbell Bench Press", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Barbell Row", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
            ],
            'intermediate': [
                {"name": "Incline Bench Press", "sets": 4, "reps": "8 reps", "rest": "90 sec"},
                {"name": "Pull-up", "sets": 4, "reps": "max reps", "rest": "90 sec"},
            ],
            'advanced': [
                {"name": "Bench Press", "sets": 5, "reps": "5 reps", "rest": "120 sec"},
                {"name": "Deadlift", "sets": 5, "reps": "5 reps", "rest": "120 sec"},
            ],
        }
    }
class AIEnhancedWorkoutSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, fitness_level):
        new_user = User(user_id, fitness_level)
        self.users[user_id] = new_user
        return new_user

    def generate_user_workout(self, user_id, difficulty, goal):
        user = self.users.get(user_id)
        if user:
            workout = WorkoutPlan(user)
            if workout.generate_workout(difficulty, goal):
                return workout
            else:
                return None  # No valid workout generated
        else:
            print(f"No user found with ID {user_id}.")
            return None

def main():
    system = AIEnhancedWorkoutSystem()
    user = system.add_user("011", "beginner")
    print(f"Added user: {user.user_id}, Fitness Level: {user.fitness_level}")

    while True:
        difficulty = input("Enter fitness level (beginner, intermediate, advanced): ").lower()
        goal = input("Enter workout goal (e.g., muscle building, weight loss): ").lower()

        workout = system.generate_user_workout(user.user_id, difficulty, goal)
        if workout:
            if input("Continue another workout? (yes/no): ").lower() != "yes":
                print("Thank you for using the workout system. See you next time!")
                break
        else:
            print("Failed to generate a workout.")
            if input("Would you like to try again? (yes/no): ").lower() != "yes":
                print("Thank you for using the workout system. See you next time!")
                break

if __name__ == "__main__":
    main()