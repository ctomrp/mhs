from django.db import connection

# from django.utils import timezone

from .models import Appointment


def fetch_appointments_by_professional(professional_id) -> list["Appointment"]:
    appointments_collection = Appointment.objects.filter(
        professional_id=professional_id
    )
    return [appointments for appointments in appointments_collection]


def fetch_appointments_by_date(date) -> list["Appointment"]:
    appointments_collection = Appointment.objects.filter(attendance_date=date)
    return [appointments for appointments in appointments_collection]


def fetch_appointments_by_date_range(date_range) -> list["Appointment"]:
    begin_date, end_date = map(str, date_range.split(","))
    query = """SELECT * FROM appointments_appointment WHERE julianday(attendance_date) BETWEEN julianday(%s) AND julianday(%s);"""
    appointments_collection = Appointment.objects.raw(query, [begin_date, end_date])
    return [appointments for appointments in appointments_collection]


def count_appointments_by_professional(professional_id) -> int:
    total = Appointment.objects.filter(professional_id=professional_id).count()
    return total


def count_appointments_by_date_range(date_range) -> int:
    begin_date, end_date = map(str, date_range.split("$"))
    query = """SELECT COUNT(*) as count FROM appointments_appointment WHERE julianday(attendance_date) BETWEEN julianday(%s) AND julianday(%s);"""
    with connection.cursor() as cursor:
        cursor.execute(query, [begin_date, end_date])
        total = cursor.fetchone()
    return total[0] if total else 0


# def fetch_daily_report(request) -> list["Appointment"]:
#     professional = request.user
#     today = timezone.now().date()
#     appointments_collection = Appointment.objects.filter(
#         professional=professional, attendance_date=today, attended=True
#     )
#     return [appointments for appointments in appointments_collection]
