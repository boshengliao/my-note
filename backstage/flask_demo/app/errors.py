# -*- coding: utf-8 -*-

from marshmallow import ValidationError as Schema_ValidationError
from mongoengine import ValidationError
from mongoengine.errors import NotUniqueError


class GeneralError(ValueError):
    pass
