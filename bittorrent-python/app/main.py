import json
import sys
import hashlib
import bencodepy

from app.utils import bytes_to_str
from app.decoder import decode_bencode

def main():
	command = sys.argv[1]

	if command == "decode":
		bencoded_value = sys.argv[2].encode()

		# Uncomment this block to pass the first stage
		decoded_value, index = decode_bencode(bencoded_value)
		print(json.dumps(decoded_value, default=bytes_to_str))
	elif command == "info":
		filepath = sys.argv[2]
		with open(filepath, "rb") as f:
			file_content = f.read()
			f.close()
   
		decoded_value, _ = decode_bencode(file_content)

		tracker_url = bytes_to_str(decoded_value['announce'])
		info = decoded_value['info']
		# Just too lazy to implement encode method =))
		info_hash = hashlib.sha1(bencodepy.encode(info))

		piece_length = info['piece length']
		pieces = info['pieces']
		pieces_hash = [pieces[i:i+piece_length] for i in range(0, len(pieces), piece_length)]

		print(f"Tracker URL: {tracker_url}")
		print(f"Length: {info['length']}")
		print(f"Info Hash: {info_hash.hexdigest()}")
		print(f"Piece Length: {piece_length}")
		for piece_hash in pieces_hash:
			print(piece_hash.hex())
	else:
		raise NotImplementedError(f"Unknown command {command}")


if __name__ == "__main__":
	main()
