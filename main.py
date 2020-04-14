from app import app
import callbacks
from layouts import set_layout

if __name__ == "__main__":
    app.layout = set_layout()
    app.run_server(debug=True, processes=True)