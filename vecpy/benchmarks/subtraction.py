from vecpy_frameworks import VecpyBenchmark
from vecpy import sub_vectors

class SubtractionBenchmark(VecpyBenchmark):
    
    def time_empty(self):
        sub_vectors([], [])

    def time_five(self):
        sub_vectors([1, 2, 3, 4], [1, 2, 3, 4])