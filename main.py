from fastapi import FastAPI
from Admin import main as admin_main
from Academics import main as academic_main
from Admission.app import main as admission_main
from Alumni import main as alumni_main
from Communication import main as communication_main
from Examination.app import main as examination_main
from Fee import main as fee_main
from Feedback import main as feedback_main
from Front_office import main as front_office_main
from Homework import main as homework_main
from Id_card import main as id_card_main
from Inventory import main as inventory_main
from Lesson_plan import main as lesson_plan_main
from Payroll import main as payroll_main
from Staff_attendance import main as staff_attendance_main
from Student_attendance import main as student_attendance_main
from Student_portal import main as student_portal_main
from Timetable import main as timetable_main
from Transport import main as transport_main

from fastapi.middleware.cors import CORSMiddleware

app= FastAPI(
    title="SSP-3.0 API"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"]
)


service= [admin_main, academic_main, admission_main, alumni_main, communication_main,
        examination_main, feedback_main, front_office_main, homework_main, id_card_main,
        inventory_main, lesson_plan_main, payroll_main, staff_attendance_main, student_attendance_main,
        student_portal_main, timetable_main, transport_main, fee_main
]
for i in service:
    app.include_router(i.app)
