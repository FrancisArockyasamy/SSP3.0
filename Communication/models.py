from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class SMS_Templates(Base):
    __tablename__ = "tbl_sms_templates"

    template_id = Column(Integer, primary_key=True)
    template_name = Column(String, unique=True)
    template_content = Column(String)
    template_type = Column(String)


class SMS_Messages(Base):
    __tablename__ = "tbl_sms_messages"

    message_id = Column(Integer, primary_key=True, index=True)
    template_id = Column(Integer, ForeignKey("tbl_sms_templates.template_id"))
    sender_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    recipient_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    message_content = Column(String)
    timestamp = Column(String)
    delivery_status = Column(String)

    template = relationship("SMS_Templates")
    sender = relationship("Users", foreign_keys=[sender_id])
    recipient = relationship("Users", foreign_keys=[recipient_id])

class Users(Base):
    __tablename__ = "tbl_users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_type = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phone_number = Column(String)

    groups = relationship("Groups", secondary="user_groups")
    messages_sent = relationship("SMS_Messages", foreign_keys=[SMS_Messages.sender_id])
    messages_received = relationship("SMS_Messages", foreign_keys=[SMS_Messages.recipient_id])
    attendance_records = relationship("Attendance")
    timetable_entries = relationship("Timetable")
    exam_entries = relationship("Exam")
    fee_reminders = relationship("Fee_Reminder")
    remarks = relationship("Remarks")
    ptm_notifications = relationship("PTM_Notification")
    left_students = relationship("Left_Students")
    alumni = relationship("Alumni")

class Groups(Base):
    __tablename__ = "tbl_groups"

    group_id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String)
    group_type = Column(String)

    members = relationship("Users", secondary="user_groups")

class User_Groups(Base):
    __tablename__ = "tbl_user_groups"

    user_id = Column(Integer, ForeignKey("tbl_users.user_id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("tbl_groups.group_id"), primary_key=True)

class Notifications(Base):
    __tablename__ = "tbl_notifications"

    notification_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    notification_type = Column(String)
    notification_content = Column(String)
    timestamp = Column(String)

    user = relationship("Users")

class Homework(Base):
    __tablename__ = "tbl_homework"

    homework_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    homework_type = Column(String)
    homework_content = Column(String)
    deadline = Column(Date)

    user = relationship("Users")

class Attendance(Base):
    __tablename__ = "tbl_attendance"

    attendance_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    date = Column(Date)
    status = Column(String)

    user = relationship("Users")

class Timetable(Base):
    __tablename__ = "tbl_timetable"

    timetable_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    day = Column(String)
    time = Column(String)
    subject = Column(String)

    user = relationship("Users")

class Exam(Base):
    __tablename__ = "tbl_exam"

    exam_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    subject = Column(String)
    portion = Column(String)
    result = Column(String)

    user = relationship("Users")

class FeeReminder(Base):
    __tablename__ = "tbl_fee_reminder"

    reminder_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    amount = Column(Integer)
    due_date = Column(Date)

    user = relationship("Users")

class Remarks(Base):
    __tablename__ = "tbl_remarks"

    remark_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    subject = Column(String)
    remark_content = Column(String)

    user = relationship("Users")

class PTMNotification(Base):
    __tablename__ = "tbl_ptm_notification"

    ptm_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    date = Column(Date)
    notification_content = Column(String)

    user = relationship("Users")

class LeftStudents(Base):
    __tablename__ = "tbl_left_students"

    left_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    reason = Column(String)

    user = relationship("Users")

class Alumni(Base):
    __tablename__ = "tbl_alumni"

    alumni_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("tbl_users.user_id"))
    graduation_year = Column(Integer)
    last_contact_date = Column(Date)

    user = relationship("Users")
