from fastapi import APIRouter, Depends
from schemas.survey import SurveyCreateRequest, SurveyCreateResponse
from services.survey_service import save_survey

router = APIRouter()

@router.get("/create_survey", response_model=SurveyCreateResponse)
async def submit_survey(survey: SurveyCreateRequest):
    return await save_survey(survey)
