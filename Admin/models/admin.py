from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, BigInteger
from sqlalchemy.orm import relationship
from ..settings.db import Base

class School(Base):
    __tablename__ = 'tbl_schools'

    school_id = Column(Integer, primary_key=True)
    school_name = Column(String, index=True)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postal_code = Column(BigInteger)
    phone_number = Column(BigInteger)
    email = Column(String)

class User(Base):
    __tablename__ = 'tbl_users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String)
    role_id = Column(Integer, ForeignKey('tbl_roles.role_id', ondelete='CASCADE'))
    is_active = Column(Boolean)
    school_id = Column(Integer, ForeignKey('tbl_schools.school_id', ondelete='CASCADE'), default_value=None)  # Added school_id

class ModuleFeature(Base):
    __tablename__ = 'tbl_module_features'

    module_feature_id = Column(Integer, primary_key=True)
    module_name = Column(String)
    feature_name = Column(String)

class Role(Base):
    __tablename__ = 'tbl_roles'

    role_id = Column(Integer, primary_key=True)
    role_name = Column(String, unique=True, index=True)
    description = Column(String)

class RolePermission(Base):
    __tablename__ = 'tbl_role_permissions'

    role_permission_id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('tbl_roles.role_id',ondelete='CASCADE'))
    module_feature_id = Column(Integer, ForeignKey('tbl_module_features.module_feature_id',ondelete='CASCADE'))

class DefaultValue(Base):
    __tablename__ = 'tbl_default_values'

    default_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('tbl_users.user_id',ondelete='CASCADE'))
    module_name = Column(String)
    default_setting = Column(String)

class AcademicYear(Base):
    __tablename__ = 'tbl_academic_years'

    year_id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('tbl_schools.school_id',ondelete='CASCADE'))
    year_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

class SchoolSetting(Base):
    __tablename__ = 'tbl_school_settings'

    setting_id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('tbl_schools.school_id',ondelete='CASCADE'))
    academic_schedule = Column(String)
    grading_system = Column(String)
    # Other settings...

class CalendarEvent(Base):
    __tablename__ = 'tbl_calendar_events'

    event_id = Column(Integer, primary_key=True)
    school_id = Column(Integer, ForeignKey('tbl_schools.school_id',ondelete='CASCADE'))
    event_name = Column(String)
    event_date = Column(Date)
    event_type = Column(String)
    description = Column(String)
