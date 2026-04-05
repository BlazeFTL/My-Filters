<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&text=My-Filters" />
</div>




<div align="center">
  <p><i>"Backup for BlazeFTL's uBlockOrigin Filters & UserScript ."</i></p>
</div>


---

# 🛡️My-Filters

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

## 👉 Method 1: One-Click Subscribe (Recommended)

Click the subscribe button to add the filter list instantly:

| Filter List | Subscribe |
|------------|-----------|
| **🛡 BlazeFTL My-Filters** | [![Subscribe](https://img.shields.io/static/v1?label=Subscribe&message=BlazeFTL%20My-Filters&color=blue&style=for-the-badge)](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/BlazeFTL/My-Filters/refs/heads/master/My-Filters_Static_Sites.txt&title=My-Filters%20-%20Static%20Sites) |

---

## 👉 Method 2: Manual Import

1. Open **uBlock Origin Dashboard**
2. Go to **Filter lists**
3. Scroll to **Custom**
4. Check **Import…**
5. Paste the URL below:

```
https://raw.githubusercontent.com/BlazeFTL/My-Filters/refs/heads/main/My-Filters_Static_Sites.txt
```

6. Click **Apply changes**
***
## 🔚 Finally follow these steps for both method 1 and 2

> ⚠️ **Important:** Trust configuration is required for both Method 1 and Method 2. These filters may use advanced scriptlets which require trusted source configuration.

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

---

### 🚀 Live Previews

Explore the latest builds and interactive tools directly on GitHub Pages:

* **[Live Editor (Final Build)](https://blazeftl.github.io/My-Filters/LiveEditorNoWrapFinal.html)** – Optimized editor with a "No Wrap" configuration for enhanced readability.
* **[Line Number Debugger](https://blazeftl.github.io/My-Filters/BrokenWrapLineNumbersBeforeCodeMirror.html)** – Experimental build focusing on line number alignment and text wrapping logic.
* **[CodeMirror 6 Migration](https://blazeftl.github.io/My-Filters/CodeMirror6FirstBuild.html)** – The initial implementation and first stable build using the CodeMirror 6 engine.
* **[CodeMirror 6 Migration Final](https://blazeftl.github.io/My-Filters/CodeMirror6V2Final.html)** – The final implementation and first stable build using the CodeMirror 6 engine.
* **[Shortener Thread Manager](https://blazeftl.github.io/My-Filters/ShortnerThreadAllComments.html)** – A specialized tool designed to aggregate and display all comments within shortener threads.

---
