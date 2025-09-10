from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import AnalyzeRequest, ChartDataRequest, Suggestion
from core.storage import save_dataframe, get_dataframe
from core.analysis import dataframe_from_upload, build_schema_summary, aggregate_for_chart
from core.llm import suggest_charts

app = FastAPI(title="Instant Analytics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

@app.post("/api/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    df = dataframe_from_upload(content, file.filename)
    upload_id = save_dataframe(df)
    return {"upload_id": upload_id, "filename": file.filename}

@app.post("/api/analyze")
async def analyze(payload: AnalyzeRequest):
    df = get_dataframe(payload.upload_id)
    summary = build_schema_summary(df)
    suggestions = suggest_charts(llm_client=None, schema_summary=summary)
    return {"suggestions": [Suggestion(**s).model_dump() for s in suggestions]}

@app.post("/api/chart-data")
async def chart_data(payload: ChartDataRequest):
    df = get_dataframe(payload.upload_id)
    data = aggregate_for_chart(df, payload.parameters)
    return {"data": data}
