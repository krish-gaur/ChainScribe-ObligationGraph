from datetime import date, datetime
from enum import Enum
from uuid import UUID, uuid4
from fastapi import FastAPI, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

app = FastAPI(title="ChainScribe Enterprise API", version="0.1.0", description="Contract intelligence control plane")

class RiskLevel(str, Enum):
    low="low"; medium="medium"; high="high"; critical="critical"
class Obligation(BaseModel):
    id: UUID = Field(default_factory=uuid4); title: str; owner: str | None = None
    due_date: date | None = None; risk: RiskLevel = RiskLevel.medium; status: str = "open"
class Contract(BaseModel):
    id: UUID = Field(default_factory=uuid4); name: str; counterparty: str; value: float
    effective_date: date; renewal_date: date | None = None; obligations: list[Obligation] = []
class CopilotQuery(BaseModel): query: str

contracts: dict[UUID, Contract] = {}

@app.get("/health")
def health(): return {"status":"ok", "timestamp":datetime.utcnow()}

@app.post("/v1/contracts/upload", status_code=202)
async def upload_contract(file: UploadFile = File(...)):
    allowed={"application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "image/png", "image/jpeg"}
    if file.content_type not in allowed: raise HTTPException(415, "PDF, DOCX, PNG, or JPEG required")
    contract_id=uuid4()
    # Production: persist blob -> emit contract_uploaded -> async extraction LangGraph.
    return {"contract_id":contract_id, "status":"processing", "event":"contract_uploaded", "filename":file.filename}

@app.get("/v1/dashboard")
def dashboard():
    return {"portfolio_value":18600000,"renewals_in_90_days":14,"risk_score":68,"compliance_health":92,"vendor_exposure":4.8}

@app.get("/v1/contracts", response_model=list[Contract])
def list_contracts(): return list(contracts.values())

@app.get("/v1/contracts/{contract_id}/graph")
def contract_graph(contract_id: UUID):
    if contract_id not in contracts: raise HTTPException(404, "Contract not found")
    c=contracts[contract_id]
    return {"nodes":[{"id":str(c.id),"type":"Contract","label":c.name},{"id":"vendor","type":"Vendor","label":c.counterparty}],"edges":[{"source":"vendor","target":str(c.id),"type":"HAS_CONTRACT"}]}

@app.get("/v1/risks")
def risks():
    return [{"id":"risk-07","kind":"unassigned_obligation","severity":"critical","contract":"MSA · Microsoft Azure","recommendation":"Assign SLA reporting owner before 18 Jul."}]

@app.post("/v1/copilot")
def copilot(body: CopilotQuery):
    return {"answer":"I found 14 contracts renewing within 90 days; 3 have elevated risk.","citations":[],"graph_query":"MATCH (c:Contract)-[:HAS_DEADLINE]->(d) WHERE d.date < date() + duration('P90D') RETURN c"}
