class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def show(self):
        print(f'{self.hours}:{self.minutes}')

    def isMorning(self):
        time = str(self.hours) + str(self.minutes)
        time = int(time)
        if 400 <= time <= 1130:
            return True
        else:
            return False

    def isDay(self):
        time = str(self.hours) + str(self.minutes)
        time = int(time)
        if 1130 < time <= 1630:
            return True
        else:
            return False

    def isEvening(self):
        time = str(self.hours) + str(self.minutes)
        time = int(time)
        if 1630 < time <= 2300:
            return True
        else:
            return False

    def isNight(self):
        if self.hours == 23 and self.minutes > 0 or self.hours in [24, 0, 00] and self.minutes >= 0:
            time = 0
        else:
            time = str(self.hours) + str(self.minutes)
            time = int(time)
        if 0 <= time < 400:
            return True
        else:
            return False

    def sayHello(self):
        if self.isMorning():
            return f'Доброе утро!'
        elif self.isDay():
            return f'Добрый день!'
        elif self.isEvening():
            return f'Добрый вечер!'
        elif self.isNight():
            return f'Доброй ночи!'

    def add(self, n):
        self.hours, self.minutes = self.hours + n // 60, self.minutes + n % 60
        if self.hours >= 24:
            self.hours = self.hours - 24
        if self.minutes >= 60:
            self.minutes = self.minutes - 60
        if self.minutes < 10:
            self.minutes = f'0{self.minutes}'
        return f'{self.hours}:{self.minutes}'



t = Time(10,20)
print(t.isMorning())
print(t.isDay())
print(t.isEvening())
print(t.isNight())
print(t.sayHello())
print(t.add(60))
