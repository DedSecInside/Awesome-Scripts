from .gzippacked import GzipPacked
from .. import TLObject
from ..types import RpcError


class RpcResult(TLObject):
    CONSTRUCTOR_ID = 0xf35c6d01

    def __init__(self, req_msg_id, body, error):
        """
        Initialize a request.

        Args:
            self: (todo): write your description
            req_msg_id: (todo): write your description
            body: (str): write your description
            error: (str): write your description
        """
        self.req_msg_id = req_msg_id
        self.body = body
        self.error = error

    @classmethod
    def from_reader(cls, reader):
        """
        Deserialize a reader object.

        Args:
            cls: (todo): write your description
            reader: (todo): write your description
        """
        msg_id = reader.read_long()
        inner_code = reader.read_int(signed=False)
        if inner_code == RpcError.CONSTRUCTOR_ID:
            return RpcResult(msg_id, None, RpcError.from_reader(reader))
        if inner_code == GzipPacked.CONSTRUCTOR_ID:
            return RpcResult(msg_id, GzipPacked.from_reader(reader).data, None)

        reader.seek(-4)
        # This reader.read() will read more than necessary, but it's okay.
        # We could make use of MessageContainer's length here, but since
        # it's not necessary we don't need to care about it.
        return RpcResult(msg_id, reader.read(), None)

    def to_dict(self):
        """
        Return a dict representation of this message.

        Args:
            self: (todo): write your description
        """
        return {
            '_': 'RpcResult',
            'req_msg_id': self.req_msg_id,
            'body': self.body,
            'error': self.error
        }
