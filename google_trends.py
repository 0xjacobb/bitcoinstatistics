from pytrends.request import TrendReq


def start():
    print("GOOGLE MODULE STARTED")
    # Parameters for GOOGLE search
    kw_list = ["Bitcoin"]
    year_start = 2019
    month_start = 1
    day_start = 1
    hour_start = 0
    year_end = 2019
    month_end = 5
    day_end = 2
    hour_end = 0

    pytrend = TrendReq()
    pytrend.build_payload(kw_list)

    search_results = pytrend.get_historical_interest(
        kw_list, year_start, month_start, day_start, hour_start, year_end, month_end, day_end, hour_end, cat=0, geo='', gprop='', sleep=0)

    # save into file
    search_results.to_csv('google_results.csv')

    # print the first 10 datapoints
    print(search_results.head(10))


if __name__ == "__main__":
    start()
