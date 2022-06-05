# Iterates through list of category links and pulls all runs from each category
import requests

# Opens text file containing a link on each line and saves each link in a string array
links = []
with open("links_to_fullgame_src_runs.txt") as f:
    for line in f:
        links.append(line)

# Removes newline from end of link
curr_link_num = 0
for curr_link in links:
    links[curr_link_num] = curr_link[:-1]
    curr_link_num += 1
del(curr_link_num)
category_amount = len(links)

print(category_amount)

# unfinished but have to change computers