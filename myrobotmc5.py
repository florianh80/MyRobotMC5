# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import sounddevice as sd
from mainwindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):

    SAMPLERATE = 48000
    FILTER = np.array([])

    CONTROL_TONES = {
        "live_mode": [17.2, 17.4, 17.6, 17.8, 17.6],
        "turn_left": [17.2, 17.4, 17.8, 17.6, 17.8],
        "turn_right": [17.2, 17.4, 17.8, 17.4, 17.8],
        "stop": [17.2, 17.4, 17.8, 18, 17.8],
        "forward": [17.2, 17.4, 17.6, 18, 17.6],
        "backward": [17.2, 17.4, 17.6, 18.2, 17.6],
        "led_fast": [17.2, 17.4, 18, 17.6, 18],
        "led_slow": [17.2, 17.4, 18, 17.4, 18],
        "sound1": [17.2, 17.4, 18, 17.8, 18],
        "sound2": [17.2, 17.4, 18, 18.2, 18],
        "sound3": [17.2, 17.4, 18.2, 17.4, 18.2],
        "sound4": [17.2, 17.4, 18.2, 17.6, 18.2],
        "sound5": [17.2, 17.4, 18.2, 17.8, 18.2],
    }

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_tonegen()
        QTimer.singleShot(100, lambda: self.exec_command("live_mode"))

        self.momentary_mode_switch()

        self.ui.actionContinuousModeSwitch.toggled.connect(self.momentary_mode_switch);

        self.ui.btnStop.clicked.connect(lambda: self.exec_command("stop"))

        self.ui.btnSound1.clicked.connect(lambda: self.exec_command("sound1"))
        self.ui.btnSound2.clicked.connect(lambda: self.exec_command("sound2"))
        self.ui.btnSound3.clicked.connect(lambda: self.exec_command("sound3"))
        self.ui.btnSound4.clicked.connect(lambda: self.exec_command("sound4"))
        self.ui.btnSound5.clicked.connect(lambda: self.exec_command("sound5"))

        self.ui.btnLEDFast.clicked.connect(lambda: self.exec_command("led_fast"))
        self.ui.btnLEDSlow.clicked.connect(lambda: self.exec_command("led_slow"))

        self.ui.actionQuit.triggered.connect(MainWindow.close)

        self.ui.btnInit.clicked.connect(lambda: self.exec_command("live_mode"))

    def init_tonegen(self):
        self.FILTER = np.append(self.FILTER, np.sin(np.arange(0, 100) / 100 * np.pi / 2.0))
        self.FILTER = np.append(self.FILTER, np.ones(int(0.15 * self.SAMPLERATE) - 200))
        self.FILTER = np.append(self.FILTER, np.sin(np.arange(100, 0, step=-1) / 100.0 * np.pi / 2.0))

    def generate_tone(self, freq):
        # samples = np.array([])

        samples = 1.0 * np.sin((np.arange(0, self.SAMPLERATE * 0.15) * 2 * np.pi * freq) / self.SAMPLERATE)
        samples = np.multiply(samples, self.FILTER)

        return samples

    def exec_command(self, cmd):
        if type(cmd) is not str:
            return

        samples = np.array([])

        tones = self.CONTROL_TONES.get(cmd) or []
        for freq in tones:
            samples = np.append(samples, self.generate_tone(freq * 1000.0))
            samples = np.append(samples, np.zeros(4800))

        sd.play(samples, self.SAMPLERATE)

    def momentary_mode_switch(self):
        try:
            self.ui.btnForward.disconnect()
            self.ui.btnBackward.disconnect()
            self.ui.btnLeft.disconnect()
            self.ui.btnRight.disconnect()
        except:
            pass

        if self.ui.actionContinuousModeSwitch.isChecked():
            self.ui.btnForward.pressed.connect(lambda: self.exec_command("forward"))
            self.ui.btnBackward.pressed.connect(lambda: self.exec_command("backward"))
            self.ui.btnLeft.pressed.connect(lambda: self.exec_command("turn_left"))
            self.ui.btnRight.pressed.connect(lambda: self.exec_command("turn_right"))

            self.ui.btnForward.released.connect(lambda: self.exec_command("stop"))
            self.ui.btnBackward.released.connect(lambda: self.exec_command("stop"))
            self.ui.btnLeft.released.connect(lambda: self.exec_command("stop"))
            self.ui.btnRight.released.connect(lambda: self.exec_command("stop"))
        else:
            self.ui.btnForward.clicked.connect(lambda : self.exec_command("forward") )
            self.ui.btnBackward.clicked.connect(lambda : self.exec_command("backward"))
            self.ui.btnLeft.clicked.connect(lambda : self.exec_command("turn_left"))
            self.ui.btnRight.clicked.connect(lambda: self.exec_command("turn_right"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
