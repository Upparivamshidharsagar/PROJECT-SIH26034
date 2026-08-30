[17:25, 30/08/2026] Vaishnavi: from pydantic import BaseModel


class ActionRequest(BaseModel):
    action: str
    value: float


class ActionResponse(BaseModel):
    allowed: bool
    executed: bool
    action: str
    value: float
    reason: str

