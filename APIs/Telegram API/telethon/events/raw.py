from .common import EventBuilder
from .. import utils


class Raw(EventBuilder):
    """
    Raw events are not actual events. Instead, they are the raw
    :tl:`Update` object that Telegram sends. You normally shouldn't
    need these.

    Args:
        types (`list` | `tuple` | `type`, optional):
            The type or types that the :tl:`Update` instance must be.
            Equivalent to ``if not isinstance(update, types): return``.

    Example
        .. code-block:: python

            from telethon import events

            @client.on(events.Raw)
            async def handler(update):
                # Print all incoming updates
                print(update.stringify())
    """
    def __init__(self, types=None, *, func=None):
        """
        Initialize the types.

        Args:
            self: (todo): write your description
            types: (todo): write your description
            func: (callable): write your description
        """
        super().__init__(func=func)
        if not types:
            self.types = None
        elif not utils.is_list_like(types):
            if not isinstance(types, type):
                raise TypeError('Invalid input type given: {}'.format(types))

            self.types = types
        else:
            if not all(isinstance(x, type) for x in types):
                raise TypeError('Invalid input types given: {}'.format(types))

            self.types = tuple(types)

    async def resolve(self, client):
          """
          Resolve a client.

          Args:
              self: (todo): write your description
              client: (todo): write your description
          """
        self.resolved = True

    @classmethod
    def build(cls, update, others=None, self_id=None):
        """
        Builds a new : class based on the server.

        Args:
            cls: (todo): write your description
            update: (todo): write your description
            others: (todo): write your description
            self_id: (str): write your description
        """
        return update

    def filter(self, event):
        """
        Returns a filter function.

        Args:
            self: (todo): write your description
            event: (todo): write your description
        """
        if not self.types or isinstance(event, self.types):
            if self.func:
                # Return the result of func directly as it may need to be awaited
                return self.func(event)
            return event
