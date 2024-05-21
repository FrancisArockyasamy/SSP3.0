from sqlalchemy.orm import Session
import models, schemas
import crud


def get_feedback(db: Session, feedback_id: int):
    return db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()

def get_feedbacks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Feedback).offset(skip).limit(limit).all()

def create_feedback(db: Session, feedback: schemas.FeedbackCreate):
    db_feedback = models.Feedback(title=feedback.title, description=feedback.description, objectives=feedback.objectives)
    db.add(db_feedback)
    db.commit()
    
    for questionnaire in feedback.questionnaires:
        db_questionnaire = models.Questionnaire(question_text=questionnaire.question_text, question_type=questionnaire.question_type, feedback_id=db_feedback.id)
        db.add(db_questionnaire)
        db.commit()
        # db.refresh(db_questionnaire)
    
    return db_feedback

# def create_feedback_response(db: Session, feedback_id: int, response: schemas.FeedbackResponseCreate):
#     with db.begin():
#         db_response = models.FeedbackResponse(participant=response.participant, feedback_id=feedback_id)
#         db.add(db_response)
#         db.commit()
#         db.refresh(db_response)
        
#         feedback = get_feedback(db, feedback_id)
#         if not feedback:
#             raise ValueError("Feedback not found")

#         # Fetch all questions at once to improve performance
#         questions = {question.id: question for question in feedback.questionnaires}
#         for i, answer in enumerate(response.answers):
#             if i not in questions:
#                 raise ValueError("Question not found")

#             db_questionnaire_response = models.QuestionnaireResponse(feedback_response_id=db_response.id, questionnaire_id=questions[i].id, answer=answer)
#             db.add(db_questionnaire_response)
#             db.commit()
#             db.refresh(db_questionnaire_response)
    
#     return db_response

def create_feedback_response(db: Session, feedback_id: int, response: schemas.FeedbackResponseCreate):
    feedback = get_feedback(db, feedback_id)
    if not feedback:
        raise ValueError("Feedback not found")

    if len(response.answers) != len(feedback.questionnaires):
        raise ValueError("Number of answers does not match number of questionnaires")

    return crud.create_feedback_response(db=db, feedback_id=feedback_id, response=response)


def analyze_feedback(db: Session, feedback_id: int):
    feedback = get_feedback(db, feedback_id)
    if not feedback:
        return None
    
    analysis = {}
    for question in feedback.questionnaires:
        responses = db.query(models.QuestionnaireResponse).filter(models.QuestionnaireResponse.questionnaire_id == question.id).all()
        answers = [response.answer for response in responses]
        analysis[question.question_text] = answers  # You can add more complex analysis here
    
    return {"feedback_id": feedback.id, "analysis": analysis}
