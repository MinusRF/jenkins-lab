from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = '/data/entries.json'

def load_entries():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_entries(entries):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(entries, f)

@app.route('/')
def index():
    entries = load_entries()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    entry = request.form.get('entry')
    if entry:
        entries = load_entries()
        entries.append(entry)
        save_entries(entries)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
