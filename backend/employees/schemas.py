from datetime import datetime, time
from uuid import UUID
from ninja import Schema


class EmployeeSchema(Schema):
    id: UUID
    name: str


class TimeEntrySchema(Schema):
    id: UUID
    employee: EmployeeSchema
    start_dt: datetime
    end_dt: datetime
    description: str
    created_at: datetime
    updated_at: datetime
