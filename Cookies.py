# please remember to remove any " or ' in your cookie

CSRF_TOKEN: str = "<LOGGED IN ACCOUNT COOKIE HERE>"

DESKTOP_HEADERS: dict = {
    "Host": "www.instagram.com",
    "Cookie": CSRF_TOKEN,
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;    q=0.9",
    "Sec-GPC": "1",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
}
MOBILE_HEADERS_STORY: dict = {
    "Accept": "*/*",
    "Cookie": CSRF_TOKEN,
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 Instagram 72.0.0.21.98",
    "Connection": "keep-alive",
    "Host": "i.instagram.com",
}
