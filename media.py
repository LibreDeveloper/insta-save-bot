import json
import requests as req
import Cookies as ck


def mediaUrl(url):
    headers = ck.MOBILE_HEADERS_STORY
    data_list = []
    res = req.get(url=f"https://i.instagram.com/api/v1/oembed/?url={url}", headers=headers)
    status = res.status_code
    if status != 404:
        media_id = res.json()
        media_id = media_id['media_id']
        print(f"media id ->{media_id}")
        res = req.get(url=f"https://i.instagram.com/api/v1/media/{media_id}/info/", headers=headers)
        res = res.json()
        items = res['items'][0]
        media_type = items['media_type']
        caption = ""
        print("media type ->",media_type)
        if media_type == 1:
            # its image
            image = items['image_versions2']['candidates'][0]['url']
            try:
                caption = items['caption']['text']
            except:
                        print('no caption')
            image_info = {
                    "type":"image",
                    "caption":caption,
                    "media": image
                }
            data_list.append(image_info)
            # works fine

        elif media_type == 2:
            # its video
            video = items['video_versions'][0]['url']
            try:
                caption = items['caption']['text']
            except:
                    print('no caption')
            video_info = {
                    "type":"video",
                    "caption":caption,
                    "media": video
                }
            data_list.append(video_info)
            # works fine

        elif media_type == 8:
            # its carousel
            carousel = items["carousel_media"]
            carousel_count = items["carousel_media_count"]
            for i in range(carousel_count):
                carousel_type = carousel[i]['media_type']

                if carousel_type == 1:
                    type = "photo"
                    url = carousel[i]['image_versions2']["candidates"][0]['url']
                    try:
                        caption = items['caption']['text']
                    except:
                        print('no caption')

                elif carousel_type == 2:
                    type = "video"
                    url = carousel[i]['video_versions'][0]['url']
                    try:
                        caption = items['caption']['text']
                    except:
                        print('no caption')
                carousel_info = {
                    "type":type,
                    "caption":caption,
                    "media": url
                }
                data_list.append(carousel_info)
            # works fine
    return data_list