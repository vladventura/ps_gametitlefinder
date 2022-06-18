# Playstation Game Title Finder

Small tool where, given a playstation game id, we attempt to find the title of this game. I've made this out of frustration after having to constantly check the game name online after leaving a few backups run all night, and forgetting which game is which.

To be clear and for the record, we're using the .tsv files from [nopaystation](https://nopaystation.com) for the search; if they don't have it, then we don't have it either 😢.

Ideally we wouldn't have to bother so much the good peeps from nopaystation, but if we want a package that's less than 5kb, this is the price we must pay 😟.

We're trying our best to avoid being annoying though: we're caching the .tsv files locally, and only re-downloading them once the server has the 'last-modified' header changed from the date that it had before.

Also, to be extra clear, these are the supported platforms as of right now:

- Playstation
- Playstation Mobile
- Playstation Portable (PSP)
- Playstation 3
- Playstation Vita

And we're only looking on games. Maybe we can incorporate looking through DLC as well, but we'll see.

# Usage

As simple as they ship it:

```python
from psgtf include psgtf

game = psgtf.find_by_id("pcsa00008")
print(game.get_name())
```

Or if you'd like to search several games at the same time:

```python
from psgtf include psgtf

games = ["PCSE00120", "psca00008", "ULUS10391"]

results = psgtf.find_by_id(games)

for psgame in results:
    print('{} -> {}'.format(psgame.get_name(), psgame.get_id()))

```

# Models

### PlaystationGame

This is the current data structure that holds the data of the game. I chose a class just in case that in the future we'd like to add more stuff to it, or fetch from some other resource to add more metadata to the games, we can do so with ease.

```python
class PlaystationGame:

    def __str__(self):
        return self.name + " " + self.id + " -> " + self.platform


    def get_name(self):
        return self.name


    def get_id(self):
        return self.id


    def get_platform(self):
        return self.platform


```

# Methods

Only a single method, `find_by_id`. It takes either a string, or a list of strings, where these string contain playstation title ids.
</br>
</br>
</br>
</br>
</br>
</br>

# FAQ (or just AQ in this case, no one is asking)

Q: Why is this a thing?  
A: Because I'm an NPS user, and if you're also a fellow NoPayStation user, then you know how annoying it is looking for a specific game to copy over to your console. What if I want to play Persona 4 Golden, but I don't know the Title ID? I'd have to Google the game's ID and match it with my folders. With this, you can make a small script that generates a text file with all the names instead.

Q: Why not just Google? Isn't it more effort to make said script?  
A: But it is not fun!! Why run when you can walk? It's fun!

Q: Any more plans for this package?  
A: Maybe not, honestly. I'll try to add the rest of the content, but we'll see.

Q: Will you make something useful next time?  
A: No promises.

Q: What did you learn with this project?  
A: I learned about publishing a package to testpypi and pypi, which is why I decided to just go through with it, might as well. I also learned about the 'last-modified' header on a request, and how this can be used to stop the request pre-flight. Lastly, I learned about how packaging works in Python; very different from what I'm used to in JS.

# Closing thoughts

Thanks for reading this, honestly. I'm open to any suggestions for the package; I don't see why not work on it a bit more, at least.
