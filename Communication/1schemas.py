# from pydantic import BaseModel
# from typing import Optional
# from datetime import datetime

# # Teacher schema
# class TeacherBase(BaseModel):
#     name: str
#     email: str

# class TeacherCreate(TeacherBase):
#     pass

# class Teacher(TeacherBase):
#     id: int
#     created_at: datetime
#     last_updated_at: datetime

#     class Config:
#         orm_mode = True

# # SMSTemplate schema
# class SMSTemplateBase(BaseModel):
#     template_name: str
#     message_content: str
#     category: str
#     created_by: int
#     last_updated_by: int

# class SMSTemplateCreate(SMSTemplateBase):
#     pass

# class SMSTemplate(SMSTemplateBase):
#     id: int
#     created_at: datetime
#     last_updated_at: datetime

#     class Config:
#         orm_mode = True

# # SentSMSMessage schema
# class SentSMSMessageBase(BaseModel):
#     sender_id: int
#     recipient_type: str
#     recipient_id: int
#     template_id: int
#     message_content: str

# class SentSMSMessageCreate(SentSMSMessageBase):
#     pass

# class SentSMSMessage(SentSMSMessageBase):
#     id: int
#     timestamp: datetime

#     class Config:
#         orm_mode = True

# # DeliveryStatus schema
# class DeliveryStatusBase(BaseModel):
#     message_id: int
#     recipient_type: str
#     recipient_id: int
#     delivery_status: str

# class DeliveryStatusCreate(DeliveryStatusBase):
#     pass

# class DeliveryStatus(DeliveryStatusBase):
#     id: int
#     delivery_time: datetime

#     class Config:
#         orm_mode = True

# # Group schema
# class GroupBase(BaseModel):
#     group_name: str
#     group_type: str
#     created_by: int
#     last_updated_by: int

# class GroupCreate(GroupBase):
#     pass

# class Group(GroupBase):
#     id: int
#     created_at: datetime
#     last_updated_at: datetime

#     class Config:
#         orm_mode = True

# # GroupMembership schema
# class GroupMembershipBase(BaseModel):
#     group_id: int
#     member_type: str
#     member_id: int

# class GroupMembershipCreate(GroupMembershipBase):
#     pass

# class GroupMembership(GroupMembershipBase):
#     id: int

#     class Config:
#         orm_mode = True
