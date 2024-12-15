class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand
        self.model = model
        self.storage = storage  # в ГБ
        self.battery_capacity = battery_capacity  # в мАч

    def get_specs(self):
        return f"{self.brand} {self.model}: {self.storage}GB, {self.battery_capacity}mAh"

    def battery_status(self):
        if self.battery_capacity > 4000:
            return "Батарея в отличном состоянии!"
        elif self.battery_capacity > 2000:
            return "Батарея средняя, может потребоваться зарядка."
        else:
            return "Батарея слабая, лучше заряжайте!"

    def is_storage_enough(self, required_storage):
        if self.storage >= required_storage:
            return f"Достаточно памяти для {required_storage}GB."
        else:
            return f"Недостаточно памяти для {required_storage}GB!"

    def describe(self):
        return f"Смартфон {self.brand} {self.model} - это отличный выбор для повседневного использования."

# Создаем экземпляры класса Smartphone
smartphone1 = Smartphone("Samsung", "Galaxy S21", 128, 4000)
smartphone2 = Smartphone("Apple", "iPhone 13", 256, 3095)

# Вызываем методы на экземплярах
print(smartphone1.get_specs())        # Samsung Galaxy S21: 128GB, 4000mAh
print(smartphone1.battery_status())    # Батарея в отличном состоянии!
print(smartphone1.is_storage_enough(64))  # Достаточно памяти для 64GB.
print(smartphone1.describe())           # Смартфон Samsung Galaxy S21 - это отличный выбор для повседневного использования.

print(smartphone2.get_specs())        # Apple iPhone 13: 256GB, 3095mAh
print(smartphone2.battery_status())    # Батарея средняя, может потребоваться зарядка.
print(smartphone2.is_storage_enough(300))  # Недостаточно памяти для 300GB!
print(smartphone2.describe())           # Смартфон Apple iPhone 13 - это отличный выбор для повседневного использования.
