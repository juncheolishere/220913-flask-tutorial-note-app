from diary import create_app

# Create APP
app = create_app()

# run
if __name__ == "__main__":
    app.run(debug=True)