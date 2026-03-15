# My-Filters

This repository serves as a **cloud backup** for my personal uBlock Origin filters & UserScript.

## 🚀 Purpose
* **Redundancy:** To ensure my custom filters are never lost if my local browser profile is cleared.
* **Syncing:** To easily sync my preferred blocking rules across different devices and browsers.
* **Version Control:** To track changes and improvements to my filtering logic over time.

## 📂 Contents
This repo contains various `filters` that include:
* Custom network filters.
* Cosmetic filtering (element hiding) for specific sites.
* Scriptlet injections for advanced ad-blocking.

---

> [!TIP]
> These filters are tailored to my specific browsing habits. If you choose to use them, some sites may break. Use with caution!

---

# 🚀 Quick Installation

## Method 1: One-Click Subscribe (Recommended)

Click the subscribe button to add the filter list instantly:

| Filter List | Subscribe |
|------------|-----------|
| **🛡 BlazeFTL My-Filters** | [![Subscribe](https://img.shields.io/static/v1?label=Subscribe&message=BlazeFTL%20My-Filters&color=blue&style=for-the-badge)](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/BlazeFTL/My-Filters/refs/heads/main/my-ublock-static-filters_2026-03-16_00.57.42.txt&title=BlazeFTL%20My-Filters) |

---

## Method 2: Manual Import

1. Open **uBlock Origin Dashboard**
2. Go to **Filter lists**
3. Scroll to **Custom**
4. Check **Import…**
5. Paste the URL below:

```
https://raw.githubusercontent.com/BlazeFTL/My-Filters/refs/heads/main/my-ublock-static-filters_2026-03-16_00.57.42.txt
```

6. Click **Apply changes**
***
> ⚠️ **Important:** Trust configuration is required for both Method 1 and Method 2.

These filters may use advanced scriptlets which require trusted source configuration.

### Steps

1. Open **uBlock Origin Dashboard → Settings**
2. Enable **I am an advanced user**
3. Click the **⚙️ gear icon**
4. Find:

```
trustedListPrefixes
```

5. Add this value (space separated):

```
https://raw.githubusercontent.com/BlazeFTL/My-Filters/
```

### Example

```
Before:
ublock-

After:
ublock- https://raw.githubusercontent.com/BlazeFTL/My-Filters/
```

6. Click **Apply changes**
7. Restart browser

---

✅ After installation the filters will automatically update from GitHub. But then again you should manually update once

### Links
* **Main Contribution Fork:** [UBO-Blazed](https://github.com/BlazeFTL/UBO-Blazed)
* **Official uAssets:** [uBlockOrigin/uAssets](https://github.com/uBlockOrigin/uAssets)
