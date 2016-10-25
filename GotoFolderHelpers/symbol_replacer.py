# -*- coding: utf-8 -*-

def symbol_replacer(intext, replace_keys={}, replace_symbol="@"):
	""" 
	Generate a new arguments list replacing "@"+some_symbol with corresponding var.
	As long as all replace symbols are matched with a valid key symbol,
	it works well enough:
		"@@" becomes "@"
		"@@@<DefinedKey>" becomes "@<CorraspondingValue>"
		"@<DefinedKey>" becomes "<CorraspondingValue>"
	Some bad behaviours include: 
		"@" followed by an undefined symbol produces an empty string,
		 i.e. it removes "@<UndefinedSymbol>" entirly.
	"""
	
	replace_keys[replace_symbol] = replace_symbol

	vals = intext.split(replace_symbol)

	# print (intext)
	# print (vals)

	output = []
	is_escaped = False
	for val in vals:
		if is_escaped:
			if val == "":
				val = replace_symbol
				# output.append(replace_keys[val])
			if val[0] in replace_keys:
				val = replace_keys[val[0]] + val[1:]
				output.append(val)
			is_escaped = False
		else:
			is_escaped = True
			if val == "":
				pass
			else:
				output.append(val)
	return "".join(output)