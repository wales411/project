from website import create_app

app = create_app()


if __name__ =='__main__':
    #to be turn off in production
    app.run(debug=True)





