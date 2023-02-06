
# coding: utf-8
 
import sys, os
from cx_Freeze import setup, Executable

file_path = input("input file: ")

if sys.platform == "win32":
    base = None # "Win32GUI" 

    os.environ['TCL_LIBRARY'] = "C:\\Users\\hakka\\anaconda3\\tcl\\tcl8.6"
    os.environ['TK_LIBRARY']  = "C:\\Users\\hakka\\anaconda3\\tcl\\tk8.6"
else:
    base = None # "Win32GUI"

#importして使っているライブラリを記載
packages = []

#importして使っているライブラリを記載（こちらの方が軽くなるという噂）
includes = [
    "sys",
    "os",
    "docx2pdf"
]

#excludesでは、パッケージ化しないライブラリやモジュールを指定する。
"""
numpy,pandas,lxmlは非常に重いので使わないなら、除く。（合計で80MBほど）
他にも、PIL(5MB)など。
"""
excludes = [
    "numpy",
    "pandas",
    "lxml"
]

exe = Executable(
    script = file_path,
    base = base
)
 
# セットアップ
setup(name = 'main',
      options = {
          "build_exe": {
              "packages": packages, 
              "includes": includes, 
              "excludes": excludes,
          }
      },
      version = '0.1',
      description = 'converter',
      executables = [exe])