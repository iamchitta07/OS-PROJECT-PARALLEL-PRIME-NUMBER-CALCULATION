import ctypes
import os

def get_runtime(upper_limit: int, children: int) -> float:
    lib_path = os.path.abspath("./utils/libtime.so")
    lib = ctypes.CDLL(lib_path)
    lib.findPrimesInParallel.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.findPrimesInParallel.restype = ctypes.c_double

    # Get the pointer and access the contents
    time_taken:float = lib.findPrimesInParallel(upper_limit, children)
    return time_taken
