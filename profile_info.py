import requests as req
import Cookies as ck


def get_profile_info(username:str) -> str:
    profile_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    res = req.get(url=profile_url , headers=ck.MOBILE_HEADERS_STORY)
    jsonStr = res.json()
    pk = jsonStr['data']['user']['id']
    bio = jsonStr['data']['user']['biography']
    fullname = jsonStr['data']['user']['full_name']
    username = jsonStr['data']['user']['username']
    followers = jsonStr['data']['user']['edge_followed_by']['count']
    followings = jsonStr['data']['user']['edge_follow']['count']
    posts_count = jsonStr['data']['user']['edge_owner_to_timeline_media']['count']
    info = f"""✅ Profile photo
<b>
Fullname: {fullname}
Username: {username}
Followers: {followers}
Followings: {followings}
Posts count: {posts_count}
PK: <code>{pk}</code>
</b>
Biography:
{bio}"""

    return info + "\n" + str(posts_count)