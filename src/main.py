from lib import DotCollection
from lib import Dot
from lib import algorithm


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

    # Brute Force
    algorithm.bruteForceShortestDistance(listOfDotBF)
    print(listOfDotBF.getNStep())
    print(listOfDotBF.getSolvingTime(), "s")
    ### Output ###

    ## Sepasang Titik Terdekat dan Jaraknya ##
    # Divide and Conquer

    # Brute Force
    print("Brute Force")
    print("Closest Points: ", "(", listOfDotBF.getClosestPoints()
          [0].getCoordinate(), ",", listOfDotBF.getClosestPoints()[1].getCoordinate(), ")")
    print("Distance:", listOfDotBF.getShortestDistance())

    ## Banyak Operasi Perhitungan Rumus Euclidean ##
    # Divide and Conquer

    # Brute Force
    print("N perhitungan")
    print("Brute Force", listOfDotBF.getNStep())

    ## Execution Time (Spesifikasikan komputer yang digunakan) ##
    # Divide and Conquer
    print("Execution Time")
    print("Brute Force:", listOfDotBF.getSolvingTime(), "s")

    # Brute Force

    ## Visualisasi titik ##
    if (nDim == 3):  # 3D
        # Divide and Conquer

        # Brute Force
        pass
    elif (nDim == 2):  # 2D
        # Divide and Conquer

        # Brute Force
        pass
    elif (nDim == 1):  # 1D
        # Divide and Conquer

        # Brute Force
        pass
