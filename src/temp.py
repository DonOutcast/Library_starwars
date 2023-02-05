# my_dict = {
#     "value": 1,
#     "next": {
#         "value": 2,
#         "next": {
#             "value": 3,
#             "next": None
#         }
#     }
# }

# tmp = None
# while my_dict:
#         next = my_dict['next']
#         my_dict['next'] = tmp
#         tmp = my_dict
#         my_dict = next
#
# my_dict = tmp
# print(my_dict)
from dataclasses import dataclass, asdict
from typing import Type, List


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: int
    distance: float
    speed: float
    calories: float

    message: str = ('Тип тренировки: {training_type}; '
                    'Длительность: {duration:.3f} ч.; '
                    'Дистанция: {distance:.3f} км; '
                    'Ср. скорость: {speed:.3f} км/ч; '
                    'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        return self.message.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    MIN_IN_H = 60
    M_IN_KM = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Метод get_spent_calories()'
                                  'не был реализован')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65
    RUNNING_CONSTANT_1 = 18
    RUNNING_CONSTANT_2 = 1.79

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        return ((self.RUNNING_CONSTANT_1
                * self.get_mean_speed()
                + self.RUNNING_CONSTANT_2)
                * self.weight / self.M_IN_KM
                * self.duration * self.MIN_IN_H)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    LEN_STEP = 0.65
    WALKING_CONSTANT_1 = 0.035
    WALKING_CONSTANT_2 = 0.029
    KMH_IN_MS = 0.278
    SM_IN_M = 100

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.WALKING_CONSTANT_1 * self.weight
                + ((self.KMH_IN_MS * self.get_mean_speed())**2
                 / self.height * self.SM_IN_M) * self.WALKING_CONSTANT_2
                * self.weight) * self.duration * self.MIN_IN_H)


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    SWIMMING_CONSTANT_1 = 1.1
    SWIMMING_CONSTANT_2 = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.SWIMMING_CONSTANT_1)
                * self.SWIMMING_CONSTANT_2 * self.weight * self.duration)

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)


def read_package(workout_type: str, data: List[float]) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_classes: dict[str, Type[Training]] = {'SWM': Swimming,
                                                  'RUN': Running,
                                                  'WLK': SportsWalking}
    if workout_type not in workout_classes:
        raise ValueError(f'Недопустимый тип тренировки - {workout_type}')
    return workout_classes[workout_type](*data)


def main(training: Type[Training]) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

