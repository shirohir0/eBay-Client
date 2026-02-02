import re
from exceptions import EbayItemIdError


def validate_item_id(raw: str) -> int:
    try:
        return int(raw)
    except ValueError:
        match = re.search(r"/itm/(\d+)", raw)
        if match:
            return int(match.group(1))

    raise EbayItemIdError("Invalid item_id or URL")
