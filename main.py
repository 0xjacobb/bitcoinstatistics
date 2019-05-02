from app import app
import time
import multiprocessing
import twitter_API
import google_trends


def start_server(app, **kwargs):
    print("APP/ SERVER STARTED")

    def run():
        app.run_server(**kwargs)

    # Run on a separate process so that it doesn't block
    server_process = multiprocessing.Process(target=run)
    server_process.start()


def start_twitter():
    p = multiprocessing.current_process()
    print('STARTING Multiprocess:', p.name)
    twitter_API.start()


def start_google():
    p = multiprocessing.current_process()
    print('STARTING Multiprocess:', p.name)
    google_trends.start()


if __name__ == "__main__":
    start_server(app)

    twitter = multiprocessing.Process(name='Twitter', target=start_twitter)
    google = multiprocessing.Process(name='Google', target=start_google)

    twitter.start()
    google.start()
