import statistics

class Statistics:

    def __init__(self, datos) -> None:        
        self.datos = datos

    def count(self) :
        return len(self.datos)

    def sum(self) :
        return sum(self.datos)

    def min(self) :
        return min(self.datos)

    def max(self) :
        return max(self.datos)
    
    def mean(self) :
        return statistics.mean(self.datos)
    
    def median(self) :
        return statistics.median(self.datos)

    def mode(self) :
        return statistics.mode(self.datos)