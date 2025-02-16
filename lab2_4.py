class Car:

    def __init__(self, color, consumption, tank_volume, mileage=0):
        """
        :param color: Цвет автомобиля
        :param consumption: Расход топлива
        :param tank_volume: Объем бака
        :param mileage: Пробег автомобиля
        """
        self.color = color
        self.consumption = consumption
        self.tank_volume = tank_volume
        self.reserve = tank_volume
        self.mileage = mileage
        self.engine_on = False

    def __str__(self):
        return f"Автомобиль. " \
               f"Цвет: {self.color}. " \
               f"Пробег: {self.mileage} км. " \
               f"Остаток топлива: {self.reserve} кВт*ч. "

    def __repr__(self):
        return f"Car('{self.color}', " \
               f"{self.consumption}, " \
               f"{self.tank_volume}, " \
               f"{self.mileage})"

    def start_engine(self) -> str:
        """
        Запуск двигателя автомобиля
        :return: Сообщение о запуске двигателя
        """
        if not self.engine_on and self.reserve > 0:
            self.engine_on = True
            return "Двигатель запущен."
        return "Двигатель уже был запущен."

    def stop_engine(self) -> str:
        """
        Остановка двигателя автомобиля
        :return: Сообщение об остановке двигателя
        """
        if self.engine_on:
            self.engine_on = False
            return "Двигатель остановлен."
        return "Двигатель уже был остановлен."

    def drive(self, distance) -> str:
        """
        Рассчитывается дистанция, которую проехал автомобиль.
        :param distance: Дистанция в километрах
        :return: Сколько километров проехали и остаток топлива
        """
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас топлива."
        self.mileage += distance
        return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."

    def refuel(self) -> None:
        """
        Заправляет автомобиль до полного объема бака
        """
        self.reserve = self.tank_volume

    def get_mileage(self) -> float:
        """
        Возвращает пробег автомобиля
        :return: Пробег автомобиля
        """
        return self.mileage

    def get_reserve(self):
        """
        Возвращает остаток топлива
        :return: Остаток топлива
        """
        return self.reserve

    def get_consumption(self):
        """
        Возвращает расход топлива
        :return: Расход топлива
        """
        return self.consumption


class ElectricCar(Car):
    """
    Класс ElectricCar, наследующийся от класса Car
    """

    def __init__(self, color, consumption, bat_capacity, mileage=0):
        """
        :param color: цвет электромобиля
        :param consumption: потребление электромобиля
        :param bat_capacity: объем батареи электромобиля
        :param mileage: пробег электромобиля
        """
        super().__init__(color, consumption, bat_capacity, mileage)
        self.bat_capacity = bat_capacity

    def __str__(self):
        """
        Перегружаем метод из базового класса.
        У электромобилей не топливо, а заряд батареи
        """
        return f"Электромобиль. " \
               f"Цвет: {self.color}. " \
               f"Пробег: {self.mileage} км. " \
               f"Остаток заряда: {self.reserve} кВт*ч. "

    def __repr__(self):
        """
        Перегружаем метод из базового класса.
        У электромобилей не топливо, а заряд батареи
        """
        return f"ElectricCar('{self.color}', " \
               f"{self.consumption}, " \
               f"{self.bat_capacity}, " \
               f"{self.mileage})"

    def drive(self, distance):
        """
        Перегружаем метод из базового класса.
        У электромобиля остаток заряда, а не топлива.
        Рассчитывается дистанция, которую проехал электромобиль.
        :param distance: Дистанция в километрах
        :return: Сколько километров проехали и остаток заряда
        """
        if not self.engine_on:
            return "Двигатель не запущен."
        if self.reserve / self.consumption * 100 < distance:
            return "Малый запас заряда."
        self.mileage += distance
        self.reserve -= distance / 100 * self.consumption
        return f"Проехали {distance} км. Остаток заряда: {self.reserve} кВт*ч."

    def recharge(self) -> None:
        """
        Заряжает батарею до максимума
        """
        self.reserve = self.bat_capacity


if __name__ == "__main__":
    electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
    print(electric_car.start_engine())
    print(electric_car.drive(100))
    print(electric_car)
    electric_car = ElectricCar(color="белый", consumption=15, bat_capacity=90)
    print(repr(electric_car))
    electric_car_1 = ElectricCar(color="чёрный", consumption=17, bat_capacity=80)
    print([electric_car, electric_car_1])
