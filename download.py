from loadSECfilings import SECdownload

def download():
    for year in range(2012, 2015):
        for month in range(1, 13):
            SECdownload(2014, 10)
