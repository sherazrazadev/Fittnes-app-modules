import random
#Now added personalized plan for user categories like (beginner,intermedia,advance) according to age,weight,heigh 
# and provide random excersice with muscle confusion

class PersonalizedWorkoutPlanner:
    def __init__(self, user_data):
        self.user_data = user_data

    def generate_workout_plan(self):
        """
        Generate a personalized workout plan based on user data.
        
        Returns:
        - A list of exercises for the workout plan.
        """
        # Example: Generate a personalized workout plan based on user's fitness level
        fitness_level = self.user_data.get('fitness_level', 'beginner')
        if fitness_level == 'beginner':
            return self.generate_beginner_workout_plan()
        elif fitness_level == 'intermediate':
            return self.generate_intermediate_workout_plan()
        elif fitness_level == 'advanced':
            return self.generate_advanced_workout_plan()

    def generate_beginner_workout_plan(self):
        """
        Generate a beginner-level workout plan.
        
        Returns:
        - A list of beginner-level exercises.
        """
        return ['Push-ups', 'Bodyweight Squats', 'Walking Lunges', 'Plank', 'Jumping Jacks']

    def generate_intermediate_workout_plan(self):
        """
        Generate an intermediate-level workout plan.
        
        Returns:
        - A list of intermediate-level exercises.
        """
        return ['Push-ups', 'Dumbbell Squats', 'Dumbbell Lunges', 'Mountain Climbers', 'Burpees']

    def generate_advanced_workout_plan(self):
        """
        Generate an advanced-level workout plan.
        
        Returns:
        - A list of advanced-level exercises.
        """
        return ['Weighted Push-ups', 'Barbell Squats', 'Barbell Lunges', 'Box Jumps', 'Pull-ups']

class MuscleConfusion:
    def __init__(self, exercise_database, user_data):
        self.exercise_database = exercise_database
        self.user_data = user_data

    def select_exercises(self, num_exercises=5):
        """
        Randomly select exercises from the exercise database while ensuring balanced targeting of different muscle groups and exercise modalities.
        
        Args:
        - num_exercises: Number of exercises to select.
        
        Returns:
        - A list of randomly selected exercises.
        """
        # Initialize personalized workout planner with user data
        workout_planner = PersonalizedWorkoutPlanner(self.user_data)
        # Generate personalized workout plan
        personalized_workout_plan = workout_planner.generate_workout_plan()
        # If the personalized workout plan has enough exercises, return it
        if len(personalized_workout_plan) >= num_exercises:
            return personalized_workout_plan[:num_exercises]
        # If not enough exercises in the personalized workout plan, complement with random exercises
        selected_exercises = personalized_workout_plan
        remaining_exercises = num_exercises - len(personalized_workout_plan)
        for _ in range(remaining_exercises):
            # Select random exercise type (strength, cardio, flexibility)
            exercise_type = random.choice(list(self.exercise_database.keys()))
            if isinstance(self.exercise_database[exercise_type], dict):
                # If exercise type has muscle groups, select random muscle group
                muscle_group = random.choice(list(self.exercise_database[exercise_type].keys()))
                # Select random exercise from the chosen muscle group
                selected_exercise = random.choice(self.exercise_database[exercise_type][muscle_group])
            else:
                # If exercise type does not have muscle groups, select random exercise directly
                selected_exercise = random.choice(self.exercise_database[exercise_type])
            selected_exercises.append(selected_exercise)
        return selected_exercises

# Example usage
exercise_database = {
    'Strength': {
        'Upper Body': ['Push-ups', 'Pull-ups', 'Bench Press'],
        'Lower Body': ['Squats', 'Deadlifts', 'Lunges']
    },
    'Cardio': ['Running', 'Cycling', 'Jumping Jacks'],
    'Flexibility': ['Stretching', 'Yoga', 'Pilates']
}
#this is the user input where user add the inforamation and we decide the excersice according to the  info...
user_data = {
    'fitness_level': 'advanced',
    'age': 20,
    'weight': 80,
    'height': 150
}

muscle_confusion = MuscleConfusion(exercise_database, user_data)
selected_exercises = muscle_confusion.select_exercises(num_exercises=5)
print("Selected Exercises:", selected_exercises)
