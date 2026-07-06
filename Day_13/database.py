from sqlalchemy import create_engine,Column, Integer, String, Boolean, ForeignKey, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "postgresql://postgres:avisdb@localhost:5433/SQLalchemy_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush= False)


Base = declarative_base()

class User(Base):
    __tablename__= "users"
    user_id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    user_name = Column(String, nullable=False)
    user_age = Column(Integer)
    user_ph_no = Column(String, unique=True)
    email = Column(String, unique=True)
    post = relationship("Post", back_populates="user")
    completed = Column(Boolean, default=False)

class Post(Base):
    __tablename__= "posts"
    post_id = Column(Integer, primary_key=True)
    course = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("User",back_populates="post")
    completed = Column(Boolean, default=False)

# creating table
Base.metadata.create_all(bind=engine)

user1=User(user_name= "siva",user_age= 28,user_ph_no= 1234567890,email= "siva@gmail.com")
user2=User(user_name= "hari",user_age= 26,user_ph_no= 9876543210,email= "hari@gmail.com")
user3=User(user_name= "ram",user_age= 27,user_ph_no= 1029384756,email= "ram@gmail.com")
user4=User(user_name= "sivahari",user_age= 25,user_ph_no= 9344058819,email= "sivahari@gmail.com")
user5=User(user_name= "dummy",user_age= 55,user_ph_no= 555555555,email= "dummy@gmail.com")

post1 = Post(post_id= 101,course= 'python',user_id= 3 )
post2 = Post(post_id= 102,course= 'sql',user_id= 6 )
post3 = Post(post_id= 103,course= 'java',user_id= 5 )
post4 = Post(post_id= 104,course= 'javascipt',user_id= 6 )
post5 = Post(post_id= 105,course= 'react',user_id= 4 )

with SessionLocal() as session:
    session.add_all([post1,post2,post3,post4,post5,user1,user2,user3,user4,user5])
    session.commit()

    #filter==========================================
    # user = session.query(User).filter(User.user_age>25).all()
    # for i in user:
    #     print(f"{i.user_name} {i.user_age} {i.user_id}")

    #update==========================================
    # user = session.query(User).filter(User.user_id == 14).first()
    # user.user_name = "dummy1"
    # print(user.user_name)
    # session.commit()

    #Delete==========================================
    # user = session.query(User).filter(User.user_name == "dummy1").first()
    # session.delete(user)
    # session.commit()

    #Relationship_check_query==========================
    # user = session.query(User).filter(User.user_id == 6).first()
    # print(user.user_name)
    # for i in user.post:
    #     print(f"{i.post_id},{i.course},{i.user_id}")