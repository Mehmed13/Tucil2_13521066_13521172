from lib import DotCollection
from lib import algorithm
from lib import visualizer
import subprocess

if __name__ == "__main__":
    ### Input ###
    valid = False
    while (not(valid)) :
        n = int(input("Masukkan banyak titik (n): "))
        nDim = int(input("Masukkan dimensi titik (nDim): "))
        if (n <= 1 or nDim < 1) :
            print("Masukan tidak valid. Pastikan banyak titik > 1 dan dimensi titik >= 1")
        else :
            valid = True

    ### Process ###

    ## Generating Dots ##
    listOfDotDnC = DotCollection.DotCollection(n, nDim)
    # algorithm.sortArrOfDot(listOfDotDnC.getArrOfDot())
    listOfDotBF = DotCollection.DotCollection()
    listOfDotDnC.copy(listOfDotBF)
    ## Calculate Shortest Distance, time, etc ##
    # Divide and Conquer
    algorithm.divideAndConquerShortestDistance(listOfDotDnC)
    # Brute Force
    algorithm.bruteForceShortestDistance(listOfDotBF)

    ### Output ###
    
    getModel = subprocess.Popen(['wmic', 'computersystem', 'get', 'model'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    model = getModel.stdout.read().decode()
    choice = input("Simpan output ke file ? Y/N\n")
    if (choice == 'Y') :
        fileName = input("Masukkan nama file : ")
        f = open(fileName, "w", encoding="utf-8")
        # Divide and Conquer
        f.write("Divide and Conquer\n")
        f.write("Closest Points: (" + str(listOfDotDnC.getClosestPoints()
            [0].getCoordinate()) + "," + str(listOfDotDnC.getClosestPoints()[1].getCoordinate())+ ")\n")
        f.write("Distance: "+ str(listOfDotDnC.getShortestDistance()) + "\n")

        # Brute Force
        f.write("Brute Force\n")
        f.write("Closest Points: ("+ str(listOfDotBF.getClosestPoints()
            [0].getCoordinate())+ "," + str(listOfDotBF.getClosestPoints()[1].getCoordinate())+ ")\n")
        f.write("Distance: "+ str(listOfDotBF.getShortestDistance()) + "\n")

        ## Banyak Operasi Perhitungan Rumus Euclidean ##
        # Divide and Conquer
        f.write("N perhitungan\n")
        f.write("Divide and Conquer: "+ str(listOfDotDnC.getNStep()) + "\n")

        # Brute Force
        f.write("Brute Force: "+ str(listOfDotBF.getNStep()) + "\n")

        ## Execution Time (Spesifikasikan komputer yang digunakan) ##
        # Divide and Conquer
        f.write("Execution Time\n")
        f.write("Divide and Conquer: "+ str(listOfDotDnC.getSolvingTime())+ "s\n")

        # Brute Force
        f.write("Brute Force: "+ str(listOfDotBF.getSolvingTime())+ "s\n")
        # Komputer yang digunakan
        f.write("Computer ")
        f.write(model)
        f.close()

    ## Sepasang Titik Terdekat dan Jaraknya ##
    # Divide and Conquer
    print("Divide and Conquer")
    print("Closest Points: ", "(", listOfDotDnC.getClosestPoints()
          [0].getCoordinate(), ",", listOfDotDnC.getClosestPoints()[1].getCoordinate(), ")")
    print("Distance: ", listOfDotDnC.getShortestDistance())

    # Brute Force
    print("Brute Force")
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

    # Komputer yang digunakan
    print("Computer", end=" ")
    print(model)

    ## Visualisasi titik ##
    if (nDim == 3):  # 3D
        visualizer.show3D(listOfDotBF)
    elif (nDim == 2):  # 2D
        visualizer.show2D(listOfDotBF)
    elif (nDim == 1):  # 1D
        visualizer.show1D(listOfDotBF)
    else:
        print("Kumpulan titik tidak dapat divisualisasikan")
