from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class AuthToken:
    access_token: str
    refresh_token: str
    user_id: int
    expires_at: datetime
