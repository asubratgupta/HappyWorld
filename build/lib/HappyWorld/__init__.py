import webbrowser, os

page = 'file:///' + os.getcwd() + '/WebPage/index.html'
if __name__ == "__main__":
    webbrowser.open_new_tab(page)