from lib import DotCollection
from lib import Dot
from lib import algorithm


if __name__ == "__main__":
    ### Input ###
    n = int(input("Masukkan banyak titik (n): "))
    nDim = int(input("Masukkan dimensi titik (nDim): "))

    ### Process ###

    ## Generating Dots ##
    listOfDot = DotCollection.DotCollection(n,nDim)
    algorithm.sortArrOfDot(listOfDot.getArrOfDot())
    listOfDot.printArr()

    ## Calculate Shortest Distance, time, etc ##
    # Divide and Conquer

    # Brute Force

    ### Output ###

    ## Sepasang Titik Terdekat dan Jaraknya ##
    # Divide and Conquer

    # Brute Force

    ## Banyak Operasi Perhitungan Rumus Euclidean ##
    # Divide and Conquer

    # Brute Force

    ## Execution Time (Spesifikasikan komputer yang digunakan) ##
    # Divide and Conquer

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
