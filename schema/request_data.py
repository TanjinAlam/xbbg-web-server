from pydantic import BaseModel, field_validator, Field
from datetime import datetime
from typing import Union, Optional, List


class RequestDataBDP(BaseModel):
    tickers_name: List[str] = Field(
        ...,
        # example="['AAPL US Equity', 'NVDA US Equity']",
    )
    fields_name: List[str] = Field(
        ...,
        # example="['Security_Name', 'GICS_Sector_Name']",
    )


class RequestDataBDH(BaseModel):
    tickers_name: List[str] = Field(
        ...,
        # example="['AAPL US Equity', 'NVDA US Equity']",
    )
    fields_name: List[str] = Field(
        ...,
        # example="['Security_Name', 'GICS_Sector_Name']",
    )
    start_date: str = Field(
        ...,
        description="Date in 'yyyy-mm-dd' format (e.g., '2023-11-08')",
        example="yyy-mm-dd",
    )
    end_date: str = Field(
        ...,
        description="Date in 'yyyy-mm-dd' format (e.g., '2023-11-08')",
        example="yyy-mm-dd",
    )
