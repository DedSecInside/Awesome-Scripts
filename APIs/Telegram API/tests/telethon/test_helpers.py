"""
tests for telethon.helpers
"""

from base64 import b64decode

import pytest

from telethon import helpers


def test_strip_text():
    """
    Remove test text.

    Args:
    """
    assert helpers.strip_text(" text ", []) == "text"
    # I can't interpret the rest of the code well enough yet


class TestSyncifyAsyncContext:
    class NoopContextManager:
        def __init__(self, loop):
            """
            Initialize the loop.

            Args:
                self: (todo): write your description
                loop: (str): write your description
            """
            self.count = 0
            self.loop = loop

        async def __aenter__(self):
              """
              Return the number.

              Args:
                  self: (todo): write your description
              """
            self.count += 1
            return self

        async def __aexit__(self, exc_type, *args):
              """
              Called when an exception is raised.

              Args:
                  self: (todo): write your description
                  exc_type: (todo): write your description
              """
            assert exc_type is None
            self.count -= 1

        __enter__ = helpers._sync_enter
        __exit__ = helpers._sync_exit

    def test_sync_acontext(self, event_loop):
        """
        Test if the event_loop has been received.

        Args:
            self: (todo): write your description
            event_loop: (todo): write your description
        """
        contm = self.NoopContextManager(event_loop)
        assert contm.count == 0

        with contm:
            assert contm.count == 1

        assert contm.count == 0

    @pytest.mark.asyncio
    async def test_async_acontext(self, event_loop):
          """
          Make an event_async.

          Args:
              self: (todo): write your description
              event_loop: (todo): write your description
          """
        contm = self.NoopContextManager(event_loop)
        assert contm.count == 0

        async with contm:
            assert contm.count == 1

        assert contm.count == 0


def test_generate_key_data_from_nonce():
    """
    Generate a nonce key.

    Args:
    """
    gkdfn = helpers.generate_key_data_from_nonce

    key_expect = b64decode(b'NFwRFB8Knw/kAmvPWjtrQauWysHClVfQh0UOAaABqZA=')
    nonce_expect = b64decode(b'1AgjhU9eDvJRjFik73bjR2zZEATzL/jLu9yodYfWEgA=')
    assert gkdfn(123456789, 1234567) == (key_expect, nonce_expect)
