# -*- coding: utf-8 -*-

import sys, os

# add parent dir to PYTHONPATH, for import of GotoFolder module
basename = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(basename)

from GotoFolderHelpers.symbol_replacer import symbol_replacer

tests_texts =[
"@d",
"-cur_console:nad:@d",
"-cur_console:nad:@@d",
"-cur_console:nad:@@@d",
"@", # UNDEFINED BEHAVIOR!
"@@",
"@a", # UNDEFINED BEHAVIOR!
"NoSymbol"
]


def main():
	for text in tests_texts:
		print (symbol_replacer(text, {"d":"<DIR>", "l":"<LINE>"}))
		print ("-----------")

if __name__ == '__main__':
	main()