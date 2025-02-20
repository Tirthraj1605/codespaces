from flask import Flask, render_template
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv('USER') or os.getenv('USERNAME')

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime('%Y-%m-%d %H:%M:%S %f')[:-3]

    # Get 'top' command output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

    return render_template('index.html', name="Your Name", user=username, time=formatted_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)