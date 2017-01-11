# sample_db -- A Sample Tracking Database
# Copyright (C) 2017  Maxwell Murphy, Jordan Wilheim
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Model(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)


class Sample(Model):
    __tablename__ = 'sample'


class MatrixPlate(Model):
    __tablename__ = 'matrix_plate'
    label = Column(String, unique=True, index=True)


class MatrixTube(Model):
    __tablename__ = 'matrix_tube'
    plate_id = Column(Integer, ForeignKey('matrix_plate.id'))
    plate = relationship('MatrixPlate', backref="tubes")
