from pydantic import BaseModel

class CustomerDetails(BaseModel):

    # Customer Information
    age: int
    job: str
    marital: str
    education: str
    default: str

    # Financial Information
    balance: int
    housing: str
    loan: str

    # Contact Information
    contact: str
    day: int
    month: str

    # Campaign Information
    duration: int
    campaign: int
    pdays: int
    previous: int
    poutcome: str
    