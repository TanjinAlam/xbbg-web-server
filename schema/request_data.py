from pydantic import BaseModel, field_validator, Field
from datetime import datetime, timedelta
from typing import Union, Optional, List
from typing import ClassVar


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
     # Calculate default dates one week prior
    default_start_date: ClassVar[datetime] = datetime.now() - timedelta(weeks=1)
    default_end_date: ClassVar[datetime] = datetime.now()
    
    tickers_name: List[str] = Field(
        ...,
        # example="['AAPL US Equity', 'NVDA US Equity']",
    )
    fields_name: List[str] = Field(
        ...,
        # example="['Security_Name', 'GICS_Sector_Name']",
    )
    start_date: str = Field(
        default=default_start_date.strftime('%Y-%m-%d'),
        description="Date in 'yyyy-mm-dd' format (e.g., '2023-11-08')",
        example="yyy-mm-dd",
    )
    end_date: str = Field(
        default=default_end_date.strftime('%Y-%m-%d'),
        description="Date in 'yyyy-mm-dd' format (e.g., '2023-11-08')",
        example="yyy-mm-dd",
    )

    
    
    
