from gcs import gcs_app

app = gcs_app()

if __name__ == '__main__':
    app.run(debug=True)