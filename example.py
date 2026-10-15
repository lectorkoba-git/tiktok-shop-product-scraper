"""
Example: Scrape TikTok Shop product details, SKUs and live stock via Apify Python Client.
Requires: pip install apify-client
"""
import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
client = ApifyClient(APIFY_TOKEN)

run_input = {
    "productUrls": [
        "1732201471924867654",
        "https://shop.tiktok.com/view/product/1730700737574179367"
    ],
    "countryCode": "US",
    "includeReviews": True,
    "maxReviewsPerProduct": 5
}

print("🚀 Launching TikTok Shop Product Scraper on Apify Cloud...")
run = client.actor("magic-scraper/tiktok-shop-product-scraper").call(run_input=run_input)

print(f"✅ Run finished with status: {run.get('status')}")
print("📊 Extracted Product Details:\n")

dataset_id = run["defaultDatasetId"]
for item in client.dataset(dataset_id).iterate_items():
    print(f"Product: {item.get('title')}")
    print(f"  Price: ${item.get('current_price')} (Discount: {item.get('discount_percent')}%)")
    print(f"  Total Live Stock: {item.get('total_stock')} units")
    print(f"  Sold Count: {item.get('sold_count')}")
    print(f"  SKU Variants ({item.get('skus_count')} variants):")
    for sku in item.get("skus", []):
        print(f"    - {sku.get('sku_name')}: Stock={sku.get('stock')} | ${sku.get('price')}")
    print(f"  Seller: {item.get('seller', {}).get('seller_name')} (Rating: {item.get('seller', {}).get('seller_rating')})\n")
