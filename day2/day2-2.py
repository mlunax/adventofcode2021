#!/usr/bin/env python3
def raw_input():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return lines
def main():
    hor = 0
    aim = 0
    depth = 0
    idata = raw_input()
    for d in idata:
        command = d.split()[0]
        num = int(d.split()[1])
        match command:
            case "up":
                aim -= num
            case "down":
                aim += num
            case "forward":
                hor += num
                depth = depth + (aim * num)
        print(hor, aim, depth)
    print(hor, aim, depth)
    print(hor * depth)
if __name__ == "__main__":
    main();
