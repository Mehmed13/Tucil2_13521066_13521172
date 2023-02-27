from lib import DotCollection
from lib import algorithm
from lib import visualizer


if __name__ == "__main__":
    ### Input ###
    n = int(input("Masukkan banyak titik (n): "))
    nDim = int(input("Masukkan dimensi titik (nDim): "))

    ### Process ###

    ## Generating Dots ##
    listOfDotDnC = DotCollection.DotCollection(n, nDim)
    # algorithm.sortArrOfDot(listOfDotDnC.getArrOfDot())
    listOfDotDnC.printArr()
    listOfDotBF = DotCollection.DotCollection()
    listOfDotDnC.copy(listOfDotBF)
    listOfDotBF.printArr()
    ## Calculate Shortest Distance, time, etc ##
    # Divide and Conquer
    algorithm.divideAndConquerShortestDistance(listOfDotDnC)
    # Brute Force
    algorithm.bruteForceShortestDistance(listOfDotBF)

    ### Output ###

    ## Sepasang Titik Terdekat dan Jaraknya ##
    # Divide and Conquer
    print("Divide and Conquer")
    print(listOfDotDnC.getClosestIndexes())
    print("Closest Points: ", "(", listOfDotDnC.getClosestPoints()
          [0].getCoordinate(), ",", listOfDotDnC.getClosestPoints()[1].getCoordinate(), ")")
    print("Distance: ", listOfDotDnC.getShortestDistance())

    # Brute Force
    print("Brute Force")
    print(listOfDotBF.getClosestIndexes())
    print("Closest Points: ", "(", listOfDotBF.getClosestPoints()
          [0].getCoordinate(), ",", listOfDotBF.getClosestPoints()[1].getCoordinate(), ")")
    print("Distance: ", listOfDotBF.getShortestDistance())

    ## Banyak Operasi Perhitungan Rumus Euclidean ##
    # Divide and Conquer
    print("N perhitungan")
    print("Divide and Conquer: ", listOfDotDnC.getNStep())

    # Brute Force
    print("Brute Force: ", listOfDotBF.getNStep())

    ## Execution Time (Spesifikasikan komputer yang digunakan) ##
    # Divide and Conquer
    print("Execution Time")
    print("Divide and Conquer: ", listOfDotDnC.getSolvingTime(), "s")

    # Brute Force
    print("Brute Force: ", listOfDotBF.getSolvingTime(), "s")

    ## Visualisasi titik ##
    if (nDim == 3):  # 3D
        visualizer.show3D(listOfDotBF)
    elif (nDim == 2):  # 2D
        visualizer.show2D(listOfDotBF)
    elif (nDim == 1):  # 1D
        visualizer.show1D(listOfDotBF)
    else:
        print("Kumpulan titik tidak dapat divisualisasikan")
