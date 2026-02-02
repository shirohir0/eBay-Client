import aiohttp
from settings import settings

BASE_OAUTH = f"{settings.EBAY_BASE_URL}/identity/v1/oauth2/token"


class EbayAuthClient:
    def __init__(self, client_id: str, client_secret: str):
        self._client_id = client_id
        self._client_secret = client_secret

    async def get_access_token(self, session: aiohttp.ClientSession) -> str:
        data = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope",
        }

        async with session.post(
            BASE_OAUTH,
            data=data,
            auth=aiohttp.BasicAuth(self._client_id, self._client_secret),
        ) as response:
            if response.status != 200:
                raise Exception(
                    f"OAuth error {response.status}: {await response.text()}"
                )

            payload = await response.json()
            return payload["access_token"]
