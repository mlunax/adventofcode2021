from sys import argv, stdin

def part1():
    data = list([])
    gamma = []
    epsilon = []
    for line in stdin.readlines():
        cline = []
        if line == '\n':
            continue
        for c in line:
            if c != '\n':
                cline.append(c)
        data.append(cline)
    for i in range(0, len(data[0])):
        d = [x[i] for x in data]
        on = {'0': 0, '1': 0}
        for a in d:
            on[a] += 1
        gamma.append(max(on, key=on.get))
        epsilon.append(min(on, key=on.get))
    gamma = int("".join(gamma),base=2)
    epsilon = int("".join(epsilon),base=2)
    print("Gamma: ")
    print(gamma)
    print("Epsilon: ")
    print(epsilon)
    print("Multiple: ")
    print(gamma * epsilon)


def part2():
    ...

def main():
    match argv[1]:
        case "1":
            part1()
        case "2":
            part2()


if __name__ == "__main__":
    main()
