class WorkoutPlan:
    def __init__(self):
        self.current_month = 1
        self.current_week = 1
        self.completed_months = 0
        self.month_one_plan = self.month_one_workout_plan()
        self.month_two_plan = self.month_two_workout_plan()
        self.month_three_plan = self.month_three_workout_plan()
        self.month_four_plan = self.month_four_workout_plan()

    def month_one_workout_plan(self):
        week_one = [
            "Week 1:",
            "- Bench Press",
            "- Incline Dumbbell Press",
            "- Chest Dips",
            "- Barbell Decline Bench Press",
            "- Dumbbell Pullover",
            "- Cable Flyes",
            "- Incline Bench Press",
            "- Dumbbell Flyes",
            "- Chest Dips",
            "- Close Grip Bench Press",
            "- Machine Chest Press",
            "- Push-Ups",
            "- Pull-Ups",  # Added for back
            "- Barbell Rows",  # Added for back
            "- Squats",  # Added for legs
            "- Leg Press",  # Added for legs
            "- Planks"  # Added for core
        ]

        week_two = [
            "Week 2:",
            "- Barbell Bench Press",
            "- Incline Dumbbell Press",
            "- Chest Dips",
            "- Decline Bench Press",
            "- Dumbbell Pullover",
            "- Cable Flyes",
            "- Flat Bench Dumbbell Press",
            "- Pec Deck Flyes",
            "- Triceps Dips",
            "- Incline Hammer Strength Press",
            "- Cable Crossover",
            "- Push-Ups",
            "- Chin-Ups",  # Added for back
            "- Dumbbell Rows",  # Added for back
            "- Lunges",  # Added for legs
            "- Deadlifts",  # Added for legs and back
            "- Bicycle Crunches"  # Added for core
        ]

        week_three = [
            "Week 3:",
            "- Bench Press",
            "- Incline Dumbbell Press",
            "- Chest Dips",
            "- Decline Bench Press",
            "- Dumbbell Pullover",
            "- Cable Flyes",
            "- Flat Bench Dumbbell Press",
            "- Pec Deck Flyes",
            "- Triceps Dips",
            "- Incline Hammer Strength Press",
            "- Cable Crossover",
            "- Push-Ups",
            "- Lat Pulldowns",  # Added for back
            "- Seated Cable Rows",  # Added for back
            "- Front Squats",  # Added for legs
            "- Calf Raises",  # Added for legs
            "- Hanging Leg Raises"  # Added for core
        ]

        week_four = [
            "Week 4:",
            "- Bench Press",
            "- Incline Dumbbell Press",
            "- Chest Dips",
            "- Decline Bench Press",
            "- Dumbbell Pullover",
            "- Cable Flyes",
            "- Flat Bench Dumbbell Press",
            "- Pec Deck Flyes",
            "- Triceps Dips",
            "- Incline Hammer Strength Press",
            "- Cable Crossover",
            "- Push-Ups",
            "- Pull-Ups",  # Added for back
            "- T-Bar Rows",  # Added for back
            "- Bulgarian Split Squats",  # Added for legs
            "- Stiff-Leg Deadlifts",  # Added for legs
            "- Russian Twists"  # Added for core
        ]
        # Combine weeks into a month
        month_one_plan = [week_one, week_two, week_three, week_four]

        return month_one_plan

    def month_two_workout_plan(self):
        week_one = [
            "Week 1:",
            "- Bench Press (Paused Reps)",
            "- Incline Dumbbell Press (Drop Sets)",
            "- Chest Dips (Weighted)",
            "- Barbell Decline Bench Press (Paused Reps)",
            "- Dumbbell Pullover (Cable Pullovers)",
            "- Cable Flyes (Single Arm Flyes)",
            "- Incline Bench Press (Flat Bench Press with Bands)",
            "- Dumbbell Flyes (Machine Flyes)",
            "- Chest Dips (Triceps Dips)",
            "- Close Grip Bench Press (Wide Grip Bench Press)",
            "- Machine Chest Press (Single Arm Chest Press)",
            "- Push-Ups (Diamond Push-Ups)",
            "- Pull-Ups (Weighted)",
            "- Barbell Rows (Single Arm)",
            "- Squats (Paused Squats)",
            "- Leg Press (Single-Leg)",
            "- Planks (Weighted)"
        ]

        week_two = [
            "Week 2:",
            "- Barbell Bench Press (Paused Reps)",
            "- Incline Dumbbell Press (Neutral Grip)",
            "- Chest Dips (Band Assisted)",
            "- Decline Bench Press (Bench Press with Chains)",
            "- Dumbbell Pullover (Single Arm Dumbbell Pullover)",
            "- Cable Flyes (Low to High Cable Flyes)",
            "- Flat Bench Dumbbell Press (Smith Machine Press)",
            "- Pec Deck Flyes (Reverse Pec Deck Flyes)",
            "- Triceps Dips (Weighted)",
            "- Incline Hammer Strength Press (Unilateral)",
            "- Cable Crossover (High to Low Crossover)",
            "- Push-Ups (Clapping Push-Ups)",
            "- Chin-Ups (Close Grip)",
            "- Dumbbell Rows (Incline)",
            "- Lunges (Walking Lunges)",
            "- Deadlifts (Deficit Deadlifts)",
            "- Bicycle Crunches (Weighted)"
        ]

        week_three = [
            "Week 3:",
            "- Bench Press (Close Grip)",
            "- Incline Dumbbell Press (Arnold Press)",
            "- Chest Dips (Weighted)",
            "- Decline Bench Press (Floor Press)",
            "- Dumbbell Pullover (With Rotation)",
            "- Cable Flyes (Single Arm with Bands)",
            "- Flat Bench Dumbbell Press (Reverse Grip Press)",
            "- Pec Deck Flyes (Cable Flyes)",
            "- Triceps Dips (Incline Dips)",
            "- Incline Hammer Strength Press (Decline Dumbbell Press)",
            "- Cable Crossover (Low to High)",
            "- Push-Ups (Wide Grip Push-Ups)",
            "- Lat Pulldowns (Behind the Neck)",
            "- Seated Cable Rows (Standing Cable Rows)",
            "- Front Squats (Overhead Squats)",
            "- Calf Raises (Donkey Calf Raises)",
            "- Hanging Leg Raises (With Twist)"
        ]

        week_four = [
            "Week 4:",
            "- Bench Press (Paused Reps)",
            "- Incline Dumbbell Press (Drop Sets)",
            "- Chest Dips (Close Grip)",
            "- Decline Bench Press (Incline Bench Press with Chains)",
            "- Dumbbell Pullover (Cable Pullover)",
            "- Cable Flyes (Reverse Flyes)",
            "- Flat Bench Dumbbell Press (Incline Dumbbell Press with Chains)",
            "- Pec Deck Flyes (Machine Flyes)",
            "- Triceps Dips (Bench Dips with Weight)",
            "- Incline Hammer Strength Press (Flat Bench Press)",
            "- Cable Crossover (Dumbbell Cross Punches)",
            "- Push-Ups (Spiderman Push-Ups)",
            "- Pull-Ups (L-Sit Pull-Ups)",
            "- T-Bar Rows (360 Degree T-Bar Rows)",
            "- Bulgarian Split Squats (Single Leg Deadlift)",
            "- Stiff-Leg Deadlifts (Romanian Deadlifts)",
            "- Russian Twists (Medicine Ball Twists)"
        ]

        # Combine weeks into a month
        month_two_plan = [week_one, week_two, week_three, week_four]
        return month_two_plan

    
    def month_three_workout_plan(self):
        week_one = [
            "Week 1:",
            "- Barbell Bench Press",
            "- Incline Dumbbell Press",
            "- Chest Dips",
            "- Pull-Ups",  
            "- Deadlifts",
            "- Squats",
            "- Plank with Arm Lift",
            "- Bent Over Rows",
            "- Leg Raises",
            "- Shoulder Press",
            "- Bicep Curls",
            "- Tricep Kickbacks"
        ]

        week_two = [
            "Week 2:",
            "- Decline Cable Press",
            "- Single-Arm Resistance Band Flyes",
            "- Medicine Ball Push-up",
            "- Chin-Ups",
            "- Lunges",
            "- Romanian Deadlifts",
            "- Russian Twists",
            "- T-Bar Row",
            "- Hanging Knee Raises",
            "- Lateral Raises",
            "- Hammer Curls",
            "- Dips"
        ]

        week_three = [
            "Week 3:",
            "- Cable Flyes",
            "- Dumbbell Bench Press",
            "- Resistance Band Chest Press",
            "- Wide-Grip Pull-Ups",
            "- Front Squats",
            "- Step-Ups",
            "- Bicycle Crunches",
            "- One-Arm Dumbbell Row",
            "- Cable Woodchoppers",
            "- Arnold Press",
            "- Preacher Curls",
            "- Skull Crushers"
        ]

        week_four = [
            "Week 4:",
            "- Smith Machine Decline Press",
            "- Cable Crossover",
            "- Push-Ups",
            "- Lat Pulldowns",
            "- Bulgarian Split Squats",
            "- Calf Raises",
            "- Ab Rollouts",
            "- Reverse Flyes",
            "- Leg Press",
            "- Upright Rows",
            "- Concentration Curls",
            "- Overhead Tricep Extensions"
        ]

        month_three_plan = [week_one, week_two, week_three, week_four]
        return month_three_plan

    
    def month_four_workout_plan(self):
        week_one = [
            "Week 1:",
            "- Barbell Bench Press (with bands)",
            "- Incline Dumbbell Press (drop sets)",
            "- Chest Dips (weighted)",
            "- Pull-Ups (with negative reps)",
            "- Deadlifts (deficit deadlifts)",
            "- Squats (front squats)",
            "- Plank with Arm Lift (on stability ball)",
            "- Bent Over Rows (underhand grip)",
            "- Leg Raises (hanging from bar)",
            "- Shoulder Press (Arnold press)",
            "- Bicep Curls (21s method)",
            "- Tricep Kickbacks (with resistance bands)"
        ]

        week_two = [
            "Week 2:",
            "- Decline Cable Press (with increased incline)",
            "- Single-Arm Resistance Band Flyes (alter angles)",
            "- Medicine Ball Push-up (on Bosu ball)",
            "- Chin-Ups (weighted)",
            "- Lunges (walking lunges with twist)",
            "- Romanian Deadlifts (single-leg)",
            "- Russian Twists (with medicine ball)",
            "- T-Bar Row (reverse grip)",
            "- Hanging Knee Raises (to the side for obliques)",
            "- Lateral Raises (cable lateral raises)",
            "- Hammer Curls (cross body)",
            "- Dips (on rings or suspended)"
        ]

        week_three = [
            "Week 3:",
            "- Cable Flyes (single arm with increased tension)",
            "- Dumbbell Bench Press (paused reps)",
            "- Resistance Band Chest Press (double bands for increased resistance)",
            "- Wide-Grip Pull-Ups (L-sit pull-ups)",
            "- Front Squats (overhead squats)",
            "- Step-Ups (with knee raise at top)",
            "- Bicycle Crunches (on a decline bench)",
            "- One-Arm Dumbbell Row (with rotation at top)",
            "- Cable Woodchoppers (high to low)",
            "- Arnold Press (with rotation at bottom)",
            "- Preacher Curls (with slow negatives)",
            "- Skull Crushers (incline bench)"
        ]

        week_four = [
            "Week 4:",
            "- Smith Machine Decline Press (close grip)",
            "- Cable Crossover (decline angle)",
            "- Push-Ups (with clapping)",
            "- Lat Pulldowns (behind the neck)",
            "- Bulgarian Split Squats (with dumbbells)",
            "- Calf Raises (seated calf raises)",
            "- Ab Rollouts (standing rollout from knees)",
            "- Reverse Flyes (with pec deck machine)",
            "- Leg Press (single-leg press)",
            "- Upright Rows (with kettlebells)",
            "- Concentration Curls (standing, leaning forward slightly)",
            "- Overhead Tricep Extensions (with cable)"
        ]

        month_four_plan = [week_one, week_two, week_three, week_four]
        return month_four_plan



    def display_current_month_plan(self):
        if self.current_month == 1:
            month_plan = self.month_one_plan
        elif self.current_month == 2:
            month_plan = self.month_two_plan
        elif self.current_month == 3:
            month_plan = self.month_three_plan
        else:  # Assuming current_month == 4
            month_plan = self.month_four_plan

        print(f"Current Month: {self.current_month}")
        for week in month_plan:
            print("\n".join(week))
            print()

    def update_progress(self):
        self.current_week = 1  # Reset week to 1 when switching months
        self.completed_months += 1
        if self.completed_months % 4 == 0:  
            self.current_month = 1  # Reset back to the beginning
        else:
            self.current_month += 1  # Otherwise, move to the next month 
            if self.current_month > 4:  # Reset after reaching month 4 
                self.current_month = 1 


    def simulate_workout_progress(self):
        while True:
            self.display_current_month_plan()
            completed = input("Have you completed this month? (yes/no): ").lower().strip()
            if completed == "yes":
                self.update_progress()
            else:
                print("Keep up the good work! Continue with your workouts.")
            print()

            if self.completed_months == 12:  # Adjust this number based on how many months you want to simulate
                print("Congratulations! You have completed the workout simulation.")
                break

# Instantiate WorkoutPlan class
workout_planner = WorkoutPlan()

# Simulate workout progress
workout_planner.simulate_workout_progress()
