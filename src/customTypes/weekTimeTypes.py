from __future__ import annotations

class duration:
    days: int
    hours: int
    minutes: int

    def __init__(self, days: int, hours: int, minutes: int):
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'{self.days} days, {self.hours} hours, {self.minutes} minutes'

class weekTime:
    '''
    implemets a weekly time. Stores the day (Monday to Sunday), and time
    '''
    def __init__(self, dayNum: int = 0, hour: int = 0, minute: int = 0):
        if dayNum < 0 or dayNum >= 7:
            raise ValueError(f'invalid dayNum = {dayNum}. dayNum should be an integer between 0 and 6 (inclusive).')
        if hour < 0 or hour >= 24:
            raise ValueError(f'invalid hour = {hour}. hour should be an integer between 0 and 23 (inclusive).')
        if minute < 0 or minute >= 60:
            raise ValueError(f'invalid minute = {minute}. minute should be an integer between 0 and 59 (inclusive).')
        
        # no errors at this point
        self.dayNum = dayNum
        self.hour = hour
        self.minute = minute

    dayNum: int
    hour: int
    minute: int

    # methods
    def timeMinus(self, otherTime: weekTime) -> duration:
        '''
        calculates the time between this weektime to 'otherTime' weektime. Assumes 
        that current weekTime is after 'otherTime', ie: currentTime - otherTime
        '''
        toMinus: int = 0

        minutes: int = self.minute - otherTime.minute
        if (minutes < 0):
            toMinus = 1
            minutes += 60
        
        hours: int = self.hour - otherTime.hour - toMinus
        if (hours < 0):
            toMinus = 1
            hours += 24
        else:
            toMinus = 0
        
        days: int = (self.dayNum - otherTime.dayNum - toMinus + 7) % 7
        return duration(days, hours, minutes)
