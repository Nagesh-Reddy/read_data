import json

def normalize_data(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    normalized_data = []
    for i in range(len(data["id"])):
        normalized_row = {
            "id": data["id"][str(i)],
            "title": data["title"][str(i)],
            "danceability": data["danceability"][str(i)],
            "energy": data["energy"][str(i)],
            "key": data["key"][str(i)],
            "loudness": data["loudness"][str(i)],
            "mode": data["mode"][str(i)],
            "acousticness": data["acousticness"][str(i)],
            "instrumentalness": data["instrumentalness"][str(i)],
            "liveness": data["liveness"][str(i)],
            "valence": data["valence"][str(i)],
            "tempo": data["tempo"][str(i)],
            "duration_ms": data["duration_ms"][str(i)],
            "time_signature": data["time_signature"][str(i)],
            "num_bars": data["num_bars"][str(i)],
            "num_sections": data["num_sections"][str(i)],
            "num_segments": data["num_segments"][str(i)],
            "class": data["class"][str(i)],
            "rating": None
        }
        normalized_data.append(normalized_row)
    
    return normalized_data
