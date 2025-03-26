import random

class Exercise:
    def __init__(self, name, muscle_group, variations, target_reps):
        self.name = name
        self.muscle_group = muscle_group
        self.variations = variations
        self.target_reps = target_reps
        self.current_variation_index = 0

    def adjust_for_difficulty(self, difficulty):
        # Assuming that cardio exercises are in minutes and should have a lower multiplier
        time_based_exercises = ['running', 'cycling', 'jump rope', 'stair climbing', 'hiit']  # Add other time-based exercises if needed
        multiplier = 1.5 if difficulty.lower() == 'medium' else 2 if difficulty.lower() == 'hard' else 1
        
        if self.name.lower() in time_based_exercises:
            multiplier = 1.25 if difficulty.lower() == 'medium' else 1.5 if difficulty.lower() == 'hard' else 1

        self.target_reps = int(self.target_reps * multiplier)

    def get_current_variation(self):
        return self.variations[self.current_variation_index]

    def select_easier_variation(self):
        if self.current_variation_index > 0:
            self.current_variation_index -= 1

    def select_harder_variation(self):
        if self.current_variation_index < len(self.variations) - 1:
            self.current_variation_index += 1


class WorkoutPlan:
    def __init__(self, user):
        self.user = user
        self.current_plan = []

    def generate_workout(self, difficulty, muscle_group):
        # Reinitialize the current plan with fresh exercises each time
        self.current_plan = self.select_exercises(difficulty, muscle_group)
        if not self.current_plan:
            print("No workout to execute.")
            return False
        self.execute_workout()
        return True

    def select_exercises(self, difficulty, muscle_group):
        # Fetch a new instance of the exercise database
        exercise_database = create_exercise_database()
        # Filter exercises based on the muscle group
        filtered_exercises = [ex for ex in exercise_database if ex.muscle_group.lower() == muscle_group.lower()]
        # Apply difficulty settings freshly
        for exercise in filtered_exercises:
            exercise.adjust_for_difficulty(difficulty)
        
        # Randomly select exercises to form a workout plan
        return random.sample(filtered_exercises, min(5, len(filtered_exercises)))

    def execute_workout(self):
        print("Starting workout...")
        for exercise in self.current_plan:
            print(f"Performing: {exercise.name} - Reps: {exercise.target_reps} - Variation: {exercise.get_current_variation()}")
        print("Workout completed!")

    def collect_feedback(self):
        comments = input("Any specific feedback (too hard, too easy)? ")
        # Adjust current workout based on feedback
        self.adjust_workout(comments)

    def adjust_workout(self, feedback):
        if "too hard" in feedback.lower():
            for exercise in self.current_plan:
                exercise.select_easier_variation()
                exercise.target_reps = max(5, exercise.target_reps - 2)
        elif "too easy" in feedback.lower():
            for exercise in self.current_plan:
                exercise.select_harder_variation()
                exercise.target_reps = min(48, exercise.target_reps + 2)

        # Re-execute to reflect adjustments, if needed:
        print("Adjusting workout and re-executing based on feedback...")
        self.execute_workout()

class User:
    def __init__(self, user_id, fitness_level,  exercise_history=None):
        self.user_id = user_id
        self.fitness_level = fitness_level
        self.exercise_history = exercise_history if exercise_history else []
        self.performance_metrics = []
        self.feedback_history = []
        self.initial_difficulty_set = False
        self.preferences = {}

    def log_performance(self, exercise_name, sets, reps, weight, perceived_effort):
        self.performance_metrics.append({
            'exercise': exercise_name,
            'sets': sets,
            'reps': reps,
            'weight': weight,
            'effort': perceived_effort
        })
def create_exercise_database():
    return [
        Exercise("Bench Press", "chest", ["standard", "with chains"], 12),
        Exercise("Push-ups", "chest", ["standard", "diamond"], 15),
        Exercise("Pull-ups", "back", ["weighted", "assisted"], 10),
        Exercise("Barbell Row", "back", ["underhand grip", "overhand grip"], 12),
        Exercise("Squats", "legs", ["barbell", "dumbbell"], 15),
        Exercise("Lunges", "legs", ["walking", "reverse"], 18),
        Exercise("Overhead Press", "shoulders", ["barbell", "dumbbell"], 10),
        Exercise("Lateral Raises", "shoulders", ["single-arm", "cable"], 15),
        Exercise("Dumbbell Flyes", "chest", ["flat bench", "incline bench"], 12),
        Exercise("Chest Dips", "chest", ["parallel bars", "assisted machine"], 15),
        Exercise("Lat Pulldowns", "back", ["wide grip", "close grip"], 12),
        Exercise("T-Bar Rows", "back", ["wide grip", "close grip"], 12),
        Exercise("Leg Press", "legs", ["machine", "sled"], 15),
        Exercise("Romanian Deadlifts", "legs", ["barbell", "dumbbell"], 12),
        Exercise("Leg Curls", "legs", ["machine", "stability ball"], 15),
        Exercise("Front Raises", "shoulders", ["dumbbell", "cable"], 12),
        Exercise("Reverse Flyes", "shoulders", ["dumbbell", "cable"], 15),
        Exercise("Shrugs", "shoulders", ["barbell", "dumbbell"], 12),
        Exercise("Bicep Curls", "arms", ["barbell", "dumbbell", "cable"], 15),
        Exercise("Tricep Dips", "arms", ["parallel bars", "bench"], 12),
        Exercise("Skull Crushers", "arms", ["barbell", "dumbbell", "cable"], 15),
        Exercise("Hammer Curls", "arms", ["dumbbell", "cable"], 15),
        Exercise("Tricep Pushdowns", "arms", ["cable", "band"], 15),
        Exercise("Planks", "core", ["forearm", "straight arm"], 30),  # Time in seconds
        Exercise("Russian Twists", "core", ["bodyweight", "medicine ball"], 20),
        Exercise("Bicycle Crunches", "core", ["bodyweight"], 20),
        Exercise("Leg Raises", "core", ["hanging", "on floor"], 15),
        Exercise("Woodchoppers", "core", ["cable", "medicine ball"], 12),
        Exercise("Running", "cardio", ["treadmill", "outdoor"], 30),  # Time in minutes
        Exercise("Cycling", "cardio", ["stationary", "outdoor"], 45),  # Time in minutes
        Exercise("Jump Rope", "cardio", ["single", "double"], 10),
        Exercise("Stair Climbing", "cardio", ["machine", "actual stairs"], 20),
        Exercise("HIIT", "cardio", ["interval training"], 30),
        Exercise("Yoga Poses", "flexibility", ["downward dog", "warrior pose"], 30),
        Exercise("Stretching", "flexibility", ["dynamic", "static"], 20),
        Exercise("Foam Rolling", "flexibility", ["full body", "targeted areas"], 20),
        Exercise("Mobility Drills", "mobility", ["hip circles", "shoulder rotations"], 15)
    ]


class AIEnhancedWorkoutSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, fitness_level):
        new_user = User(user_id, fitness_level)
        self.users[user_id] = new_user
        return new_user

    def generate_user_workout(self, user_id, difficulty, muscle_group):
        user = self.users.get(user_id)
        if user:
            workout = WorkoutPlan(user)
            if workout.generate_workout(difficulty, muscle_group):
                workout.collect_feedback()  # Collect feedback only if workout was successfully generated
                return workout
            else:
                return None  # No valid workout generated
        print(f"No user found with ID {user_id}.")
        return None

def main():
    system = AIEnhancedWorkoutSystem()
    user = system.add_user("011", "Beginner")
    print(f"Added user: {user.user_id}, Fitness Level: {user.fitness_level}")

    while True:
        difficulty = input("Enter workout difficulty (Easy, Medium, Hard): ").lower()
        muscle_group = input("Target muscle group (e.g., chest, back, legs, shoulders, arms, core, cardio, flexibility): ").lower()


        workout = system.generate_user_workout(user.user_id, difficulty, muscle_group)
        if workout:
            if input("Continue another workout? (yes/no): ").lower() != "yes":
                print("Thank you for using the workout system. See you next time!")
                break
        else:
            if input("Failed to generate a workout. Would you like to try again? (yes/no): ").lower() != "yes":
                print("Thank you for using the workout system. See you next time!")
                break

if __name__ == "__main__":
    main()
