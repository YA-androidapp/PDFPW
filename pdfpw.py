#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Required:
#   pip install pikepdf


import pikepdf
import itertools
import sys


target_pdf = './in.pdf'
output_pdf = './out.pdf'

CHARS = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
MIN_DIGIT = 4
MAX_DIGIT = 4


def main():
    for count in range(MIN_DIGIT, MAX_DIGIT + 1):
        print(' ' * 10 + 'Number of digits: {}'.format(count))

        for password in itertools.product(CHARS,repeat=MIN_DIGIT):
            try:
                pdf = pikepdf.open(target_pdf, password=''.join(password))
                pdf_unlock = pikepdf.new()
                pdf_unlock.pages.extend(pdf.pages)
                pdf_unlock.save(output_pdf)
            except:
                pass # print(' ' * 10 + 'Wrong: ' + password)
            else:
                print('Searched: ' + password)
                sys.exit()

        count += 1


if __name__ == '__main__':
    main()
