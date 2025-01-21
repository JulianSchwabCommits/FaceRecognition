# Face Recognition in Python Using DeepFace

A real-time face recognition system using OpenCV and DeepFace. This script captures live video from a webcam and verifies whether the detected face matches a reference image.

## Features

- Real-time face detection using OpenCV
- Face verification using DeepFace
- Multi-threading for better performance
- Displays messages:
  - **"Hi, [Your Name]"** if the face matches the reference image
  - **"Face found, no match!"** if a face is detected but does not match
  - **"Face not found!"** if no face is detected

## Requirements

Before running the script, ensure you have the necessary dependencies installed:

```bash
pip install opencv-python deepface
```

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/JulianSchwabCommits/FaceRecognition.git
   cd FaceRecognition
   ```

2. **Place your reference image** in the appropriate directory:

   ```
   ...\FaceRecognitionPython\YourImage.jpg
   ```

   If using a different image path, update the script accordingly.

3. **Run the script**:

   ```bash
   python face_recognition.py
   ```

4. **How the program works**:
   - The webcam will start, and the program will analyze faces in real time.
   - If your face matches the reference image, it will display:  
     **"Hi, [Your Name]"**.
   - If a face is detected but does not match, it will display:  
     **"Face found, no match!"**.
   - If no face is detected, it will display:  
     **"Face not found!"**.

5. **Exit the program** by pressing `q`.

## How It Works

- Captures video frames using OpenCV.
- Every 30 frames, it checks whether a face is detected and compares it with the reference image using DeepFace.
- Uses multi-threading to ensure the main loop remains responsive.
- Displays real-time results on the video stream.
