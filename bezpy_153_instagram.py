import os

USER = 'sv650y'  # Profile Name
PSSWD = 'Badge7383!'
USERID = 67105256295
# account linked to your google voice, previously linked to your regular phone number

# ======================================================================================================================
# instaloader
# ======================================================================================================================
# requires pip install instaloader - downloads instagram videos
# https://pypi.org/project/instaloader/
# log into instagram first on your PC and you don't need to use ig.login() method below.
def use_instaloader():
    from instaloader import Instaloader, Profile
    ig = Instaloader(dirname_pattern=r'C:\instagram\{target}')

    # ig.login(USER, PSSWD)  # for most features, this is only required if you are not currently logged into instagram
    # best not to login this way as they may restrict your account

    profile_name = 'f45_training_greatneckplaza'   # id = 9475274603
    profile_name = 'confidanze_fitness'  # id=1765910273
    ig_userid = ig.check_profile_id(profile_name=profile_name).id
    ig_profile_pic_url = ig.check_profile_id(profile_name=profile_name).profile_pic_url_hd

    posts_to_download = {'C5PB5A5Od23'}
    p = Profile.from_username(ig.context, profile_name)  # profile object
    # igtv_iter = p.get_igtv_posts()  # iterator of igtv posts
    # followers_iter = p.get_followers()
    # folowees_iter = p.get_followees()
    # similar_accounts = list(p.get_similar_accounts())

    post_iter = p.get_posts()  # returns iterator of all posts
    posts = [post for post in post_iter if post.shortcode in posts_to_download]
    for post in posts:
        ig.download_post(post, target=profile_name)

    # ig.download_profile(profile_name=profile_name, profile_pic_only=True)    # downloads profile picture only
    # ig.download_profile(profile_name=profile_name)                           # downloads entire profile (all media)
    # ig.download_pic      NOT SURE HOW THIS WORKS

    # ig.get_stories(1765910273)  # NOT WORKING

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
    use_instagram_stories()