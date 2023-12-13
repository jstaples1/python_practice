def getCourtName(soup):

    match = soup.find(name='h1',class_='facility-name')
    print(match.text)

def getDaysOfWeek(soup):
    matches = soup.find_all(name='strong',class_='bm-booking-block-header-day')
    for m in matches: 
        print(m.text,end="\n")


def getTimes(soup,time):
    matches = soup.find_all(name='span',attrs={'title':time})  
    print("There are ",len(matches), " courts available at " , time)
    # for m in matches: 
    #     print(m.text,end="\n")     
    # 
    # 

def getDataUIDs(soup):
    matches = soup.find_all(name='div',attrs={'data-uid':True})
    for m in matches: 
        print(m['data-uid'],end="\n")   

def getCourtURL(facilityId,date):

    facilityIds = []
    facilityId='c0668c1c-1fd6-4432-a20e-4c50aaad5baa'     
    date = '2023-12-14T00:44:05.314Z'

    url='https://ubc.perfectmind.com/24063/Clients/BookMe4LandingPages/Facility?facilityId='+ facilityId+ '&widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e&arrivalDate='+ date +'&landingPageBackUrl=https://ubc.perfectmind.com/24063/Clients/BookMe4FacilityList/List?calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e&widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&embed=False&singleCalendarWidget=true://ubc.perfectmind.com/24063/Clients/BookMe4FacilityList/List?widgetId=c7c36ee3-2494-4de2-b2cb-d50a86487656&calendarId=e65c1527-c4f8-4316-b6d6-3b174041f00e'

    
    return url   


def getFreeCourts(date,time):

    #court 1
    getCourtURL('c0668c1c-1fd6-4432-a20e-4c50aaad5baa', date)
    

    #court 2
    getCourtURL('e2d99dda-cdc4-4af4-8df6-6c8061ffd56f', date)


    