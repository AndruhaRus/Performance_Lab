import sys


def min_moves(nums):
    """
  Вычисляет минимальное количество ходов для приведения всех элементов массива к одному числу.

  Args:
    nums: список целых чисел.

  Returns:
    int: минимальное количество ходов.
  """
    median = sorted(nums)[len(nums) // 2]  # Медиана массива
    moves = 0
    for num in nums:
        moves += abs(num - median)
    return moves


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ошибка: требуется один аргумент: файл с числами.")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as f:
            nums = [int(line.strip()) for line in f]

        min_moves_count = min_moves(nums)
        print(min_moves_count)

    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        sys.exit(1)
    except ValueError:
        print("Ошибка: файл содержит некорректные данные.")
        sys.exit(1)
