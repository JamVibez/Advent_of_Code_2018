file = open("data.txt",mode="r")
a = list(map(int, file.readlines()))
file.close()

print(sum(a))
