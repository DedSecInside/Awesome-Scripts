import pickle

from telethon.errors import RPCError, BadRequestError, FileIdInvalidError, NetworkMigrateError


def _assert_equality(error, unpickled_error):
    """
    Asserts that the given error is raised.

    Args:
        error: (todo): write your description
        unpickled_error: (todo): write your description
    """
    assert error.code == unpickled_error.code
    assert error.message == unpickled_error.message
    assert type(error) == type(unpickled_error)
    assert str(error) == str(unpickled_error)


def test_base_rpcerror_pickle():
    """
    Test if pickle for pickle.

    Args:
    """
    error = RPCError("request", "message", 123)
    unpickled_error = pickle.loads(pickle.dumps(error))
    _assert_equality(error, unpickled_error)


def test_rpcerror_pickle():
    """
    Test for pickle and pickled.

    Args:
    """
    error = BadRequestError("request", "BAD_REQUEST", 400)
    unpickled_error = pickle.loads(pickle.dumps(error))
    _assert_equality(error, unpickled_error)


def test_fancy_rpcerror_pickle():
    """
    Test if pickle is a pickle file.

    Args:
    """
    error = FileIdInvalidError("request")
    unpickled_error = pickle.loads(pickle.dumps(error))
    _assert_equality(error, unpickled_error)


def test_fancy_rpcerror_capture_pickle():
    """
    Test if rpigrate network.

    Args:
    """
    error = NetworkMigrateError(request="request", capture=5)
    unpickled_error = pickle.loads(pickle.dumps(error))
    _assert_equality(error, unpickled_error)
    assert error.new_dc == unpickled_error.new_dc
