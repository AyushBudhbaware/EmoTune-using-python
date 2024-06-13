# Emotion_recognition-using-python
This Python script uses OpenCV and DeepFace to detect emotions in real-time from a webcam and plays corresponding background music using Pygame.

Requirements

Python 3.x
OpenCV
DeepFace
Pygame
Installation

You can install the required libraries using pip:

pip install opencv-python deepface pygame
Use code with caution.
content_copy
Usage

Save the script as emotion_music_player.py.
Run the script from your terminal:
Bash
python emotion_music_player.py
Use code with caution.
content_copy
The script will start capturing video from your webcam and play music based on your detected emotions.
Press 'q' to quit the program.
Explanation

The script first imports the necessary libraries: OpenCV, DeepFace, Pygame, and os.
It then loads the pre-trained Haar cascade classifier for face detection.
Pygame mixer is initialized for playing audio files.
A dictionary maps emotions to corresponding sound effects included in the Pygame examples directory.
The script starts capturing video from the webcam.
In a loop, it:
Captures a frame from the webcam.
Converts the frame to grayscale for face detection.
Detects faces in the grayscale frame.
For each detected face:
Extracts the face region of interest (ROI).
Uses DeepFace to analyze the emotion in the face ROI.
Determines the dominant emotion.
Updates the current emotion and plays the corresponding music file using Pygame, if it exists.
Draws a rectangle around the detected face and displays the predicted emotion on the frame.
Finally, the script displays the frame and waits for the 'q' key to be pressed to quit.
Note

This script uses pre-defined sound effects for different emotions. You can modify the emotion_to_music dictionary to use your own music files.
The script relies on the Pygame example sounds being available in the default location. Make sure you have Pygame installed correctly.
