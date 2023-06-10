import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionrealtimeatdsys-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "228477":
        {
            "name": "Mishal",
            "major": "Machine",
            "starting_year": 2023,
            "total_attendance": 5,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "228489":
        {
            "name": "Navneet",
            "major": "Computer",
            "starting_year": 2022,
            "total_attendance": 3,
            "standing": "LG",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "228494":
        {
            "name": "Om Prakash",
            "major": "Social",
            "starting_year": 2020,
            "total_attendance": 4,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "228498":
        {
            "name": "Siddhant",
            "major": "Data",
            "starting_year": 2022,
            "total_attendance": 2,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "228456":
        {
            "name": "Harsh",
            "major": "Gaming",
            "starting_year": 2020,
            "total_attendance": 2,
            "standing": "VG",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "228448":
        {
            "name": "Gulshan",
            "major": "Maths",
            "starting_year": 2020,
            "total_attendance": 1,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)