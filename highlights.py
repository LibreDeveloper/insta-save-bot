import requests as req
import Cookies as ck


def get_highlight_id(username):
    reel_id_list = []
    all_highlight_list = []
    profile_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    res = req.get(url=profile_url , headers=ck.MOBILE_HEADERS_STORY)
    jsonStr = res.json()
    user_id = jsonStr['data']['user']['id']
    highlight_id_url = f"https://i.instagram.com/api/v1/highlights/{user_id}/highlights_tray/"
    print("user id ->",user_id)
    res = req.get(url=highlight_id_url,headers=ck.MOBILE_HEADERS_STORY)
    highlight_json = res.json()
    for i in range(len(highlight_json['tray'])):
        print("reel id ->",highlight_json['tray'][i]['id'])
        reel_id_list.append(highlight_json['tray'][i]['id'])

    for i in range(len(reel_id_list)):
        highlight_url = f"https://i.instagram.com/api/v1/feed/reels_media/?reel_ids={reel_id_list[i]}"
        res = req.get(url=highlight_url,headers=ck.MOBILE_HEADERS_STORY)
        strJson = res.json()
        items = strJson['reels'][reel_id_list[i]]['items']
        for i in range(len(items)):
            if items[i]['media_type'] == 1:
                # its image
                all_highlight_list.append(items[i]['image_versions2']['candidates'][0]['url'])
            elif items[i]['media_type'] == 2:
                # its video
                all_highlight_list.append(items[i]['video_versions'][0]['url'])
    
    return all_highlight_list
