from ga import init_field, is_win, player_step, set_ceil, enemy_step, is_avalible_ceil

def main():
    field = init_field()
    print_field(field)

    first_player, second_player = 'x', "0"

    while True:
        x, y = get_step(first_player)
        player_step(x, y, first_player, field)
        print_field(field)

        if is_win(field, first_player):
            print(f"Победил игрок {first_player}")
            break

        if not is_avalible_ceil(field):
            print('Ничья')
            break

        x, y = get_step(second_player)
        enemy_step(x, y, second_player, field)
        print(field)
        if is_win(field, second_player):
            print(f"Победил игрок {second_player}")
            break

        if not is_avalible_ceil(field):
            print('Ничья')
            break

    if is_win(field, second_player):
        print(f"Победил игрок {second_player}")

print("Игра закончена")

is_wined = False

def get_step(player_symbol: str) -> tuple[int, int]:
    while True:
        step = input(f"Игрок {player_symbol} введите две координаты через пробел: ")
        coords = step.split()
        if len(coords) < 2:
            print("Введено слишком мало координат")
        elif len(coords) > 2:
            print("Введено слишком много координат")
        x_str: str
        y_str: str
        x_str, y_str = coords

        if not x_str.isdigit():
            print("Координата х не число")
            continue

        if not y_str.isdigit():
            print("Координата y не число")
            continue
        x, y = int(x_str), int(y_str)

        if not 0 < x < 3 + 1:
            print("Неверная координата х")
            continue
        if not 0 < y < 3 + 1:
            print("Неверная координата y")
            continue

        return x-1, y-1





def print_field(field) -> None:
    for row in field:
        for ceil in row:
            print(ceil, end=" ")
        print()
if __name__ == '__main__':
    main()
