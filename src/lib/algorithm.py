import math


def swap(arrOfDot, a, b) :
        print("swap")
        temp = arrOfDot[a]
        arrOfDot[a] = arrOfDot[b]
        arrOfDot[b] = temp

# Sort arrOfDot berdasarkan coordinate[0] (sumbu X), memakai algoritma quicksort versi 2 dengan pemilihan pivot selalu elemen pertama
def partition(arrOfDot, i, j) :
    pivotX = arrOfDot[i].getCoordinate()[0]
    p = i+1
    q = j
    while (p < q) :
        while arrOfDot[p].getCoordinate()[0] < pivotX :
            p += 1
        while arrOfDot[q].getCoordinate()[0] > pivotX :
            q -= 1
        
        if (p < q) :
            swap(arrOfDot,p,q)
    
    swap(arrOfDot,i,q)
    return q

def sortArrOfDot(arrOfDot, i=0, j=-1) :
    if (j==-1) :
        j = len(arrOfDot)-1
    if (i < j) :
        pos = partition(arrOfDot,i,j)
        sortArrOfDot(arrOfDot,i,pos-1)
        sortArrOfDot(arrOfDot,pos+1,j)

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


def bruteForceShortestDistance(arrOfDot):
    distance = 0
