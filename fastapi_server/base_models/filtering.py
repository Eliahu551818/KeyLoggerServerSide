from pydantic import BaseModel
from typing import Optional

# Define a Pydantic model for the filter parameters
class LogFilter(BaseModel):
    from_date: Optional[str] = None  # e.g., "2025-01-01"
    to_date: Optional[str] = None    # e.g., "2025-02-26"
    window: Optional[str] = None     # e.g., "main"