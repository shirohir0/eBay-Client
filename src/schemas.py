from pydantic import BaseModel, Field
from typing import List, Optional


class SellerInfo(BaseModel):
    username: Optional[str]
    feedback_summary: Optional[str]


class LocationInfo(BaseModel):
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]


class DeliveryWindow(BaseModel):
    min: Optional[str] = Field(None, description="Min delivery date")
    max: Optional[str] = Field(None, description="Max delivery date")


class ShippingOption(BaseModel):
    type: Optional[str]
    cost_usd: float
    cost_rub: float
    currency: str
    delivery_window: DeliveryWindow


class EbayItemResponse(BaseModel):
    item_id: Optional[str]
    title: Optional[str]
    short_description: Optional[str]
    description: Optional[str]

    price_usd: float
    currency: str
    price_rub: float

    condition: Optional[str]
    category_path: Optional[str]
    brand: Optional[str]
    manufacturer_part_number: Optional[str]

    seller: SellerInfo
    location: LocationInfo

    availability_status: Optional[str]
    available_quantity: Optional[int]

    item_url: Optional[str]
    image_url: Optional[str]

    shipping_options: List[ShippingOption]
    returns_accepted: Optional[bool]
    payment_methods: List[str]
