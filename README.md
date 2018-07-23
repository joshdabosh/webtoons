<center>
  <h1>Webtoons site scraper</h1>
  <h3>For Python3</h3>
</center>
Note: this module was based off of [this](https://github.com/Galactus03/webtoons)
repository for Python2. Big thanks to @Galactus03!

I added more resiliency to the functions, and fixed quite some bugs.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This module has these functions:

`popularity_age(age, sex, toShow)` -> takes in parameters age, sex, and toShow. If not given, random.choice chooses age and sex, and toShow defaults to integer 5.
Returns /<toShow/> amount of the most popular webtoons based on age and sex.

`author_comics(author)` -> takes in parameter author.
Returns all comics that the specified author has created.

`new_releases(toShow)` -> takes in parameter toShow.
Returns /<toShow/> amount of webtoons that were updated today

`top10_of_day()` -> takes in no parameters.
Returns the top 10 most popular comics today.

`best_rated(toShow)` -> takes in parameter toShow.
Returns /<toShow/> amount of the most popular webtoons.

`top_in_genre(g, toShow)` -> takes in parameters g and toShow.
Returns /<toShow/> amount of the most popular comics in genre /<g/>.

<h3>**INSTALLATION DIRECTIONS**</h3>
Since lxml, a required module, needs the development packages of both libxml2 and libxslt. If you don't have them already, isntall them with:"
```
sudo apt-get install libxml2-dev libxslt-dev
```
(Hint: An easy way to check if you have them already is to try `pip3 install lxml`. If it errors out and it tells you that it's missing a few packages, you should go ahead and install libxml2 and libxslt. If not, congrats! You've installed a dependency on your own.)

// I CAN'T GET TWINE TO UPLOAD MY MODULE TO PYPI YET SO PIP3 INSTALL WON'T WORK - USE ALTERNATE INSTALLATION DIRECTIONS
Then run
`pip3 install webtoons`
to install webtoons (this module!)

<h3>**ALTERNATE INSTALL DIRECTIONS**</h3>
Alternatively, you can install this module by cloning the repository and installing it:
```
git clone https://github.com/joshdabosh/webtoons.git
cd webtoons
sudo python3 setup.py install
```

<h3>**USE**</h3>
To use, simply start an instance of webtoons and run a few functions!
```
import webtoons
wt = webtoons.Webtoons()
print(wt.top10_of_day())
# returns the top 10 comics of the day
```

Comments or suggestions are welcome!
