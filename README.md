### README: Face Recognition with DeepFace and OpenCV

#### **Overview**
This script performs real-time face recognition using OpenCV and DeepFace. It captures video from your webcam, compares the detected face to a reference image, and displays appropriate messages based on whether the face is found and if it matches the reference.

#### **Dependencies**
- **DeepFace** for facial recognition
- **OpenCV** for video capture and image processing

#### **Setup Instructions**

1. **Install Anaconda (if not already installed)**
   - Download and install [Anaconda](https://www.anaconda.com/products/individual) for Python 3.10.

2. **Create a Conda Environment**
   Create a Conda environment with Python 3.10 using the following command:
   ```bash
   conda create -n FaceRec python=3.10
   ```
   
3. **Activate the Environment**
   Activate your environment:
   ```bash
   conda activate FaceRec
   ```

4. **Install Dependencies**
   Use `pip` to install **DeepFace** and **OpenCV**:
   ```bash
   pip install deepface opencv-python
   ```

5. **Prepare Reference Image**
   Place the reference image (the one you want to compare against) in your project directory and update the `reference_img` path in the code:
   ```python
   reference_img = cv2.imread("path_to_your_image.jpg")
   ```

6. **Run the Script**
   Run the script:
   ```bash
   python face_recognition.py
   ```

   The webcam will start capturing, and the script will analyze each frame to see if the face matches the reference.

#### **How it Works**

1. **Video Capture**:
   - The script captures frames from your webcam using OpenCV (`cv2.VideoCapture(0)`).
   
2. **Face Detection and Matching**:
   - Every 30 frames, the `check_face` function is called in a separate thread. This function:
     - Uses DeepFace's `verify` function to compare the captured face with the reference image.
     - Updates the flags (`face_match`, `face_found`) depending on the result.
   
3. **Display Messages**:
   - The script overlays messages on the video feed based on the face matching result:
     - `"Hi, {Name}"` if a matching face is detected.
     - `"Face found no match!"` if a face is found but doesn't match.
     - `"Face not found!"` if no face is detected.
   
4. **Exit**:
   - Press `q` to exit the video feed.

#### **Important Notes**
- Ensure that your webcam is properly set up and recognized by your system.
- The script uses threading to handle the face comparison without blocking the main video loop.
- You may need to adjust the reference image path based on your system and file structure.

#### **Resources**
- [DeepFace Documentation](https://pypi.org/project/deepface/)
- [OpenCV Documentation](https://pypi.org/project/opencv-python/)

---

This README provides the basic setup and explanation of how the face recognition script works with DeepFace and OpenCV. Let me know if you need further assistance!