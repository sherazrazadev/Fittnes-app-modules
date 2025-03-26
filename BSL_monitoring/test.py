import csv
import datetime
import speech_recognition as sr
import csv
import datetime
import spacy

def extract_bsl(text):
    # Load the English NER model from spaCy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Extract entities with label "CARDINAL" (numerical values)
    bsl_values = [ent.text for ent in doc.ents if ent.label_ == "CARDINAL"]

    # Return the first extracted numerical value as blood sugar level
    if bsl_values:
        return float(bsl_values[0])
    else:
        return None

def get_bsl_input():
    while True:
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak your blood sugar level (BSL):")
                audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            bsl = extract_bsl(text)
            if bsl is not None:
                return bsl
            else:
                print("No blood sugar level detected in the input. Please try again.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your speech.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except ValueError:
            print("Invalid input. Please speak a numeric value.")

# Remaining code remains the same
def categorize_bsl(bsl):
    if bsl < 70:
        return 'Low'
    elif bsl >= 140:
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
    filename = 'bsl.csv'
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Timestamp', 'BSL', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, if yes, write header
        if csvfile.tell() == 0:
            writer.writeheader()

        # Get BSL input from the user 5 times a day
        for _ in range(5):
            bsl = get_bsl_input()
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            BSL_status = categorize_bsl(bsl)

            writer.writerow({'Timestamp': timestamp, 'BSL': bsl, 'Status': BSL_status})
            print("Data recorded successfully.")
            provide_recommendations(bsl, BSL_status)

if __name__ == "__main__":
    main()
