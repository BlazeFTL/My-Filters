#!/usr/bin/env python3
import asyncio
import re
import sys
import os
import aiohttp

# Exact mirrors of gorhill's config.js
DNS_QUERIES = [
    "https://cloudflare-dns.com/dns-query?name={hn}&type=A",
    "https://dns.google/resolve?name={hn}&type=A",
]
THROTTLE = 0.25  # 250ms

# Exact mirrors of gorhill's parkedDomainAuthorities
PARKED_RE = [
    re.compile(r'^traff-\d+\.hugedomains\.com\.?$'),
    re.compile(r'^\d+\.parkingcrew\.net\.?$'),
    re.compile(r'^ns\d\.centralnic\.net\.?(\s|$)'),
    re.compile(r'^ns\d\.pananames\.com\.?(\s|$)'),
]

dns_cache = {}


async def validate_hostname(session, hn):
    """
    Mirrors gorhill's validateHostname():
    Try each DNS server; return the first result where Status != 2.
    Returns None if all servers fail or return Status 2.
    """
    await asyncio.sleep(THROTTLE)
    for url_tpl in DNS_QUERIES:
        url = url_tpl.format(hn=hn)
        try:
            async with session.get(
                url,
                headers={"accept": "application/dns-json"},
                timeout=aiohttp.ClientTimeout(total=10),
            ) as resp:
                data = await resp.json(content_type=None)
                if data.get("Status") != 2:
                    return data
        except Exception:
            pass
    return None


def check_hostname(result):
    """
    Mirrors gorhill's checkHostname().
    Returns a diagnostic string if bad, None if ok/alive.
    """
    if not isinstance(result, dict):
        return None                           # inconclusive → keep
    status = result.get("Status")
    if status == 1: return "format error"
    if status == 2: return "dns server failure"
    if status == 3: return "name error"       # NXDOMAIN — dead
    if status == 4: return "not implemented"
    if status == 5: return "refused"
    answers = result.get("Answer") or []
    for entry in answers:
        data = entry.get("data", "")
        for pat in PARKED_RE:
            if pat.search(data):
                return "parked"
    return None                               # Status 0, no parking → alive


async def is_dead(session, hn):
    if hn in dns_cache:
        return dns_cache[hn]
    result = await validate_hostname(session, hn)
    dead = check_hostname(result) is not None
    dns_cache[hn] = dead
    return dead


# Matches comma-separated domain list before ## (cosmetic/scriptlet rules)
# Gorhill's processExt() handles this via parser.extOptions() -> hn field
RULE_RE = re.compile(
    r'^((?:~?[a-zA-Z0-9\-\*]+(?:\.[a-zA-Z0-9\-\*]+)*)(?:,(?:~?[a-zA-Z0-9\-\*]+(?:\.[a-zA-Z0-9\-\*]+)*))*)(##.+)$'
)


def should_skip(hn):
    """Mirrors gorhill's per-hostname skip conditions."""
    if hn.endswith('.onion'):
        return True
    if re.match(r'^\d+\.\d+\.\d+\.\d+$', hn):
        return True
    if '*' in hn:
        return True
    return False


async def process(input_path):
    with open(input_path, encoding="utf-8") as f:
        lines = f.readlines()

    out = []
    backup_commented = set()
    connector = aiohttp.TCPConnector(limit=5)
    async with aiohttp.ClientSession(connector=connector) as session:
        for line in lines:
            raw = line.rstrip("\n")

            if not raw or raw.startswith("!") or raw.startswith("["):
                out.append(line)
                continue

            m = RULE_RE.match(raw)
            if not m:
                out.append(line)
                continue

            domains_str, rule = m.group(1), m.group(2)
            domains = [d for d in domains_str.split(",") if d]

            checked = []
            for d in domains:
                bare = d.lstrip("~")
                if should_skip(bare):
                    checked.append((d, False))  # skip → treat as alive (keep)
                    continue
                dead = await is_dead(session, bare)
                checked.append((d, dead))

            alive_domains = [d for d, dead in checked if not dead]

            if alive_domains:
                if len(alive_domains) == len(domains):
                    out.append(line)                              # nothing changed
                else:
                    out.append(",".join(alive_domains) + rule + "\n")
            else:
                # All dead — keep first as backup (gorhill style)
                if domains[0] not in backup_commented:
                    out.append("! All Dead Kept One Backup\n")
                    backup_commented.add(domains[0])
                out.append(domains[0] + rule + "\n")

    return out


def main():
    if len(sys.argv) < 2:
        print("Usage: check_dead_domains.py <filter_file>")
        sys.exit(1)

    inp = sys.argv[1]
    base, ext = os.path.splitext(inp)
    out_path = f"{base}_Dead Domain Cleaned{ext}"

    result = asyncio.run(process(inp))

    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(result)

    print(f"Done → {out_path}")


if __name__ == "__main__":
    main()
