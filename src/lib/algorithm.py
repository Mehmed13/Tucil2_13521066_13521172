import math
import time
import random


def swap(arrOfDot, a, b):
    temp = arrOfDot[a]
    arrOfDot[a] = arrOfDot[b]
    arrOfDot[b] = temp

# Sort arrOfDot berdasarkan coordinate[0] (sumbu X), memakai algoritma quicksort versi 2 dengan pemilihan pivot selalu elemen pertama


def partition(arrOfDot, i, j, axis):
    # Ambil pivot dari elemen acak
    pivotIndex = random.randint(i, j)
    # Tukar dengan elemen pertama
    swap(arrOfDot, i, pivotIndex)
    pivot = arrOfDot[i].getCoordinate()[axis]
    p = i+1
    q = j
    while (p < q):
        while p < j and arrOfDot[p].getCoordinate()[axis] < pivot:
            p += 1
        while arrOfDot[q].getCoordinate()[axis] > pivot:
            q -= 1

        if (p < q):
            swap(arrOfDot, p, q)

    swap(arrOfDot, i, q)
    return q


def sortArrOfDot(arrOfDot, i=0, j=-1, axis=0):
    if (j == -1):
        j = len(arrOfDot)-1
    if (i < j):
        pos = partition(arrOfDot, i, j, axis)
        sortArrOfDot(arrOfDot, i, pos-1, axis)
        sortArrOfDot(arrOfDot, pos+1, j, axis)

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
        closest_indexes = [1, 0]

        for i in range(len(arrOfDot)):
            for j in range(i+1, len(arrOfDot)):
                num_step += 1
                distance = calculateDistance(arrOfDot[i], arrOfDot[j])
                if (distance < shortest_distance):
                    shortest_distance = distance
                    closest_indexes[0] = i
                    closest_indexes[1] = j
        listOfDot.getArrOfDot()[closest_indexes[0]].setColor("red")
        listOfDot.getArrOfDot()[closest_indexes[1]].setColor("red")
    exec_time = time.time() - start_time
    listOfDot.setShortestDistance(shortest_distance)
    listOfDot.setClosestIndexes(closest_indexes[0], closest_indexes[1])
    listOfDot.setNStep(num_step)
    listOfDot.setSolvingTime(exec_time)
    print("Brute Force Done")


def searchShortestPartition(arrOfDot, i, j, numStep=0):
    # Diasumsikan i adalah indeks awal partisi dan j indeks akhir partisi
    if (j-i == 0):
        print("Hanya 1 titik dalam partisi")
        return 1e6, [-1, -1], numStep
    elif (j-i == 1):  # Hanya ada 1 pasang titik
        # kembalikan tuple berisi shortest distance dan closest index
        return calculateDistance(arrOfDot[i], arrOfDot[j]), [i, j], numStep+1
    elif (j-i == 2):  # Ada 3 titik (penanganan kasus ganjil)
        dist1 = calculateDistance(arrOfDot[i], arrOfDot[i+1])
        dist2 = calculateDistance(arrOfDot[i], arrOfDot[j])
        dist3 = calculateDistance(arrOfDot[i+1], arrOfDot[j])
        if (dist1 <= dist2):
            if (dist1 <= dist3):
                return dist1, [i, i+1], numStep+3
            else:
                return dist3, [i+1, j], numStep+3
        else:
            if (dist2 <= dist3):
                return dist2, [i, j], numStep+3
            else:
                return dist3, [i+1, j], numStep+3
    else:  # Ada lebih dari 3 titik
        mid = (i+j)//2
        dist1, closestIndex1, numStep = searchShortestPartition(
            arrOfDot, i, mid, numStep)
        dist2, closestIndex2, numStep = searchShortestPartition(
            arrOfDot, mid+1, j, numStep)
        minDist = -1
        closestIndex = [-1, -1]
        if (dist1 <= dist2):
            minDist = dist1
            closestIndex = closestIndex1
        else:
            minDist = dist2
            closestIndex = closestIndex2
        # Cari titik-titik yang dipisah garis dengan selisih jarak pada absis maksimal d
        midX = arrOfDot[mid].getCoordinate()[0]
        nDim = arrOfDot[0].getNDim()
        p = mid
        while (p >= i and abs(arrOfDot[p].getCoordinate()[0]-midX) <= minDist):
            q = mid+1
            # Sementara masih cek semua titik di dalam strip
            while (q <= j and abs(arrOfDot[q].getCoordinate()[0]-midX) <= minDist):
                inRange = True
                for dim in range(1, nDim):
                    # Cek apakah ada jarak pada sumbu tertentu yang lebih besar dari minDist
                    if (abs(arrOfDot[q].getCoordinate()[dim]-arrOfDot[p].getCoordinate()[dim]) > minDist):
                        inRange = False
                        break
                if (inRange):
                    dist3 = calculateDistance(arrOfDot[p], arrOfDot[q])
                    numStep += 1
                    if (dist3 < minDist):
                        minDist = dist3
                        closestIndex = [p, q]
                q += 1
            p -= 1
        return minDist, closestIndex, numStep


def divideAndConquerShortestDistance(listOfDot):
    arrOfDot = listOfDot.getArrOfDot()
    shortest_distance = 0
    closest_indexes = [-1, -1]
    num_step = 0

    if (len(arrOfDot) > 1):
        sortArrOfDot(arrOfDot)
        start_time = time.time()
        shortest_distance, closest_indexes, num_step = searchShortestPartition(
            arrOfDot, 0, listOfDot.getNDots()-1)
        listOfDot.getArrOfDot()[closest_indexes[0]].setColor("red")
        listOfDot.getArrOfDot()[closest_indexes[1]].setColor("red")
    else:
        print("Jumlah titik kurang")
        start_time = time.time()
        shortest_distance = 0
    exec_time = time.time() - start_time
    listOfDot.setShortestDistance(shortest_distance)
    listOfDot.setClosestIndexes(closest_indexes[0], closest_indexes[1])
    listOfDot.setNStep(num_step)
    listOfDot.setSolvingTime(exec_time)
    print("Div and conquer done")
