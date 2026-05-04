def odometer(oksana):
    pairs = list(zip(oksana[::2], oksana[1::2]))
    speeds, times = zip(*pairs)
    deltas = (t - p for p, t in zip((0, *times[:-1]), times))
    return sum(map(lambda s, dt: s * dt, speeds, deltas))
	
print(odometer([15, 1, 25, 2, 30, 3, 10, 5]))