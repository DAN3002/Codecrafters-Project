import socket
from app.command.read_info import read_info
from app.constants import PEER_ID

def handshake(filepath, url):
		(ip, port) = url.split(":")

		# Creating a socket object for the server
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((ip, int(port)))

		# Create handshake message
		torrent_file_info = read_info(filepath)
		info_hash = torrent_file_info['info_hash']
		handshake_msg = (
			b"\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00"
			+ info_hash.digest()
			+ PEER_ID.encode()
		)

		# Send handshake
		client.send(handshake_msg)

		return client
