"""
FastAPI Backend for ScamGuard AI
Connects Rule-Based Engine + Gemini LLM
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent.analyzer import analyze_message
from agent.risk_score import calculate_risk
from agent.explanation import generate_explanation
from agent.llm_engine import llm_analyze

app = FastAPI(title="ScamGuard AI API")

# CORS (frontend access allow)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    message: str
    use_llm: bool = True


@app.post("/analyze")
def analyze(req: MessageRequest):
    analysis = analyze_message(req.message)
    risk = calculate_risk(analysis["count"])
    explanation = generate_explanation(
        analysis["indicators"], risk
    )

    response = {
        "rule_based": explanation
    }

    if req.use_llm:
        response["llm"] = llm_analyze(req.message)
    else:
        response["llm"] = "LLM analysis disabled."

    return response
