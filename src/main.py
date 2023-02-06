from docx2pdf import convert
import sys
# import time
# import re


def __main__():
    try:
        count_files = len(sys.argv)-1

        for i in range(count_files):
            file_path = sys.argv[i+1]

            convert(file_path)

    except Exception as e:
        print(e)


__main__()
