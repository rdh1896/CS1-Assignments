import time

def quick_select(lst, k):
    pivot = lst[len(lst) // 2]
    smaller_lst = []
    larger_lst = []
    count = 0
    for element in lst:
        if element < pivot:
            smaller_lst.append(element)
        elif element > pivot:
            larger_lst.append(element)
        else:
            count += 1
    m = len(smaller_lst)
    if m <= k < m + count:
        return pivot
    elif m > k:
        return quick_select(smaller_lst, k)
    else:
        return quick_select(larger_lst, k - m - count)

def find_sum(lst, best):
    sum = 0
    for element in range(len(lst) - 1):
        sum = sum + abs(best - lst[element])
    return sum

def main():
    lst = []
    file = open(input("Please enter file name: "))
    line = file.readline()
    while True:
        if line == "":
            break
        else:
            line = line.strip()
            split_line = line.split(" ")
            value = int(split_line[1])
            lst.append(value)
            line = file.readline()
    if len(lst) % 2 == 0:
        start = time.time()
        q1 = quick_select(lst, len(lst) // 2)
        q2 = quick_select(lst, len(lst) // 2 - 1)
        best_location = (q1 + q2) / 2
        sum_distances = find_sum(lst, best_location)
        end = time.time()
        time_elapsed = end - start
    else:
        start = time.time()
        best_location = quick_select(lst, len(lst) // 2)
        sum_distances = find_sum(lst, best_location)
        end = time.time()
        time_elapsed = end - start
    print("Optimum new store location: ", best_location)
    print("Sum of distances to new store: ", sum_distances, "\n")
    print("elapsed time", time_elapsed)

main()





