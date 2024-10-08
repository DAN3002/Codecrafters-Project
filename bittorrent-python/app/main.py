import json
import sys

from app.utils import bytes_to_str
from app.decoder import decode_bencode

def main():
	command = sys.argv[1]

	if command == "decode":
		bencoded_value = sys.argv[2].encode()

		# Uncomment this block to pass the first stage
		decoded_value, index = decode_bencode(bencoded_value)
		print(json.dumps(decoded_value, default=bytes_to_str))
	else:
		raise NotImplementedError(f"Unknown command {command}")


if __name__ == "__main__":
	main()
