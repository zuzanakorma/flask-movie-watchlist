from dataclasses import dataclass, field
from datetime import datetime


# allows to store properties about movie and adds few more methods (like init...)
@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: list[str] = field(default_factory=list) # default value  => optional, could be empty
    series:list[str] = field(default_factory=list)
    last_watched: datetime = None
    rating: int = 0  
    tags:list[str] = field(default_factory=list)
    description: str = None
    video_link: str = None


@dataclass
class User:
    _id: str
    email: str
    password: str
    movies: list[str] = field(default_factory=list)