from functools import reduce

def ConquestCampaign(N, M, L, battalion):
    initial = set(zip(battalion[::2], battalion[1::2]))
    total = N * M

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def in_bounds(x, y):
        return 1 <= x <= N and 1 <= y <= M

    def step(state, _):
        front, visited, day = state

        if len(visited) == total:
            return state

        new_front = {
            (x+dx, y+dy)
            for (x, y) in front
            for dx, dy in directions
            if in_bounds(x+dx, y+dy) and (x+dx, y+dy) not in visited
        }

        return (new_front, visited | new_front, day + 1)

    max_steps = N * M

    final_front, final_visited, final_day = reduce(
        step,
        range(max_steps),
        (initial, initial, 1)
    )

    return final_day
    
print(ConquestCampaign(3,4,2,[2,2,3,4]))