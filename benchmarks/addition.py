from vecpy_frameworks import VecpyBenchmark
from vecpy import add_vectors

class AdditionBenchmark(VecpyBenchmark):
    
    def time_empty(self):
        add_vectors([], [])

    def time_five(self):
        add_vectors([1, 2, 3, 4], [1, 2, 3, 4])


