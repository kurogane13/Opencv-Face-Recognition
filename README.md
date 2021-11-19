# Opencv-Face-Recognition
Opencv face recognition desktop application

-----------------------------------------------------------------------------------------------------------------

Program developed by Gustavo Wydler Azuaga - 2021-11-19
-----------------------------------------------------------------------------------------------------------------

Screenshots of the program are saved in the Screenshot folder in this repo, for you to view.
-----------------------------------------------------------------------------------------------------------------

Functionality and purpose of the program.

This program is a python desktop application developed initially as a test software, to create new identity instances, and use opencv and a camera to identify the saved identities.

----------------------------------------------------------------------------------------------------------

How the program works:

When being launched, you will have simple easygui desktop application containing 2 buttons. A "Create New Identity" Button, and a "Start Face Recognition" button. 

To first run the camera, you will need to at least create ONE identity, by pressing the "Create New Identity" button. Uppon pressing the button you will have a new screen with 2 fields, "New identity/Person Name:" and ID/Document number:.

The first field (New identity/Person Name:) will take a string value, which is the object of the person name or full name.
The second field will take only integers. Minimum amount of integers is 7, and maximum is 8.

After completing correctly the 2 fields, and clicking OK, the camera will start, and in the console you will see a message, stating to press "s" key from the keyboard, to take a snapshot of the person to be identified. Once you press "s", and the the image stalls for a second, and the camera turns off, you will be presented with a window containing the taken snapshot of the new identity instance, with name, document, and complete date format, together with the data recorded

The data saved will be peristed in a pickle file called ref_name.pkl, together with a unique id, generated for the specific mame identity recorded. Erasing the ref_name.pkl, will result in removing all saved idenitities. The snapshots will remain in the path were the program was launched at that time.

-----------------------------------------------------------------------------------------------------------

How to run run and use the program:

Install the following libraries:

- import os
- import sys
- import easygui
- from easygui import *
- import face_recognition
- from face_recognition import *
- import cv2
- import numpy as np
- import glob
- import pickle
- import os
- import random
- import json
- import pandas as pd
- import datetime
- from datetime import datetime

Copy all the contents in the repo, to your /home/$USER folder, and run using python3.x face_recognition_gui.py


