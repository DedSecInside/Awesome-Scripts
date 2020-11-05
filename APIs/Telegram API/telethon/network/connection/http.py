import asyncio

from .connection import Connection, PacketCodec


SSL_PORT = 443


class HttpPacketCodec(PacketCodec):
    tag = None
    obfuscate_tag = None

    def encode_packet(self, data):
        """
        Encode packet to binary.

        Args:
            self: (todo): write your description
            data: (todo): write your description
        """
        return ('POST /api HTTP/1.1\r\n'
                'Host: {}:{}\r\n'
                'Content-Type: application/x-www-form-urlencoded\r\n'
                'Connection: keep-alive\r\n'
                'Keep-Alive: timeout=100000, max=10000000\r\n'
                'Content-Length: {}\r\n\r\n'
                .format(self._conn._ip, self._conn._port, len(data))
                .encode('ascii') + data)

    async def read_packet(self, reader):
          """
          Read a packet from the socket.

          Args:
              self: (todo): write your description
              reader: (todo): write your description
          """
        while True:
            line = await reader.readline()
            if not line or line[-1] != b'\n':
                raise asyncio.IncompleteReadError(line, None)

            if line.lower().startswith(b'content-length: '):
                await reader.readexactly(2)
                length = int(line[16:-2])
                return await reader.readexactly(length)


class ConnectionHttp(Connection):
    packet_codec = HttpPacketCodec

    async def connect(self, timeout=None, ssl=None):
          """
          Establish connection.

          Args:
              self: (todo): write your description
              timeout: (int): write your description
              ssl: (str): write your description
          """
        await super().connect(timeout=timeout, ssl=self._port == SSL_PORT)
