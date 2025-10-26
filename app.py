from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# 🔹 Futuristic HTML Template (Reusable)
def futuristic_page(title, content):
    return render_template_string(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap" rel="stylesheet">
        <style>
            body {{
                margin: 0;
                font-family: 'Orbitron', sans-serif;
                background: linear-gradient(135deg, #020024, #090979, #00d4ff);
                color: #00eaff;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                overflow: hidden;
                text-align: center;
            }}
            h1 {{
                font-size: 2.8em;
                text-shadow: 0 0 15px #00eaff, 0 0 40px #00ffff;
                animation: glow 2s infinite alternate;
            }}
            @keyframes glow {{
                from {{ text-shadow: 0 0 10px #00eaff, 0 0 20px #00ffff; }}
                to {{ text-shadow: 0 0 25px #00ffff, 0 0 50px #00eaff; }}
            }}
            .card {{
                background: rgba(0, 0, 0, 0.3);
                border: 2px solid #00eaff;
                border-radius: 20px;
                padding: 30px;
                box-shadow: 0 0 20px #00eaff, 0 0 50px #00ffff;
                max-width: 500px;
            }}
            .btn {{
                margin-top: 20px;
                padding: 10px 25px;
                font-size: 1.1em;
                color: #00eaff;
                background: transparent;
                border: 2px solid #00eaff;
                border-radius: 25px;
                cursor: pointer;
                transition: 0.3s;
            }}
            .btn:hover {{
                background: #00eaff;
                color: #000;
                box-shadow: 0 0 15px #00eaff, 0 0 30px #00ffff;
            }}
            footer {{
                position: absolute;
                bottom: 10px;
                font-size: 0.9em;
                color: #aaa;
            }}
            footer span {{
                color: #00eaff;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            {content}
        </div>
        <footer>⚡ Powered by <span>AQUILITE Cyber Systems</span></footer>
    </body>
    </html>
    """)

# 🔹 Routes
@app.route('/')
def home():
    content = """
    <h1>🌌 Welcome to AQUILITE Flask API</h1>
    <button class="btn" onclick="window.location.href='/student'">Access Student Info</button>
    """
    return futuristic_page("AQUILITE API - Home", content)

@app.route('/student')
def get_student():
    student_data = {
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    }
    content = f"""
    <h1>👨‍🎓 Student Data</h1>
    <p><strong>Name:</strong> {student_data['name']}</p>
    <p><strong>Grade:</strong> {student_data['grade']}</p>
    <p><strong>Section:</strong> {student_data['section']}</p>
    <button class="btn" onclick="window.location.href='/'">Back to Home</button>
    """
    return futuristic_page("Student Info", content)

# 🔹 Optional JSON endpoint (raw data view)
@app.route('/student/json')
def get_student_json():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

if __name__ == '__main__':
    app.run(debug=True)
