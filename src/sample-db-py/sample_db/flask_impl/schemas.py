from ..db_impl.models import Study, StudySubject, SpecimenType, Specimen, Location, StorageContainer, MatrixPlate, \
    MatrixTube
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from . import db


class BaseSchema(ModelSchema):
    class Meta:
        sqla_session = db._session
    id = fields.String()


class SpecimenTypeSchema(BaseSchema):
    class Meta:
        model = SpecimenType


class SpecimenSchema(BaseSchema):
    class Meta:
        model = Specimen
    # specimen_type = fields.Nested(SpecimenTypeSchema)


class StudySubjectSchema(BaseSchema):
    class Meta:
        model = StudySubject
    # specimens = fields.Nested(SpecimenSchema, many=True)
    study = fields.String(attribute='study_id')


class StudySchema(BaseSchema):
    class Meta:
        model = Study
        # exclude = ('subjects',)


class DetailedStudySchema(BaseSchema):
    class Meta:
        model = Study


class LocationSchema(BaseSchema):
    class Meta:
        model = Location
        exclude = ('specimen_containers',)


class StorageContainerSchema(BaseSchema):
    class Meta:
        model = StorageContainer


class MatrixTubeSchema(BaseSchema):
    class Meta:
        model = MatrixTube
    plate = fields.String(attribute='plate_id')
    specimen = fields.String(attribute='specimen_id')


class MatrixPlateSchema(BaseSchema):
    class Meta:
        model = MatrixPlate
    location = fields.String(attribute="location_id")





