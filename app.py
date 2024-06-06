from flask import Flask, request, jsonify
import textwrap
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = "AIzaSyAk6oA5r0bI2Jhe5RuM4rn3JAVOBlRUjuw"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/', methods=['POST'])
def generate_recommendations():
   
    try:
        # Get the parameters from the request data
        health_score = request.json.get('health_score')
        weight_goal = request.json.get('weightGoal')
        target_weight = request.json.get('targetWeight')
        fitness_goals = request.json.get('fitnessGoals')
        health_improvements = request.json.get('healthImprovements')

        # Generate content based on the parameters
        response = model.generate_content(f"My health score is ${health_score}\nRecommend me what I should I do to enhance my health status in terms of\n1. Nutrition\n2. Fitness\n3. Mental Health management\n4. Sleep\n\nWeight Goal: {weight_goal}\nTarget Weight: {target_weight}\nFitness Goals: {fitness_goals}\nHealth Improvements: {health_improvements}")

        # Format the response
        recommendations = textwrap.indent(response.text, '> ')
        
        return jsonify({'recommendations': recommendations}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(port=5002)
