import random
import csv
import datetime
import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def recognize_speech(prompt):
    # Placeholder function to simulate speech recognition
    # In a real application, this function would capture audio and use a speech recognition library
    return input(prompt)

def extract_numeric_value(text):
    # Process the text with spaCy
    doc = nlp(text)
    # Extract numeric values
    numeric_values = [token.text for token in doc if token.like_num]
    if numeric_values:
        # Return the first numeric value found
        return float(numeric_values[0])
    else:
        return None

def get_bsl_input():
    while True:
        bsl_text = recognize_speech("Please say your blood sugar level (BSL): ")
        bsl = extract_numeric_value(bsl_text)
        if bsl is not None:
            return bsl
        else:
            print("Could not recognize a numeric value. Please try again.")

def get_heart_rate_input():
    while True:
        heart_rate_text = recognize_speech("Please say your heart rate: ")
        heart_rate = extract_numeric_value(heart_rate_text)
        if heart_rate is not None:
            return heart_rate
        else:
            print("Could not recognize a numeric value. Please try again.")

def get_bp_input():
    while True:
        bp_text = recognize_speech("Please say your blood pressure (in the format systolic over diastolic, e.g., 120 over 80): ")
        bp_values = bp_text.split(' over ')
        systolic = extract_numeric_value(bp_values[0])
        diastolic = extract_numeric_value(bp_values[1])
        if systolic is not None and diastolic is not None:
            return systolic, diastolic
        else:
            print("Could not recognize numeric values for systolic and diastolic pressure. Please try again.")

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
