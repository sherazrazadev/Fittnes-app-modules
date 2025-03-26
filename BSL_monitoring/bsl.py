import random
import csv
import datetime
#get blood sugar/glucose level like 120,100...
def get_bsl_input():
    while True:
        try:
            bsl = float(input("Enter your blood sugar level (BSL): "))
            return bsl
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
#get heart rate in integer like 80,70,90...
def get_heart_rate_input():
    while True:
        try:
            heart_rate = float(input("Enter your heart_rate : "))
            return heart_rate
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
#get blood pressure systolic and diastolic like 120/80
def get_bp_input():
    while True:
        try:
            bp = input("Enter your blood pressure (in the format systolic/diastolic, e.g., 120/80): ")
            systolic, diastolic = map(int, bp.split('/'))
            return systolic, diastolic
        except ValueError:
            print("Invalid input. Please enter the blood pressure in the correct format.")


def categorize_bsl(bsl):
    if bsl < 70:
        return 'Low'
    elif bsl >= 140:
        return 'High'
    else:
        return 'Normal'
    
def categorize_heart_rate(heart_rate):
    if heart_rate < 60:
        return 'Low'
    elif heart_rate >= 100:
        return 'High'
    else:
        return 'Normal'

def categorize_bp(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return 'Low'
    elif systolic >= 140 or diastolic >= 90:
        return 'High'
    else:
        return 'Normal'

def provide_recommendations(bsl, status):
    if status == 'Low':
        print("Your blood sugar level is low.")
        print("Recommendation: Eat a small snack with carbohydrates, such as a piece of fruit or crackers, to raise your blood sugar level.")
    elif status == 'High':
        print("Your blood sugar level is high.")
        print("Recommendation: Engage in physical activity such as walking or jogging, and avoid high-carbohydrate foods. Instead, opt for leafy greens and lean proteins.")
    else:
        print("Your blood sugar level is within the normal range.")

def main():
    # Generate a random file name for the BSL data
    filename = 'data1.csv'
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Timestamp', 'BSL', 'Status', 'Heart Rate' ,'H-R Status','Systolic BP', 'Diastolic BP', 'BP Status' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, if yes, write header
        if csvfile.tell() == 0:
            writer.writeheader()

        # Get BSL input from the user 5 times a day
        for _ in range(5):
            bsl = get_bsl_input()
            heart_rate = get_heart_rate_input()
            systolic, diastolic = get_bp_input()
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            BSL_status = categorize_bsl(bsl)
            heart_rate_status =categorize_heart_rate(heart_rate)
            bp_status = categorize_bp(systolic, diastolic)

            writer.writerow({'Timestamp': timestamp, 'BSL': bsl,'Status': BSL_status,
                             'Heart Rate': heart_rate ,'H-R Status' : heart_rate_status,
                             'Systolic BP': systolic, 'Diastolic BP': diastolic, 'BP Status': bp_status})
            print("Data recorded successfully.")
            provide_recommendations(bsl, BSL_status)

if __name__ == "__main__":
    main()