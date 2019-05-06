from pytrends.request import TrendReq
import datetime


def start(search_words, start_date):
    print("... google module started")
    now = datetime.datetime.now()

    # Parameters for GOOGLE search
    kw_list = [search_words]
    year_start = int(start_date[:4])
    month_start = int(start_date[5:7])
    day_start = int(start_date[8:10])
    hour_start = 0
    print(kw_list, " ", year_start, " ", month_start, " ", day_start)

    # setting actual date for goggle search endpoint
    year_end = now.year
    month_end = now.month
    day_end = now.day
    hour_end = 0
    print(year_end, " ", month_end, " ", day_end)

    pytrend = TrendReq()
    pytrend.build_payload(kw_list)

    search_results = pytrend.get_historical_interest(
        kw_list, year_start, month_start, day_start, hour_start, year_end, month_end, day_end, hour_end, cat=0, geo='', gprop='', sleep=0)

    # save into file
    search_results.to_csv('google_results.csv')

    # print the first 10 datapoints
    print(search_results.head(10))


if __name__ == "__main__":
    search_words = "#bitcoin"
    start_date = "2019-04-29"
    start(search_words, start_date)
