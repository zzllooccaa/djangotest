from _datetime import date
from json import JSONEncoder

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr

from dataclasses import dataclass

import enum
import simplejson
import datetime

# Create your models here.

#Class User()

class BaseModels(object):
    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True, autoincrement=True, unique=True)

    @declared_attr
    def date_of_creation(self):
        return Column(DateTime(), default=datetime.datetime.today())

    @classmethod
    def get_by_id(cls, id):
        return db.query(cls) \
            .filter(cls.id == id) \
            .first()

    @classmethod
    def get_id(cls, ide):
        return db.query(cls).filter(cls.id == ide).first()


class BaseUser(BaseModels):

    @declared_attr
    def name(self):
        return Column(String(255), nullable=False)

    @declared_attr
    def email(self):
        return Column(String, unique=True)

    @declared_attr
    def address(self):
        return Column(String(255))

    @declared_attr
    def phone(self):
        return Column(String(20))