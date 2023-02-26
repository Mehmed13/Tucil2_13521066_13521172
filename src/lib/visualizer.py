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
    for i in range(listOfDot.getNDots()):
        coordinate = arrOfDot[i].getCoordinate()
        ax.scatter(coordinate[0], coordinate[1],
                   coordinate[2], color=arrOfDot[i].getColor())
    plt.show()


def show2D(listOfDot):
    # Fungsi untuk menampilkan visualisasi 2 dimensi dari titik-titik
    plt.title('Visualisasi 2D Kumpulan Titik')  # Title of the plot
    plt.xlabel('X-axis')  # X-Label
    plt.ylabel('Y-axis')  # Y-Label
    arrOfDot = listOfDot.getArrOfDot()
    for i in range(listOfDot.getNDots()):
        coordinate = arrOfDot[i].getCoordinate()
        plt.scatter(coordinate[0], coordinate[1], color=arrOfDot[i].getColor())
    plt.show()


def show1D(listOfDot):
    # Fungsi untuk menampilkan visualisasi 1 dimensi dari titik-titik
    plt.title('Visualisasi 1D Kumpulan Titik')  # Title of the plot
    plt.xlabel('X-axis')  # X-Label
    plt.ylabel('Y-axis')  # Y-Label
    arrOfDot = listOfDot.getArrOfDot()
    for i in range(listOfDot.getNDots()):
        coordinate = arrOfDot[i].getCoordinate()
        plt.scatter(coordinate[0], 0, color=arrOfDot[i].getColor())
    plt.show()
