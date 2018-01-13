import sys
import os
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["tdl", "_cffi_backend", "threading"]}
os.environ['TCL_LIBRARY'] = r'C:\\Users\\harri\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\\harri\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6'

base = "Win32GUI"
addtional_mods = ['numpy.core._methods', 'numpy.lib.format']
setup(  name = "SpanishStudies",
        version = "1.13.18",
        description = "Application for studying spanish",
        options = {"build_exe": build_exe_options},
        executables = [Executable("SpanishStudier.pyw", base=base)])
