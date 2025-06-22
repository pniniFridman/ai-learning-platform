from pydantic import BaseModel

class CourseBase(BaseModel):
    title: str
    description: str
    instructor: str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True