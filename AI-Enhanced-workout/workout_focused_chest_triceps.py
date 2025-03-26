# This workout Plan is heavily focused on upper body development, particularly the chest, shoulders, and triceps. 
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
            "- Push-Ups"
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
            "- Push-Ups"
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
            "- Push-Ups"
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
            "- Push-Ups"
        ]

        # Combine weeks into a month
        month_one_plan = [week_one, week_two, week_three, week_four]

        return month_one_plan

    def month_two_workout_plan(self):
        week_one = [
            "Week 1:",
            "- Bench Press (Paused Reps)",
            "- Incline Dumbbell Press (Drop Sets)",
            "- Chest Dips (Close Grip)",
            "- Barbell Decline Bench Press (Incline Bench Press)",
            "- Dumbbell Pullover (Cable Pullover)",
            "- Cable Flyes (Reverse Flyes)",
            "- Incline Bench Press (Flat Bench Dumbbell Press)",
            "- Dumbbell Flyes (Machine Flyes)",
            "- Chest Dips (Triceps Dips)",
            "- Close Grip Bench Press (Wide Grip Bench Press)",
            "- Machine Chest Press (Dumbbell Press)",
            "- Push-Ups (Diamond Push-Ups)"
        ]

        week_two = [
            "Week 2:",
            "- Barbell Bench Press",
            "- Incline Dumbbell Press (Neutral Grip)",
            "- Chest Dips (Wide Grip)",
            "- Decline Bench Press (Dumbbell)",
            "- Dumbbell Pullover (Single Arm)",
            "- Cable Flyes (Single Arm)",
            "- Flat Bench Dumbbell Press (Close Grip)",
            "- Pec Deck Flyes (Reverse Grip)",
            "- Triceps Dips (Bench)",
            "- Incline Hammer Strength Press (Unilateral)",
            "- Cable Crossover (High to Low)",
            "- Push-Ups (Clapping)"
        ]

        week_three = [
            "Week 3:",
            "- Bench Press (Close Grip)",
            "- Incline Dumbbell Press (Neutral Grip)",
            "- Chest Dips (Weighted)",
            "- Decline Bench Press (Dumbbell)",
            "- Dumbbell Pullover (Single Arm)",
            "- Cable Flyes (Single Arm)",
            "- Flat Bench Dumbbell Press (Close Grip)",
            "- Pec Deck Flyes (Reverse Grip)",
            "- Triceps Dips (Bench)",
            "- Incline Hammer Strength Press (Unilateral)",
            "- Cable Crossover (High to Low)",
            "- Push-Ups (Clapping)"
        ]

        week_four = [
            "Week 4:",
            "- Bench Press (Paused Reps)",
            "- Incline Dumbbell Press (Drop Sets)",
            "- Chest Dips (Close Grip)",
            "- Decline Bench Press (Incline Bench Press)",
            "- Dumbbell Pullover (Cable Pullover)",
            "- Cable Flyes (Reverse Flyes)",
            "- Flat Bench Dumbbell Press (Incline Dumbbell Press)",
            "- Pec Deck Flyes (Machine Flyes)",
            "- Triceps Dips (Triceps Pushdowns)",
            "- Incline Hammer Strength Press (Flat Bench Dumbbell Press)",
            "- Cable Crossover (Dumbbell Flyes)",
            "- Push-Ups (Wide Grip Push-Ups)"
        ]

        # Combine weeks into a month
        month_two_plan = [week_one, week_two, week_three, week_four]

        return month_two_plan
    
    def month_three_workout_plan(self):
        week_one = [
            "Week 1:",
            "- Dumbbell Bench Press on Stability Ball",  
            "- Incline Dumbbell Press (Neutral Grip)", 
            "- Weighted Chest Dips",  
            "- Decline Push-ups",  
            "- Resistance Band Flyes",  
            "- Medicine Ball Chest Press Throw", 
            "- Incline Dumbbell Flyes", 
            "- Barbell Bench Press (Medium Grip)",  
            "- Chest Dips (Weighted)",  
            "- Smith Machine Incline Press", 
            "- Low Cable Crossover", 
            "- Diamond Push-Ups"  
        ]

        week_two = [
            "Week 2:",
            "- Reverse Grip Bench Press", 
            "- Incline Barbell Press", 
            "- Chest Dips (Close Grip)", 
            "- Medicine Ball Slams",
            "- Svend Press",  
            "- One-Arm Dumbbell Flyes",
            "- Flat Bench Dumbbell Press",  
            "- Cable Flyes (High)",  
            "- Triceps Pushdowns",  
            "- Decline Hammer Strength Press", 
            "- Pec Deck Flyes (Reverse Grip)",  
            "- Wide-Grip Push-Ups"  
        ]

        week_three = [
            "Week 3:",
            "- Band-Resisted Bench Press",
            "- Incline Dumbbell Press (Alternating)",
            "- Chest Dips (Wide Grip)",
            "- Dumbbell Floor Press",
            "- Dumbbell Pullover (Single Arm)",
            "- Cable Crossover (Alternating High to Low)",
            "- Decline Push-ups (Feet Elevated)",
            "- Barbell Bench Press (Close Grip)",
            "- Triceps Dips (Bench)",
            "- Incline Hammer Strength Press",
            "- Pec Deck Flyes",
            "- Push-Ups (Staggered Hands)"
        ]

        week_four = [
            "Week 4:",
            "- Incline Dumbbell Press (Drop Sets)",
            "- Bench Press (Paused Reps)",
            "- Chest Dips",
            "- Decline Dumbbell Press",
            "- Single-Arm Cable Flyes",
            "- Medicine Ball Side Throws",
            "- Flat Bench Dumbbell Press",
            "- Incline Dumbbell Flyes (Alternating)",
            "- Triceps Dips",
            "- Decline Hammer Strength Press (Unilateral)",
            "- Cable Crossover",
            "- Push-Ups (Clapping)"
        ]

        month_three_plan = [week_one, week_two, week_three, week_four]
        return month_three_plan
    
    def month_four_workout_plan(self):
        week_one = [
            "Week 1:",
            "- Barbell Bench Press (Chains)", 
            "- Incline Dumbbell Press (Super Slow Reps)", 
            "- Chest Dips (Explosive)",
            "- Decline Cable Press", 
            "- Single-Arm Resistance Band Flyes",  
            "- Medicine Ball Push-up",  
            "- Cable Flyes (Low to High)",  
            "- Dumbbell Bench Press (Light Weight, High Reps)",  
            "- Resistance Band Chest Press",  
            "- Smith Machine Decline Press",  
            "- Cable Crossover (Unilateral)", 
            "- Push-Ups (One Leg Raised)"  
        ]

        week_two = [
            "Week 2:",
            "- Incline Dumbbell Press (Feet Elevated)", 
            "- Barbell Floor Press", 
            "- Chest Dips (Forward Lean)", 
            "- Incline Push-ups (Hands Close)", 
            "- Dumbbell Pullover (with Twist)",  
            "- One-Arm Landmine Press",  
            "- Flat Bench Dumbbell Flyes (Supinated Grip)",
            "- Barbell Bench Press (Partial Reps - Top Half)",  
            "- Triceps Pushdowns (Rope Attachment)",  
            "- Incline Hammer Strength Press (Neutral Grip)",  
            "- Pec Deck Flyes (Single-Arm)", 
            "- Push-Ups (Alternating Wide and Close)"   
        ]

        week_three = [
            "Week 3:",
            "- Dumbbell Bench Press (Isometric Hold at Bottom)", 
            "- Incline Dumbbell Press (Partial Reps - Bottom Half)",
            "- Chest Dips (Band-Assisted)",
            "- Decline Push-ups (Hands Elevated)",
            "- Medicine Ball Chest Pass (With Partner)",
            "- Cable Crossover (Kneeling)",
            "- Flat Bench Dumbbell Press (Feet Elevated)",  
            "- Incline Dumbbell Flyes (Supinated Grip)",
            "- Triceps Pushdowns (V-Bar Attachment)",
            "- Decline Hammer Strength Press",  
            "- Pec Deck Flyes", 
            "- Stability Ball Push-Ups"    
        ]

        week_four = [
            "Week 4:",
            "- Barbell Bench Press (21s - 7 Bottom, 7 Top, 7 Full)", 
            "- Weighted Decline Push-ups",
            "- Chest Dips (Explosive, Light Weight)",
            "- Incline Dumbbell Press (Super Slow Negative)",
            "- Cable Flyes (Alternating Single-Arm, High to Low)", 
            "- Plyometric Push-ups",
            "- Flat Bench Dumbbell Press (Light Weight, High Reps)",
            "- One-Arm Dumbbell Flyes (Heavy Weight)", 
            "- Triceps Dips (Forward Lean)",  
            "- Smith Machine Incline Press (Close Grip)",
            "- Pec Deck Flyes (Reverse Grip)",
            "- Push-Ups (Spiderman)"
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
