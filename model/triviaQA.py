# """ database dependencies to support sqliteDB examples """
# from random import randrange
# import json
# from __init__ import app, db
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy import ForeignKey



# ''' Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along '''

# # Define the Post class to manage actions in 'posts' table,  with a relationship to 'users' table
# # class Post(db.Model):
# #     __tablename__ = 'posts'

# #     # Define the Notes schema
# #     id = db.Column(db.Integer, primary_key=True)
# #     note = db.Column(db.Text, unique=False, nullable=False)
# #     image = db.Column(db.String, unique=False)
# #     # Define a relationship in Notes Schema to userID who originates the note, many-to-one (many notes to one user)
# #     userID = db.Column(db.Integer, db.ForeignKey('users.id'))

# #     # Constructor of a Notes object, initializes of instance variables within object
# #     def __init__(self, id, note, image):
# #         self.userID = id
# #         self.note = note
# #         self.image = image

# #     # Returns a string representation of the Notes object, similar to java toString()
# #     # returns string
# #     def __repr__(self):
# #         return "Notes(" + str(self.id) + "," + self.note + "," + str(self.userID) + ")"

# #     # CRUD create, adds a new record to the Notes table
# #     # returns the object added or None in case of an error
# #     def create(self):
# #         try:
# #             # creates a Notes object from Notes(db.Model) class, passes initializers
# #             db.session.add(self)  # add prepares to persist person object to Notes table
# #             db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
# #             return self
# #         except IntegrityError:
# #             db.session.remove()
# #             return None

# #     # CRUD read, returns dictionary representation of Notes object
# #     # returns dictionary
# #     def read(self):
# #         # encode image
# #         path = app.config['UPLOAD_FOLDER']
# #         file = os.path.join(path, self.image)
# #         file_text = open(file, 'rb')
# #         file_read = file_text.read()
# #         file_encode = base64.encodebytes(file_read)
        
# #         return {
# #             "id": self.id,
# #             "userID": self.userID,
# #             "note": self.note,
# #             "image": self.image,
# #             "base64": str(file_encode)
# #         }




# # Define the User class to manage actions in the 'users' table
# # -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# # -- a.) db.Model is like an inner layer of the onion in ORM
# # -- b.) User represents data we want to store, something that is built on db.Model
# # -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
# class QA(db.Model):
#     __tablename__ = 'questions'  # table name is plural, class name is singular

#     # Define the User schema with "vars" from object
#     id = db.Column(db.Integer, primary_key=True)
#     _question = db.Column(db.String(255), ForeignKey('question'), unique=True, nullable=True)
#     _answer = db.Column(db.String(255), unique=False, nullable=False)
    
#         # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
#     posts = db.relationship("Post", cascade='all, delete', backref='users', lazy=True)
#     # posts = db.relationship("Post", cascade='all, delete', backref='users', lazy=True)

#     # constructor of a User object, initializes the instance variables within object (self)
#     def __init__(self, question, answer):
#         self._question = question    # variables with self prefix become part of the object, 
#         self._answer = answer

#     # a name getter method, extracts name from object
#     @property
#     def question(self):
#         return self._question
    
#     # a setter function, allows name to be updated after initial object creation
#     @question.setter
#     def question(self, question):
#         self._question = question
    
#     # a getter method, extracts email from object
#     @property
#     def answer(self):
#         return self._answer
    
#     # a setter function, allows name to be updated after initial object creation
#     @answer.setter
#     def answer(self, answer):
#         self._answer = answer
        
#     # check if uid parameter matches user id in object, return boolean
#     def is_question(self, answer):
#         return self._answer == answer

#     # output content using str(object) in human readable form, uses getter
#     # output content using json dumps, this is ready for API response
#     def __str__(self):
#         return json.dumps(self.read())

#     # CRUD create/add a new record to the table
#     # returns self or None on error
#     def create(self):
#         try:
#             # creates a person object from User(db.Model) class, passes initializers
#             db.session.add(self)  # add prepares to persist person object to Users table
#             db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
#             return self
#         except IntegrityError:
#             db.session.remove()
#             return None

#     # CRUD read converts self to dictionary
#     # returns dictionary
#     def read(self):
#         return {
#             "id": self.id,
#             "question": self.question,
#             "answer": self.answer,
#         }



# """Database Creation and Testing """


# # Builds working data for testing
# def initQAs():
#     with app.app_context():
#         """Create database and tables"""
#         db.init_app(app)
#         db.create_all()
        
#         """Tester data for table"""
#         q1 = QA(question='what is 1 + 1', answer='2')
#         q2 = QA(question='what is 2 + 2', answer='4')
#         q3 = QA(question='what is 3 + 3', answer='6')
#         q4 = QA(question='what is 4 + 4', answer='8')
#         q5 = QA(question='what is 5 + 5', answer='10')

#         questions = [q1, q2, q3, q4, q5]

#         """Builds sample user/note(s) data"""
#         for question in questions:
#             try:
#                 # '''add a few 1 to 4 notes per user'''
#                 # for num in range(randrange(1, 4)):
#                 #     note = "#### " +  str(question) + " note " + str(num) + ". \n Generated by test data."
#                 #     question.posts.append(Post(id = question.id, note=note, image='ncs_logo.png'))
#                 # '''add user/post data to table'''
#                 question.create()
#             except IntegrityError:
#                 '''fails with bad or duplicate data'''
#                 db.session.rollback()
#                 print(f"Records exist, duplicate email, or error: {questions.id}")
            









# #ChatGPT Debug Code

# # import os
# # import base64
# # import json
# # from datetime import date
# # from random import randrange
# # from sqlalchemy.exc import IntegrityError

# # from __init__ import app, db



# # class Post(db.Model):
# #     __tablename__ = 'posts'


# #     id = db.Column(db.Integer, primary_key=True)
# #     note = db.Column(db.Text, nullable=False)
# #     image = db.Column(db.String, nullable=False)
# #     userID = db.Column(db.Integer, db.ForeignKey('users.id'))

# #     def __init__(self, userID, note, image):
# #         self.userID = userID
# #         self.note = note
# #         self.image = image

# #     def __repr__(self):
# #         return f'Post({self.id}, {self.note}, {self.image}, {self.userID})'

# #     def create(self):
# #         try:
# #             db.session.add(self)
# #             db.session.commit()
# #             return self
# #         except IntegrityError:
# #             db.session.rollback()
# #             return None

# #     def read(self):
# #         path = app.config['UPLOAD_FOLDER']
# #         file_path = os.path.join(path, self.image)
# #         with open(file_path, 'rb') as f:
# #             image_data = f.read()
# #         encoded_image = base64.b64encode(image_data).decode('utf-8')
# #         return {
# #             'id': self.id,
# #             'userID': self.userID,
# #             'note': self.note,
# #             'image': self.image,
# #             'base64': encoded_image
# #         }


# # class QA(db.Model):
# #     __tablename__ = 'questions'

# #     id = db.Column(db.Integer, primary_key=True)
# #     question = db.Column(db.String(255), nullable=False, unique=True)
# #     answer = db.Column(db.String(255), nullable=False)

# #     def __init__(self, question, answer):
# #         self.question = question
# #         self.answer = answer

# #     @property
# #     def question(self):
# #         return self._question

# #     @question.setter
# #     def question(self, question):
# #         self._question = question

# #     @property
# #     def answer(self):
# #         return self._answer

# #     @answer.setter
# #     def answer(self, answer):
# #         self._answer = answer

# #     def is_answer(self, answer):
# #         return self.answer == answer

# #     def __str__(self):
# #         return json.dumps(self.read())

# #     def create(self):
# #         try:
# #             db.session.add(self)
# #             db.session.commit()
# #             return self
# #         except IntegrityError:
# #             db.session.rollback()
# #             return None

# #     def read(self):
# #         return {
# #             'id': self.id,
# #             'question': self.question,
# #             'answer': self.answer,
# #         }

# #     # CRUD update: updates user name, password, phone
# #     # returns self
# #     def update(self, question="", answer=""):
# #         """only updates values with length"""
# #         if len(question) > 0:
# #             self.question = question
# #         if len(answer) > 0:
# #             self.answer = answer
# #         db.session.commit()
# #         return self

# #     # CRUD delete: remove self
# #     # None
# #     def delete(self):
# #         db.session.delete(self)
# #         db.session.commit()
# #         return None


