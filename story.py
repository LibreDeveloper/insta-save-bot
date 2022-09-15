import requests as req
import Cookies as ck
import media

def get_profile_info(username:str):
    data_list = []
    profile_url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    res = req.get(url=profile_url , headers=ck.MOBILE_HEADERS_STORY)
    jsonStr = res.json()
    pk = jsonStr['data']['user']['id']
    bio = jsonStr['data']['user']['biography']
    print(pk)


    story_url = f"https://i.instagram.com/api/v1/feed/user/{pk}/reel_media/"
    res = req.get(url=story_url,headers=ck.MOBILE_HEADERS_STORY)
    profile_json = res.json()
    try:
        profile_pid = profile_json['user']['profile_pic_id']
    except:
        profile_pid = ""
        print('no profile found.')
    items = profile_json['items']
    if len(items) !=0:
        for i in range(len(items)):
            media_type = items[i]['media_type']
            print("story type ->",media_type)
            if media_type == 1:
                # its image
                image = items[i]['image_versions2']['candidates'][0]['url']
                image_info = {
                        "type":"image",
                        "media": image
                    }
                data_list.append(image_info)
                # works fine

            elif media_type == 2:
                # its video
                video = items[i]['video_versions'][0]['url']
                video_info = {
                        "type":"video",
                        "media": video
                    }
                data_list.append(video_info)

    if profile_pid != "":
        res = req.get(url=f"https://i.instagram.com/api/v1/media/{profile_pid}/info/", headers=ck.MOBILE_HEADERS_STORY)
        print(res.status_code)
        if res.status_code == 200:
            res = res.json()
            profile = res['items'][0]['image_versions2']['candidates'][0]['url']
            data_list.append({
                'profile':profile,
                'bio':bio
            })
        elif res.status_code == 400:
            profile = jsonStr['data']['user']['profile_pic_url_hd']
            data_list.append({
                'profile':profile,
                'bio':bio
            })

    return data_list