from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    # HTML and CSS for the loading animation
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body, html {
                height: 100%;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: #f3f4f6;
                font-family: Arial, sans-serif;
            }
            .loader {
                border: 16px solid #f3f4f6; /* Light grey */
                border-top: 16px solid #3498db; /* Blue */
                border-radius: 50%;
                width: 120px;
                height: 120px;
                animation: spin 2s linear infinite;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            .message {
                position: absolute;
                top: 70%;
                text-align: center;
                font-size: 24px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="loader"></div>
        <div class="message">THIS BOT IS MADE BY EZIKEL </div>
    </body>
    </html>
    '''
    return html_content

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
