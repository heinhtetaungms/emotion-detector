"""
This module provides a Flask-based web service for emotion detection.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the index.html template.

    Returns:
        str: Rendered HTML template.
    """
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detection():
    """
    Analyze the text for emotions and return the results as JSON.

    Returns:
        str or jsonify: JSON response with emotion analysis results.
    """
    if request.method == 'POST':
        data = request.get_json()
        text_to_analyze = data.get('text', '')

        if text_to_analyze:
            result = emotion_detector(text_to_analyze)

            response = {
                'anger': result['anger'],
                'disgust': result['disgust'],
                'fear': result['fear'],
                'joy': result['joy'],
                'sadness': result['sadness'],
                'dominant_emotion': result['dominant_emotion']
            }

            return jsonify(response)

    return 'Invalid input', 400


if __name__ == '__main__':
    app.run(debug=True)
