from pydantic import BaseModel

class Word(BaseModel):
    normal_form: str
    gender: str
    case: str
    number: str
    