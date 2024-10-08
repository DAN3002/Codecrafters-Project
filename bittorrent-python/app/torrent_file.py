import hashlib
import bencodepy

from app.decoder import decode_bencode
from app.utils import bytes_to_str

def read_info(filepath):
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

	return {
		'tracker_url': tracker_url,
		'file_length': info['length'],
		'info_hash': info_hash,
		'piece_length': piece_length,
		'pieces_hash': pieces_hash,
	}

__all__ = ["read_info"]
