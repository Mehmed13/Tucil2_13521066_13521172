from random import uniform


class Dot:
    # Constructor
    def __init__(self, nDim):
        # Attributes
        self._nDim = nDim
        self._color = 'blue'
        self._coordinate = list()  # Pembangkitan coordinate acak
        for i in range(nDim):
            # Ini buat starting, mungkin nanti direvisi lagi
            # tipe coordinate adalah floating point
            self._coordinate.append(uniform(-10000, 10000))

    # Getter
    def getNDim(self):
        return self._nDim

    def getColor(self):
        return self._color

    def getCoordinate(self):
        return self._coordinate

    # Setter
    def setColor(self, color):
        self._color = color
