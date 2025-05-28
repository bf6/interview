from ninja import NinjaAPI
from datetime import date, datetime, time
from typing import Optional

from employees.models import Employee, TimeEntry
from employees.schemas import TimeEntrySchema

time_entries_api = NinjaAPI(urls_namespace="time-entries")
