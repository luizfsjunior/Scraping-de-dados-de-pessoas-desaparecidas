from instaloader import instaloader, Profile

listaURLs = ['sinalidplidal', 'desaparecidospcba', 'desaparecidosdhppce']


ig = instaloader.Instaloader()

for cadaURL in listaURLs:

    PROFILE = cadaURL
    profile = Profile.from_username(ig.context, PROFILE)
    posts = profile.get_posts()

    for post in posts:
        ig.download_post(post, PROFILE)
