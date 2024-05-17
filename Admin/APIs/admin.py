from fastapi import APIRouter, HTTPException, status, Depends
from ..settings.db import get_db
from ..settings.auth import encrypt_pwd, verify_pwd, genToken, authenticate
from ..schemas import admin as admin_schema
from ..models import admin as admin_model
from sqlalchemy.orm import Session
from typing import List
from fastapi.security import OAuth2PasswordRequestForm


app= APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

# School APIs
@app.post("/schools", response_model=admin_schema.School)
def create_school(school: admin_schema.SchoolCreate, db: Session = Depends(get_db)):
    db_school = admin_model.School(**school.model_dump())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

@app.get("/schools/", response_model=list[admin_schema.School])
def read_schools(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(admin_model.School).offset(skip).limit(limit).all()

@app.get("/schools/{school_id}", response_model=admin_schema.School)
def read_school(school_id: int, db: Session = Depends(get_db)):
    db_school = db.query(admin_model.School).filter(admin_model.School.school_id == school_id).first()
    if db_school is None:
        raise HTTPException(status_code=404, detail="School not found")
    return db_school

@app.put("/schools/{school_id}")
def update_school(school_id: int, school: admin_schema.SchoolCreate, db: Session = Depends(get_db)):
    db_school = db.query(admin_model.School).filter(admin_model.School.school_id == school_id)
    if db_school.first() is None:
        raise HTTPException(status_code=404, detail="School not found")
    db_school.update(school.model_dump())
    db.commit()
    return {"status":True,"message":"School updated successfully"}

@app.delete("/schools/{school_id}")
def delete_school(school_id: int, db: Session = Depends(get_db)):
    db_school = db.query(admin_model.School).filter(admin_model.School.school_id == school_id)
    if db_school.first() is None:
        raise HTTPException(status_code=404, detail="School not found")
    db_school.delete()
    db.commit()
    return {"status":True,"message":"School deleted successfully"}

app1= APIRouter(
    prefix="/admin",
    tags=["Admin - Module,feature,role"]
)

# Module Features APIs
@app1.post("/module_features/", response_model=List[admin_schema.ModuleFeature])
def create_module_feature(module_feature: List[admin_schema.ModuleFeatureCreate], db: Session = Depends(get_db), current_user= Depends(authenticate)):
    if current_user['role_id'] != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")
    output=[]
    for i in module_feature:
        data= admin_model.ModuleFeature(**i.model_dump())
        db.add(data)
        db.commit()
        db.refresh(data)
        output.append(data)
    return output

@app1.get("/module_features/", response_model=list[admin_schema.ModuleFeature])
def read_module_features(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    data= db.query(admin_model.ModuleFeature).limit(limit).offset(skip).all()
    return data

@app1.put("/module_features/{module_feature_id}")
def update_module_feature(module_feature_id: int, module_feature: admin_schema.ModuleFeatureCreate, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    if current_user['role_id'] != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")
    data= db.query(admin_model.ModuleFeature).filter(admin_model.ModuleFeature.module_feature_id == module_feature_id)
    if not data.first():
        raise HTTPException(status_code=404, detail="Module feature not found")
    data.update(module_feature.model_dump())
    db.commit()
    return {"status":True,"message":"Module feature updated successfully"}
    
@app1.delete("/module_features/{module_feature_id}")
def delete_module_feature(module_feature_id: int, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    if current_user['role_id'] != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")
    db_module_feature = db.query(admin_model.ModuleFeature).filter(admin_model.ModuleFeature.module_feature_id == module_feature_id)
    if db_module_feature.first():
        db_module_feature.delete()
        db.commit()
        return {"status":True,"message": "Module feature deleted successfully"}
    else:
        return {"error": "Module feature not found"}
    

# Role APIs
@app1.post("/roles/", response_model=List[admin_schema.Role])
def create_role(role: List[admin_schema.RoleCreate], db: Session = Depends(get_db), current_user= Depends(authenticate)):
    if current_user['role_id'] != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")
    output=[]
    for data in role:
        db_role = admin_model.Role(**data.model_dump())
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        output.append(db_role)
    return output

@app1.get("/roles/", response_model=list[admin_schema.Role])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(admin_model.Role).offset(skip).limit(limit).all()

@app1.get("/roles/{role_id}", response_model=admin_schema.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = db.query(admin_model.Role).filter(admin_model.Role.role_id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@app1.put("/roles/{role_id}")
def update_role(role_id: int, role: admin_schema.RoleCreate, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    if current_user['role_id'] != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")
    db_role = db.query(admin_model.Role).filter(admin_model.Role.role_id == role_id)
    if db_role.first():
        db_role.update(role.model_dump())
        db.commit()
        return {"status":True,"message":"Role updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Role not found")

@app1.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    if current_user['role_id'] != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")
    db_role = db.query(admin_model.Role).filter(admin_model.Role.role_id == role_id).first()
    if db_role:
        db.delete(db_role)
        db.commit()
        return {"status":True,"message": "Role deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Role not found")
    
# RolePermission APIs
@app1.post("/role_permissions/", response_model=List[admin_schema.RolePermission])
def create_role_permissions(roles: List[int], module_features: List[int], db: Session = Depends(get_db), current_user= Depends(authenticate)):
    if current_user['role_id'] != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")
    created_role_permissions = []
    for role_id in roles:
        check_role= db.query(admin_model.Role).filter(admin_model.Role.role_id== role_id).first()
        if check_role:
            for module_feature_id in module_features:
                module= db.query(admin_model.ModuleFeature).filter(admin_model.ModuleFeature.module_feature_id == module_feature_id).first()
                if module:
                    role_permission_data = {
                        "role_id": role_id,
                        "module_feature_id": module_feature_id
                    }
                    check= db.query(admin_model.RolePermission).filter_by(**role_permission_data).first()
                    if not check:
                        db_role_permission = admin_model.RolePermission(**role_permission_data)
                        db.add(db_role_permission)
                        db.commit()
                        db.refresh(db_role_permission)
                        created_role_permissions.append(db_role_permission)
    return created_role_permissions

# Define endpoint to retrieve module features for a given role ID
@app1.get("/role_permissions/{role_id}/module_features", response_model=List[admin_schema.ModuleFeature])
def get_module_features_for_role(role_id: int, db: Session = Depends(get_db)):
    # Query database to get module features associated with the role ID
    db_role_permissions = db.query(admin_model.RolePermission).filter(admin_model.RolePermission.role_id == role_id).all()
    if not db_role_permissions:
        raise HTTPException(status_code=404, detail="No module features found for the role")
    
    # Extract module feature IDs from role permissions
    module_feature_ids = [rp.module_feature_id for rp in db_role_permissions]

    # Query database to get module features for the extracted IDs
    db_module_features = db.query(admin_model.ModuleFeature).filter(admin_model.ModuleFeature.module_feature_id.in_(module_feature_ids)).all()
    return db_module_features

@app1.delete("/role_permissions/{role_permission_id}")
def delete_role_permission(role_permission_id: int, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    if current_user['role_id'] != 1:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")
    db_role_permission = db.query(admin_model.RolePermission).filter(admin_model.RolePermission.role_permission_id == role_permission_id).first()
    if db_role_permission:
        db.delete(db_role_permission)
        db.commit()
        return {"message": "Role permission deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Role permission not found")

app2= APIRouter(
    prefix="/admin",
    tags=["Users"],
)
# User APIs
@app2.post("/users", response_model=admin_schema.User)
def create_user(user: admin_schema.UserCreate, db: Session = Depends(get_db)):
    user.password= encrypt_pwd(user.password)
    user_data = admin_model.User(**user.model_dump())
    role= db.query(admin_model.Role).filter(admin_model.Role.role_id == user.role_id).first()
    if user.school_id:
        school= db.query(admin_model.School).filter(admin_model.School.school_id == user.school_id).first()
    if role is None or (user.school_id is not None and school is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The specified role or school does not exist")
    username= db.query(admin_model.User).filter(admin_model.User.username == user.username).first()
    if username:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="The username already exists")
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data

@app2.get("/users", response_model=List[admin_schema.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(admin_model.User).filter(admin_model.User.is_active == True).offset(skip).limit(limit).all()
    return users

@app2.get("/users/{user_id}", response_model=admin_schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(admin_model.User).filter(admin_model.User.user_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app2.post("/login")
def login(data: OAuth2PasswordRequestForm= Depends(), db:Session= Depends(get_db)):
    user= db.query(admin_model.User).filter(admin_model.User.username == data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not verify_pwd(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    access_token= genToken({'usetname':data.username, 'user_id':user.user_id, 'role_id':user.role_id})
    return {"access_token": access_token, "token_type": "bearer"}

app3=APIRouter(
    prefix="/admin",
    tags=["Default values"]
)
# DefaultValue APIs
@app3.post("/default_values/", response_model=admin_schema.DefaultValue)
def create_default_value(default_value: admin_schema.DefaultValueCreate, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    default_value.user_id= current_user['user_id']
    db_default_value = admin_model.DefaultValue(**default_value.model_dump())
    db.add(db_default_value)
    db.commit()
    db.refresh(db_default_value)
    return db_default_value

# Read DefaultValue by ID
@app3.get("/default_values", response_model=List[admin_schema.DefaultValue])
def read_default_value(default_id: int, db: Session = Depends(get_db), current_user= Depends(authenticate)):

    db_default_value = db.query(admin_model.DefaultValue).filter(admin_model.DefaultValue.user_id == current_user['user_id']).all()
    if db_default_value is None:
        raise HTTPException(status_code=404, detail="DefaultValue not found")
    return db_default_value

# Update DefaultValue
@app3.put("/default_values/{default_id}", response_model=admin_schema.DefaultValue)
def update_default_value(default_id: int, default_value: admin_schema.DefaultValueCreate, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    db_default_value = db.query(admin_model.DefaultValue)\
        .filter(admin_model.DefaultValue.default_id == default_id,\
                    admin_model.DefaultValue.user_id == current_user['user_id']).first()
    if db_default_value:
        for key, value in default_value.model_dump().items():
            setattr(db_default_value, key, value)
        db.commit()
        db.refresh(db_default_value)
        return db_default_value
    else:
        raise HTTPException(status_code=404, detail="DefaultValue not found")

# Delete DefaultValue
@app3.delete("/default_values/{default_id}")
def delete_default_value(default_id: int, db: Session = Depends(get_db), current_user= Depends(authenticate)):
    db_default_value = db.query(admin_model.DefaultValue)\
        .filter(admin_model.DefaultValue.default_id == default_id,admin_model.DefaultValue.user_id == current_user['user_id']).first()
    if db_default_value:
        db.delete(db_default_value)
        db.commit()
        return {"message": "DefaultValue deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="DefaultValue not found")

app4=APIRouter(
    prefix="/admin",
    tags=["Academic years, calender events"]
)

# Create AcademicYear
@app4.post("/academic_years/", response_model=admin_schema.AcademicYear)
def create_academic_year(academic_year: admin_schema.AcademicYearCreate, db: Session = Depends(get_db)):
    db_academic_year = admin_model.AcademicYear(**academic_year.dict())
    db.add(db_academic_year)
    db.commit()
    db.refresh(db_academic_year)
    return db_academic_year

# Read AcademicYear by ID
@app4.get("/academic_years/{year_id}", response_model=admin_schema.AcademicYear)
def read_academic_year(year_id: int, db: Session = Depends(get_db)):
    db_academic_year = db.query(admin_model.AcademicYear).filter(admin_model.AcademicYear.year_id == year_id).first()
    if db_academic_year is None:
        raise HTTPException(status_code=404, detail="AcademicYear not found")
    return db_academic_year

# Update AcademicYear
@app4.put("/academic_years/{year_id}", response_model=admin_schema.AcademicYear)
def update_academic_year(year_id: int, academic_year: admin_schema.AcademicYearCreate, db: Session = Depends(get_db)):
    db_academic_year = db.query(admin_model.AcademicYear).filter(admin_model.AcademicYear.year_id == year_id).first()
    if db_academic_year:
        for key, value in academic_year.dict().items():
            setattr(db_academic_year, key, value)
        db.commit()
        db.refresh(db_academic_year)
        return db_academic_year
    else:
        raise HTTPException(status_code=404, detail="AcademicYear not found")

# Delete AcademicYear
@app4.delete("/academic_years/{year_id}")
def delete_academic_year(year_id: int, db: Session = Depends(get_db)):
    db_academic_year = db.query(admin_model.AcademicYear).filter(admin_model.AcademicYear.year_id == year_id).first()
    if db_academic_year:
        db.delete(db_academic_year)
        db.commit()
        return {"message": "AcademicYear deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="AcademicYear not found")
    
# Create SchoolSetting
@app4.post("/school_settings/", response_model=admin_schema.SchoolSetting)
def create_school_setting(school_setting: admin_schema.SchoolSettingCreate, db: Session = Depends(get_db)):
    db_school_setting = admin_model.SchoolSetting(**school_setting.dict())
    db.add(db_school_setting)
    db.commit()
    db.refresh(db_school_setting)
    return db_school_setting

# Read SchoolSetting by ID
@app4.get("/school_settings/{setting_id}", response_model=admin_schema.SchoolSetting)
def read_school_setting(setting_id: int, db: Session = Depends(get_db)):
    db_school_setting = db.query(admin_model.SchoolSetting).filter(admin_model.SchoolSetting.setting_id == setting_id).first()
    if db_school_setting is None:
        raise HTTPException(status_code=404, detail="SchoolSetting not found")
    return db_school_setting

# Update SchoolSetting
@app4.put("/school_settings/{setting_id}", response_model=admin_schema.SchoolSetting)
def update_school_setting(setting_id: int, school_setting: admin_schema.SchoolSettingCreate, db: Session = Depends(get_db)):
    db_school_setting = db.query(admin_model.SchoolSetting).filter(admin_model.SchoolSetting.setting_id == setting_id).first()
    if db_school_setting:
        for key, value in school_setting.dict().items():
            setattr(db_school_setting, key, value)
        db.commit()
        db.refresh(db_school_setting)
        return db_school_setting
    else:
        raise HTTPException(status_code=404, detail="SchoolSetting not found")

# Delete SchoolSetting
@app4.delete("/school_settings/{setting_id}")
def delete_school_setting(setting_id: int, db: Session = Depends(get_db)):
    db_school_setting = db.query(admin_model.SchoolSetting).filter(admin_model.SchoolSetting.setting_id == setting_id).first()
    if db_school_setting:
        db.delete(db_school_setting)
        db.commit()
        return {"message": "SchoolSetting deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="SchoolSetting not found")

# Create CalendarEvent
@app4.post("/calendar_events/", response_model=admin_schema.CalendarEvent)
def create_calendar_event(calendar_event: admin_schema.CalendarEventCreate, db: Session = Depends(get_db)):
    db_calendar_event = admin_model.CalendarEvent(**calendar_event.dict())
    db.add(db_calendar_event)
    db.commit()
    db.refresh(db_calendar_event)
    return db_calendar_event

# Read CalendarEvent by ID
@app4.get("/calendar_events/{event_id}", response_model=admin_schema.CalendarEvent)
def read_calendar_event(event_id: int, db: Session = Depends(get_db)):
    db_calendar_event = db.query(admin_model.CalendarEvent).filter(admin_model.CalendarEvent.event_id == event_id).first()
    if db_calendar_event is None:
        raise HTTPException(status_code=404, detail="CalendarEvent not found")
    return db_calendar_event

# Update CalendarEvent
@app4.put("/calendar_events/{event_id}", response_model=admin_schema.CalendarEvent)
def update_calendar_event(event_id: int, calendar_event: admin_schema.CalendarEventCreate, db: Session = Depends(get_db)):
    db_calendar_event = db.query(admin_model.CalendarEvent).filter(admin_model.CalendarEvent.event_id == event_id).first()
    if db_calendar_event:
        for key, value in calendar_event.dict().items():
            setattr(db_calendar_event, key, value)
        db.commit()
        db.refresh(db_calendar_event)
        return db_calendar_event
    else:
        raise HTTPException(status_code=404, detail="CalendarEvent not found")

# Delete CalendarEvent
@app4.delete("/calendar_events/{event_id}")
def delete_calendar_event(event_id: int, db: Session = Depends(get_db)):
    db_calendar_event = db.query(admin_model.CalendarEvent).filter(admin_model.CalendarEvent.event_id == event_id).first()
    if db_calendar_event:
        db.delete(db_calendar_event)
        db.commit()
        return {"message": "CalendarEvent deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="CalendarEvent not found")