from pymonad.maybe import Just, Nothing

# посадка птиц на левую сторону
to_left = lambda num: lambda state: (
    Nothing
    if abs((state[0] + num) - state[1]) > 4
    else Just((state[0] + num, state[1]))
)

# посадка птиц на правую сторону
to_right = lambda num: lambda state: (
    Nothing
    if abs((state[1] + num) - state[0]) > 4
    else Just((state[0], state[1] + num))
)

# банановая кожура
banana = lambda _: Nothing

# вывод результата
def show(maybe):
    if maybe == Nothing:
        print(False)
    else:
        print(True)
        
# начальное состояние
begin = lambda: Just((0, 0))

show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-2))
)

show(
    begin()
    .bind(to_left(2))
    .bind(to_right(5))
    .bind(to_left(-1))
)

show(
    begin()
    .bind(to_left(2))
    .bind(banana)
    .bind(to_right(5))
    .bind(to_left(-1))
)