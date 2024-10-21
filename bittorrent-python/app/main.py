import json
import sys

from app.utils import bytes_to_str
from app.decoder import decode_bencode
from app.command import get_peers, read_info, handshake

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
		peers = get_peers()

		for peer in peers:
			print(peer)
	elif command == 'handshake':
		filepath = sys.argv[2]
		url = sys.argv[3]

		client = handshake(filepath, url)
		peer_id = client.recv(68)[48:].hex()
		print(f"Peer ID: {peer_id}")
	else:
		raise NotImplementedError(f"Unknown command {command}")

if __name__ == "__main__":
	main()
