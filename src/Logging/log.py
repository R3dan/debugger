import os
import typing
import enum
from datetime import date, time, datetime as dt
import time as tm
from typing import Any
import json


class Log:
    _default_level = 1

    def __init__(self, _default_level=_default_level) -> None:
        self.logs = []
        self._default_level = _default_level

    def log(self, level, notes):
        def log_decorater(func):
            def log_wrapper(*args, **kwargs):
                self.add_log(Log =Event_Log(level=level, notes=notes, func=func))
                func(*args, **kwargs)
                return func
            return log_wrapper
        return log_decorater
    
    def add_log(self, Log):
        if int(Log.level) > 2:
            print(f"====== DEBUGGER ======\n\nEvent\n    Level: {Log.level}\n    Function: {Log.func}\n    Notes: {Log.notes}\n    Time: {Log.time}\n    Date: {Log.date}")
        self.logs.append(Log)

    def print(self):
        for log in self.logs:
            print(str(log.level) + "     " + str(log.notes) + "       " + str(log.func) + "       " + str(log.time) + "       " + str(log.date))




    def dict(self, filter: typing.Union[None, list] = None):
        _dict = []
        for log in self.logs:
            x = {"Level":log.level,
                 "Notes":log.notes,
                 "Function":log.func,
                 "Datetime":{
                     "Time": log.time,
                     "Date": log.date
                    }
                 }
            _dict.append(x)
        return _dict



class Event_Log:
    def __init__(self, level, notes, func="", time = "", date = ""):
        self.level = level
        self.notes = notes
        self.func = func
        DtTime = [dt.now().hour, dt.now().minute, dt.now().second, dt.now().microsecond]
        self.time = time or DtTime
        DtDate=[dt.now().day, dt.now().month, dt.now().year]
        self.date = date or DtDate


def log(level, notes, time = "", date = ""):
    Log = Event_Log(level, notes, time=time, date=date)
    return Log




logger = Log(3)

@logger.log(3,"ABS")
def function(number):
    return number


function(3)