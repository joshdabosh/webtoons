<center>
  <h1>Webtoons site scraper, for Python 3</h1>
</center>
Note: this module was based off of (this)[https://github.com/Galactus03/webtoons]
repository for Python2. Big thanks to @Galactus03!

I added more resiliency to the functions, transferred all code to Python3 syntax, fixed quite some bugs, and made it return results.

----

This module has these functions:

`popularity_age(age, sex, toShow)` -> takes in parameters age, sex, and toShow. If not given, random.choice chooses age and sex, and toShow defaults to integer 5.
Returns list of toShow amount of the most popular webtoons based on age and sex.

`author_comics(author)` -> takes in parameter author.
Returns list of all comics that the specified author has created.

`new_releases(toShow)` -> takes in parameter toShow.
Returns list of toShow amount of webtoons that were updated today

`top10_of_day()` -> takes in no parameters.
Returns list of the top 10 most popular comics today.

`best_rated(toShow)` -> takes in parameter toShow.
Returns list of toShow amount of the most popular webtoons.

`top_in_genre(g, toShow)` -> takes in parameters g and toShow.
Returns list of toShow amount of the most popular comics in genre g.

----

<h3>INSTALLATION DIRECTIONS (pip)</h3>
To install, simply run

    sudo pip3 install webtoons

to install webtoons (this module!), requests, and BeautifulSoup4, which are dependencies.


<h3>ALTERNATE INSTALLATION DIRECTIONS (cloning)</h3>
Clone the repository and install it:

    git clone https://github.com/joshdabosh/webtoons.git
    cd webtoons
    sudo python3 setup.py install

----

<h3>USE</h3>
To use, simply start an instance of webtoons and run a few functions!

    import webtoons
    wt = webtoons.Webtoons()
    print(wt.top10_of_day())
    # prints the top 10 comics of the day


----

Comments or suggestions are welcome!
