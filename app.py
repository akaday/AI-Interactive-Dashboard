from flask import Flask, render_template
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data
    data = px.data.gapminder()
    fig = px.line(data, x='year', y='pop', color='country', title='Population Over Time')
    graphJSON = fig.to_json()
    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)
