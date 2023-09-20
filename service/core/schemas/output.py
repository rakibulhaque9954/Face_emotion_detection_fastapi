from pydantic import BaseModel

class APIOutput(BaseModel):
    emotions: str
    time_elapsed_preprocessing: str
    time_elapsed: str
