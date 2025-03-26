workouts = {
    'muscle building': {
        'beginner': {
            1: [
                {"name": "Dumbbell Bench Press", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Barbell Row", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Lat pull-down", "sets": 3, "reps": "10 reps", "rest": "90 sec"}
            ],
            2: [
                {"name": "Leg Press", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Seated Calf Raise", "sets": 3, "reps": "15 reps", "rest": "90 sec"},
                {"name": "Crunches", "sets": 3, "reps": "15 reps", "rest": "45 sec"}
            ],
            3: [
                {"name": "Incline Dumbbell Bench Press", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Dumbbell Row", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Dumbbell Lateral Raise", "sets": 3, "reps": "10 reps", "rest": "30-45 sec"}
            ],
            4: [
                {"name": "Barbell Squat", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Barbell Deadlift", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Hanging leg raise", "sets": 3, "reps": "15 reps", "rest": "45 sec"}
            ]
        },
        'intermediate': {
            1: [
                {"name": "Barbell back squat", "sets": 5, "reps": "5 reps", "rest": "1-2 min"},
                {"name": "Barbell Bench Press - Medium Grip", "sets": 5, "reps": "5 reps", "rest": "1-2 min"},
                {"name": "Barbell Row", "sets": 5, "reps": "5 reps", "rest": "1-2 min"}
            ],
            2: [
                {"name": "Barbell front squat", "sets": 5, "reps": "5 reps", "rest": "1-2 min"},
                {"name": "Seated barbell shoulder press", "sets": 5, "reps": "5 reps", "rest": "1-2 min"},
                {"name": "Barbell Deadlift", "sets": 5, "reps": "5 reps", "rest": "1-2 min"}
            ],
            3: [
                {"name": "Barbell Curl", "sets": 3, "reps": "8 reps", "rest": "30-45 sec"},
                {"name": "Seated triceps press", "sets": 3, "reps": "8 reps", "rest": "30-45 sec"},
                {"name": "Pull-up", "sets": 3, "reps": "8 reps", "rest": "30-45 sec"}
            ],
            4: [
                {"name": "Barbell Squat", "sets": 5, "reps": "5 reps", "rest": "1-2 min"},
                {"name": "Barbell Bench Press - Medium Grip", "sets": 5, "reps": "5 reps", "rest": "1-2 min"},
                {"name": "Barbell Row", "sets": 5, "reps": "5 reps", "rest": "1-2 min"}
            ]
        },
        'advanced': {
            1: [
                {"name": "Olympic Barbell Squat", "sets": 5, "reps": "5 reps", "rest": "90 sec"},
                {"name": "Bench Press - Powerlifting Style", "sets": 5, "reps": "5 reps", "rest": "90 sec"},
                {"name": "Pendlay Rows", "sets": 5, "reps": "5 reps", "rest": "90 sec"}
            ],
            2: [
                {"name": "Front Squat", "sets": 5, "reps": "5 reps", "rest": "1 min"},
                {"name": "Overhead Press", "sets": 5, "reps": "5 reps", "rest": "1 min"},
                {"name": "Deadlift", "sets": 5, "reps": "3 reps", "rest": "1-2 min"}
            ],
            3: [
                {"name": "Snatch Grip Deadlift", "sets": 5, "reps": "5 reps", "rest": "90 sec"},
                {"name": "Incline Bench Press", "sets": 5, "reps": "5 reps", "rest": "90 sec"},
                {"name": "T-Bar Row", "sets": 5, "reps": "5 reps", "rest": "90 sec"}
            ],
            4: [
                {"name": "Weighted Pull-ups", "sets": 5, "reps": "5 reps", "rest": "45 sec"},
                {"name": "Weighted Dips", "sets": 5, "reps": "5 reps", "rest": "45 sec"},
                {"name": "Muscle-ups", "sets": 3, "reps": "5 reps", "rest": "1 min"}
            ]
        }
    },
    'weight loss': {
        'beginner': {
            1: [
                {"name": "Dumbbell Goblet Squat", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Barbell or Kettlebell Deadlift", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Walking Lunge", "sets": 3, "reps": "20 reps (10 each side)", "rest": "60 sec"},
                {"name": "Leg Curl and Extension", "sets": 3, "reps": "12 reps", "rest": "60 sec", "optional": True}
            ],
            2: [
                {"name": "Low Intensity Cardio", "duration": "20 min"}
            ],
            3: [
                {"name": "Pullup or Lat Pulldown", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Dumbbell Overhead Press", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Dumbbell Row", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Dumbbell Bench Press", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Biceps Curl and Triceps Extension", "sets": 3, "reps": "12 reps", "rest": "60 sec", "optional": True}
            ],
            4: [
                {"name": "Low Intensity Cardio", "duration": "20 min"},
                {"name": "Interval Conditioning", "description": "3 rounds of 15 sec work and 15 sec rest for each exercise", "exercises": [
                    {"name": "Squat or Jump Squat"},
                    {"name": "Box Stepup or Power Stepup"},
                    {"name": "Alternating Lunge or Jumping Lunge"},
                    {"name": "Lateral Box Stepup or Ice Skater"},
                    {"name": "Burpee"}
                ]}
            ]
        },
        'intermediate': {
            1: [
                {"name": "Dumbbell Goblet Squat", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Barbell or Kettlebell Deadlift", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Walking Lunge", "sets": 3, "reps": "20 reps (10 each side)", "rest": "60 sec"},
                {"name": "Leg Curl and Extension", "sets": 3, "reps": "12 reps", "rest": "60 sec", "optional": True}
            ],
            2: [
                {"name": "Low Intensity Cardio", "duration": "25 min"}
            ],
            3: [
                {"name": "Pullup or Lat Pulldown", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Dumbbell Overhead Press", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Dumbbell Row", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Dumbbell Bench Press", "sets": 3, "reps": "12 reps", "rest": "60 sec"},
                {"name": "Biceps Curl and Triceps Extension", "sets": 3, "reps": "12 reps", "rest": "60 sec", "optional": True}
            ],
            4: [
                {"name": "Low Intensity Cardio", "duration": "25 min"},
                {"name": "Interval Conditioning", "description": "4 rounds of 15 sec work and 15 sec rest for each exercise", "exercises": [
                    {"name": "Squat or Jump Squat"},
                    {"name": "Box Stepup or Power Stepup"},
                    {"name": "Alternating Lunge or Jumping Lunge"},
                    {"name": "Lateral Box Stepup or Ice Skater"},
                    {"name": "Burpee"}
                ]}
            ]
        },
        'advanced': {
            1: [
                {"name": "Barbell Back Squat or Dumbbell Goblet Squat", "sets": 3, "reps": "8 reps", "rest": "60 sec"},
                {"name": "Barbell or Kettlebell Deadlift", "sets": 3, "reps": "8 reps", "rest": "60 sec"},
                {"name": "Walking Lunge", "sets": 3, "reps": "16 reps (8 each side)", "rest": "60 sec"},
                {"name": "Leg Curl and Extension", "sets": 3, "reps": "10 reps", "rest": "60 sec", "optional": True}
            ],
            2: [
                {"name": "Low Intensity Cardio", "duration": "30 min"}
            ],
            3: [
                {"name": "Pullup or Lat Pulldown", "sets": 3, "reps": "8 reps", "rest": "60 sec"},
                {"name": "Barbell or Dumbbell Overhead Press", "sets": 3, "reps": "8 reps", "rest": "60 sec"},
                {"name": "Barbell or Dumbbell Row", "sets": 3, "reps": "8 reps", "rest": "60 sec"},
                {"name": "Barbell or Dumbbell Bench Press", "sets": 3, "reps": "8 reps", "rest": "60 sec"},
                {"name": "Biceps Curl and Triceps Extension", "sets": 3, "reps": "10 reps", "rest": "60 sec", "optional": True}
            ],
            4: [
                {"name": "Low Intensity Cardio", "duration": "30 min"},
                {"name": "Interval Training/Conditioning", "description": "6 rounds of 15 sec work and 15 sec rest for each exercise", "exercises": [
                    {"name": "Squat or Jump Squat"},
                    {"name": "Box Stepup or Power Stepup"},
                    {"name": "Alternating Lunge or Jumping Lunge"},
                    {"name": "Lateral Box Stepup or Ice Skater"},
                    {"name": "Burpee"}
                ]}
            ]
            
        }
    },

    'gain weight' : {
        'beginner': {
            1: [
                {"name": "Bench Press", "sets": 5, "reps": "5 reps", "rest": "2 min"},
                {"name": "Triceps Dip", "sets": 3, "reps": "8 reps", "rest": "90 sec"},
                {"name": "Push-Up", "sets": 3, "reps": "10 reps", "rest": "60 sec"}
            ],
            2: [
                {"name": "Squat", "sets": 7, "reps": "5 reps", "rest": "2 min"},
                {"name": "Leg Press", "sets": 5, "reps": "10 reps", "rest": "2 min"},
                {"name": "Calf Raise", "sets": 5, "reps": "15 reps", "rest": "90 sec"},
                {"name": "Plank", "sets": 3, "reps": "30 sec hold", "rest": "60 sec"}
            ],
            3: [
                {"name": "Military Press", "sets": 5, "reps": "5 reps", "rest": "2 min"},
                {"name": "Shrug", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Lateral Raise", "sets": 3, "reps": "12 reps", "rest": "60 sec"}
            ],
            4: [
                {"name": "Pull-Up", "sets": 8, "reps": "As many as possible", "rest": "2 min"},
                {"name": "Barbell Row", "sets": 5, "reps": "5 reps", "rest": "2 min"},
                {"name": "Bicep Curl", "sets": 4, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Hanging Leg Raise", "sets": 4, "reps": "15 reps", "rest": "90 sec"}
            ],
        },
        'intermediate': {
            1: [
                {"name": "Incline Bench Press", "sets": 5, "reps": "5 reps", "rest": "2 min"},
                {"name": "Skull Crusher", "sets": 3, "reps": "8 reps", "rest": "90 sec"},
                {"name": "Chest Fly", "sets": 3, "reps": "10 reps", "rest": "60 sec"}
            ],
            2: [
                {"name": "Deadlift", "sets": 7, "reps": "5 reps", "rest": "2 min"},
                {"name": "Leg Curl", "sets": 5, "reps": "10 reps", "rest": "2 min"},
                {"name": "Seated Calf Raise", "sets": 5, "reps": "15 reps", "rest": "90 sec"},
                {"name": "Ab Wheel Rollout", "sets": 3, "reps": "10 reps", "rest": "60 sec"}
            ],
            3: [
                {"name": "Arnold Press", "sets": 5, "reps": "5 reps", "rest": "2 min"},
                {"name": "Face Pull", "sets": 3, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Front Raise", "sets": 3, "reps": "12 reps", "rest": "60 sec"}
            ],
            4: [
                {"name": "Lat Pulldown", "sets": 8, "reps": "5 reps", "rest": "2 min"},
                {"name": "T-Bar Row", "sets": 5, "reps": "5 reps", "rest": "2 min"},
                {"name": "Hammer Curl", "sets": 4, "reps": "10 reps", "rest": "90 sec"},
                {"name": "Cable Crunch", "sets": 4, "reps": "15 reps", "rest": "90 sec"}
            ],
        },
        'advanced': {
            1: [
                {"name": "Barbell Bench Press", "sets": 8, "reps": "3 reps", "rest": "3 min"},
                {"name": "Weighted Dip", "sets": 4, "reps": "6 reps", "rest": "2 min"},
                {"name": "Pec Deck Machine", "sets": 4, "reps": "8 reps", "rest": "90 sec"}
            ],
            2: [
                {"name": "Squat", "sets": 10, "reps": "3 reps", "rest": "3 min"},
                {"name": "Hack Squat", "sets": 5, "reps": "5 reps", "rest": "2 min"},
                {"name": "Standing Calf Raise", "sets": 5, "reps": "12 reps", "rest": "90 sec"},
                {"name": "Cable Woodchoppers", "sets": 3, "reps": "10 reps each side", "rest": "60 sec"}
            ],
            3: [
                {"name": "Overhead Press", "sets": 7, "reps": "3 reps", "rest": "3 min"},
                {"name": "Barbell Shrug", "sets": 4, "reps": "6 reps", "rest": "2 min"},
                {"name": "Reverse Fly", "sets": 4, "reps": "8 reps", "rest": "90 sec"}
            ],
            4: [
                {"name": "Close Grip Bench Press", "sets": 8, "reps": "3 reps", "rest": "3 min"},
                {"name": "EZ Bar Curl", "sets": 4, "reps": "6 reps", "rest": "2 min"},
                {"name": "Concentration Curl", "sets": 4, "reps": "8 reps", "rest": "90 sec"},
                {"name": "Roman Chair Sit-up", "sets": 4, "reps": "15 reps", "rest": "90 sec"}
            ],
        }
    },  
    'improve flexibility' : {
        'beginner': {
            1: [
                {"name": "Cat-Cow Stretch", "duration": "2 min", "description": "Gently increases flexibility in the spine."},
                {"name": "Seated Forward Bend", "duration": "2 min", "description": "Stretches the hamstrings and lower back."},
                {"name": "Knee to Chest Stretch", "duration": "1 min each side", "description": "Relieves tension in the lower back and stretches the hamstrings."}
            ],
            2: [
                {"name": "Butterfly Stretch", "duration": "2 min", "description": "Opens the hips and stretches the inner thighs."},
                {"name": "Neck Side Stretch", "duration": "1 min each side", "description": "Reduces neck stiffness and increases flexibility of the neck."},
                {"name": "Child’s Pose", "duration": "3 min", "description": "Relaxes the back while gently stretching the hips, thighs, and ankles."}
            ],
            3: [
                {"name": "Standing Quadriceps Stretch", "duration": "1 min each side", "description": "Stretches the front of the thigh and improves balance."},
                {"name": "Cobra Pose", "duration": "2 min", "description": "Strengthens the spine and stretches chest and abdomen."},
                {"name": "Seated Twist", "duration": "1 min each side", "description": "Increases spinal mobility and stretches the back."}
            ],
            4: [
                {"name": "Dynamic Leg Swings", "duration": "2 min each side", "description": "Improves dynamic flexibility and warms up the leg muscles."},
                {"name": "Sphinx Pose", "duration": "2 min", "description": "Gentle backbend that helps stretch the chest, shoulders, and abdomen."},
                {"name": "Ankle Stretch", "duration": "1 min each side", "description": "Improves flexibility in the ankles, aiding in overall balance and mobility."}
            ]
        },
        'intermediate': {
            1: [
                {"name": "Pigeon Pose", "duration": "2 min each side", "description": "Excellent for opening the hips and stretching the hip flexors and lower back."},
                {"name": "Standing Forward Fold", "duration": "2 min", "description": "Stretches the hamstrings and calves and relaxes the spine."},
                {"name": "Camel Pose", "duration": "1 min", "description": "Opens up the front body, stretches the chest and improves spinal flexibility."}
            ],
            2: [
                {"name": "Lizard Pose", "duration": "2 min each side", "description": "Deeply stretches the hip flexors, hamstrings, and quadriceps."},
                {"name": "Extended Triangle Pose", "duration": "1 min each side", "description": "Stretches and opens the legs, groin, and hips, and strengthens the shoulders."},
                {"name": "Reverse Prayer Pose", "duration": "2 min", "description": "Improves flexibility in shoulders and upper back."}
            ],
            3: [
                {"name": "Deep Squat", "duration": "3 min", "description": "Improves flexibility in the hips, ankles, and lower back."},
                {"name": "Bridge Pose", "duration": "2 min", "description": "Stretches the chest, neck, and spine."},
                {"name": "Half Lord of the Fishes Pose", "duration": "1 min each side", "description": "Increases flexibility and elasticity of the spine and hips."}
            ],
            4: [
                {"name": "Warrior III Pose", "duration": "1 min each side", "description": "Improves balance and stability while stretching the legs and hips."},
                {"name": "Bow Pose", "duration": "1 min", "description": "Stretches the entire front of the body and strengthens the back muscles."},
                {"name": "Standing Hip Flexor Stretch", "duration": "2 min each side", "description": "Targets the hip flexors and helps improve flexibility in the hip region."}
            ]
        },
        'advanced': {
            1: [
                {"name": "King Pigeon Pose", "duration": "2 min each side", "description": "Advanced hip opener that also stretches the thighs, glutes, and psoas."},
                {"name": "Full Wheel Pose", "duration": "1 min", "description": "Deeply stretches the front of the body and strengthens the arms and legs."},
                {"name": "Standing Split", "duration": "1 min each side", "description": "Challenges balance and stretches the hamstrings and calves."}
            ],
            2: [
                {"name": "Monkey Pose", "duration": "2 min each side", "description": "Stretches the hamstrings and opens hip flexors."},
                {"name": "Advanced Camel Pose", "duration": "1.5 min", "description": "Deepens the camel pose stretch for the chest and front of the body."},
                {"name": "Arm Balance Scorpion", "duration": "1 min", "description": "Improves balance and flexibility in the back and shoulders."}
            ],
            3: [
                {"name": "Lotus Pose", "duration": "3 min", "description": "Calms the brain, stimulates the pelvis, spine, abdomen, and bladder, stretches the ankles and knees."},
                {"name": "Bound Lotus Pose", "duration": "2 min each side", "description": "Deep stretch for the entire lower body and helps improve focus."},
                {"name": "Gravity Pose", "duration": "3 min", "description": "Deep relaxation and stretch for the hips and lower back."}
            ],
            4: [
                {"name": "Advanced Prasarita Padottanasana", "duration": "2 min", "description": "Deep stretch for the legs and improves overall balance and flexibility."},
                {"name": "Yoga Nidrasana", "duration": "1 min", "description": "Challenges flexibility in legs and hips, often called the 'sleeping yogi pose'."},
                {"name": "Eight Angle Pose", "duration": "1 min", "description": "Advanced arm balance that enhances strength and flexibility in the arms and core."}
            ]
        }
    },

    'increase endurance/stamina' : {
        'beginner': {
            1: [
                {"name": "Brisk Walking", "duration": "30 min", "description": "Maintain a brisk pace to elevate heart rate moderately."},
                {"name": "Light Jogging", "duration": "10 min", "description": "A gentle jog to start building cardiovascular capacity."}
            ],
            2: [
                {"name": "Cycling", "duration": "20 min", "description": "Stationary or outdoor cycling at a steady, moderate pace."},
                {"name": "Dynamic Stretches", "duration": "10 min", "description": "Prepare muscles and joints for increased activity."}
            ],
            3: [
                {"name": "Swimming", "duration": "20 min", "description": "Freestyle or breaststroke swimming to improve cardiovascular endurance."},
                {"name": "Aqua Jogging", "duration": "10 min", "description": "Low impact jogging in the water to build stamina with minimal joint strain."}
            ],
            4: [
                {"name": "HIIT", "duration": "20 min", "description": "High-Intensity Interval Training with alternating sprinting and walking intervals of 30 seconds each."},
                {"name": "Cool Down", "duration": "10 min", "description": "Slow walking and stretching to aid recovery."}
            ]
        },
        'intermediate': {
            1: [
                {"name": "Jogging", "duration": "30 min", "description": "Maintain a steady jogging pace to improve cardiovascular health."},
                {"name": "Hill Sprints", "duration": "15 min", "description": "Short bursts up a moderate incline to build power and endurance."}
            ],
            2: [
                {"name": "Cycling", "duration": "40 min", "description": "Moderate to high-intensity cycling, including some uphill."},
                {"name": "Core Workouts", "duration": "15 min", "description": "Core strengthening exercises to support cycling posture and endurance."}
            ],
            3: [
                {"name": "Swimming Intervals", "duration": "30 min", "description": "Swim laps with interval sprinting every third lap."},
                {"name": "Pool Drills", "duration": "15 min", "description": "Use paddles and kickboards for specific stroke improvement and endurance."}
            ],
            4: [
                {"name": "HIIT", "duration": "30 min", "description": "Structured HIIT session with 1 min high intensity followed by 1 min of rest, repeated."},
                {"name": "Stretching", "duration": "10 min", "description": "Focus on flexibility to enhance muscle recovery and performance."}
            ]
        },
        'advanced': {
            1: [
                {"name": "Long Distance Running", "duration": "60 min", "description": "Extended running at a challenging pace to increase stamina."},
                {"name": "Speed Work", "duration": "20 min", "description": "Fartlek training for speed and endurance integration."}
            ],
            2: [
                {"name": "Cycling", "duration": "60 min", "description": "Long-distance cycling with intervals of high intensity."},
                {"name": "Strength Training", "duration": "20 min", "description": "Leg and core strength exercises to support long cycling sessions."}
            ],
            3: [
                {"name": "Competitive Swimming", "duration": "45 min", "description": "Structured swimming practice focusing on speed and endurance."},
                {"name": "Technique Drills", "duration": "15 min", "description": "Technical swimming drills to improve efficiency and stamina."}
            ],
            4: [
                {"name": "Advanced HIIT", "duration": "40 min", "description": "Advanced interval training with minimal rest periods between intense efforts."},
                {"name": "Active Recovery", "duration": "20 min", "description": "Low intensity activity focusing on recovery and flexibility."}
            ]
        }
    },
    'gain strength': {
        'beginner': {
            1: [
                {"name": "Squat", "sets": 3, "reps": "8 reps", "rest": "2 min", "description": "Focus on form and technique to build a foundation for strength."},
                {"name": "Bench Press", "sets": 3, "reps": "8 reps", "rest": "2 min", "description": "Standard bench press for chest and arm strength."},
            ],
            2: [
                {"name": "Deadlift", "sets": 3, "reps": "8 reps", "rest": "2 min", "description": "Fundamental lifting exercise that targets overall body strength."},
                {"name": "Pull-ups", "sets": 3, "reps": "As many as possible", "rest": "2 min", "description": "Enhances upper body strength, especially in the back and biceps."}
            ],
            3: [
                {"name": "Leg Press", "sets": 3, "reps": "10 reps", "rest": "2 min", "description": "Strengthens the quadriceps, hamstrings, and glutes."},
                {"name": "Military Press", "sets": 3, "reps": "8 reps", "rest": "2 min", "description": "Develops shoulder strength and stability."},
            ],
            4: [
                {"name": "Barbell Row", "sets": 3, "reps": "8 reps", "rest": "2 min", "description": "Strengthens the back, shoulders, and biceps."},
                {"name": "Dips", "sets": 3, "reps": "10 reps", "rest": "2 min", "description": "Targets the triceps and chest for increased upper body strength."}
            ]
        },
        'intermediate': {
            1: [
                {"name": "Front Squat", "sets": 4, "reps": "6 reps", "rest": "2 min", "description": "Increases core and quad strength with a focus on stability."},
                {"name": "Incline Bench Press", "sets": 4, "reps": "6 reps", "rest": "2 min", "description": "Targets the upper portion of the chest and shoulders."},
            ],
            2: [
                {"name": "Sumo Deadlift", "sets": 4, "reps": "6 reps", "rest": "2 min", "description": "Focuses more on the legs and hips than the conventional deadlift."},
                {"name": "Weighted Pull-ups", "sets": 4, "reps": "6 reps", "rest": "2 min", "description": "Enhances upper body strength with added resistance."}
            ],
            3: [
                {"name": "Romanian Deadlift", "sets": 4, "reps": "6 reps", "rest": "2 min", "description": "Strengthens the hamstrings and lower back."},
                {"name": "Push Press", "sets": 4, "reps": "6 reps", "rest": "2 min", "description": "Combines the overhead press with a slight leg drive for more power."},
            ],
            4: [
                {"name": "Pendlay Row", "sets": 4, "reps": "6 reps", "rest": "2 min", "description": "Strengthens the entire back with a focus on explosiveness."},
                {"name": "Skull Crushers", "sets": 4, "reps": "8 reps", "rest": "2 min", "description": "Isolates the triceps for enhanced arm strength."}
            ]
        },
        'advanced': {
            1: [
                {"name": "Back Squat", "sets": 5, "reps": "5 reps", "rest": "3 min", "description": "Heavy squatting for maximal leg and core strength."},
                {"name": "Close-Grip Bench Press", "sets": 5, "reps": "5 reps", "rest": "3 min", "description": "Focuses on triceps strength and chest."},
            ],
            2: [
                {"name": "Deficit Deadlift", "sets": 5, "reps": "5 reps", "rest": "3 min", "description": "Increases the range of motion for improved strength from the floor."},
                {"name": "Weighted Chin-ups", "sets": 5, "reps": "5 reps", "rest": "3 min", "description": "Builds superior upper body strength with additional weight."},
            ],
            3: [
                {"name": "Hack Squat", "sets": 5, "reps": "5 reps", "rest": "3 min", "description": "Targets the quadriceps for powerful leg strength."},
                {"name": "Arnold Press", "sets": 5, "reps": "5 reps", "rest": "3 min", "description": "Comprehensive shoulder workout that also engages upper chest and back."},
            ],
            4: [
                {"name": "T-Bar Row", "sets": 5, "reps": "5 reps", "rest": "3 min", "description": "Focuses on middle back strength."},
                {"name": "Dumbbell Flyes", "sets": 5, "reps": "5 reps", "rest": "3 min", "description": "Isolates the chest muscles for development and strength."}
            ]
        }
    },
    'mental wellness' : {
        'beginner': {
            1: [
                {"name": "Gentle Yoga", "duration": "30 min", "description": "Simple yoga poses that focus on slow movements and deep breathing to reduce stress."},
                {"name": "Guided Meditation", "duration": "10 min", "description": "A guided session to introduce meditation techniques for calming the mind."},
            ],
            2: [
                {"name": "Basic Tai Chi", "duration": "30 min", "description": "Tai chi movements focusing on fluid, gentle motions to improve balance and calm."},
                {"name": "Progressive Muscle Relaxation", "duration": "10 min", "description": "Techniques to relax each muscle group sequentially to relieve stress."},
            ],
            3: [
                {"name": "Breathing Exercises", "duration": "20 min", "description": "Practices that focus on controlled breathing to enhance relaxation and mental focus."},
                {"name": "Nature Walk", "duration": "20 min", "description": "A gentle walk in a natural setting to help clear the mind and improve mood."},
            ],
            4: [
                {"name": "Restorative Yoga", "duration": "30 min", "description": "Yoga poses held for longer periods to aid in relaxation and stress relief."},
                {"name": "Mindfulness Meditation", "duration": "10 min", "description": "Meditation practice focusing on being present and mindful of the current moment."},
            ]
        },
        'intermediate': {
            1: [
                {"name": "Hatha Yoga", "duration": "45 min", "description": "A moderate yoga class that balances physical exercise with mental meditation."},
                {"name": "Deep Breathing Techniques", "duration": "15 min", "description": "Advanced breathing methods to control stress and improve lung capacity."},
            ],
            2: [
                {"name": "Intermediate Tai Chi", "duration": "45 min", "description": "More dynamic tai chi forms that help improve mental and physical coordination."},
                {"name": "Autogenic Training", "duration": "15 min", "description": "A relaxation technique that involves visualizing calm and peace to reduce stress."},
            ],
            3: [
                {"name": "Outdoor Meditation", "duration": "30 min", "description": "Meditation practices performed outdoors to connect with nature and enhance peace."},
                {"name": "Reflective Journaling", "duration": "15 min", "description": "Writing thoughts and feelings to explore emotional patterns and foster relaxation."},
            ],
            4: [
                {"name": "Power Yoga", "duration": "45 min", "description": "A vigorous yoga workout that improves strength, flexibility, and mental focus."},
                {"name": "Guided Visualization", "duration": "15 min", "description": "A mental exercise to visualize positive images and scenarios, promoting relaxation."},
            ]
        },
        'advanced': {
            1: [
                {"name": "Ashtanga Yoga", "duration": "60 min", "description": "An intense yoga practice that improves physical strength, flexibility, and mental focus."},
                {"name": "Zen Meditation", "duration": "20 min", "description": "A practice of 'sitting meditation' that emphasizes alertness and presence of mind."},
            ],
            2: [
                {"name": "Advanced Tai Chi", "duration": "60 min", "description": "Complex tai chi sequences that challenge the body while calming the mind."},
                {"name": "Biofeedback", "duration": "20 min", "description": "Using sensors to monitor physiological activities to teach control over the body’s responses to stress."},
            ],
            3: [
                {"name": "Dynamic Meditation", "duration": "45 min", "description": "A unique form of meditation that includes physical activity to release energy and stress."},
                {"name": "Yoga Nidra", "duration": "20 min", "description": "A form of guided relaxation that simulates deep sleep while maintaining consciousness."},
            ],
            4: [
                {"name": "Kundalini Yoga", "duration": "60 min", "description": "Focuses on awakening energy centers in the body through dynamic poses, breathing, and meditation."},
                {"name": "Silent Retreat", "duration": "20 min", "description": "A period of silence to deepen focus, self-awareness, and inner peace."},
            ]
        }

    },

    'senior/olders fittness' : {
        'beginner': {
            1: [
                {"name": "Chair Yoga", "duration": "30 min", "description": "Yoga exercises performed with the aid of a chair to improve flexibility and balance."},
                {"name": "Walking", "duration": "15 min", "description": "Light walking to maintain cardiovascular health and mobility."},
            ],
            2: [
                {"name": "Water Aerobics", "duration": "30 min", "description": "Gentle aerobic exercises in a pool to reduce stress on joints while improving endurance."},
                {"name": "Stretching", "duration": "15 min", "description": "Basic stretches to improve flexibility and reduce muscle stiffness."},
            ],
            3: [
                {"name": "Balance Exercises", "duration": "20 min", "description": "Simple balance exercises such as standing on one foot or walking heel to toe to improve stability."},
                {"name": "Light Dumbbell Work", "duration": "20 min", "description": "Using light weights to enhance muscle tone and support joint health."},
            ],
            4: [
                {"name": "Tai Chi", "duration": "30 min", "description": "Gentle martial arts movements focusing on fluid motions and balance."},
                {"name": "Meditation", "duration": "15 min", "description": "Guided meditation to enhance mental wellness and reduce stress."},
            ]
        },
        'intermediate': {
            1: [
                {"name": "Pilates", "duration": "30 min", "description": "Moderate-intensity Pilates to strengthen the core and improve flexibility."},
                {"name": "Brisk Walking", "duration": "20 min", "description": "Slightly vigorous walking to enhance cardiovascular fitness and stamina."},
            ],
            2: [
                {"name": "Resistance Band Exercises", "duration": "30 min", "description": "Exercises using resistance bands to build strength and improve muscle function without heavy weights."},
                {"name": "Dynamic Stretching", "duration": "15 min", "description": "Engaging in active movements to stretch and warm up the muscles."},
            ],
            3: [
                {"name": "Group Exercise Classes", "duration": "30 min", "description": "Participating in group classes such as Zumba Gold designed for seniors to keep fitness fun and engaging."},
                {"name": "Cycling on a Stationary Bike", "duration": "20 min", "description": "Using a stationary bike to build leg strength and promote heart health."},
            ],
            4: [
                {"name": "Advanced Tai Chi", "duration": "30 min", "description": "More complex Tai Chi routines to challenge balance and mental focus."},
                {"name": "Relaxation Exercises", "duration": "15 min", "description": "Practices such as deep breathing to relax the body and mind."},
            ]
        },
        'advanced': {
            1: [
                {"name": "Strength Training", "duration": "30 min", "description": "Engaging in more challenging strength training with appropriate weights to enhance muscle mass and bone density."},
                {"name": "Power Walking", "duration": "20 min", "description": "Fast-paced walking to boost heart rate and improve overall fitness."},
            ],
            2: [
                {"name": "Yoga", "duration": "30 min", "description": "Practicing more advanced yoga poses to improve flexibility and core strength."},
                {"name": "Functional Training", "duration": "20 min", "description": "Exercises that mimic daily activities to improve functional movement and reduce the risk of falls."},
            ],
            3: [
                {"name": "Circuit Training", "duration": "30 min", "description": "A circuit of various exercises targeting all major muscle groups with minimal rest between exercises."},
                {"name": "Agility Drills", "duration": "20 min", "description": "Simple agility exercises to maintain quickness and flexibility."},
            ],
            4: [
                {"name": "Competitive Sports", "duration": "30 min", "description": "Participation in senior competitive sports like tennis or swimming to keep physically and socially active."},
                {"name": "Deep Meditation", "duration": "20 min", "description": "Longer sessions of meditation to foster deep relaxation and mental clarity."},
            ]
        }

    },

    'weight maintenance' : {
        'beginner': {
            1: [
                {"name": "Moderate Cardio", "duration": "30 min", "description": "Activities like brisk walking or light jogging to burn calories effectively."},
                {"name": "Basic Strength Training", "duration": "20 min", "description": "Simple weight lifting exercises using body weight or light dumbbells to maintain muscle mass."},
            ],
            2: [
                {"name": "Cycling", "duration": "30 min", "description": "Stationary or outdoor cycling at a moderate pace to help with calorie burn."},
                {"name": "Yoga", "duration": "20 min", "description": "Gentle yoga session to improve flexibility and relieve stress."},
            ],
            3: [
                {"name": "Swimming", "duration": "30 min", "description": "Low-impact exercise that provides good cardiovascular benefits and calorie burn."},
                {"name": "Core Exercises", "duration": "20 min", "description": "Focus on strengthening the abdominal and lower back muscles."},
            ],
            4: [
                {"name": "Dance Aerobics", "duration": "30 min", "description": "A fun way to maintain cardiovascular health and manage weight."},
                {"name": "Stretching", "duration": "20 min", "description": "Stretching session to improve overall flexibility and prevent injuries."},
            ]
        },
        'intermediate': {
            1: [
                {"name": "Interval Running", "duration": "30 min", "description": "Running with intervals of sprinting and jogging to increase calorie burn."},
                {"name": "Circuit Training", "duration": "30 min", "description": "A series of strength exercises performed one after another with minimal rest."},
            ],
            2: [
                {"name": "Spin Class", "duration": "45 min", "description": "High-intensity cycling class for endurance and calorie burning."},
                {"name": "Pilates", "duration": "30 min", "description": "Enhances core strength and improves postural alignment."},
            ],
            3: [
                {"name": "Hiking", "duration": "60 min", "description": "Engaging in a moderate to strenuous hike to burn calories and enjoy nature."},
                {"name": "Bodyweight Exercises", "duration": "30 min", "description": "Using body weight for resistance training to maintain muscle mass."},
            ],
            4: [
                {"name": "Kickboxing", "duration": "45 min", "description": "A high-energy workout to improve strength, fitness, and agility."},
                {"name": "Active Stretching", "duration": "15 min", "description": "Dynamic stretches to improve mobility and muscle function."},
            ]
        },
        'advanced': {
            1: [
                {"name": "CrossFit", "duration": "60 min", "description": "High-intensity training program that improves strength and conditioning."},
                {"name": "Heavy Strength Training", "duration": "45 min", "description": "Heavy lifting session focusing on all major muscle groups."},
            ],
            2: [
                {"name": "Long-Distance Running", "duration": "60 min", "description": "Running at a steady pace to increase stamina and calorie expenditure."},
                {"name": "Advanced Yoga", "duration": "45 min", "description": "Complex poses that challenge flexibility, strength, and balance."},
            ],
            3: [
                {"name": "Competitive Sports", "duration": "90 min", "description": "Participation in sports like basketball, soccer, or tennis for overall fitness."},
                {"name": "Functional Training", "duration": "30 min", "description": "Exercises that mimic everyday activities to improve body mechanics."},
            ],
            4: [
                {"name": "Triathlon Training", "duration": "120 min", "description": "Combining swimming, cycling, and running for ultimate fitness maintenance."},
                {"name": "Recovery Techniques", "duration": "30 min", "description": "Practices like foam rolling and deep tissue massage to aid in recovery."},
            ]
        }

    },
}



# Define functions to handle user input, workout generation, and feedback
def get_user_input():
    user_id = input("Enter your User ID: ")
    level = input("Enter your fitness level (beginner, intermediate, advanced): ").lower()
    goal = input("Enter your goal (muscle building, weight loss, gain weight, improve flexibility, increase endurance/stamina, gain strength, senior/olders fitness, mental wellness, weight maintenance): ").lower()
    return user_id, level, goal

def generate_workout_plan(level, goal):
    # Validate user input and select the appropriate workout
    if goal in workouts and level in workouts[goal]:
        selected_workout = workouts[goal][level]
        plan = {}
        for week in range(1, 5):  # Assume there are 4 weeks defined
            plan[week] = selected_workout.get(week, [])
        return plan
    else:
        raise ValueError("Invalid goal or fitness level")

def display_workout_plan(plan):
    for week, exercises in plan.items():
        print(f"Week {week}:")
        for ex in exercises:
            if 'sets' in ex:
                print(f"  - {ex['name']}: {ex['sets']} sets of {ex['reps']} reps, rest {ex['rest']}")
            elif 'duration' in ex:  # Check if the exercise has a 'duration' key
                print(f"  - {ex['name']}: {ex['duration']} duration")  # Display the duration if present
            if 'optional' in ex:
                print("    *Optional exercise")
            if 'exercises' in ex:
                print("    Interval Conditioning:")
                for interval_ex in ex['exercises']:
                    print(f"      - {interval_ex['name']}")
                print(f"      {ex['description']}")

def get_feedback():
    feedback = input("Was the workout too hard, too easy, or just right? (Enter 'hard', 'easy', or 'just right'): ").lower()
    return feedback

# Main function to run the program
def main():
    try:
        while True:
            user_id, level, goal = get_user_input()
            plan = generate_workout_plan(level, goal)
            display_workout_plan(plan)
            feedback = get_feedback()
            print("Thank you for your feedback!")
            option = input("Do you want to generate another workout plan? (yes/no): ").lower()
            if option != 'yes':
                break
    except Exception as e:
        print(str(e))

# Execute the program
main()