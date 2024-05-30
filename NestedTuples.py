albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984)
]

print(len(albums))

for name, artist, year in albums:
    print("Albums: {}, Artist: {}, Year: {}".format(name, artist, year))