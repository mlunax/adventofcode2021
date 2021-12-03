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
    depth = 0
    hor = 0
    idata = raw_input()
    for d in idata:
        command = d.split()[0]
        num = int(d.split()[1])
        match command:
            case "up":
                depth -= num
            case "down":
                depth += num
            case "forward":
                hor += num
    print(hor * depth)
if __name__ == "__main__":
    main();
