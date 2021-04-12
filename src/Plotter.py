#import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
from math import floor
import matplotlib

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class ScrollableWindow(QtWidgets.QMainWindow):
    def __init__(self, fig):
        self.qapp = QtWidgets.QApplication([])

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0,0,0,0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        self.show()
        exit(self.qapp.exec_()) 

def ShowPlot(i, BER, E, Prob, Length):
    names=["Stop and wait", "Go back n","Selective Repeat", 
           "Kod parzystości", "Kod dublowania", "CRC32"]
    i=0
    fig, axes = plt.subplots(ncols=3, nrows=3, figsize=(16,16))
    for ax in axes.flatten():
        ax.plot(Prob, E, label="E")
        ax.plot(Prob, BER,  label="BER")
        ax.legend()
        ax.set_title(names[i%3 ] + " || " + names[int(floor(i/3))+3] + " || " + "Długośc ramki "+ str(Length) )
        ax.set_xlabel('Prawodopodobieństwo błedu')
        ax.set_ylabel('Współczynnik:')   
        i += 1
    okno = ScrollableWindow(fig)
