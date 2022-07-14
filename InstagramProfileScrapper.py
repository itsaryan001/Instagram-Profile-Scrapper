import instaloader


def insta_scrapper():
    bot = instaloader.Instaloader()

    profile = input('Enter Username: ')

    user = instaloader.Profile.from_username(bot.context, profile)

    print(f'''
        Username: {user.username}
        Name: {user.full_name}
        User Id: {user.userid}
        Posts: {user.mediacount}
        Followers: {user.followers}
        Following: {user.followees}
        Bio: {user.biography}
        Link In Bio: {user.external_url}
    ''')

    profile2 = input("Want to scrap another profile? 'y' or 'n': ").lower()

    if profile2 == 'y':
        insta_scrapper()

    else:
        exit()


insta_scrapper()
