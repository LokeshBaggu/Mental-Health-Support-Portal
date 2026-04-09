from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for simplicity
mood_log = []

# Predefined articles
articles = [
    {
        "id": 1,
        "title": "Understanding Anxiety",
        "excerpt": "Learn about the common symptoms and coping mechanisms for anxiety disorders.",
        "content": "Anxiety is a normal human emotion. However, when feelings of intense fear and distress become overwhelming and prevent us from doing everyday activities, it may be an anxiety disorder. Symptoms include constant worry, restlessness, trouble concentrating, and physical symptoms like rapid heartbeat. Coping mechanisms involve deep breathing, mindfulness, exercise, and seeking professional help if needed."
    },
    {
        "id": 2,
        "title": "The Importance of Sleep",
        "excerpt": "Discover how quality sleep impacts your overall mental and physical well-being.",
        "content": "Sleep plays a vital role in good health and well-being throughout your life. Getting enough quality sleep at the right times can help protect your mental health, physical health, quality of life, and safety. Lack of sleep can affect your mood, judgment, and ability to learn and retain information."
    },
    {
        "id": 3,
        "title": "Building Resilience",
        "excerpt": "Strategies to bounce back from adversity and build emotional strength.",
        "content": "Resilience is the process of adapting well in the face of adversity, trauma, tragedy, threats, or significant sources of stress. Building resilience involves developing strong relationships, maintaining a positive outlook, accepting that change is a part of living, and taking decisive actions during difficult situations."
    }
]

# Predefined stress tips
stress_tips = [
    "Take deep breaths: Inhale for 4 seconds, hold for 4, exhale for 4.",
    "Go for a short walk to clear your mind and get some fresh air.",
    "Listen to calming music or nature sounds.",
    "Practice mindfulness or meditation for 5-10 minutes.",
    "Write down your feelings in a journal.",
    "Connect with a friend or family member."
]

@app.route('/')
def index():
    return render_template('index.html', articles=articles, tips=stress_tips)

@app.route('/api/mood', methods=['POST'])
def add_mood():
    data = request.get_json()
    mood = data.get('mood')
    note = data.get('note', '')
    
    if not mood:
        return jsonify({'error': 'Mood is required'}), 400
        
    entry = {'mood': mood, 'note': note, 'date': 'Just now'} # Simplified date
    mood_log.insert(0, entry) # Add to beginning
    
    return jsonify({'message': 'Mood logged successfully', 'log': mood_log[:5]})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').lower()
    
    response = "I'm here to listen. How does that make you feel?"
    
    # Simple keyword-based responses
    if 'sad' in message or 'depressed' in message:
        response = "I'm sorry you're feeling that way. It's okay to feel sad sometimes. Remember, reaching out to a professional or a loved one can really help."
    elif 'anxious' in message or 'stress' in message:
        response = "Stress can be overwhelming. Have you tried any of our stress management tips located on the home page? Taking deep breaths might help right now."
    elif 'happy' in message or 'good' in message:
        response = "That's wonderful to hear! It's great to acknowledge the good moments."
    elif 'help' in message:
        response = "If you are in crisis, please contact your local emergency services or a crisis helpline immediately. I am an AI and cannot provide professional medical advice."
        
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
