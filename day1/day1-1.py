#!/usr/bin/env python3
def main():
    incn = 0
    data = []
    while True:
        line = input()
        if line:
            data.append(int(line))
        else:
            break
    for i, d in enumerate(data):
        if i <= 0:
            continue
        if d > data[i-1]:
            incn = incn + 1
    print(incn)
if __name__ == "__main__":
    main()
