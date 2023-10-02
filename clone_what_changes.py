pip install flask

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for messages (not suitable for production)
messages = []

@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@app.route("/send_message", methods=["POST"])
def send_message():
    user = request.form["user"]
    message = request.form["message"]
    messages.append({"user": user, "message": message})
    return jsonify({"status": "Message sent successfully!"})

if __name__ == "__main__":
    app.run(debug=True)


<!DOCTYPE html>
<html>
<head>
    <title>Simple Chat</title>
    <style>
        /* Add your CSS styles here */
    </style>
</head>
<body>
    <h1>Simple Chat Application</h1>
    <div id="chat">
        {% for msg in messages %}
        <p><strong>{{ msg.user }}:</strong> {{ msg.message }}</p>
        {% endfor %}
    </div>
    <form id="message-form">
        <input type="text" id="user" placeholder="Your Name">
        <input type="text" id="message" placeholder="Type a message">
        <button type="submit">Send</button>
    </form>
    <script>
        const messageForm = document.getElementById("message-form");
        const userField = document.getElementById("user");
        const messageField = document.getElementById("message");
        const chatDiv = document.getElementById("chat");

        messageForm.addEventListener("submit", function (e) {
            e.preventDefault();
            const user = userField.value;
            const message = messageField.value;
            sendMessage(user, message);
            messageField.value = "";
        });

        function sendMessage(user, message) {
            fetch("/send_message", {
                method: "POST",
                body: new URLSearchParams({ user, message }),
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === "Message sent successfully!") {
                    chatDiv.innerHTML += `<p><strong>${user}:</strong> ${message}</p>`;
                }
            });
        }
    </script>
</body>
</html>


python app.py

