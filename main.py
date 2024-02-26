from collections.abc import Generator
import sys
from pyray import *
from utils import *

width = 1200
height = 900

speed = 1

dots:list[Vector2] = []
generator: None | Generator[list[Vector2]] = None

best_distance = sys.maxsize
best_path: list[Vector2] = []

init_window(width, height, "Particles")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)

    draw_rectangle(0,0, width, 40, GRAY)

    if gui_button(Rectangle(10, 10, 100, 20), "Start"):
        print("Starting simulation")
        generator = generate_solutions(dots, len(dots))

    if gui_button(Rectangle(120, 10, 100, 20), "Clear"):
        print("Clear")
        generator = None
        dots = []
        best_path = []
        best_distance = sys.maxsize

    if is_mouse_button_pressed(0) and get_mouse_y() > 50:
       dots.append(get_mouse_position())

    if generator:
        solution = next(generator, None)

        if solution:
            distance = evaluate_distance(solution)
            draw_text(f"Current best distance is {best_distance}", 10, 40, 30, BLUE)

            if distance < best_distance:
                best_distance = distance
                best_path = solution

        else:
            draw_text(f"Final best distance is {best_distance}", 10, 40, 30, RED)

    for i in range(0, len(best_path)):
        next_index = (i + 1) % len(best_path)
        draw_line(int(best_path[i].x), int(best_path[i].y), int(best_path[next_index].x), int(best_path[next_index].y), BLUE)
    
    for dot in dots:
        draw_circle(int(dot.x), int(dot.y), 5 , RED)

    end_drawing()
close_window()