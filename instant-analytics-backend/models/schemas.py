from pydantic import BaseModel
from typing import Literal, Dict

ChartType = Literal['bar','line','pie','scatter','area']

class Suggestion(BaseModel):
    title: str
    chart_type: ChartType
    parameters: Dict[str, str]
    insight: str

class AnalyzeRequest(BaseModel):
    upload_id: str

class ChartDataRequest(BaseModel):
    upload_id: str
    parameters: Dict[str, str]
