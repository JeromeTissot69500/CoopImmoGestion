from flask import Markup
from ..db.db import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm.exc import NoResultFound
from .Property import Property
from .Address import Address


class Apartment(Property):
    # Mapping Class with db table
    __tablename__ = "Apartment"
    _stage = db.Column('stage', db.Integer, nullable=False)
    _outdoor = db.Column('outdoor', db.Boolean, default=False, nullable=False)

    # Constructor
    def __init__(self, property_id: int, reference: str, living_area: float, rooms: int,
                 address: Address, stage: int, outdoor: bool):
        super().__init__(property_id, reference, living_area, rooms, address)
        self._stage = stage
        self._outdoor = outdoor

    # Define getter and setter property
    @hybrid_property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, stage):
        self._stage = stage

    @hybrid_property
    def outdoor(self):
        return self._outdoor

    @outdoor.setter
    def outdoor(self, outdoor):
        self._outdoor = outdoor

    # Define string representation for Apartment object
    def __repr__(self):
        return f'<UserApp>: {self.reference}'

    @classmethod
    def read(cls):
        try:
            apartments = cls.query.all()
            return apartments
        except NoResultFound:
            return []
        except Exception:
            return None

    @classmethod
    def create(cls, user_input, apartment_address):
        # get outdoor value in boolean type
        if user_input.get('outdoor'):
            outdoor = bool(Markup(user_input['outdoor']))
        else:
            outdoor = False

        apartment = cls(None, user_input['reference'], user_input['living_area'], user_input['rooms'],
                        apartment_address, user_input['stage'], outdoor)
        try:
            db.session.add(apartment)
            db.session.commit()
            return apartment
        except Exception:
            db.session.rollback()
            return None
