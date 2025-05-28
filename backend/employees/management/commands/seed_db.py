import datetime

from django.core.management.base import BaseCommand
from datetime import timezone

from employees.models import Employee, TimeEntry
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Seeds the database with initial data for Employees and TimeEntries"

    def handle(self, *args, **options):
        # We'll add the logic to create employees and time entries here
        self.stdout.write(self.style.SUCCESS("Starting database seeding..."))

        # Get or create an admin superuser
        user, created = User.objects.get_or_create(
            username="admin",
            email="admin@example.com",
            is_superuser=True,
            is_staff=True,
        )
        user.set_password("admin")
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("Created admin superuser"))
        else:
            self.stdout.write(self.style.SUCCESS("Admin superuser already exists"))

        # Create Employees using get_or_create
        self.stdout.write("Getting or Creating Employees...")
        employee1, created1 = Employee.objects.get_or_create(name="Alice Smith")
        if created1:
            self.stdout.write(f"Created employee: {employee1.name}")
        else:
            self.stdout.write(f"Found existing employee: {employee1.name}")

        employee2, created2 = Employee.objects.get_or_create(name="Bob Johnson")
        if created2:
            self.stdout.write(f"Created employee: {employee2.name}")
        else:
            self.stdout.write(f"Found existing employee: {employee2.name}")

        employee3, created3 = Employee.objects.get_or_create(name="Charlie Brown")
        if created3:
            self.stdout.write(f"Created employee: {employee3.name}")
        else:
            self.stdout.write(f"Found existing employee: {employee3.name}")

        # Create Time Entries
        self.stdout.write("Getting or Creating Time Entries...")

        # Time entries for Alice
        entry1_start = datetime.datetime(
            2024, 1, 10, 8, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry1_end = datetime.datetime(
            2024, 1, 10, 9, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry1_desc = "Worked on project X documentation"
        time_entry1, created_te1 = TimeEntry.objects.get_or_create(
            employee=employee1,
            start_dt=entry1_start,
            end_dt=entry1_end,
            description=entry1_desc,
            defaults={
                "employee": employee1,
                "start_dt": entry1_start,
                "end_dt": entry1_end,
                "description": entry1_desc,
            },
        )
        if created_te1:
            self.stdout.write(f"Created time entry for {employee1.name}: {entry1_desc}")
        else:
            self.stdout.write(
                f"Found existing time entry for {employee1.name}: {entry1_desc}"
            )

        entry2_start = datetime.datetime(
            2024, 1, 11, 10, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry2_end = datetime.datetime(
            2024, 1, 11, 13, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry2_desc = "Client meeting and follow-up actions"
        time_entry2, created_te2 = TimeEntry.objects.get_or_create(
            employee=employee1,
            start_dt=entry2_start,
            end_dt=entry2_end,
            description=entry2_desc,
            defaults={
                "employee": employee1,
                "start_dt": entry2_start,
                "end_dt": entry2_end,
                "description": entry2_desc,
            },
        )
        if created_te2:
            self.stdout.write(f"Created time entry for {employee1.name}: {entry2_desc}")
        else:
            self.stdout.write(
                f"Found existing time entry for {employee1.name}: {entry2_desc}"
            )

        # Time entries for Bob
        entry3_start = datetime.datetime(
            2024, 1, 12, 9, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry3_end = datetime.datetime(
            2024, 1, 12, 13, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry3_desc = "Development work on feature Y"
        time_entry3, created_te3 = TimeEntry.objects.get_or_create(
            employee=employee2,
            start_dt=entry3_start,
            end_dt=entry3_end,
            description=entry3_desc,
            defaults={
                "employee": employee2,
                "start_dt": entry3_start,
                "end_dt": entry3_end,
                "description": entry3_desc,
            },
        )
        if created_te3:
            self.stdout.write(f"Created time entry for {employee2.name}: {entry3_desc}")
        else:
            self.stdout.write(
                f"Found existing time entry for {employee2.name}: {entry3_desc}"
            )

        entry4_start = datetime.datetime(
            2024, 1, 9, 14, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry4_end = datetime.datetime(
            2024, 1, 9, 16, 30, 0, tzinfo=datetime.timezone.utc
        )
        entry4_desc = "Code review for sprint 2"
        time_entry4, created_te4 = TimeEntry.objects.get_or_create(
            employee=employee2,
            start_dt=entry4_start,
            end_dt=entry4_end,
            description=entry4_desc,
            defaults={
                "employee": employee2,
                "start_dt": entry4_start,
                "end_dt": entry4_end,
                "description": entry4_desc,
            },
        )
        if created_te4:
            self.stdout.write(f"Created time entry for {employee2.name}: {entry4_desc}")
        else:
            self.stdout.write(
                f"Found existing time entry for {employee2.name}: {entry4_desc}"
            )

        # Time entries for Charlie
        entry5_start = datetime.datetime(
            2024, 1, 7, 10, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry5_end = datetime.datetime(
            2024, 1, 7, 14, 0, 0, tzinfo=datetime.timezone.utc
        )
        entry5_desc = "Research on new technologies"
        time_entry5, created_te5 = TimeEntry.objects.get_or_create(
            employee=employee3,
            start_dt=entry5_start,
            end_dt=entry5_end,
            description=entry5_desc,
            defaults={
                "employee": employee3,
                "start_dt": entry5_start,
                "end_dt": entry5_end,
                "description": entry5_desc,
            },
        )
        if created_te5:
            self.stdout.write(f"Created time entry for {employee3.name}: {entry5_desc}")
        else:
            self.stdout.write(
                f"Found existing time entry for {employee3.name}: {entry5_desc}"
            )

        self.stdout.write(
            f"Processed {TimeEntry.objects.count()} time entries in total."
        )

        self.stdout.write(self.style.SUCCESS("Successfully seeded database!"))
