import os
import sys

USER = 'sv650y'  # Profile Name
PSSWD = 'Badge7383!'
USERID = 67105256295
# account linked to your google voice, previously linked to your regular phone number

# https://toolzu.com/downloader/instagram/video/
# Use this link to download public videos / photos / stories e.t.c
# Note: Stories = the 24 HR videos posted when you click on the circle icon

# ======================================================================================================================
# instaloader: 4.13.1 installed 9/18/2024
# ======================================================================================================================
# requires pip install instaloader - downloads instagram videos
# https://pypi.org/project/instaloader/
# log into instagram first on your PC and you don't need to use ig.login() method below.
def use_instaloader():
    from instaloader import Instaloader, Profile

    profile_name = 'northvalleygrp'
    # profile_name = 'f45_training_greatneckplaza'   # id = 9475274603
    # profile_name = 'confidanze_fitness'  # id=1765910273
    # profile_name = 'tamarbezalely'   # id=3450447760  == p.username
    # profile_name = 'sv650y'

    dir_name = rf'C:\instagram\{profile_name}'
    os.makedirs(dir_name, exist_ok=True)
    ig = Instaloader(dirname_pattern=dir_name)
    # ig.login(USER, PSSWD)  # for most features, this is only required if you are not currently logged into instagram
    # best not to login this way as they may restrict your account

    ig_profile = ig.check_profile_id(profile_name=profile_name)
    ig_profile_photo = ig_profile.profile_pic_url
    ig_full_name = ig_profile.full_name

    p = Profile.from_username(ig.context, profile_name)  # profile object
    p_id = p.userid

    # stories = list(ig.get_stories(userids=[p_id]))   # current stories, login required
    # for story in stories:
    #     print(story.video_url)


    # igtv_iter = p.get_igtv_posts()  # iterator of igtv posts
    # followers_iter = p.get_followers()
    # folowees_iter = p.get_followees()
    # similar_accounts = list(p.get_similar_accounts())


    # print('posts', list(p.get_posts()))  # takes a long time is there are a lot of posts

    post_iter = p.get_posts()  # returns iterator of all posts
    # post = next(post_iter)  # most recent post
    # post.shortcode    # DADpS7Kqe7y  c.f. with https://www.instagram.com/p/DADpS7Kqe7y/
    # post.video_url    # https://scontent.cdninstagram.com/o1/v/t16/f1/m86/F146DEBB7B60FE5DD6441DD9F91EB18F_video_dashinit.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuNzIwLmRhc2hfYmFzZWxpbmVfMV92MSJ9&_nc_ht=scontent.cdninstagram.com&_nc_cat=110&vs=2c15a6234d15886b&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9GMTQ2REVCQjdCNjBGRTVERDY0NDFERDlGOTFFQjE4Rl92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dBZ3ZjUnRYSERsckh0RUJBTG1fNnlCaHVScEJicV9FQUFBRhUCAsgBACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJtLNr-uu6vcFFQIoAkMzLBdAMbMzMzMzMxgSZGFzaF9iYXNlbGluZV8xX3YxEQB1_gcA&ccb=9-4&oh=00_AYApxcGje2k_v_pwNhmsgqpn3W8CyWuMRH00idur2qbnfA&oe=66ECFE78&_nc_sid=1d576d

    posts_to_download = {'C_hA0-GyT_K'}
    posts = [post for post in post_iter if post.shortcode in posts_to_download]  # get only the posts you want

    for post in posts:
        print(post.shortcode, post.video_url)
        ig.download_post(post, target=profile_name)      # download only the posts you want

    # ig.download_profile(profile_name=profile_name, profile_pic_only=True)    # downloads profile picture only
    # ig.download_profile(profile_name=profile_name)                           # downloads entire profile (all media)
    # ig.download_pic      NOT SURE HOW THIS WORKS


# ======================================================================================================================
# instabot
# ======================================================================================================================
# to send messages
# requires `pip install instabot`
def use_instabot():
    from instabot import Bot
    bot = Bot()
    bot.login(username=USER, password=PSSWD)
    bot.send_message("Hi Brother", ["Receiver's Username"])

# ======================================================================================================================
# instabot
# ======================================================================================================================
# to send messages
# requires `pip install instagram-stories`
def use_instagram_stories():
    os.environ["HOME"] = r"C:\instagram"
    from instagram import instagram
    instagram.home_path()     # returns 'C:\\instagram'
    # can't do anything else with it

if __name__ == '__main__':
    use_instaloader()