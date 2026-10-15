# 📦 TikTok Shop Product Scraper: SKU Matrix, Live Stock & Reviews

[![TikTok Shop Product Scraper](https://apify.com/actor-badge?actor=magic-scraper/tiktok-shop-product-scraper)](https://apify.com/magic-scraper/tiktok-shop-product-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$2.00%20%2F%201K%20results-blue?style=flat-square)
![No Cookies Required](https://img.shields.io/badge/Cookies-Not%20Required-success?style=flat-square)
![Speed](https://img.shields.io/badge/Speed-~1.5s%20per%20product-brightgreen?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Extract granular product data from **TikTok Shop** by URL or ID: complete SKU variant matrix, exact live inventory stock quantities, prices, specifications, high-res images, seller store metrics, and verified customer reviews.

> ⚡ **Try it directly in your browser without code:**  
> 👉 **[Run TikTok Shop Product Scraper on Apify (Free $5 Monthly Credits)](https://apify.com/magic-scraper/tiktok-shop-product-scraper)**

---

## 🎯 Who is this for?

- **E-Commerce Inventory Trackers:** Monitor competitor stock depletion rates to estimate real daily sales velocity.
- **Dropshippers & DTC Brands:** Reverse-engineer top-performing variants (colors/sizes) and product specifications.
- **Price Monitoring Engines:** Track instant price fluctuations and promotion discounts across TikTok Shop PDP pages.
- **Review & Sentiment Analysts:** Extract verified buyer reviews for market research and product improvements.

---

## ⚡ Why Choose This Scraper Over Competitors?

| Feature | **Our Product Scraper** | Competing Scrapers |
| :--- | :---: | :---: |
| **Speed (per product)** | ⚡ **~1.5 seconds** | 🐢 10–25 seconds |
| **Inventory Stock Level** | ✅ **Exact numerical stock per SKU** | ❌ Missing or binary in-stock |
| **Pricing** | 💰 **$2.00 / 1,000 products** ($0.002/item) | 💸 $10.00 – $20.00 / 1,000 |
| **Minimal Start Fee** | 🏷️ **$0.001** | 💸 $0.05 – $0.10 |
| **Customer Reviews** | ✅ Included with verified purchase badges | 💸 Extra surcharge per review |
| **Seller Catalog Metrics** | ✅ Store rating, total sales, product count | ❌ Basic seller name only |
| **Anti-Bot & Headless Free** | ✅ Direct SSR parsing without browser | ❌ Heavy browser crashes |

---

## 📖 How to Scrape TikTok Shop Products (Step-by-Step)

1. **Paste Product URLs or IDs:** Provide TikTok Shop URLs (e.g. `https://shop.tiktok.com/view/product/1732201471924867654`) or bare numeric IDs (`1732201471924867654`).
2. **Configure Options:** Choose whether to include customer reviews and set `maxReviewsPerProduct` (default: 10, prefilled with 5 for quick testing).
3. **Run & Export:** Click **Start**. Export results to **CSV, Excel, JSON, Google Sheets**, or integrate directly into your database via API.

---

## 📥 Input Parameters

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| `productUrls` | `array[string]` | **Yes** | `["1732201471924867654"]` | List of TikTok Shop product URLs or numeric product IDs. |
| `countryCode` | `string` | No | `"US"` | Market region: `"US"` (United States) or `"GB"` (United Kingdom). |
| `includeReviews` | `boolean` | No | `true` | Whether to extract top customer reviews. |
| `maxReviewsPerProduct` | `integer` | No | `10` | Maximum reviews to return per product (0–50). |
| `proxyConfiguration` | `object` | No | Datacenter | Proxy settings. Apify Datacenter or Residential proxy. |

---

## 📤 Sample Output (JSON)

```json
{
  "product_id": "1732201471924867654",
  "title": "FDA-Cleared LED Face Mask with Red Light Therapy",
  "current_price": 499.00,
  "original_price": 599.00,
  "currency": "USD",
  "discount_percent": 17,
  "sold_count": 1995,
  "total_stock": 2442,
  "in_stock": true,
  "skus_count": 1,
  "skus": [
    {
      "sku_id": "1732201467243565638",
      "sku_name": "Default",
      "price": 499.00,
      "original_price": 599.00,
      "stock": 2442,
      "in_stock": true
    }
  ],
  "specifications": {
    "Material": "Medical-Grade Silicone",
    "Light Modes": "Red, Near-Infrared, Amber"
  },
  "seller": {
    "seller_id": "7495135195055819334",
    "seller_name": "Solawave",
    "seller_rating": 4.8,
    "shop_url": "https://shop.tiktok.com/us/store/solawave/7495135195055819334",
    "total_sales": 4990,
    "total_products": 24
  },
  "reviews": [
    {
      "review_id": "7495820381023",
      "rating": 5,
      "text": "Remarkable improvement in skin firmness after 3 weeks of daily use.",
      "user_name": "Sarah M.",
      "is_verified_purchase": true
    }
  ]
}
```

---

## 💻 Developer Quickstart (Python & Node.js)

### Python (`apify-client`)

```bash
pip install apify-client
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN"))

run_input = {
    "productUrls": ["1732201471924867654"],
    "countryCode": "US",
    "includeReviews": True,
    "maxReviewsPerProduct": 10
}

run = client.actor("magic-scraper/tiktok-shop-product-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f"Product: {item['title']} | Total Stock: {item['total_stock']} | Price: ${item['current_price']}")
    for sku in item.get('skus', []):
        print(f"  SKU: {sku.get('sku_name')} | Stock: {sku.get('stock')} | Price: ${sku.get('price')}")
```

---

## 💳 Pricing & Free Tier ($5 Monthly Credit)

This Actor uses Apify's **Pay-Per-Result** model:
- **$2.00 per 1,000 product detail rows** ($0.002 per product).
- **$0.001 minimal start fee**.
- Every Apify user receives **$5.00 in free usage credits every month** — test with **2,500 products free each month**!

👉 **[Start Scraping Free on Apify](https://apify.com/magic-scraper/tiktok-shop-product-scraper)**
