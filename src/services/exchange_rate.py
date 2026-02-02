import aiohttp
from typing import Final


CBR_DAILY_URL: Final = "https://www.cbr-xml-daily.ru/daily_json.js"


class CurrencyRateError(Exception):
    pass


class CurrencyRateClient:
    def __init__(self, timeout: int = 5):
        self._timeout = aiohttp.ClientTimeout(total=timeout)
        self._session: aiohttp.ClientSession | None = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession(timeout=self._timeout)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if self._session:
            await self._session.close()

    async def get_rate(self, currency_code: str) -> float:
        if not self._session:
            raise RuntimeError("ClientSession not initialized")

        async with self._session.get(CBR_DAILY_URL) as response:
            if response.status != 200:
                raise CurrencyRateError(
                    f"CBR API error {response.status}"
                )

            data = await response.json(content_type=None)

        try:
            valute = data["Valute"][currency_code.upper()]
        except KeyError:
            raise CurrencyRateError(
                f"Currency {currency_code} not found"
            )

        value = float(valute["Value"])
        nominal = int(valute["Nominal"])

        return value / nominal
