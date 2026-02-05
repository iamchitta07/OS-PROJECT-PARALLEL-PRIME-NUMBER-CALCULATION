import ctypes
import os

def get_logical_cores():
    lib_path = os.path.abspath("./utils/libcpu.so")
    lib = ctypes.CDLL(lib_path)
    lib.getCPUInfo.restype = ctypes.c_int

    # Get the pointer and access the contents
    cores = lib.getCPUInfo()
    return cores
