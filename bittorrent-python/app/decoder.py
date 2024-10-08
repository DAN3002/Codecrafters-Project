from app.utils import bytes_to_str

def decode_list(bencoded_value):
	init_len = len(bencoded_value)
	bencoded_value = bencoded_value[1:]

	decoded_list = []
	while len(bencoded_value) != 0 and chr(bencoded_value[0]) != 'e':
		decoded_value, new_index = decode_bencode(bencoded_value)
		decoded_list.append(decoded_value)
  
		bencoded_value = bencoded_value[new_index + 1:]

	return decoded_list, init_len - len(bencoded_value) 

def decode_string(bencoded_value):
	colon_index = bencoded_value.find(b":")
	if colon_index == -1:
		raise ValueError("Invalid encoded value")
	
	string_size = int(bencoded_value[0:colon_index])
	if (colon_index + string_size > len(bencoded_value)):
		raise ValueError("Invalid string size")

	str_value = bencoded_value[colon_index + 1:colon_index + string_size + 1]
	new_index = colon_index + string_size

	return str_value, new_index

def decode_int(bencoded_value):
	end_int_index = bencoded_value.find(b"e")
	if end_int_index == -1:
		raise ValueError("Invalid encoded value")
	return int(bencoded_value[1:end_int_index]), end_int_index

def decode_dict(bencoded_value):
	init_len = len(bencoded_value)
	bencoded_value = bencoded_value[1:]

	decoded_dict = {}
	while len(bencoded_value) != 0 and chr(bencoded_value[0]) != 'e':
		key, new_index = decode_bencode(bencoded_value)
		bencoded_value = bencoded_value[new_index + 1:]
		key = bytes_to_str(key)

		value, new_index = decode_bencode(bencoded_value)
		bencoded_value = bencoded_value[new_index + 1:]
  
		decoded_dict[key] = value
	
	return decoded_dict, init_len - len(bencoded_value)

def decode_bencode(bencoded_value):
	if chr(bencoded_value[0]).isdigit():
		return decode_string(bencoded_value)
	elif chr(bencoded_value[0]) == 'i':
		return decode_int(bencoded_value)
	elif chr(bencoded_value[0]) == 'l':
		return decode_list(bencoded_value)
	elif chr(bencoded_value[0]) == 'd':
		return decode_dict(bencoded_value)
	else:
		raise NotImplementedError("")

__all__ = ["decode_bencode"]
