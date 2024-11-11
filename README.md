# DriveAcademy
DriveAcademy is a Django web app for managing driving school courses. It allows creating and managing categories, series, and questions for theoretical driving tests. The app supports media integration (images, audio, video) and provides CRUD functionality to efficiently manage learning content.


auto_school/
├── auto_school/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── courses/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── tests.py


+----------------+
|   Category     |
+----------------+
| id: PK         |
| name: String   |
| description: Text |
+----------------+
         |
         | (Many-to-Many via CategorySeries)
         |
+--------------------------+
|   CategorySeries         |
+--------------------------+
| id: PK                   |
| category_id: FK -> Category.id |
| series_id: FK -> Series.id   |
+--------------------------+
         |
         |
+----------------+
|    Series      |
+----------------+
| id: PK         |
| title: String  |
| description: Text |
+----------------+
         |
         | (Many-to-Many via SeriesQuestion)
         |
+--------------------------+
|      SeriesQuestion      |
+--------------------------+
| id: PK                   |
| series_id: FK -> Series.id |
| question_id: FK -> Question.id |
+--------------------------+
         |
         |
+----------------------+
|      Question        |
+----------------------+
| id: PK               |
| order: Integer       |
| type: Enum (image, audio, video) |
| image_data: Binary   |
| audio_data: Binary   |
| video_data: Binary   |
| options: JSON        |
| true_options: JSON   |
+----------------------+
