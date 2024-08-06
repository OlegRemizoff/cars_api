from django.db import models

# Марка
# Модель
# Год выпуска
# Тип топлива (бензин, дизель, электричество, гибрид)
# Тип КПП (механическая, автоматическая, вариатор, робот)
# Пробег
# Цена
# new_car = Auto.objects.create(name="Granta", model=lada, year=2012, mileage=231730, price=330000, fuel=1, transmission=1)

class ModelAuto(models.Model):
    name = models.CharField("Модель", max_length=200)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'


class Auto(models.Model):
    name = models.CharField("Марка", max_length=200)
    model = models.ForeignKey(ModelAuto, verbose_name="Модель", on_delete=models.CASCADE)
    year = models.IntegerField('Год выпуска')
    mileage = models.PositiveIntegerField("Пробег(км)")
    price = models.IntegerField("Цена")
    fuel = models.PositiveBigIntegerField("Тип топлива",
        choices=(
            (1, "бензин"),
            (2, "дизель"),
            (3, "электричество"),
            (4, "гибрид"),
        ),
    )
    transmission = models.PositiveBigIntegerField("КПП",
        choices=(
            (1, "механическая"),
            (2, "автоматическая"),
            (3, "вариатор"),
            (4, "робот")
        ),
    )

    
    def __str__(self) -> str:
        return f'id: {self.model} | {self.name}'
    
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'