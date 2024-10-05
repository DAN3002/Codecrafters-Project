def check_next_char(file_contents, current_index, expected_char):
	if current_index + 1 >= len(file_contents):
		return False

	if file_contents[current_index + 1] != expected_char:
		return False

	return True

def scan_string(current_index, file_contents):
	content = ""
	have_string = False
 
	index = current_index + 1
	while index < len(file_contents):
		if file_contents[index] == "\n":
			break
		elif file_contents[index] != "\"":
			content += file_contents[index]
		else:
			have_string = True
			break

		index += 1
  
	return content if have_string else None, index

def scan_numberic(current_index, file_contents):
	value = ""
	
	index = current_index
	while index < len(file_contents):
		c = file_contents[index]
		
		if c.isnumeric():
			value += c
		elif c == ".":
			# Already have dot in number => stop
			if "." in value:
				break
			else:
				value += c
		else:
			break

		index += 1

	return value, index
	
