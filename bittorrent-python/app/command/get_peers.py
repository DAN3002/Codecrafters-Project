import requests

from app.command.read_info import read_info
from app.decoder import decode_bencode
from app.constants import PEER_ID

def get_peers(filepath):
	torrent_file_info = read_info(filepath)

	request_parrams = {
		'info_hash': torrent_file_info['info_hash'].digest(),
		'peer_id': PEER_ID,
		'port': 6881,
		'uploaded': 0,
		'downloaded': 0,
		'left': torrent_file_info['file_length'],
		'compact': 1,
	}
	res = requests.get(torrent_file_info['tracker_url'], params=request_parrams)
	decoded_res, _ = decode_bencode(res.content)
	peers = decoded_res['peers']

	peers_out = []
	for i in range(0, len(peers), 6):
		peer = peers[i : i + 6]
		ip = '.'.join([str(b) for b in peer[:4]])
		port = int.from_bytes(peer[4:])
		peers_out.append(f"{ip}:{port}")

	return peers_out
