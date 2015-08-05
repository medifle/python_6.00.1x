class Time(object):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return str(self.hours) + ":" + \
                str(self.minutes) + ":" + \
                str(self.seconds)