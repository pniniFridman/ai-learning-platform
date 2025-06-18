from sqlalchemy import Column, Integer, String
from ..database.database import Base # שימו לב לשינוי כאן, מייבאים מ-Base מהקובץ החדש
# אם תרצה/י להוסיף קשרים (relationships) בעתיד, תצטרך/י לייבא גם את relationship ו-ForeignKey.

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    description = Column(String)
    instructor = Column(String)