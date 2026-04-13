from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # In a real app, you could fetch project data from a database here
    return render_template('portfolio.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.json
    print(f"Message from {data['name']}: {data['message']}")
    return jsonify({"status": "success", "message": "Message sent!"})

if __name__ == '__main__':
    app.run(debug=True)