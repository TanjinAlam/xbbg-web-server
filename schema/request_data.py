from pydantic import BaseModel, field_validator, Field
from datetime import datetime
from typing import Union, Optional, List


class RequestBody(BaseModel):
    tickers_name: List[str] = Field(
        ...,
        # example="['AAPL US Equity', 'NVDA US Equity']",
    )
    fields_name: List[str] = Field(
        ...,
        # example="['Security_Name', 'GICS_Sector_Name']",
    )
    date_string: str = Field(
        ...,
        description="Date in 'yyyy-mm-dd' format (e.g., '2023-11-08')",
        example="yyy-mm-dd",
    )
