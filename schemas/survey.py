from pydantic import BaseModel


class SurveyCreateRequest(BaseModel):
    survey_id: str


class SurveyCreateResponse(BaseModel):
    status: str
    message: str
