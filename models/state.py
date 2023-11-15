#!/usr/bin/python3
""" State model module """
from models.base_model import BaseModel


class State(BaseModel):
    """Models a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
