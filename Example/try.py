from Soldier import Soldier

tester = Soldier()

youtube = tester.set_page("https://www.youtube.com")
searchbar = youtube.set_field("input#search")
searchbutton = youtube.set_field("button#search-icon-legacy")
filterfield = youtube.set_field("ytd-toggle-button-renderer >a >paper-button")
unfilterfield = youtube.set_field("button-renderer > gd")
home = youtube.set_field("yt-formatted-string.ytd-guide-entry-renderer:nth-of-type(1)")

youtube.edit(searchbar, "deadpool")
youtube.click(searchbutton)
youtube.wait_for(unfilterfield)
youtube.check_field(filterfield)
youtube.check_url("http://www.youtube.com")
youtube.check_url("https://www.youtube.com/results?search_query=deadpool")
youtube.back()
youtube.wait_for(home)
youtube.check_url("http://www.youtube.com")
youtube.compare(home, "Home")
youtube.check_prop(searchbar, "value" , "deadpool")
youtube.get_text(home)



local = tester.set_page("http://127.0.0.1:5500/")
a = local.set_field("#a")
b = local.set_field("#b")
local.compare(a, b)

tester.run(youtube)
tester.close()
