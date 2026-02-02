from fastapi import APIRouter, Depends
from services.ebay.client import EbayClient
from schemas import EbayItemResponse
from api.v1.dependencies import get_ebay_client
from utils import validate_item_id

router = APIRouter()

@router.get(
    "/items/",
    response_model=EbayItemResponse,
    summary="Get item info from eBay",
)
async def get_item(
    item_id: str,
    ebay_client: EbayClient = Depends(get_ebay_client),
):
    item_id = validate_item_id(item_id)
    data = await ebay_client.fetch_item_info(item_id)
    return data

