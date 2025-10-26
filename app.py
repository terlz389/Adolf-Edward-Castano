from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# Futuristic HTML template
futuristic_home = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🚀 AQUILITE Flask API</title>
<style>
  body {
    margin: 0;
    font-family: 'Orbitron', sans-serif;
    background: radial-gradient(circle at top, #020024, #090979, #00d4ff);
    color: #00eaff;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    text-align: center;
    overflow: hidden;
  }

  h1 {
    font-size: 3em;
    text-shadow: 0 0 20px #00eaff, 0 0 40px #00ffff;
    letter-spacing: 3px;
    animation: glow 2s infinite alternate;
  }

  @keyframes glow {
    from { text-shadow: 0 0 10px #00eaff, 0 0 20px #00ffff; }
    to { text-shadow: 0 0 25px #00ffff, 0 0 50px #00eaff; }
  }

  .btn {
    margin-top: 30px;
    padding: 12px 30px;
    font-size: 1.2em;
    color: #00eaff;
    background: transparent;
    border: 2px solid #00eaff;
    border-radius: 30px;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
  }

  .btn:hover {
    background: #00eaff;
    color: #000;
    box-shadow: 0 0 20px #00eaff, 0 0 40px #00ffff;
  }

  footer {
    position: absolute;
    bottom: 15px;
    font-size: 0.9em;
    color: #aaa;
  }

  footer span {
    color: #00eaff;
  }
</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
</head>
<body>
  <h1>🌌 Welcome to AQUILITE Flask API</h1>
  <button class="btn" onclick="window.location.href='/student'">View Student JSON</button>
  <footer>Powered by <span>AQUILITE Tech Labs</span> ⚡</footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(futuristic_home)

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

if __name__ == '__main__':
    app.run(debug=True)
