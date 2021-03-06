#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.review import Review
import models
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'

    city_id = Column(
        String(60),
        ForeignKey('cities.id'),
        nullable=False
    )
    user_id = Column(
        String(60),
        ForeignKey('users.id'),
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    description = Column(
        String(1024),
        nullable=True
    )
    number_rooms = Column(
        Integer,
        default=0,
        nullable=False
    )
    number_bathrooms = Column(
        Integer,
        default=0,
        nullable=False
    )
    max_guest = Column(
        Integer,
        default=0,
        nullable=False
    )
    price_by_night = Column(
        Integer,
        default=0,
        nullable=False
    )
    latitude = Column(
        Float,
        nullable=True
    )
    longitude = Column(
        Float,
        nullable=True
    )

    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete-orphan'
        )
        amenities = relationship(
            'Amenity',
            secondary='place_amenity',
            viewonly='False',
        )
    else:
        @property
        def reviews(self):
            review_list = []
            for id, review in models.storage.all(Review).items():
                if self.id == review.place.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            amenities_list = []
            for amenity in amenity_ids:
                if self.id == amenity.id:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, amenity):
            if type(amenity).__name__ == 'Amenity':
                self.amenity_ids.append(amenity)
