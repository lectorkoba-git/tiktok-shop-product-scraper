# 📦 TikTok Shop Product Scraper: SKU Matrix, Live Stock & Reviews

[![TikTok Shop Product Scraper](https://apify.com/actor-badge?actor=magic-scraper/tiktok-shop-product-scraper)](https://apify.com/magic-scraper/tiktok-shop-product-scraper)
![Free Tier](https://img.shields.io/badge/Apify%20Free%20Tier-$5%20Monthly%20Credit-blue?style=flat-square)
![Pay-Per-Result](https://img.shields.io/badge/Pricing-$2.00%20%2F%201K%20results-blue?style=flat-square)
![No Cookies Required](https://img.shields.io/badge/Cookies-Not%20Required-success?style=flat-square)
![Export](https://img.shields.io/badge/Export-JSON%20|%20CSV%20|%20Excel-orange?style=flat-square)

Python and Node.js examples for the **[TikTok Shop Product Scraper](https://apify.com/magic-scraper/tiktok-shop-product-scraper)** on Apify: full TikTok Shop product pages by URL or ID — every SKU variant with price and numeric stock, specifications, category, images, seller metrics and customer reviews.

> ⚡ **No code needed:** 👉 **[Run it in your browser on Apify (free $5 monthly credit)](https://apify.com/magic-scraper/tiktok-shop-product-scraper)**

---

## 🎯 Who is this for?

- **Inventory & competitor trackers** — follow stock per SKU and sell-through over time.
- **Dropshippers & sellers** — check variants, prices and reviews before listing a product.
- **Brand managers** — monitor resellers and review sentiment on TikTok Shop.

---

## 📌 Key Facts

| | |
| :--- | :--- |
| **Pricing** | $2.00 per 1,000 products + $0.00005 start fee; reviews come inside the product record at no extra charge |
| **Run time (measured)** | ~3–20 s for one product with 5 reviews |
| **Inventory** | Numeric `stock` per SKU and `total_stock` |
| **How it works** | HTTP requests with browser TLS impersonation, server-rendered page data, no headless browser |
| **Proxy** | Apify Proxy pinned to the market country automatically; a flagged IP is swapped for a fresh one |
| **Unknown values** | `null` — nothing is guessed |
| **Login / cookies** | Not required |

---

## 🚀 Quickstart

### Python

```bash
pip install apify-client
export APIFY_TOKEN=your_token   # https://console.apify.com/settings/integrations
python example.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("magic-scraper/tiktok-shop-product-scraper").call(run_input={
    "productUrls": ["1732201471924867654"],
    "includeReviews": True,
    "maxReviewsPerProduct": 5,
})

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["title"][:60], "| stock:", item["total_stock"], "| SKUs:", item["skus_count"])
```

### Node.js

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('magic-scraper/tiktok-shop-product-scraper').call({
    productUrls: ['https://shop.tiktok.com/view/product/1732201471924867654'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

---

## 📥 Input

| Parameter | Type | Default | Description |
| :--- | :--- | :---: | :--- |
| `productUrls` | `array[string]` | required | Product URLs (`/view/product/...`, `/pdp/...`) or numeric IDs. |
| `countryCode` | `string` | `US` | `US` or `GB`. |
| `includeReviews` | `boolean` | `true` | Include customer reviews. |
| `maxReviewsPerProduct` | `integer` | `10` | Reviews per product (0–50). |
| `proxyConfiguration` | `object` | `{"useApifyProxy": true}` | Apify Proxy, country set from `countryCode`. |

---

## 📤 Output

One record per product: `product_id`, `title`, `description`, `category_name`, `category_path`, `brand_name`, `current_price`, `original_price`, `currency`, `discount_percent`, `sold_count`, `estimated_revenue`, `rating`, `reviews_count`, `total_stock`, `in_stock`, `skus_count`, `skus[]` (`sku_id`, `sku_name`, `price`, `original_price`, `stock`, `in_stock`, `sku_image_url`), `specifications`, `seller` (`seller_id`, `seller_name`, `seller_rating`, `shop_url`, `total_sales`, `total_products`, `review_count`), `shipping_info`, `main_image_url`, `images[]`, `reviews[]` (`review_id`, `rating`, `review_text`, `sku_name`, `is_verified_purchase`, `is_incentivized_review`, `reviewer_name`, `created_at`), `product_url`, `scraped_at`.

### Sample record (real run, shortened)

```json
{
  "product_id": "1732201471924867654",
  "title": "FDA-Cleared LED Face Mask with Red Light Therapy –  Infrared & Amber Light, LightBoost Eye Cream + Face & Neck Serum Set",
  "category_name": "Microcurrent Devices",
  "category_path": "Beauty & Personal Care > Personal Care Appliances > Facial Beauty Devices > Skin Care Devices > Microcurrent Devices",
  "brand_name": null,
  "current_price": 499,
  "original_price": null,
  "currency": "USD",
  "discount_percent": null,
  "sold_count": 2519,
  "estimated_revenue": 1256981,
  "rating": null,
  "reviews_count": 553,
  "total_stock": 7443,
  "in_stock": true,
  "skus_count": 1,
  "skus": [
    {"sku_id": "1732201467243565638", "sku_name": "Default", "price": 499, "original_price": null, "stock": 7443, "in_stock": true, "sku_image_url": null}
  ],
  "specifications": {"Material": "Silicone", "Manufacturer": "Solawave", "Battery capacity (mAh)": "3600"},
  "seller": {
    "seller_id": "7495135195055819334",
    "seller_name": "Solawave",
    "seller_rating": 4.8,
    "shop_url": "https://shop.tiktok.com/us/store/shop/7495135195055819334",
    "total_sales": 5636,
    "total_products": 5,
    "review_count": 388
  },
  "shipping_info": null,
  "reviews": [
    {
      "review_id": "7699762904353474317",
      "rating": 5,
      "review_text": "It’s extremely easy to use. It fits the contours of my face properly and doesn’t slide around. ...",
      "sku_name": null,
      "is_verified_purchase": true,
      "is_incentivized_review": true,
      "reviewer_name": "J**r C**s",
      "created_at": "2026-10-23T07:34:28.837000"
    }
  ],
  "product_url": "https://shop.tiktok.com/us/pdp/wrinkle-retreat-pro-led-face-mask-anti-aging-treatment/1732201471924867654",
  "scraped_at": "2026-10-29T11:03:54.963782+00:00"
}
```

---

## 🤖 For AI Agents

Call `magic-scraper/tiktok-shop-product-scraper` via the [Apify MCP server](https://mcp.apify.com/) or the API with `{"productUrls": ["<id or URL>"]}`. Set `includeReviews: false` when only price and stock are needed; unavailable products are skipped without failing the batch.

---

## 🔗 Related Scrapers

- [TikTok Shop Search Scraper](https://apify.com/magic-scraper/tiktok-shop-search-scraper) — find products by keyword first.
- [TikTok Video & Hashtag Scraper](https://apify.com/magic-scraper/tiktok-video-hashtag-scraper) — videos promoting shop products.
- [Temu Trending Products & Lightning Deals Tracker](https://apify.com/magic-scraper/temu-trending-products-scraper)

---

## 📄 License

MIT — see [LICENSE](LICENSE). This repository contains usage examples; the scraper itself runs on [Apify](https://apify.com/magic-scraper/tiktok-shop-product-scraper).
