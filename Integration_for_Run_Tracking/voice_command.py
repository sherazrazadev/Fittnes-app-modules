import speech_recognition as sr

def listen(retry_count=3, timeout=1, phrase_time_limit=3):
    if retry_count == 0:
        print("Failed after several attempts.")
        return None

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Helps to calibrate the recognizer sensitivity to ambient noise
        print("Listening...")
        try:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = r.recognize_google(audio)
            print('You said:', text)

            # Handling a specific command such as "stop"
            if text.lower() == "stop":
                print("Stopping as requested.")
                return None

            return text
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio, please try again")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except Exception as e:
            print("An error occurred: {}".format(e))

    return listen(retry_count - 1)  # Retry recursively

listen()  # Start the listening function
