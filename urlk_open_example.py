from urllib.request import urlopen


def save_file(value):
    try:
        f = open("url_data.txt", "a")
        f.write(value )
        f.close()
    except Exception:
        print("Could not save file")


with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words=[]
    for line in story:
        lines=line.decode('utf-8')
        save_file(lines)
        line_words=line.decode('utf-8').split()
        for words in line_words:
            story_words.append(words)

print(story_words)

        #content=line.read()
        #print(content)
        #print(line)
        #save_file(line)




