#!/usr/bin/env python3
def main():
    incn = 0
    data = []
    t_data = []
    while True:
        line = input()
        if line:
            data.append(int(line))
        else:
            break
    for i, d in enumerate(data):
        if i+3 > len(data):
            break
        t_data.append(d+data[i+1]+data[i+2])
    for i, d in enumerate(t_data):
        if i <= 0:
            continue
        if d > t_data[i-1]:
            incn = incn + 1
    print(incn)
if __name__ == "__main__":
    main()
