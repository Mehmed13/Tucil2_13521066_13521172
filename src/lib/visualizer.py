import matplotlib.pyplot as plt


def show3D(listOfDot):
    # Fungsi untuk menampilkan visualisasi 3 dimensi dari titik-titik
    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')
    plt.title("Visualisasi 3D Kumpulan Titik")
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    arrOfDot = listOfDot.getArrOfDot()
    dot1 = arrOfDot[listOfDot.getClosestIndexes()[0]]
    dot2 = arrOfDot[listOfDot.getClosestIndexes()[1]]
    for i in range(listOfDot.getNDots()):
        if ((i != listOfDot.getClosestIndexes()[0]) and (i != listOfDot.getClosestIndexes()[1])):
            coordinate = arrOfDot[i].getCoordinate()
            ax.scatter(coordinate[0], coordinate[1],
                       coordinate[2], color=arrOfDot[i].getColor())
    coordinate1 = arrOfDot[listOfDot.getClosestIndexes()[0]].getCoordinate()
    coordinate2 = arrOfDot[listOfDot.getClosestIndexes()[1]].getCoordinate()
    ax.scatter(coordinate1[0], coordinate1[1],
               coordinate1[2], color=arrOfDot[listOfDot.getClosestIndexes()[0]].getColor())
    ax.scatter(coordinate2[0], coordinate2[1],
               coordinate2[2], color=arrOfDot[listOfDot.getClosestIndexes()[1]].getColor())
    plt.show()


def show2D(listOfDot):
    # Fungsi untuk menampilkan visualisasi 2 dimensi dari titik-titik
    plt.title('Visualisasi 2D Kumpulan Titik')  # Title of the plot
    plt.xlabel('X-axis')  # X-Label
    plt.ylabel('Y-axis')  # Y-Label
    arrOfDot = listOfDot.getArrOfDot()
    for i in range(listOfDot.getNDots()):
        if ((i != listOfDot.getClosestIndexes()[0]) and (i != listOfDot.getClosestIndexes()[1])):
            coordinate = arrOfDot[i].getCoordinate()
            plt.scatter(coordinate[0], coordinate[1],
                        color=arrOfDot[i].getColor())

    coordinate1 = arrOfDot[listOfDot.getClosestIndexes()[
        0]].getCoordinate()
    coordinate2 = arrOfDot[listOfDot.getClosestIndexes()[1]].getCoordinate()
    plt.scatter(coordinate1[0], coordinate1[1],
                color=arrOfDot[listOfDot.getClosestIndexes()[0]].getColor())
    plt.scatter(coordinate2[0], coordinate2[1],
                color=arrOfDot[listOfDot.getClosestIndexes()[1]].getColor())
    plt.show()


def show1D(listOfDot):
    # Fungsi untuk menampilkan visualisasi 1 dimensi dari titik-titik
    plt.title('Visualisasi 1D Kumpulan Titik')  # Title of the plot
    plt.xlabel('X-axis')  # X-Label
    plt.ylabel('Y-axis')  # Y-Label
    arrOfDot = listOfDot.getArrOfDot()
    for i in range(listOfDot.getNDots()):
        if ((i != listOfDot.getClosestIndexes()[0]) and (i != listOfDot.getClosestIndexes()[1])):
            coordinate = arrOfDot[i].getCoordinate()
            plt.scatter(coordinate[0], 0,
                        color=arrOfDot[i].getColor())

    coordinate1 = arrOfDot[listOfDot.getClosestIndexes()[
        0]].getCoordinate()
    coordinate2 = arrOfDot[listOfDot.getClosestIndexes()[1]].getCoordinate()
    plt.scatter(coordinate1[0], 0,
                color=arrOfDot[listOfDot.getClosestIndexes()[0]].getColor())
    plt.scatter(coordinate2[0], 0,
                color=arrOfDot[listOfDot.getClosestIndexes()[1]].getColor())
    plt.show()
