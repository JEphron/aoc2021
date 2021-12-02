def part1(lines):
    h = 0
    v = 0
    for line in lines:
        if not line:
            break
        action, n = line.split()
        n = int(n)
        if action == "forward":
            h += n
        if action == "up":
            v -= n
        if action == "down":
            v += n
    print(h * v)


def part2(lines):
    h = 0
    v = 0
    aim = 0
    for line in lines:
        if not line:
            break
        action, n = line.split()
        n = int(n)
        if action == "forward":
            h += n
            v += aim * n
        if action == "up":
            aim -= n
        if action == "down":
            aim += n
    print(h * v)


if __name__ == "__main__":
    data = open("day2.txt").read()
    part1(data.split("\n"))
    part2(data.split("\n"))
