import json

with open('./output_raw_data.json') as fp:
    data = json.load(fp)

with open('./song_lyrics.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
