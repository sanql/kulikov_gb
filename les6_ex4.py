class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} стронулся.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}.'

    def show_speed(self):
        return f'\nСкорость автомобиля = {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        # def __init__(self, speed, color, name, is_police):
        #     super().__init__(speed, color, name, is_police)
        if self.speed > 60:
            return f'\nПревышение скорости! Скорость автомобиля {self.speed}.'
        else:
            return f'Скорость автомобиля {self.name} допустимая.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nПревышение скорости! Скорость автомобиля {self.speed}.'
        else:
            return f'Скорость автомобиля {self.name} допустимая.'


class PoliceCar(Car):
    pass


town = TownCar('Ауди', 70, 'синий', False)
print('\n1:\n' + town.go(), town.show_speed(), town.turn('влево'), town.turn('вправо'), town.stop())

sport = SportCar('Ауди РС', 170, 'красный', False)
print('\n2:\n' + sport.go(), sport.show_speed(), sport.turn('вправо'), sport.turn('влево'), sport.stop())

work = WorkCar('ВАЗ', 30, 'белый', False)
print('\n3:\n' + work.go(), work.show_speed(), work.turn('вправо'), work.stop())

police = PoliceCar('Лада', 100, 'бело-синий', True)
print('\n4:\n' + police.go(), police.show_speed(), police.turn('вправо'), police.turn('влево'), police.stop())
