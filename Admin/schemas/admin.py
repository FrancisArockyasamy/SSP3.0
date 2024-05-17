from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

# School schema
class SchoolBase(BaseModel):
    school_name: str
    address: str
    city: str
    state: str
    country: str
    postal_code: int
    phone_number: str
    email: EmailStr

class SchoolCreate(SchoolBase):
    pass

class School(SchoolBase):
    school_id: int

    class Config:
        from_attributes = True

# Schema for user
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    role_id: int
    school_id: int
    is_active:bool

class User(UserBase):
    user_id: int
    is_active: bool
    role_id: int
    school_id: int

    class Config:
        from_attributes = True

# schema for modules
class ModuleFeatureBase(BaseModel):
    module_name: str
    feature_name: str

class ModuleFeatureCreate(ModuleFeatureBase):
    pass

class ModuleFeature(ModuleFeatureBase):
    module_feature_id: int

    class Config:
        from_attributes = True

# Schema for roles
class RoleBase(BaseModel):
    role_name: str
    description: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    role_id: int

    class Config:
        from_attributes = True

# For role permission

class RolePermission(BaseModel):
    role_permission_id: int
    role_id: int
    module_feature_id:int
    class Config:
        from_attributes = True

# Default values
class DefaultValueBase(BaseModel):
    user_id: int
    module_name: str
    default_setting: str

class DefaultValueCreate(DefaultValueBase):
    pass

class DefaultValue(DefaultValueBase):
    default_id: int

    class Config:
        from_attributes = True

# for Academic years
class AcademicYearBase(BaseModel):
    school_id: int
    year_name: str
    start_date: date
    end_date: date

class AcademicYearCreate(AcademicYearBase):
    pass

class AcademicYear(AcademicYearBase):
    year_id: int

    class Config:
        from_attributes = True

# Schema for SchoolSetting
class SchoolSettingBase(BaseModel):
    school_id: int
    academic_schedule: Optional[str] = None
    grading_system: Optional[str] = None
    # Add other settings here...

class SchoolSettingCreate(SchoolSettingBase):
    pass

class SchoolSetting(SchoolSettingBase):
    setting_id: int

    class Config:
        from_attributes = True

# Schema for CalendarEvent
class CalendarEventBase(BaseModel):
    school_id: int
    event_name: str
    event_date: date
    event_type: Optional[str] = None
    description: Optional[str] = None

class CalendarEventCreate(CalendarEventBase):
    pass

class CalendarEvent(CalendarEventBase):
    event_id: int

    class Config:
        from_attributes = True