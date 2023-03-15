# C2-Week06
## Cat Face Detection and Cutting
This program detects and cuts the faces of cats in images using OpenCV. It uses the haarcascade_frontalcatface_extended.xml file for the Cascade Classifier and cat_test_7.jpg file for testing purposes.

### Installation
To run this program, the following libraries should be installed:  
math, os, cv2

### Usage
To run the program, execute the `load()` function in the Python interpreter or run the program in a Python IDE. The program will ask for the breed of the cats that you want to detect and cut. The images should be located in the `datasets/<breed>/original` folder. The program will then create a new folder called `datasets/<breed>/faces` to save the cut faces.

## Functions
`detect(filename)`
This function takes a filename as input and detects the cat's face in the image. It returns the coordinates of the cat's face if it is detected, otherwise it returns None.

`cut(filename)`
This function takes a filename as input and uses the `detect()` function to get the coordinates of the cat's face. It then cuts the cat's face out of the image and returns it. If the face is not detected, it returns None.

`load()`
This function prompts the user for the breed of cats they want to detect and cut. It then searches for images of that breed in the `datasets/<breed>/original` folder, detects and cuts the cat's face, and saves the cut face in the `datasets/<breed>/faces` folder. If the face is not detected, it will log a error. The function prints the success rate of face detection and cutting.
