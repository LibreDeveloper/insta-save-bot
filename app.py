from telegram import *
from telegram.ext import *
import Texts as txt
import media
import story
import highlights as hl
import profile_info as pf
import posts
import os

TOKEN = "<YOUR BOT TOKEN HERE>"


def start(update: Update, context: CallbackContext):
    update.message.reply_text(text=txt.START_MESSAGE, parse_mode=ParseMode.HTML)


def echo(update: Update, context: CallbackContext):
    dl_msg = update.message.reply_text("⌛️ Proccessing....")
    user_msg = update.message.text
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    username = update.effective_user.username


    # check for post
    if "https://www.instagram.com/p/" in user_msg or "https://www.instagram.com/tv/" in user_msg or "https://www.instagram.com/reel/" in user_msg:
        print('post detected')
        db.update_dl(user_id)
        media_info = media.mediaUrl(user_msg)
        if len(media_info) > 1:
            context.bot.delete_message(chat_id, dl_msg.message_id)
            for i in range(len(media_info)):
                if media_info[i]['type'] == 'photo':
                    update.message.reply_photo(photo=media_info[i]['media'], caption="Saved with 💙 by @YOUR_BOT_USERNAME 🤖")
                else:
                    try:
                        update.message.reply_video(video=media_info[i]['media'],
                                                   caption="Saved with 💙 by @YOUR_BOT_USERNAME 🤖")
                    except:
                        url = media_info[i]['media']
                        update.message.reply_text(
                            text=f"👇\n\n<a href='{url}'>Download</a>" + "\n" + "Saved with 💙 by @YOUR_BOT_USERNAME 🤖",parse_mode=ParseMode.HTML)
            update.message.reply_text(text="✅ Post caption:\n\n" + media_info[0]['caption'])
        elif len(media_info) != 0:
            if media_info[0]['type'] == 'photo':
                update.message.reply_photo(photo=media_info[i]['media'], caption="Saved with 💙 by @YOUR_BOT_USERNAME 🤖")
            else:
                try:
                    update.message.reply_video(video=media_info[i]['media'], caption="Saved with 💙 by @YOUR_BOT_USERNAME 🤖")
                except:
                    url = media_info[0]['media']
                    update.message.reply_text(
                        text=f"👇\n\n<a href='{url}'>Download</a>" + "\n" + "Saved with 💙 by @YOUR_BOT_USERNAME 🤖",parse_mode=ParseMode.HTML)

            update.message.reply_text(text="✅ Post caption:\n\n" + media_info[0]['caption'])
        elif len(media_info) == 0:
            update.message.reply_text(
                text="🔒 This post is private!")
    # check for profile
    else:
        db.update_dl(user_id)
        print('username detected')
        username = user_msg.split('?')[0].replace('www.', '').replace("https://instagram.com/", '').replace(' ',
                                                                                                            '').replace(
            '/', '')
        print('username ->', username)
        profile_info = story.get_profile_info(username)
        context.bot.delete_message(chat_id, dl_msg.message_id)
        prof = pf.get_profile_info(username)
        highlight_count = hl.get_highlight_id(username)
        posts_count = prof.split('\n')[-1]
        story_count = story.get_profile_info(username)
        if len(story_count) > 0:
            story_count = len(story_count) - 1
        profile_keyboard = [
            [InlineKeyboardButton(f"📱 Stories ({story_count})", callback_data=f"1 {username}")],
            [InlineKeyboardButton(f"🖼 Highlights ({len(highlight_count)})", callback_data=f"2 {username}")],
            [InlineKeyboardButton(f"📥 Posts ({posts_count})", callback_data=f"3 {username}")]
        ]
        profile_keyboard_markup = InlineKeyboardMarkup(inline_keyboard=profile_keyboard, resize_keyboard=True)
        print(profile_info)
        if "profile" in profile_info[-1]:
            prof = prof[:prof.rfind("\n")]
            print()
            update.message.reply_document(
                document=profile_info[-1]['profile'], caption=f"{prof}"+ "\n\n" + "Saved with 💙 by @YOUR_BOT_USERNAME 🤖",
                reply_markup=profile_keyboard_markup, parse_mode=ParseMode.HTML)
        else:
            # try:
                prof = prof[:prof.rfind("\n")]
                update.message.reply_text(f'No profile photo\n\n{prof}' + "\n\n" + "Saved with 💙 by @YOUR_BOT_USERNAME 🤖",
                                          parse_mode=ParseMode.HTML, reply_markup=profile_keyboard_markup)
            # except:
            #     update.message.reply_text("Username not found!")


def button_handler(update: Update, context: CallbackContext):
    q = update.callback_query
    q.answer()
    if "1 " in q.data:
        username = q.data.split(' ')[1]
        print('query ->', username)
        profile_info = story.get_profile_info(username)
        print(len(profile_info))
        if len(profile_info) == 1 or len(profile_info) == 0:
            q.message.reply_text("This profile is private or has not any story!")
        else:
            for i in range(len(profile_info) - 1):
                if profile_info[i]['type'] == 'photo':
                    q.message.reply_photo(photo=profile_info[i]['media'])
                else:
                    q.message.reply_video(video=profile_info[i]['media'])
    elif "2 " in q.data:
        username = q.data.split(' ')[1]
        highlights = hl.get_highlight_id(username)
        if len(highlights) == 0:
            q.message.reply_text("This account has not any highlight!")
        for i in range(len(highlights)):
            q.message.reply_document(document=highlights[i], caption="Saved with 💙 by @YOUR_BOT_USERNAME 🤖")
    elif "3 " in q.data:
        username = q.data.split(' ')[1]
        post = posts.get_posts(username)
        if len(post) == 0:
            q.message.reply_text("This profile has not any post!")
        for i in range(len(post)):
            cap = post[i]['caption']
            if len(cap) > 1024:
                q.message.reply_document(document=post[i]['media'], caption="Saved with 💙 by @YOUR_BOT_USERNAME 🤖")
                q.message.reply_text(text=cap)
            else:
                q.message.reply_document(document=post[i]['media'], caption=cap)


def help(update: Update, context: CallbackContext):
    update.message.reply_text(text=txt.HELP_MESSAGE, parse_mode=ParseMode.HTML)


def main():
    """
    first of all check for open ports on you host provider then put it in below variable
    please note that if you want to run bot on VPS(virtual private server) or your local computer please use 'updater.start_polling()' method instead of webhook
    """
    # PORT = "<YOUR PORT HERE>"
    # PORT = int(os.environ.get('PORT', PORT))

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start, run_async=True))
    dispatcher.add_handler(CommandHandler("help", help, run_async=True))
    dispatcher.add_handler(CallbackQueryHandler(button_handler, run_async=True))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo, run_async=True))

    print("ig bot is running .....")


    """
    uncomment below line for webhook method on your python host
    """
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=PORT,
    #                       url_path=TOKEN,
    #                       webhook_url="https://YOUR-DOMAIN.com/" + TOKEN)


    """
    uncomment below line to use on VPS or your localhost computer
    """
    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
