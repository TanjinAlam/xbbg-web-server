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
    adjust: Optional[str] = None
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
    
    
class RequestDataBDS(BaseModel):
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
    


class RequestDataBDIB(BaseModel):
     # Calculate default dates one week prior
    default_start_date: ClassVar[datetime] = datetime.now() - timedelta(weeks=2)
    
    ticker_name: str = Field(
        ...,
        example="BHP AU Equity",
    )
    session: Optional[str] = None
    query_type: Optional[str] = None
    date: str = Field(
        default=default_start_date.strftime('%Y-%m-%d'),
        description="Date in 'yyyy-mm-dd' format (e.g., '2023-11-08')",
        example="yyy-mm-dd",
    )
    
    

class RequestDataEarning(BaseModel):
     # Calculate default dates one week prior
    default_start_date: ClassVar[datetime] = datetime.now() - timedelta(weeks=2)
    
    ticker_name: str = Field(
        ...,
        example="BHP AU Equity",
    )
    by: str  = Field(
        ...,
        example="Geo",
    )
    query_type: str = Field(
        ...,
        example="Revenue",
    )
    currency: Optional[str] = None
    level: Optional[str] = None
    date: Optional[int] = Field(
        default=default_start_date.strftime('%Y'),
        description="Date in 'yyyy' format (e.g., '2020')",
        example="2018",
    )
    period: Optional[int] = Field(
        example=1,
    )
   
    
    


class RequestDataDividend(BaseModel):
     # Calculate default dates one week prior
    default_start_date: ClassVar[datetime] = datetime.now() - timedelta(weeks=1)
    default_end_date: ClassVar[datetime] = datetime.now()
    
    tickers_name: List[str] = Field(
        ...,
        # example="['AAPL US Equity', 'NVDA US Equity']",
    )
    query_type: str = Field(
        ...,
        example="all",
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
    