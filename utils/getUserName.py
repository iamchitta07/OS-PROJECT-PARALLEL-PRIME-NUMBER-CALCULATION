import ctypes
import os

def get_user_name()->str:
    lib_path = os.path.abspath("./utils/libusername.so")
    lib = ctypes.CDLL(lib_path)
    lib.getUserName.restype = ctypes.c_char_p

    raw_result = lib.getUserName()
    user_name:str = raw_result.decode('utf-8')
    return user_name
