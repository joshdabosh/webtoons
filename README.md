Note: this module was based off of [this](https://github.com/Galactus03/webtoons)
repository for Python2. Big thanks to @Galactus03!

I added more resiliency to the functions, and fixed quite some bugs.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This module has these functions:

`popularity_age(age, sex, toShow)` -> takes in parameters age, sex, and toShow. If not given, random.choice chooses age and sex, and toShow defaults to integer 5.
Returns <toShow> amount of the most popular webtoonsbased on age and sex.

`author_comics(author)` -> takes in parameter author.
Returns all comics that the specified author has created.

`new_releases(toShow)` -> takes in parameter toShow.
Returns <toShow> amount of webtoons that were updated today

`top10_of_day()` -> takes in no parameters.
Returns the top 10 most popular comics today.

`best_rated(toShow)` -> takes in parameter toShow.
Returns <toShow> amount of the most popular webtoons.

`top_in_genre(g, toShow)` -> takes in parameters g and toShow.
Returns <toShow> amount of the most popular comics in genre <g>.


To start use, you need to have bs4, lxml, and requests:
`pip3 install bs4 lxml requests`

Then run
`pip3 install webtoons`
to install webtoons (this module!)


To use, simply start an instance of webtoons and run a few functions!
```
import webtoons
wt = webtoons.Webtoons()
print(wt.top10_of_day())
# returns the top 10 comics of the day
```

Comments or suggestions are welcome!