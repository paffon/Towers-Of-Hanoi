import my_classes


def get_rings():
    max_rings = 20
    user_input = input("How many rings should there be on the first tower? (<{})\n".format(max_rings))
    if user_input.isdigit():
        rings_number = int(user_input)
    else:
        rings_number = max_rings + 1

    i = 1
    max_trials = 4
    while rings_number > max_rings and i < max_trials:
        i += 1
        user_input = input("The number of rings must be less than {} (Attempt {}/{}): \n".format(max_rings, i, max_trials))
        if user_input.isdigit():
            rings_number = int(user_input)
        else:
            rings_number = max_rings + 1

    if i == max_trials:
        rings_number = 3  # default
        print("Default chosen: {} rings.".format(rings_number))
    return rings_number


if __name__ == '__main__':
    while input("\nReady to start? (y/n) ") != "n":
        n = get_rings()
        board = my_classes.Board(n)
        board.solve_me()
