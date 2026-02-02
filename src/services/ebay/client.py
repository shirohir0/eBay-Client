from typing import Any

import aiohttp

from services.ebay.auth import EbayAuthClient
from exceptions import (
    EbayApiError,
    EbayItemNotFoundError
)
from services.exchange_rate import CurrencyRateClient
from mappers import map_ebay_item_response
from settings import settings


class EbayClient:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        timeout: int = 10,
    ):
        self._auth = EbayAuthClient(client_id, client_secret)
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self._session: aiohttp.ClientSession | None = None
        self._token: str | None = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession(timeout=self._timeout)
        self._token = await self._auth.get_access_token(self._session)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._session:
            await self._session.close()

    async def _get(
        self, path: str, *, params: dict | None = None, item_id: str | int
    ) -> dict[str, Any]:
        assert self._session and self._token

        headers = {"Authorization": f"Bearer {self._token}"}

        async with self._session.get(
            f"{settings.EBAY_BASE_URL}buy/browse/v1/item/v1|{item_id}|0",
            headers=headers,
            params=params,
        ) as response:
            if response.status == 404:
                raise EbayItemNotFoundError("Item not found")

            if response.status != 200:
                raise EbayApiError(
                    f"eBay API error {response.status}: {await response.text()}"
                )

            return await response.json()

    async def fetch_item_info(self, item_id: int) -> dict:
        data = await self._get(..., item_id=item_id)

        async with CurrencyRateClient() as client:
            USD_RATE = await client.get_rate("USD")

        return map_ebay_item_response(data, USD_RATE)

