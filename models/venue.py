from pydantic import BaseModel


class Venue(BaseModel):
    """
    Represents the data structure of a Venue.
    """

    name: str
    price: int
    kilometerstand : int
    erstzulassung: str

