from Luna import CMD_HELP, tbot
import os
from Luna import tbot
import re
import bs4
import requests
from telethon import types
from telethon.tl import functions
from Luna.events import register

langi = "en"


@register(pattern="^/imdb (.*)")
async def imdb(e):
    if e.fwd_from:
        return
    try:
        movie_name = e.pattern_match.group(1)
        remove_space = movie_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name + "&s=all"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml")
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext("td").findNext("td").text
        mov_link = (
            "http://www.imdb.com/" + odds[0].findNext("td").findNext("td").a["href"]
        )
        page1 = requests.get(mov_link)
        soup = bs4.BeautifulSoup(page1.content, "lxml")
        if soup.find("div", "poster"):
            poster = soup.find("div", "poster").img["src"]
        else:
            poster = ""
        if soup.find("div", "title_wrapper"):
            pg = soup.find("div", "title_wrapper").findNext("div").text
            mov_details = re.sub(r"\s+", " ", pg)
        else:
            mov_details = ""
        credits = soup.findAll("div", "credit_summary_item")
        if len(credits) == 1:
            director = credits[0].a.text
            writer = "Not available"
            stars = "Not available"
        elif len(credits) > 2:
            director = credits[0].a.text
            writer = credits[1].a.text
            actors = []
            for x in credits[2].findAll("a"):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        else:
            director = credits[0].a.text
            writer = "Not available"
            actors = []
            for x in credits[1].findAll("a"):
                actors.append(x.text)
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        if soup.find("div", "inline canwrap"):
            story_line = soup.find("div", "inline canwrap").findAll("p")[0].text
        else:
            story_line = "Not available"
        info = soup.findAll("div", "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll("a")
                for i in a:
                    if "country_of_origin" in i["href"]:
                        mov_country.append(i.text)
                    elif "primary_language" in i["href"]:
                        mov_language.append(i.text)
        if soup.findAll("div", "ratingValue"):
            for r in soup.findAll("div", "ratingValue"):
                mov_rating = r.strong["title"]
        else:
            mov_rating = "Not available"
        await e.reply(
            "<a href=" + poster + ">&#8203;</a>"
            "<b>Title : </b><code>"
            + mov_title
            + "</code>\n<code>"
            + mov_details
            + "</code>\n<b>Rating : </b><code>"
            + mov_rating
            + "</code>\n<b>Country : </b><code>"
            + mov_country[0]
            + "</code>\n<b>Language : </b><code>"
            + mov_language[0]
            + "</code>\n<b>Director : </b><code>"
            + director
            + "</code>\n<b>Writer : </b><code>"
            + writer
            + "</code>\n<b>Stars : </b><code>"
            + stars
            + "</code>\n<b>IMDB Url : </b>"
            + mov_link
            + "\n<b>Story Line : </b>"
            + story_line,
            link_preview=True,
            parse_mode="HTML",
        )
    except IndexError:
        await e.reply("Plox enter **Valid movie name** kthx")

from bs4 import BeautifulSoup
import requests
from Luna import tbot
from Luna.events import register

@register(pattern="^/movie (.*)")
async def yts(event):
 name = event.pattern_match.group(1)
 for page in range(1, 2):
  url = "https://yts.mx/browse-movies/" + name + "/all/all/0/seeds/0/all"
  r = requests.get(url).text
  soup = BeautifulSoup(r, "html.parser")
  for name in soup.findAll(
      "div",
      class_="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"):
    mov_name = name.find("div", class_="browse-movie-bottom")
    movie_name = mov_name.a.text
    movie_year = mov_name.div.text
    movie_name = movie_name + " " + movie_year
    rating = name.find("h4", class_="rating", text=True)
    if rating is not None:
      rating = rating.text
      rating = rating[:3]
    else:
      rating = "0.0"
    if rating[2] == "/":
      rating = rating[0:2]
    try:
      #Handles Movie Name Containing [xx]
      if movie_name[0] == "[" and movie_name[3] == "]":
        movie_name = movie_name[5:]
      movie_name = movie_name.replace(" ", "-")
      index = 0
      for char in movie_name:  #Handles Special Character In Url
        if char.isalnum() == False and char != "-":
          movie_name = movie_name.replace(char, "")
      for char in movie_name:
        if char == "-" and movie_name[index + 1] == "-":
          movie_name = movie_name[:index] + movie_name[index + 1:]
        if index < len(movie_name) - 1:
          index = index + 1
      if "" in movie_name:  #Handles Movie Url Containing ""
        movie_name = movie_name.replace("--", "-")
      movie_url = "https://yts.mx/movie/" + movie_name
      movie_url = movie_url.lower()
      request = requests.get(movie_url).text
      n_soup = BeautifulSoup(request, "lxml")
      info = n_soup.find("div", class_="bottom-info")
      torrent_info = n_soup.find("p", class_="hidden-xs hidden-sm")
      genre = n_soup.findAll("h2")[1].text
      likes = info.find("span", id="movie-likes").text
      imdb_link = info.find("a", title="IMDb Rating")["href"]
      for torrent in torrent_info.findAll("a"):
        if (torrent.text[:3] == "720"):
          torrent_720 = torrent["href"]
        if torrent.text[:4] == "1080":
          torrent_1080 = torrent["href"]
    except Exception as e:
      likes = None
      genre = None
      num_downloads = None
      imdb_link = None
      torrent_720 = None
      torrent_1080 = None
      pass
    movie_name = mov_name.a.text
    text = "Name :", movie_name
    text += "Year :", movie_year
    text += "IMDb Links :", imdb_link
    text += "Genre :", genre
    text += "IMDb Ratings :", rating
    text += "Likes :", likes
    text += "YTS Link :", movie_url
    await event.reply(text)

 
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /imdb - Get full info about a movie with imdb.com
 - /rt - Get Full Details including Cast of a movie from RottenTomatoes
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
