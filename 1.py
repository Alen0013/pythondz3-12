class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheels):
        if wheels == 2:
            return f"Это мотоцикл марки {self.name}."
        elif wheels == 3:
            return f"Это трицикл марки {self.name}."
        elif wheels == 4:
            return f"Это автомобиль марки {self.name}."
        else:
            return f"Я не знаю таких ТС марки {self.name}."

    def get_vehicle_advice(self):
        if self.mileage < 50000:
            return f"Неплохо, {self.name}, можно брать."
        elif 50001 <= self.mileage <= 100000:
            return f"{self.name}, надо внимательно проверить."
        elif 100001 <= self.mileage <= 150000:
            return f"{self.name}, надо провести полную диагностику."
        else:
            return f"{self.name}, лучше не покупать."

# Создаем экземпляры класса Vehicle
vehicle1 = Vehicle("BMW", 30000)
vehicle2 = Vehicle("Audi", 75000)
vehicle3 = Vehicle("Kawasaki", 120000)
vehicle4 = Vehicle("Tesla", 160000)

# Проверяем все методы на каждом экземпляре
print(vehicle1.get_vehicle_type(2))  # Мотоцикл
print(vehicle1.get_vehicle_advice())  # Неплохо, BMW, можно брать.

print(vehicle2.get_vehicle_type(4))  # Автомобиль
print(vehicle2.get_vehicle_advice())  # Audi, надо внимательно проверить.

print(vehicle3.get_vehicle_type(2))  # Мотоцикл
print(vehicle3.get_vehicle_advice())  # Kawasaki, надо провести полную диагностику.

print(vehicle4.get_vehicle_type(4))  # Автомобиль
print(vehicle4.get_vehicle_advice())  # Tesla, лучше не покупать.
