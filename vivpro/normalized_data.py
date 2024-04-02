import sys
sys.path.append('/home/user/my_package')

from flask import Flask, render_template, request, redirect, url_for
from read_data import normalize_data
app = Flask(__name__)

# Sample normalized data
normalized_data = normalize_data('playlist[76].json')
items_per_page = 10

#http://127.0.0.1:5000/api/all?page=3
@app.route('/api/all', methods=['GET'])
def get_all_data():
    page = int(request.args.get('page', 1))
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page

    paginated_data = normalized_data[start_index:end_index]

    total_pages = len(normalized_data) // items_per_page + (1 if len(normalized_data) % items_per_page > 0 else 0)

    return render_template('table.html', data=paginated_data, page=page, total_pages=total_pages)

#http://127.0.0.1:5000/api/song?title=3AM
@app.route('/api/song', methods=['GET'])
def get_song_by_title():
    title = request.args.get('title')
    song = next((item for item in normalized_data if item["title"] == title), None)
    if song:
        return render_template('song.html', song=song)
    else:
        return render_template('error.html', message="Song not found"), 404

#http://127.0.0.1:5000/api/rate
@app.route('/api/rate', methods=['POST'])
def rate_song():
    song_id = request.form.get('id')
    rating = request.form.get('rating')

    # Find song by ID and also update rating
    for song in normalized_data:
        if song['id'] == song_id:
            song['rating'] = rating
            return redirect(url_for('get_all_data'))
    return render_template('error.html', message="Song not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
