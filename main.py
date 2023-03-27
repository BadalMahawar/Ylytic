from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)
API_URL = 'https://dev.vlvtic.com/vlvtic/test'



@app.route('/search')
def search_comments():
    # Parse search parameters from query string
    author = request.args.get('search_author')
    text = request.args.get('search_text')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')

    # Construct parameters for the underlying API
    params = {}
    if author:
        params['author'] = author
    if text:
        params['text'] = text
    if at_from:
        params['at_from'] = at_from
    if at_to:
        params['at_to'] = at_to
    if like_from:
        params['like_from'] = like_from
    if like_to:
        params['like_to'] = like_to
    if reply_from:
        params['reply_from'] = reply_from
    if reply_to:
        params['reply_to'] = reply_to

    # Call the underlying API with the constructed parameters
    response = requests.get(API_URL, params=params)

    # Parse the JSON response and extract the comments
    data = json.loads(response.text)
    comments = data['comments']

    # Return the comments in a JSON response
    return jsonify(comments=comments)



if __name__ == '__main__':
    app.run(debug=True)

