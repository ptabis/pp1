class Zbiory:
    @staticmethod
    def iloczyn(zbior1, zbior2):
        return zbior1.intersection(zbior2)
    @staticmethod
    def suma(zbior1, zbior2):
        return zbior1|zbior2
    @staticmethod
    def roznica(zbior1, zbior2):
        return zbior1-zbior2
    