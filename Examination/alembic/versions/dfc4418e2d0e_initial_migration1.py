"""Initial migration1

Revision ID: dfc4418e2d0e
Revises: 86a1c3e67069
Create Date: 2024-05-17 12:48:07.248778

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfc4418e2d0e'
down_revision: Union[str, None] = '86a1c3e67069'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subjects',
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('subject_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('subject_id')
    )
    op.create_index(op.f('ix_subjects_subject_id'), 'subjects', ['subject_id'], unique=False)
    op.create_table('examinations',
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('exam_name', sa.String(), nullable=False),
    sa.Column('exam_type', sa.String(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=False),
    sa.Column('grading_system', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['class_id'], ['classes.class_id'], ),
    sa.PrimaryKeyConstraint('exam_id')
    )
    op.create_index(op.f('ix_examinations_exam_id'), 'examinations', ['exam_id'], unique=False)
    op.create_table('co_curricular_grades',
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('activity_name', sa.String(), nullable=False),
    sa.Column('grade', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('grade_id')
    )
    op.create_index(op.f('ix_co_curricular_grades_grade_id'), 'co_curricular_grades', ['grade_id'], unique=False)
    op.create_table('exam_attendance',
    sa.Column('attendance_id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('attendance_status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['examinations.exam_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('attendance_id')
    )
    op.create_index(op.f('ix_exam_attendance_attendance_id'), 'exam_attendance', ['attendance_id'], unique=False)
    op.create_table('exam_settings',
    sa.Column('setting_id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('mark_entry_method', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['examinations.exam_id'], ),
    sa.PrimaryKeyConstraint('setting_id')
    )
    op.create_index(op.f('ix_exam_settings_setting_id'), 'exam_settings', ['setting_id'], unique=False)
    op.create_table('exam_subjects',
    sa.Column('exam_subject_id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['examinations.exam_id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.subject_id'], ),
    sa.PrimaryKeyConstraint('exam_subject_id')
    )
    op.create_index(op.f('ix_exam_subjects_exam_subject_id'), 'exam_subjects', ['exam_subject_id'], unique=False)
    op.create_table('hall_tickets',
    sa.Column('hall_ticket_id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('generated_ticket', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['examinations.exam_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('hall_ticket_id')
    )
    op.create_index(op.f('ix_hall_tickets_hall_ticket_id'), 'hall_tickets', ['hall_ticket_id'], unique=False)
    op.create_table('optional_subjects',
    sa.Column('option_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.subject_id'], ),
    sa.PrimaryKeyConstraint('option_id')
    )
    op.create_index(op.f('ix_optional_subjects_option_id'), 'optional_subjects', ['option_id'], unique=False)
    op.create_table('physical_metrics',
    sa.Column('metric_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('metric_id')
    )
    op.create_index(op.f('ix_physical_metrics_metric_id'), 'physical_metrics', ['metric_id'], unique=False)
    op.create_table('progress_cards',
    sa.Column('progress_card_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('template_id', sa.Integer(), nullable=False),
    sa.Column('generated_card', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['examinations.exam_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('progress_card_id')
    )
    op.create_index(op.f('ix_progress_cards_progress_card_id'), 'progress_cards', ['progress_card_id'], unique=False)
    op.create_table('results',
    sa.Column('result_id', sa.Integer(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('result_status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['examinations.exam_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('result_id')
    )
    op.create_index(op.f('ix_results_result_id'), 'results', ['result_id'], unique=False)
    op.create_table('marks',
    sa.Column('mark_id', sa.Integer(), nullable=False),
    sa.Column('exam_subject_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('marks', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exam_subject_id'], ['exam_subjects.exam_subject_id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.PrimaryKeyConstraint('mark_id')
    )
    op.create_index(op.f('ix_marks_mark_id'), 'marks', ['mark_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_marks_mark_id'), table_name='marks')
    op.drop_table('marks')
    op.drop_index(op.f('ix_results_result_id'), table_name='results')
    op.drop_table('results')
    op.drop_index(op.f('ix_progress_cards_progress_card_id'), table_name='progress_cards')
    op.drop_table('progress_cards')
    op.drop_index(op.f('ix_physical_metrics_metric_id'), table_name='physical_metrics')
    op.drop_table('physical_metrics')
    op.drop_index(op.f('ix_optional_subjects_option_id'), table_name='optional_subjects')
    op.drop_table('optional_subjects')
    op.drop_index(op.f('ix_hall_tickets_hall_ticket_id'), table_name='hall_tickets')
    op.drop_table('hall_tickets')
    op.drop_index(op.f('ix_exam_subjects_exam_subject_id'), table_name='exam_subjects')
    op.drop_table('exam_subjects')
    op.drop_index(op.f('ix_exam_settings_setting_id'), table_name='exam_settings')
    op.drop_table('exam_settings')
    op.drop_index(op.f('ix_exam_attendance_attendance_id'), table_name='exam_attendance')
    op.drop_table('exam_attendance')
    op.drop_index(op.f('ix_co_curricular_grades_grade_id'), table_name='co_curricular_grades')
    op.drop_table('co_curricular_grades')
    op.drop_index(op.f('ix_examinations_exam_id'), table_name='examinations')
    op.drop_table('examinations')
    op.drop_index(op.f('ix_subjects_subject_id'), table_name='subjects')
    op.drop_table('subjects')
    # ### end Alembic commands ###
