import time

def partition(pivot, lst):
    (less, same, more) = ([], [], [])
    for element in lst:
        if element > pivot:
            more.append(element)
        elif element < pivot:
            less.append(element)
        else:
            same.append(element)
    return (less, same, more)

def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        (less, same, more) = partition(pivot, lst)
        return quick_sort(less) + same + quick_sort(more)

def find_median(lst):
    sorted_list = quick_sort(lst)
    if len(lst) % 2 == 0:
        return (sorted_list[len(lst) // 2] + sorted_list[len(lst) // 2 - 1]) / 2
    else:
        return sorted_list[len(lst) // 2]

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
    start = time.time()
    best_location = find_median(lst)
    sum_distances = find_sum(lst, best_location)
    end = time.time()
    time_elapsed = end - start
    print("Optimum new store location: ", best_location)
    print("Sum of distances to new store: ", sum_distances, "\n")
    print("elapsed time", time_elapsed)

main()



