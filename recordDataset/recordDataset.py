####################################################################################################
# recordDataset.py
####################################################################################################
import tkinter as tk
import serial, threading

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Erstellen und Platzieren der Steuerelemente
        self.__buttonWidth = 15
        self.__entryWidth = 40
        self.__listBoxWidth = 50
        self.__listBoxHight = 20

        self.startButton = tk.Button(self, text="Start", width=self.__buttonWidth, command=self.startCom)
        self.startButton.grid(row=0, column=0, pady=10, padx=(0, 10), sticky="E")

        self.stopButton = tk.Button(self, text="Stop", width=self.__buttonWidth, command=self.stopCom)
        self.stopButton.grid(row=0, column=1, pady=10, padx=(10, 0), sticky="W")

        self.deleteButton = tk.Button(self, text="Löschen", width=self.__buttonWidth, command=self.clearData)
        self.deleteButton.grid(row=1, column=0, pady=10, padx=(0, 10), sticky="E")

        self.saveDataButton = tk.Button(self, text="Speicheren", width=self.__buttonWidth, command=self.createFile)
        self.saveDataButton.grid(row=1, column=1, pady=10, padx=(10, 0), sticky="W")

        self.pathEntry = tk.Entry(self, width=self.__entryWidth)
        self.pathEntry.insert(0, "Path:\\\\")
        self.pathEntry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self, width=self.__listBoxWidth, height=self.__listBoxHight,
                                  yscrollcommand=self.scrollbar.set)
        self.listbox.insert(tk.END, "Nr.    |   ax  |    ay     |   az  |   gx  |   gy  |   gz")
        self.scrollbar["command"] = self.listbox.yview
        self.listbox.grid(row=3, column=0, columnspan=2, sticky="NESW", padx=(10, 0))
        self.scrollbar.grid(row=3, column=2, sticky="NSW")

        self.statusLabel = tk.Label(self, text="Status: ")
        self.statusLabel.grid(row=4, column=0, pady=5, columnspan=2, sticky="W", padx=10)

        # ********************************************

        self.ser = serial.Serial(port='COM5', baudrate=115200, bytesize=8, timeout=100, stopbits=serial.STOPBITS_ONE)
        self.startRecording = False
        self.data = list()

    def startCom(self):
        self.startRecording = True
        self.comThread = threading.Thread(target=self.readSerial)
        self.comThread.start()
        self.statusLabel.config(text="Status: Start recording")
        print("Start recording")

    def stopCom(self):
        self.startRecording = False
        # TODO Wie beendet man einen Thread in Python? Überhaupt nötig? -> wird von selbst beendet wenn auf False gesetzt?
        self.statusLabel.config(text="Status: Stop recording")
        print("Stop recording")

    def readSerial(self):
        while self.startRecording:
            line = self.ser.readline()
            str = line.decode('utf-8').replace("\r\n", "\n")

            print(str)
            self.listbox.insert(tk.END, str)
            self.data.append(str)

    def clearData(self):
        self.data.clear()
        self.listbox.delete(0, tk.END)
        self.listbox.insert(tk.END, "Nr.    |   ax  |   ay  |   az  |   gx  |   gy  |   gz")

    def createFile(self):
        strPath = self.pathEntry.get()
        try:
            datei = open(strPath, "w", encoding="utf-8")
            datei.writelines(self.data)
            datei.close()
            self.statusLabel.config(text="Status: File erstellt")
            print("Status: File erstellt")
        except Exception as ex:
            self.statusLabel.config(text="Status: Datei konnte nicht erstellt werden")
            print("Status: Datei konnte nicht erstellt werden\nException:", ex)

# Hauptprogramm
def recordDataset():
    # Fenster erstellen und Titel festlegen
    root = tk.Tk()
    root.title("")
    root.resizable(False, False)

    # Instanz der App-Klasse erzeugen und ins Fenster packen
    app = App(root)
    app.pack()

    root.mainloop()

# recordDataset()