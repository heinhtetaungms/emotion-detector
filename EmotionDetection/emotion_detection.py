import requests


def emotion_detector(text_to_analyze):
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        emotion_predictions = result.get('emotionPredictions', [])
        if emotion_predictions:
            emotions = emotion_predictions[0].get('emotion', {})

            output = {
                'anger': emotions.get('anger', 0),
                'disgust': emotions.get('disgust', 0),
                'fear': emotions.get('fear', 0),
                'joy': emotions.get('joy', 0),
                'sadness': emotions.get('sadness', 0),
            }

            dominant_emotion = max(output, key=output.get)
            output['dominant_emotion'] = dominant_emotion

            return output

    return "Error: Emotion detection failed"
