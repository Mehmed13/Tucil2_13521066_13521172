import Dot
import math


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
