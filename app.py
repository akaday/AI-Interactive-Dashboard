from flask import Flask, render_template # type: ignore
import plotly.express as px # type: ignore

app = Flask(__name__)

@app.route('/another')
def another():
    return render_template('another_page.html')


if __name__ == '__main__':
    app.run(debug=True)
