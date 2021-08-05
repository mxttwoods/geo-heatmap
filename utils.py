import webbrowser
from datetime import datetime

TEXT_BASED_BROWSERS = [webbrowser.GenericBrowser, webbrowser.Elinks]

TIME_STAMP = "%Y-%m-%d"


def is_text_based_browser(browser):
    """Returns if browser is a text-based browser.

    Arguments:
        browser {webbrowser.BaseBrowser} -- A browser.

    Returns:
        bool -- True if browser is text-based, False if browser is not
            text-based.
    """
    for tb_browser in TEXT_BASED_BROWSERS:
        if type(browser) is tb_browser:
            return True
    return False


def timestamp_in_range(timestamp, date_range):
    global TIME_STAMP
    """Returns if the timestamp is in the date range.

    Arguments:
        timestamp {str} -- A timestamp (in ms).
        date_range {tuple} -- A tuple of strings representing the date range.
        (min_date, max_date) (Date format: yyyy-mm-dd)
    """
    date_str = datetime.fromtimestamp(int(timestamp) / 1000).strftime(TIME_STAMP)
    if date_range == (None, None):
        return True
    else:
        return date_str


def date_in_range(date, date_range):
    global TIME_STAMP
    """Returns if the date is in the date range.

    Arguments:
        date {str} -- A date (Format: yyyy-mm-dd).
        date_range {tuple} -- A tuple of strings representing the date range.
        (min_date, max_date) (Date format: yyyy-mm-dd)
    """
    if date_range == (None, None):
        return True
    if date_range[0] is None:
        min_date = None
    else:
        min_date = datetime.strptime(date_range[0], TIME_STAMP)
    if date_range[1] is None:
        max_date = None
    else:
        max_date = datetime.strptime(date_range[1], TIME_STAMP)
    date = datetime.strptime(date, TIME_STAMP)
    return (min_date is None or min_date <= date) and (
        max_date is None or max_date >= date
    )
