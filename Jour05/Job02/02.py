def draw_rectangle(width, height):
    if width < 1 or height < 1:
        print("Width and height must be positive integers.")
        return

    for _ in range(height):
        print('|' + '-' * (width - 1) + '|')

draw_rectangle(10, 3)