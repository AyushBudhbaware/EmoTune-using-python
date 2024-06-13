import cv2
from deepface import DeepFace
import pygame
import os

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize pygame mixer
pygame.mixer.init()

# Path to pygame example sounds
pygame.examples_path = os.path.join(os.path.dirname(pygame.__file__), 'examples/data')

# Emotion to music mapping (using Pygame example sounds)
emotion_to_music = {
    'happy': os.path.join(pygame.examples_path, 'house_lo.wav'),
    'sad': os.path.join(pygame.examples_path, 'moon_lo.wav'),
    'angry': os.path.join(pygame.examples_path, 'moog_lo.wav'),
    'neutral': os.path.join(pygame.examples_path, 'drums.wav')
}

# Start capturing video
cap = cv2.VideoCapture(0)

# Initialize current emotion
current_emotion = 'neutral'

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale frame to RGB format
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = rgb_frame[y:y + h, x:x + w]

        # Perform emotion analysis on the face ROI
        result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

        # Determine the dominant emotion
        emotion = result[0]['dominant_emotion']
        print(f"Detected emotion: {emotion}")

        # Change music based on detected emotion (if different)
        if emotion != current_emotion:
            current_emotion = emotion
            music_file = emotion_to_music.get(emotion, emotion_to_music['neutral'])  # Default to neutral tone
            print(f"Loading music file: {music_file}")

            if os.path.exists(music_file):
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play(loops=-1)  # Play looped indefinitely
            else:
                print(f"Music file '{music_file}' not found in directory '{pygame.examples_path}'.")

        # Draw rectangle around face and label with predicted emotion
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Facial Expression-Based Music Player', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
