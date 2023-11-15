#!/usr/bin/python3
""" User Model Module """
from models.base_model import BaseModel


class User(BaseModel):
    """ A user model that models a typicl user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
