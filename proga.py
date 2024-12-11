"с помощью ооп"
from __future__ import annotations
from abc import ABC, abstractmethod
import random

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass

class ArrayMediator(Mediator):
    def __init__(self) -> None:
        self.array1 = []
        self.array2 = []

    def notify(self, sender: object, event: str) -> None:
        if event == "input_arrays":
            self.array1 = input_large_number_array("Введите первый массив чисел: ")
            self.array2 = input_large_number_array("Введите второй массив чисел: ")
        elif event == "generate_arrays":
            size = int(input("Введите размер массивов: "))
            self.array1 = generate_large_number_array(size)
            self.array2 = generate_large_number_array(size)
            print(f"Сгенерированный первый массив: {self.array1}")
            print(f"Сгенерированный второй массив: {self.array2}")
        elif event == "perform_operation":
            operation = input("Введите операцию (+ или -): ")
            if operation == '+':
                result = sum_arrays(self.array1, self.array2)
                print(f"Результат суммы: {result}")
            elif operation == '-':
                result = subtract_arrays(self.array1, self.array2)
                print(f"Результат разности: {result}")
            else:
                print("Неверная операция.")

def input_large_number_array(prompt: str) -> list[int]:
    """Ввод массива чисел вручную."""
    return list(map(int, input(prompt).split()))

def generate_large_number_array(size: int) -> list[int]:
    """Генерация случайного массива чисел."""
    return [random.randint(0, 9) for _ in range(size)]

def sum_arrays(array1: list[int], array2: list[int]) -> list[int]:
    """Суммирует два массива."""
    max_length = max(len(array1), len(array2))
    array1 = [0] * (max_length - len(array1)) + array1
    array2 = [0] * (max_length - len(array2)) + array2
    return [a + b for a, b in zip(array1, array2)]

def subtract_arrays(array1: list[int], array2: list[int]) -> list[int]:
    """Вычитает второй массив из первого."""
    max_length = max(len(array1), len(array2))
    array1 = [0] * (max_length - len(array1)) + array1
    array2 = [0] * (max_length - len(array2)) + array2
    return [a - b for a, b in zip(array1, array2)]

def task1_menu(mediator: ArrayMediator) -> None:
    """Меню первого задания."""
    while True:
        print("\nЗадание 1: Сумма и разность массивов")
        print("1) Ввод массивов вручную")
        print("2) Генерация случайных массивов")
        print("3) Выполнить операцию")
        print("4) Вернуться в главное меню")

        choice = input("Выберите опцию: ")

        if choice == '1':
            mediator.notify(None, "input_arrays")
        elif choice == '2':
            mediator.notify(None, "generate_arrays")
        elif choice == '3':
            mediator.notify(None, "perform_operation")
        elif choice == '4':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    mediator = ArrayMediator()
    task1_menu(mediator)
