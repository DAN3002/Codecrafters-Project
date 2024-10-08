# json.dumps() can't handle bytes, but bencoded "strings" need to be
# bytestrings since they might contain non utf-8 characters.
#
# Let's convert them to strings for printing to the console.
def bytes_to_str(data):
	if isinstance(data, bytes):
		return data.decode()

	raise TypeError(f"Type not serializable: {type(data)}")
