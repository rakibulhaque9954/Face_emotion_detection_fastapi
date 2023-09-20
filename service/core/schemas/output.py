from pydantic import BaseModel
from typing import List

class APIOutput(BaseModel):
    emotion: str
    time_elapsed_preprocessing: str
    time_elapsed: str
