from pydantic import BaseModel
from typing import Dict

class WheelSpecBase(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: str
    fields: Dict[str, str]

class WheelSpecCreate(WheelSpecBase):
    pass

class WheelSpecResponse(BaseModel):
    success: bool
    message: str
    data: Dict[str, str]



class BogieChecksheetBase(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: str
    bogieDetails: Dict[str, str]
    bogieChecksheet: Dict[str, str]
    bmbcChecksheet: Dict[str, str]

class BogieChecksheetCreate(BogieChecksheetBase):
    pass

class BogieChecksheetResponse(BaseModel):
    success: bool
    message: str
    data: Dict[str, str]
