#!/usr/bin/python3
"""Define the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class that represent a state.

    Attribute:
        name (str): name of state.
        """

    name = ""
