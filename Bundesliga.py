class Bundesliga:

    class Vereine:
        def __init__(self):
            self.vereine = list()

    class Jahre:
        def __init__(self):
            self.jahre = {}

        def __setitem__(self, key, value):
            self.jahre[key] = value

    def __init__(self):
        self.bundesliga = {}
        self.jahre = Bundesliga.Jahre()
        self.vereine = Bundesliga.Vereine()

    def neuer_spieler(self, name):
        self.bundesliga[name] = self.jahre

    def vereine_hinzufuegen(self, daten):

        name = 0
        aktueller_verein = 1
        vereinsname = 2
        von = 3
        bis = 4

        for i in range(0, len(daten)):
            self.neuer_spieler(daten[name])
            if (daten[von] == daten[bis]):
                self.jahre[daten[von]] = daten[vereinsname]
            else:
                for k in range(daten[von], daten[bis]):
                    self.jahre[k] = daten[vereinsname]

            vereinsname = vereinsname+3
            von = von+3
            bis = bis+3

            if (bis >= len(daten)):
                for index in range(daten[von], 2023):
                    self.jahre[index] = daten[vereinsname]
                self.jahre[2023] = daten[aktueller_verein]
                break
