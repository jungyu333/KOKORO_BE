import uvicorn


def main():

    uvicorn.run(
        app="app.server:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        workers=1,
    )


if __name__ == "__main__":
    main()
