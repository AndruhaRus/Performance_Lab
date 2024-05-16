import sys
import math


def point_circle_position(circle_x, circle_y, radius, point_x, point_y):
    distance = math.sqrt(((point_x - circle_x) ** 2) + ((point_y - circle_y) ** 2))
    if abs(distance - radius) < 1e-6:  # Проверка на равенство с учетом погрешности
        return 0
    elif distance < radius:
        return 1
    else:
        return 2


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Ошибка: требуется два аргумента: файл с окружностью и файл с точками.")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        with open(circle_file, 'r') as f:
            circle_x, circle_y = map(float, f.readline().split())
            radius = float(f.readline())

        with open(points_file, 'r') as f:
            for line in f:
                point_x, point_y = map(float, line.split())
                position = point_circle_position(circle_x, circle_y, radius, point_x, point_y)
                print(position)

    except FileNotFoundError:
        print("Ошибка: один или оба файла не найдены.")
        sys.exit(1)
    except ValueError:
        print("Ошибка: некорректные данные в файлах.")
        sys.exit(1)
