import pytest

from telethon import TelegramClient, events, types, utils


def get_client():
    """
    Return client.

    Args:
    """
    return TelegramClient(None, 1, '1')


def get_user_456():
    """
    Get a list of a given username.

    Args:
    """
    return types.User(
        id=456,
        access_hash=789,
        first_name='User 123'
    )


@pytest.mark.asyncio
async def test_get_input_users_no_action_message_no_entities():
      """
      Get the input message input.

      Args:
      """
    event = events.ChatAction.build(types.UpdateChatParticipantDelete(
        chat_id=123,
        user_id=456,
        version=1
    ))
    event._set_client(get_client())

    assert await event.get_input_users() == []


@pytest.mark.asyncio
async def test_get_input_users_no_action_message():
      """
      Test for users input.

      Args:
      """
    user = get_user_456()
    event = events.ChatAction.build(types.UpdateChatParticipantDelete(
        chat_id=123,
        user_id=456,
        version=1
    ))
    event._set_client(get_client())
    event._entities[user.id] = user

    assert await event.get_input_users() == [utils.get_input_peer(user)]


@pytest.mark.asyncio
async def test_get_users_no_action_message_no_entities():
      """
      Builds the action.

      Args:
      """
    event = events.ChatAction.build(types.UpdateChatParticipantDelete(
        chat_id=123,
        user_id=456,
        version=1
    ))
    event._set_client(get_client())

    assert await event.get_users() == []


@pytest.mark.asyncio
async def test_get_users_no_action_message():
      """
      Test for a message.

      Args:
      """
    user = get_user_456()
    event = events.ChatAction.build(types.UpdateChatParticipantDelete(
        chat_id=123,
        user_id=456,
        version=1
    ))
    event._set_client(get_client())
    event._entities[user.id] = user

    assert await event.get_users() == [user]
