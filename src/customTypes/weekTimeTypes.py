from __future__ import annotations

class duration:
    days: int
    hours: int
    minutes: int

    def __init__(self, days: int = 0, hours: int = 0, minutes: int = 0):
        self.days = days
        self.hours = hours
        self.minutes = minutes

    def greaterThan(self, otherDuration: duration) -> bool:
        '''
        returns true if self is strictly greater than some other duration 
        '''
        if self.days > otherDuration.days:
            return True
        if self.days < otherDuration.days:
            return False
        
        # same number of days 
        if self.hours > otherDuration.hours:
            return True
        if self.hours < otherDuration.hours:
            return False
        
        # same number of days and hours
        if self.minutes > otherDuration.minutes:
            return True
        else:
            return False

    def equal(self, otherDuration: duration) -> bool:
        '''
        checks if self is equal to some other duration
        '''
        return (self.days == otherDuration.days and self.hours == otherDuration.hours and self.minutes == otherDuration.minutes)

    def greaterThanEqual(self, otherDuration: duration) -> bool:
        greaterThanCondition = self.greaterThan(otherDuration)
        equalCondition = self.equal(otherDuration)
        return greaterThanCondition or equalCondition

    def add(self, otherDuration: duration) -> duration:
        '''
        adds otherDuration to self and returns it. Does not change self and otherDuration
        '''
        retDuration = duration(self.days, self.hours, self.minutes)

        hoursFromMinutes = (retDuration.minutes + otherDuration.minutes) // 60
        retDuration.minutes = (retDuration.minutes + otherDuration.minutes) % 60

        daysFromHours = (retDuration.hours + otherDuration.hours + hoursFromMinutes) // 24
        retDuration.hours = (retDuration.hours + otherDuration.hours + hoursFromMinutes) % 24
        
        retDuration.days = daysFromHours + otherDuration.days

        return retDuration

    def minus(self, otherDuration: duration) -> duration:
        '''
        minuses otherDuration from self and returns it. Does not change self and otherDuration. Assumes that self is greater than or equal to otherDuration
        '''
        retDuration = duration(self.days, self.hours, self.minutes)
        retDuration.minutes -= otherDuration.minutes
        if (retDuration.minutes < 0):
            hoursNeeded = -1 * (retDuration.minutes // 60)
            retDuration.minutes %= 60
            retDuration.hours -= hoursNeeded

        retDuration.hours -= otherDuration.hours
        if (retDuration.hours < 0):
            daysNeeded = -1 * (retDuration.hours // 24)
            retDuration.hours %= 24
            retDuration.days -= daysNeeded

        retDuration.days -= otherDuration.days

        return retDuration
        

    def totalMinutes(self) -> int:
        '''
        returns the total duration of self in minutes
        '''

        minutesFromDays = self.days * 24 * 60
        minutesFromHours = self.hours * 60
        return minutesFromDays + minutesFromHours + self.minutes
        

    def __str__(self):
        return f'{self.days} days, {self.hours} hours, {self.minutes} minutes'

class weekTime:
    '''
    implemets a weekly time. Stores the day (Monday to Sunday), and time
    '''
    dayNum: int
    hour: int
    minute: int

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

    def equal(self, otherTime: weekTime) -> bool:
        '''
        checks if self is equal to another weekTime
        '''
        return (self.dayNum == otherTime.dayNum and self.hour == otherTime.hour and self.minute == otherTime.minute)