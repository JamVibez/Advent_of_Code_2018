import time

file = open("data.txt", mode="r")
a = list(map(int, file.readlines()))
file.close()

start_frequency = 0
test_list = [3, 3, 4, -2, -4]
test_list1 = [-6, 3, 8, 5, -6]
temp_list = [0]
print("Start frequency =", start_frequency)

current_table = a

while True:
    for index, value in enumerate(current_table):
        start_frequency += current_table[index]
        #print("Sprawdzam: ",start_frequency)
        for i, v in enumerate(temp_list):
            #print("Sprawdzam czy freq: ", start_frequency, "to:", temp_list[i])
            if start_frequency == temp_list[i]:
                print("PIERWSZY DUPLIKAT TO:",start_frequency)
                time.sleep(600)
        temp_list.append(start_frequency)
        #print(temp_list)
