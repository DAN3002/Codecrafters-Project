import json
import sys
import requests

from app.utils import bytes_to_str
from app.decoder import decode_bencode
from app.torrent_file import read_info

def main():
	command = sys.argv[1]

	if command == "decode":
		bencoded_value = sys.argv[2].encode()

		decoded_value, _ = decode_bencode(bencoded_value)
		print(json.dumps(decoded_value, default=bytes_to_str))
	elif command == "info":
		filepath = sys.argv[2]

		torrent_file_info = read_info(filepath)

		print(f"Tracker URL: {torrent_file_info['tracker_url']}")
		print(f"Length: {torrent_file_info['file_length']}")
		print(f"Info Hash: {torrent_file_info['info_hash'].hexdigest()}")
		print(f"Piece Length: {torrent_file_info['piece_length']}")

		pieces_hash = torrent_file_info['pieces_hash']
		for piece_hash in pieces_hash:
			print(piece_hash.hex())
	elif command == 'peers':
		filepath = sys.argv[2]
		torrent_file_info = read_info(filepath)

		request_parrams = {
			'info_hash': torrent_file_info['info_hash'].digest(),
			'peer_id': "00112233445566778899",
			'port': 6881,
			'uploaded': 0,
			'downloaded': 0,
			'left': torrent_file_info['file_length'],
			'compact': 1,
		}
		res = requests.get(torrent_file_info['tracker_url'], params=request_parrams)
		decoded_res, _ = decode_bencode(res.content)
		peers = decoded_res['peers']

		for i in range(0, len(peers), 6):
			peer = peers[i : i + 6]
			ip = '.'.join([str(b) for b in peer[:4]])
			port = int.from_bytes(peer[4:])
			print(f"{ip}:{port}")
	else:
		raise NotImplementedError(f"Unknown command {command}")

if __name__ == "__main__":
	main()
