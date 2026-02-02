from settings import settings
from services.ebay.client import EbayClient

async def get_ebay_client():
    async with EbayClient(
        client_id=settings.EBAY_CLIENT,
        client_secret=settings.EBAY_SECRET,
    ) as client:
        yield client
