# 👨‍🎓 Real-Time Face Attendance System

This project is a real-time face attendance system that utilizes face recognition to automatically mark attendance for students. It uses a webcam to capture live video feed, detects faces in the video stream, compares them with known faces in the database, and records attendance for recognized students. 

## ⚙ Features

- Automatic face detection and recognition.
- Real-time attendance marking.
- Integration with Firebase for data storage in Real-time.
- User-friendly graphical interface.

## 📄 Requirements

- Python 3.7.6
- PyCharm IDE
- Webcam
- Graphics library
- Face Recognition module
- Firebase Realtime Database

## 📑Prerequisites
- Before running the project, make sure you have the following prerequisites installed:
- Python 3.7.6
- Graphics library
- OpenCV
- Face Recognition
- Firebase Admin SDK
- Other dependencies specified in the `'requirements.txt'` file

## 🚀 Getting Started

1. Clone the repository.
2. Install the required dependencies by running the following command:
```
pip install -r requirements.txt.
```
3. Set up the database using Firebase.
4. Update the necessary configurations.
5. Run the application.


## ☂ Usage
- Run the AddDatatoDatabase.py script to populate the Firebase database with sample student data.
```
python AddDatatoDatabase.py
```
- Run the EncodeGenrator.py script to generate encodings for known student faces and save them to the EncodeFile.p file.
```
python EncodeGenrator.py
```
- Finally, run the main.py script to start the real-time face attendance system.
```
python main.py
```


## 🛠 Configuration
You can modify the configuration of the system by changing the following files:

- `'AddDatatoDatabase.py'`: Modify the sample student data and database URL.
- `'EncodeGenrator.py'`: Update the image folder path and storage bucket URL.
- `'main.py'`: Customize the GUI and other settings.

## 🔗 References
- OpenCV: https://opencv.org/
- Dlib: http://dlib.net/
- Face Recognition: https://github.com/ageitgey/face_recognition
- Firebase Admin SDK: https://firebase.google.com/docs/admin/setup

