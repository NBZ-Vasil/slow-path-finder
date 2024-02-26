
from pyray import vector_2distance, Vector2

def generate_solutions(indices: list[Vector2], n: int) :

    if (n ==  1):
        yield indices.copy()
    else:
        for i in range(n):
            yield from generate_solutions(indices, n - 1)
            swap_index = i if (n % 2 == 0) else 0
            indices[swap_index], indices[n-1] = indices[n-1], indices[swap_index]

          


def evaluate_distance(indices: list[Vector2]):
    tour_dst = float(0)
    for i in range(0, len(indices)):
        next_index = (i + 1) % len(indices)
        tour_dst += vector_2distance(indices[i], indices[next_index])

    return int(tour_dst)
   

if __name__ == "__main__":
    test = [Vector2(15, 15), Vector2(24,65), Vector2(54,22), Vector2(4,6)]


    for i in generate_solutions(test, len(test)):
        print(evaluate_distance(i))