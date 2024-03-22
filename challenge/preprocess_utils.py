"""
This module contains utility functions for preprocessing data.
"""

from datetime import datetime

import pandas as pd


def get_period_day(date: str) -> str:
    """
    Get period of the day from a date.

    Parameters
    ----------
    date : str
        Date in format '%Y-%m-%d %H:%M:%S'.

    Returns
    -------
    str
        Period of the day ('mañana', 'tarde', 'noche').
    """
    date_time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").time()
    morning_min = datetime.strptime("05:00", "%H:%M").time()
    morning_max = datetime.strptime("11:59", "%H:%M").time()
    afternoon_min = datetime.strptime("12:00", "%H:%M").time()
    afternoon_max = datetime.strptime("18:59", "%H:%M").time()
    evening_min = datetime.strptime("19:00", "%H:%M").time()
    evening_max = datetime.strptime("23:59", "%H:%M").time()
    night_min = datetime.strptime("00:00", "%H:%M").time()
    night_max = datetime.strptime("4:59", "%H:%M").time()

    if morning_max > date_time > morning_min:
        return "mañana"
    if afternoon_max > date_time > afternoon_min:
        return "tarde"
    if (evening_max > date_time > evening_min) or (night_max > date_time > night_min):
        return "noche"
    raise ValueError(f"Invalid date {date_time}")


def is_high_season(fecha: str) -> int:
    """
    Check if a date is in high season.

    Parameters
    ----------
    fecha : str
        Date in format '%Y-%m-%d %H:%M:%S'.

    Returns
    -------
    int
        1 if the date is in high season, 0 otherwise.
    """
    fecha_anio = int(fecha.split("-")[0])
    fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
    range1_min = datetime.strptime("15-Dec", "%d-%b").replace(year=fecha_anio)
    range1_max = datetime.strptime("31-Dec", "%d-%b").replace(year=fecha_anio)
    range2_min = datetime.strptime("1-Jan", "%d-%b").replace(year=fecha_anio)
    range2_max = datetime.strptime("3-Mar", "%d-%b").replace(year=fecha_anio)
    range3_min = datetime.strptime("15-Jul", "%d-%b").replace(year=fecha_anio)
    range3_max = datetime.strptime("31-Jul", "%d-%b").replace(year=fecha_anio)
    range4_min = datetime.strptime("11-Sep", "%d-%b").replace(year=fecha_anio)
    range4_max = datetime.strptime("30-Sep", "%d-%b").replace(year=fecha_anio)

    if (
        (range1_max >= fecha >= range1_min)
        or (range2_max >= fecha >= range2_min)
        or (range3_max >= fecha >= range3_min)
        or (range4_max >= fecha >= range4_min)
    ):
        return 1
    return 0


def get_min_diff(data: pd.Series) -> float:
    """
    Get the difference in minutes between two dates.

    Parameters
    ----------
    data : pd.Series
        Series with two dates in format '%Y-%m-%d %H:%M:%S'.

    Returns
    -------
    float
        Difference in minutes.
    """
    fecha_o = datetime.strptime(data["Fecha-O"], "%Y-%m-%d %H:%M:%S")
    fecha_i = datetime.strptime(data["Fecha-I"], "%Y-%m-%d %H:%M:%S")
    min_diff = ((fecha_o - fecha_i).total_seconds()) / 60
    return min_diff
