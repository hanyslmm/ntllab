# used to manipulate diff parts of py run-time env.
import sys
import os
# import all modules needed for configuration
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# base instance inherit all features of SQLAlchemy
Base = declarative_base()

# add usertype class definition code
class Usertype(Base):
    __tablename__ = 'usertype'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

# add user class definition code [] user course regestration regestrationdetails ]
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    usertype = Column(Integer, ForeignKey('type.id'))
    type = relationship(Usertype)

# add semester class definition code
class Semester(Base):
    __tablename__ = 'semester'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

# add Regestration class definition code
class Regestration(Base):
    __tablename__ = 'regestration'
    id = Column(Integer, primary_key = True)
    student_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    semester_id = Column(Integer, ForeignKey('semester.id'))
    semester = relationship(Semester)

# add courses class definition code
class Courses(Base):
    __tablename__ = 'Courses Name'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

# add RegestrationDetails class definition code
class ResgestrationDetails(Base):
    __tablename__ = 'Resgestration Details'
    id = Column(Integer, primary_key = True)
    RegId = Column(Integer, ForeignKey('Reg.id'))
    Reg = relationship(Regestration)
    course_id = Column(Integer, ForeignKey('courses.id'))
    courses = relationship(Courses)
    final_grade = Column(Integer)


# === to connect to an existing db or create a new one ===
engine = create_engine('sqlite:///regestration.db')
Base.metadata.create_all(engine)
print("connected to restaurantmenu database")
