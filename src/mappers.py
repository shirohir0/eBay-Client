from typing import Any

def map_ebay_item_response(data: dict[str, Any], USD_RATE: int) -> dict[str, Any]:
    price_value = float(data["price"]["value"])

    location = data.get("itemLocation", {})
    seller = data.get("seller", {})

    estimated = data.get("estimatedAvailabilities", [{}])[0]

    return {
        "item_id": data.get("itemId"),
        "title": data.get("title"),
        "short_description": data.get("shortDescription"),
        "description": data.get("description"),
        "price_usd": price_value,
        "currency": data["price"]["currency"],
        "price_rub": round(price_value * USD_RATE, 4),
        "condition": data.get("condition"),
        "category_path": data.get("categoryPath"),
        "brand": data.get("brand"),
        "manufacturer_part_number": data.get("mpn"),
        "seller": {
            "username": seller.get("username"),
            "feedback_summary": (
                f"{seller.get('feedbackPercentage')}% "
                f"({seller.get('feedbackScore')} reviews)"
            ),
        },
        "location": {
            "city": location.get("city"),
            "state": location.get("stateOrProvince"),
            "country": location.get("country"),
        },
        "availability_status": estimated.get(
            "estimatedAvailabilityStatus"
        ),
        "available_quantity": estimated.get(
            "estimatedAvailableQuantity"
        ),
        "item_url": data.get("itemWebUrl"),
        "image_url": data.get("image", {}).get("imageUrl"),
        "shipping_options": [
            {
                "type": option.get("type"),
                "cost_usd": float(option["shippingCost"]["value"]),
                "cost_rub": float(option["shippingCost"]["value"]) * USD_RATE,
                "currency": option["shippingCost"]["currency"],
                "delivery_window": {
                    "min": option.get("minEstimatedDeliveryDate"),
                    "max": option.get("maxEstimatedDeliveryDate"),
                },
            }
            for option in data.get("shippingOptions", [])
        ],
        "returns_accepted": data.get("returnTerms", {}).get(
            "returnsAccepted"
        ),
        "payment_methods": [
            method.get("paymentMethodType")
            for method in data.get("paymentMethods", [])
        ],
    }
