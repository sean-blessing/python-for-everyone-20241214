from dataclasses import dataclass

@dataclass
class Movie:
    title:str = ""
    year: int = 0
    rating: str = "G"
    director: str = ""
