import inspect

import pytest

from telethon import TelegramClient


@pytest.mark.asyncio
async def test_send_message_with_file_forwards_args():
      """
      Send a message to a test test.

      Args:
      """
    arguments = {}
    sentinel = object()

    for value, name in enumerate(inspect.signature(TelegramClient.send_message).parameters):
        if name in {'self', 'entity', 'file'}:
            continue  # positional

        if name in {'message'}:
            continue  # renamed

        if name in {'link_preview'}:
            continue  # make no sense in send_file

        arguments[name] = value

    class MockedClient(TelegramClient):
        # noinspection PyMissingConstructor
        def __init__(self):
            """
            Initialize the object

            Args:
                self: (todo): write your description
            """
            pass

        async def send_file(self, entity, file, **kwargs):
              """
              Sends a file to the specified entity.

              Args:
                  self: (str): write your description
                  entity: (str): write your description
                  file: (str): write your description
              """
            assert entity == 'a'
            assert file == 'b'
            for k, v in arguments.items():
                assert k in kwargs
                assert kwargs[k] == v

            return sentinel

    client = MockedClient()
    assert (await client.send_message('a', file='b', **arguments)) == sentinel
