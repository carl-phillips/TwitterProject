import twitter
import tkinter
import datetime

def run():
    api = twitter.Api(consumer_key='7SVoyHlwYgm90Y5HSzmTzUQ9O',
                      consumer_secret='D0crcrKca9S3TXuqGRPYhzBN0LJut34MecER8Ly8fb3xrM0Gja',
                      access_token_key='1199488399238926336-1jV9xq8bs4zdP5qiq96cUwP5GF1Fuz',
                      access_token_secret='71hibaH8BPkPwCytm5CH9N4RJonaRCrSKUqG9y3dwo2Ix')

    print(api.VerifyCredentials())

    search_string = "trump";
    result_type = "recent";
    time_range = datetime.date(2019, 11, 3);
    tweet_count = 100;

    search = "q=" + str(search_string) + "%20&result_type=" + str(result_type) + "&since=" + str(time_range) + "&count=" + str(tweet_count);
    print(search)
    results = api.GetSearch(raw_query=search)
    print(str(results.__len__()))

    for result in results:
        print(str(result))


    m = tkinter.Tk()
    m.title('Twitter')
    exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
    exit_button.grid(row=12)
    sterm_label = tkinter.Label(m, text="Search Term", width=10)
    search_term = tkinter.Text(m, height=1, width=30)
    since_date_label = tkinter.Label(m, text="Since Date", width=10)
    since_date = tkinter.Text(m, height=1, width=30)
    until_date_label = tkinter.Label(m, text="Until Date", width=10)
    until_date = tkinter.Text(m, height=1, width=30)
    result_label = tkinter.Label(m, text="Result Type", width=10)
    retult_type = tkinter.OptionMenu(m, "recent", "mixed", "popular")
    count_label = tkinter.Label(m, text="Count (up to 100)", width=10)
    count = tkinter.Text(m, height=1, width=30)

    sterm_label.grid(row=1, column=0)
    search_term.grid(row=1, column=1)
    since_date_label.grid(row=2, column=0)
    since_date.grid(row=2, column=1)
    until_date_label.grid(row=4, column=0)
    until_date.grid(row=4, column=1)
    result_label.grid(row=7, column=1)
    retult_type.grid(row=8, column=0)
    count_label.grid(row=8, column=1)

    m.mainloop()



if __name__ == '__main__':
    run()