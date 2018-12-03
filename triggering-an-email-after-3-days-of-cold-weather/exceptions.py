

class AddressNotFound(Exception):
    """
    Raised when the city is unknown or the URL is unknown
    """


class NotAuthorized(Exception):
    """
    Raised when the API Token is invalid
    """


class TemperatureNotFound(Exception):
    """
    Raised when the temperature is not found
    """


class UnhandledStatusCode(Exception):
    """
    Raised when the status code in not handled
    """