import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading

def get_html_data(url):
    data=requests.get(url)
    return data



def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="site-stats-count").find("ul").find_all("li")
    all_details=""
    for bg in info_div:
      count = bg.find("strong").get_text()
      text = bg.find("span").get_text()
      all_details = all_details + text + " : " + count + "\n"
      return all_details


def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing..")
    mainLabel['text'] = newdata


def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 cases of INDIA",
            message=get_corona_detail_of_india(),
            timeout=10,
            app_icon='icon.ico'
        )
        time.sleep(30)




root = tk.Tk()
root.geometry("900x800")
root.iconbitmap("icon.ico")
root.title("CORONA DATA TRACKER - INDIA")
root.configure(background='white')
f = ("poppins", 25, "bold")

banner = tk.PhotoImage(file="banner.png")
bannerLabel = tk.Label(root, image=banner)
bannerLabel.pack()

mainLabel = tk.Label(root, text=get_corona_detail_of_india(),font=f, background='white')
mainLabel.pack()



reBtn=tk.Button(root, text="REFRESH", font=f, relief='solid',  command=refresh)
reBtn.pack()

th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()

