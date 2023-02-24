import math
import time


def swap(arrOfDot, a, b):
    print("swap")
    temp = arrOfDot[a]
    arrOfDot[a] = arrOfDot[b]
    arrOfDot[b] = temp

# Sort arrOfDot berdasarkan coordinate[0] (sumbu X), memakai algoritma quicksort versi 2 dengan pemilihan pivot selalu elemen pertama


def partition(arrOfDot, i, j):
    pivotX = arrOfDot[i].getCoordinate()[0]
    p = i+1
    q = j
    while (p < q):
        while arrOfDot[p].getCoordinate()[0] < pivotX:
            p += 1
        while arrOfDot[q].getCoordinate()[0] > pivotX:
            q -= 1

        if (p < q):
            swap(arrOfDot, p, q)

    swap(arrOfDot, i, q)
    return q


def sortArrOfDot(arrOfDot, i=0, j=-1):
    if (j == -1):
        j = len(arrOfDot)-1
    if (i < j):
        pos = partition(arrOfDot, i, j)
        sortArrOfDot(arrOfDot, i, pos-1)
        sortArrOfDot(arrOfDot, pos+1, j)

# Fungsi Untuk menghitung jarak antara dua buah titik


def calculateDistance(dot1, dot2):
    distance = 0  # inisialisasi
    # Penghitungan d = sqrt((x1-x2)^2 + (y1-y2)^2 + ...)
    for i in range(dot1.getNDim()):
        distance += math.pow((dot1.getCoordinate()[i] -
                             dot2.getCoordinate()[i]), 2)
    distance = math.sqrt(distance)
    return distance

# Fungsi untuk mencari shortest distance dengan algoritma brute force


def bruteForceShortestDistance(listOfDot):
    arrOfDot = listOfDot.getArrOfDot()
    shortest_distance = 0
    closest_indexes = [-1, -1]
    num_step = 0
    start_time = time.time()

    if (len(arrOfDot) > 1):
        shortest_distance = calculateDistance(arrOfDot[0], arrOfDot[1])
        closest_indexes = [0, 1]

        for i in range(len(arrOfDot)):
            for j in range(i+1, len(arrOfDot)):
                num_step += 1
                distance = calculateDistance(arrOfDot[i], arrOfDot[j])
                if (distance < shortest_distance):
                    shortest_distance = distance
                    closest_indexes = [i, j]
    exec_time = time.time() - start_time
    listOfDot.setShortestDistance(shortest_distance)
    listOfDot.setClosestIndexes(closest_indexes[0], closest_indexes[1])
    listOfDot.setNStep(num_step)
    listOfDot.setSolvingTime(exec_time)
