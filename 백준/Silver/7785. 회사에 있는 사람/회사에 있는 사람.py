
n = int(input())

chulgen = set()

for i in range(n):
    data = list(map(str, input().split(" ")))
    name, action = data[0], data[1]
    if action == "enter":
        chulgen.add(name)
    else:
        chulgen.remove(name)

arr = []
for i in chulgen:
    arr.append(i)
arr.sort(reverse=True)

if __name__ == "__main__":
    print("\n".join(arr))


