from dataclasses import dataclass

@dataclass
class ValidateTokenQuery:
    access_token: str
