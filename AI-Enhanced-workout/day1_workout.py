import random

class PersonalizedWorkoutPlanner:
    def __init__(self, user_data):
        self.user_data = user_data

    def generate_workout_plan(self):
        """
        Generate a personalized workout plan based on user data.
        
        Returns:
        - A list of exercises for the workout plan.
        """
        # Ask the user for their fitness level
        fitness_level = input("Enter your fitness level (beginner/intermediate/professional): ").lower()
        
        # Generate a personalized workout plan based on the user's fitness level
        if fitness_level == 'beginner':
            return self.generate_beginner_workout_plan()
        elif fitness_level == 'intermediate':
            return self.generate_intermediate_workout_plan()
        elif fitness_level == 'professional':
            return self.generate_professional_workout_plan()
        else:
            print("Invalid fitness level. Please enter either beginner, intermediate, or professional.")
            return []

    def generate_beginner_workout_plan(self):
        """
        Generate a beginner-level workout plan.
        
        Returns:
        - A list of beginner-level exercises.
        """
        return ['Barbell Bench Press', 'Dumbbell Bench Press', 'Pushup',
                'Chest Flye', 'Incline Dumbbell Press']

    def generate_intermediate_workout_plan(self):
        """
        Generate an intermediate-level workout plan.
        
        Returns:
        - A list of intermediate-level exercises.
        """
        return ['Barbell Bench Press', 'Dumbbell Bench Press', 'Cable Crossover',
                'Dumbbell Flye', 'Decline Bench Press']

    def generate_professional_workout_plan(self):
        """
        Generate a professional-level workout plan.
        
        Returns:
        - A list of professional-level exercises.
        """
        return ['Barbell Bench Press', 'Dumbbell Bench Press', 'Pushup',
                'Machine Chest Press', 'Pullover']

class MuscleConfusion:
    def __init__(self, exercise_database, user_data):
        self.exercise_database = exercise_database
        self.user_data = user_data
        self.previous_exercises = []

    def select_exercises(self, num_exercises=5):
        """
        Randomly select exercises from the exercise database while ensuring balanced targeting of different exercise categories.
        
        Args:
        - num_exercises: Number of exercises to select.
        
        Returns:
        - A list of randomly selected exercises.
        """
        # Initialize personalized workout planner with user data
        workout_planner = PersonalizedWorkoutPlanner(self.user_data)
        # Generate personalized workout plan
        personalized_workout_plan = workout_planner.generate_workout_plan()
        
        # Determine number of exercises to select from each category
        num_fixed_compound_exercises = 3  # Number of fixed compound exercises
        num_custom_exercises = num_exercises - num_fixed_compound_exercises
        
        selected_exercises = []
        
        # Add fixed compound exercises from the personalized workout plan
        selected_exercises.extend(personalized_workout_plan[:num_fixed_compound_exercises])
        
        # Select custom isolation exercises randomly from the exercise database
        custom_exercises = self.select_random_exercises(num_custom_exercises)
        selected_exercises.extend(custom_exercises)
        
        return selected_exercises
    
    def select_random_exercises(self, num_exercises):
        """
        Select a specified number of random exercises from the entire exercise database.
        
        Args:
        - num_exercises: The number of exercises to select.
        
        Returns:
        - A list of randomly selected exercises.
        """
        all_exercises = [exercise for category_exercises in self.exercise_database.values() for exercise in category_exercises]
        available_exercises = [exercise for exercise in all_exercises if exercise not in self.previous_exercises]
        return random.sample(available_exercises, num_exercises)

# Example usage
exercise_database = {
    'Chest': ['Barbell Bench Press', 'Dumbbell Bench Press', 'Alternating Dumbbell Bench Press',
              'Hips-Off, Single-Arm Bench Press', 'Cable Crossover', 'Incline Dumbbell Press',
              'Dumbbell Half Flye', 'Dumbbell Flye', 'Incline Dumbbell Flye', 'Low-Incline Press',
              'Speed Bench Press', 'Landmine Press', 'Floor Press', 'Floor Press', 'Pullover',
              'Plate Pressout', '3-Way Suspension Trainer Flye', 'Pushup', 'Medicine Ball Crossover Pushup',
              'Close-Grip Pushup', 'Plyo Pushup', 'Wide-Grip Pushup', 'Triceps Extension', 'Pec Deck',
              'Wide-Grip Dips', 'Smith Machine Incline Press', 'Decline Pushup', 'One-arm Flye Pushup',
              'High Peak Pushup', 'Plank to Pushup', 'One-arm Hang Snatch', 'Burpee']
}

user_data = {}

muscle_confusion = MuscleConfusion(exercise_database, user_data)
while True:
    selected_exercises = muscle_confusion.select_exercises(num_exercises=5)
    print("Selected Exercises:", selected_exercises)
    # Ask if one month has passed
    one_month_completed = input("Has one month passed? (yes/no): ").lower()
    if one_month_completed == 'yes':
        muscle_confusion.previous_exercises = selected_exercises
    else:
        break
