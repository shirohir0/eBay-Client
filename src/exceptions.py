class EbayError(Exception):
    pass


class EbayApiError(EbayError):
    pass


class EbayItemNotFoundError(EbayError):
    pass


class EbayCountryError(EbayError):
    pass


class EbayItemIdError(EbayError):
    pass
