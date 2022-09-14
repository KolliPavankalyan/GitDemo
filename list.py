songs = [
{"title":"hapy","playcount":1},
{"title":"ymca","playcount":6},
{"title":"Tocix","playcount":10}
]
print(max(songs, key=lambda n: n['playcount'])['title'])