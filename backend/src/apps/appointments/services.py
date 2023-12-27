from django.db.models import Q
from django.db import connection
from django.shortcuts import get_list_or_404, get_object_or_404
from datetime import date

from .models import Appointment


def fetch_appointments_by_professional(professional_id) -> list["Appointment"]:
    appointments_list = Appointment.objects.filter(professional_id=professional_id)
    return [appointments for appointments in appointments_list]


def count_appointments_by_professional(professional_id) -> int:
    total = Appointment.objects.filter(professional_id=professional_id).count()
    return total


def fetch_appointments_by_date(date) -> list["Appointment"]:
    appointments_list = Appointment.objects.filter(attendance_date=date)
    return [appointments for appointments in appointments_list]


def fetch_appointments_by_date_range(date_range):
    begin_date, end_date = map(str, date_range.split(","))
    query = """SELECT * FROM appointments_appointment WHERE julianday(attendance_date) BETWEEN julianday(%s) AND julianday(%s);"""
    results = Appointment.objects.raw(query, [begin_date, end_date])
    appointments = list(results)
    return appointments


def count_appointments_by_date_range(date_range):
    begin_date, end_date = map(str, date_range.split(","))
    query = """SELECT COUNT(*) as count FROM appointments_appointment WHERE julianday(attendance_date) BETWEEN julianday(%s) AND julianday(%s);"""
    with connection.cursor() as cursor:
        cursor.execute(query, [begin_date, end_date])
        result = cursor.fetchone()
    return result[0] if result else 0
