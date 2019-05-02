from app import app
import time
import multiprocessing
import twitter_API
import google_trends


def start_server(app, **kwargs):
    def run():
        app.run_server(**kwargs)

    # Run on a separate process so that it doesn't block
    server_process = multiprocessing.Process(target=run)
    server_process.start()


if __name__ == "__main__":
    start_server(app)
    twitter_API.start()
    google_trends.start()
