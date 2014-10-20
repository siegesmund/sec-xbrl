from loadSECfilings import SECdownload

years = range(2010, 2015)
months = range(1,13)

def download():
    for year in years:
        for month in months:
            SECdownload(2014, 10)
