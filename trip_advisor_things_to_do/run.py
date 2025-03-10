import requests
import json
import time
import random

cities = [
    "Paris, France",
    "Madrid, Spain",
    # "Tokyo, Japan",
    # "Rome, Italy",
    # "Milan, Italy",
    # "New York City",
    # "Amsterdam, Netherlands",
    # "Sydney, Australia",
    # "Singapore, Singapore",
    # "Barcelona, Spain",
    # "Taipei, Taiwan",
    # "Seoul, South Korea",
    # "London, United Kingdom",
    # "Dubai, United Arab Emirates",
    # "Berlin, Germany",
    # "Osaka, Japan",
    # "Bangkok, Thailand",
    # "Los Angeles",
    # "Istanbul, Turkey",
    # "Melbourne, Australia",
    # "Hong Kong, China",
    # "Munich, Germany",
    # "Las Vegas",
    # "Florence, Italy",
    # "Prague, Czech Republic",
    # "Dublin, Ireland",
    # "Kyoto, Japan",
    # "Vienna, Austria",
    # "Lisbon, Portugal",
    # "Venice, Italy",
    # "Kuala Lumpur, Malaysia",
    # "Athens, Greece",
    # "Orlando, Florida",
    # "Toronto, Canada",
    # "Miami",
    # "San Francisco",
    # "Shanghai, China",
    # "Frankfurt, Germany",
    # "Copenhagen, Denmark",
    # "Zurich, Switzerland",
    # "Washington, D.C.",
    # "Pattaya-Chonburi, Thailand",
    # "Vancouver, Canada",
    # "Stockholm, Sweden",
    # "Mexico City, Mexico",
    # "Oslo, Norway",
    # "São Paulo, Brazil",
    # "Phuket, Thailand",
    # "Helsinki, Finland",
    # "Brussels, Belgium",
    # "Budapest, Hungary",
    # "Guangzhou, China",
    # "Nice, France",
    # "Palma de Mallorca, Spain",
    # "Honolulu, Hawaii",
    # "Beijing, China",
    # "Warsaw, Poland",
    # "Seville, Spain",
    # "Valencia, Spain",
    # "Shenzhen, China",
    # "Doha, Qatar",
    # "Abu Dhabi, United Arab Emirates",
    # "Antalya, Turkey",
    # "Fukuoka, Japan",
    # "Sapporo, Japan",
    # "Busan, South Korea",
    # "Macau, China",
    # "Edinburgh, United Kingdom",
    # "Montreal, Canada",
    # "Cancún, Mexico",
    # "Bologna, Italy",
    # "Rhodes, Greece",
    # "Verona, Italy",
    # "Delhi, India",
    # "Porto, Portugal",
    # "Ho Chi Minh City, Vietnam",
    # "Buenos Aires, Argentina",
    # "Marne-La-Vallée, France",
    # "Rio de Janeiro, Brazil",
    # "Kraków, Poland",
    # "Heraklion, Greece",
    # "Johor Bahru, Malaysia",
    # "Hanoi, Vietnam",
    # "Tel Aviv, Israel",
    # "Sharjah, United Arab Emirates",
    # "Thessaloniki, Greece",
    # "Lima, Peru",
    # "Medina, Saudi Arabia",
    # "Tbilisi, Georgia",
    # "Riyadh, Saudi Arabia",
    # "Tallinn, Estonia",
    # "Marrakech, Morocco",
    # "Mecca, Saudi Arabia",
    # "Denpasar, Indonesia",
    # "Punta Cana, Dominican Republic",
    # "Santiago, Chile",
    # "Vilnius, Lithuania",
    # "Jerusalem, Israel",
    # "Zhuhai, China",
    # "Cairo, Egypt"
]

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Length': '4603',
    'Content-Type': 'application/json',
    'Cookie': '_ga_QX0Q50ZC9P=GS1.1.1741644904.1.1.1741645108.7.0.0; TASID=FDDED0942AA348ACB99E0DF9F1B2BA2F; __vt=HuerX4t2ji0iJwDWABQCT24E-H_BQo6gx1APGQJPtzQDx6zNuH4dw_xol6qc1egpa2OwzLCCixrZwC8syzQTtYZ7Sd_QiOEO_75TJAsPLSgu2M9kGf4EZL457SX6yMRBiWM79m2-mT3OA70sJDXm0I6CGw; _ga=GA1.1.1477049954.1741644905; _gcl_aw=GCL.1741645105.null; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+10+2025+15%3A18%3A24+GMT-0700+(Pacific+Daylight+Time)&version=202405.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=0d66d091-2bc6-4f44-8643-4c631f7c453b&interactionCount=0&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CSSPD_BG%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false; _gcl_au=1.1.1728296440.1741644905; datadome=Y1ctvVr7ELyGpB7KsccQDNCYmOn_gPjEGDYbFkjHLgi12yTlE8VBZnh9_yd3jheFib9_qhe6Rcc1jKJUD10cX6~Jkp0d0W4XNa3j3v_UUh9LLnT4IcOG7CGdDI9NRVBo; TATrkConsent=eyJvdXQiOiJTT0NJQUxfTUVESUEiLCJpbiI6IkFEVixBTkEsRlVOQ1RJT05BTCJ9; TASession=V2ID.FDDED0942AA348ACB99E0DF9F1B2BA2F*SQ.3*LS.Home*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*TRA.true*LD.1*EAU._; TAUD=LA-1741645103674-1*RDD-1-2025_03_10*LG-1-2.1.F.*LD-2-.....; _lr_sampling_rate=100; __eoi=ID=24d463751f4d423d:T=1741644905:RT=1741644905:S=AA-AfjbQ4s3LsniuvUSsmnTDLuUL; __gads=ID=8b9f6df0caa39ee7:T=1741644905:RT=1741644905:S=ALNI_MYTk7uMnVTcaxsqek1YtKH9qZv3LA; __gpi=UID=0000106b50da68fb:T=1741644905:RT=1741644905:S=ALNI_MbPcNbOiOJA4XqwGQX9vlsy3DeBzA; _lc2_fpi=b140173de591--01jp120erj5nspvf7nw6btyhhb; _lc2_fpi_meta=%7B%22w%22%3A1741644905235%7D; _li_dcdm_c=.tripadvisor.com; pbjs_sharedId=d7f14567-db89-4233-b27e-ded52364015d; pbjs_sharedId_cst=zix7LPQsHA%3D%3D; _lr_env_src_ats=false; _lr_retry_request=true; pbjs_li_nonid=%7B%22nonId%22%3A%2212-zFaWqmagmAVgX%2F89ubbD4XsqRQMQPEptkLSRWhzkAwQOC0FbgyA1%2BjGg3E2hYfuH6c8aDgYcLxYfU71H36qhacsMBfPFVSS%2BjRHwflHJ1wBIRg%3D%3D%22%7D; pbjs_li_nonid_cst=zix7LPQsHA%3D%3D; pbjs_unifiedID=%7B%22TDID%22%3A%22fde388bf-4c8b-4382-bb8f-437358573a11%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222025-03-10T22%3A15%3A05%22%7D; pbjs_unifiedID_cst=zix7LPQsHA%3D%3D; TAReturnTo=%1%%2Fbusiness; ServerPool=C; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; PAC=AAtFyHI41k1pI6a4JyzksUJpKlORIsHgBJXwKXdNx8xMxFilYWzq8UfHNlm5gYe3MaDmJ4SyNIgNE1Zh2_pRE5EUdczV4lzBDOfd2eF9mK9G38SERnBNOrc7zl8V75O2DGsL3zrymZ80mjgCoVv9SD1mUYZ0q8EjUV_cqYRgJ6n-5IqtY-afdgGXe2awEQQQo_j8yGDTR7uMpbGZ0oKsvLk%3D; PMC=V2*MS.11*MD.20250206*LD.20250310; SRT=TART_SYNC; TADCID=iYGTlUviKwCIwTESABQCJ4S5rDsRRMescG99HippfoQmI2XcD7Xp09MaLjRdFHorJPm-XNFSN2GugcBqttp7UzFqrLyTjOZNMLg; TART=%1%enc%3A3E%2BX8dKbrWI%2Fx3uYlf89baLlfI%2FQAjpQ5z4pORmvRoYrk9k1SOGgZ8J9hhzhiMB7Nox8JbUSTxk%3D; TASameSite=1; TAUnique=%1%enc%3Ag%2FBfPPEDsYCqx028Jm1c1ND9pqH4u3hKH0CHSQvr%2Fs0fIbs8%2F8zm16a9hAwhmYbYNox8JbUSTxk%3D; TASSK=enc%3AANywNJ3fQ9Zfkq2qfvkK0cBEBNCyH1Y15ZI1ejseT0kTKWhCT%2BaXWsYosSF8QoDMdnmTBWN2qG0Frj5rgJlmy25LMnj1GL7rJUMa6IS19fEKpOghgHgggaQpZTNM0UCCIw%3D%3D; VRMCID=%1%V1*id.10568*llp.%2Fdevelopers*e.1739473761170',
    'Origin': 'https://www.tripadvisor.com',
    'Priority': 'u=3, i',
    'Referer': 'https://www.tripadvisor.com/Search?q=Paris%2C+France&geo=1&ssrc=A&searchNearby=false&searchSessionId=000ad8b47968cf0e.ssid&offset=0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'same-origin',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15'
}

url = 'https://www.tripadvisor.com/data/graphql/ids'
pages = range(36)
aggregated_results = []

for city in cities:
    city_str = city.replace(', ', '-').replace(' ', '_').lower()
    
    for page in pages:
        data = [{"variables":{"events":[{"schemaName":"user_navigated","eventJson":"{\"producer_ref\":\"web-platform-domain\",\"uid\":\"1ec46726-48ad-422d-8b12-5680dfbd8be3\",\"identifiers\":{},\"navigation_type\":\"USER_INITIATED\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15\",\"origin\":\"https://www.tripadvisor.com\",\"referrer\":\"https://www.tripadvisor.com/Search?q=Paris%2C+France&geo=1&ssrc=A&searchNearby=false&searchSessionId=000ad8b47968cf0e.ssid&offset=0\",\"from_route\":{\"page\":\"Search\",\"params\":{\"geo\":\"1\",\"q\":\"" + city + "\",\"offset\":\"" + str(30*page) + "\",\"ssrc\":\"A\",\"searchSessionId\":\"000ad8b47968cf0e.ssid\",\"searchNearby\":\"false\"},\"path\":\"/Search?q=" + city + "&geo=1&ssrc=A&searchNearby=false&searchSessionId=000ad8b47968cf0e.ssid&offset=" + str(30*page) + "\",\"fragment\":\"\"},\"to_route\":{\"page\":\"Search\",\"params\":{\"q\":\"" + city + "\",\"geo\":\"1\",\"ssrc\":\"A\",\"searchNearby\":\"false\",\"searchSessionId\":\"000ad8b47968cf0e.ssid\",\"offset\":\"" + str(30*page) + "\"},\"path\":\"/Search?q=" + city + "&geo=1&ssrc=A&searchNearby=false&searchSessionId=000ad8b47968cf0e.ssid&offset=" + str(30*page) + "\",\"fragment\":\"\"},\"client_timestamp\":\"2025-03-10T22:18:28.251Z\"}"}]},"extensions":{"preRegisteredQueryId":"636d0b9184b2fc29"}},{"variables":{"events":[{"schemaName":"page_viewed__2","eventJson":"{\"producer_ref\":\"web-platform-domain\",\"event\":\"page_viewed\",\"page\":{\"name\":\"Search\",\"locale\":\"en-US\",\"tld\":\"com\",\"uid\":\"33333393-f2af-4465-8d8b-d411938d0025\"},\"event_source\":{\"brand\":\"TA\",\"governance\":{\"domain\":\"Unknown\"}},\"event_type\":{\"name\":\"Page Viewed\",\"version\":2},\"route\":{\"page\":\"Search\",\"params\":{\"q\":\"" + city + "\",\"geo\":\"1\",\"ssrc\":\"A\",\"searchNearby\":\"false\",\"searchSessionId\":\"000ad8b47968cf0e.ssid\",\"offset\":\"" + str(30*page) + "\"},\"path\":\"/Search?q=" + city + "&geo=1&ssrc=A&searchNearby=false&searchSessionId=000ad8b47968cf0e.ssid&offset=" + str(30*page) + "\",\"fragment\":\"\"},\"filter\":{\"experiences\":{\"party\":{\"total\":0,\"adults\":0,\"children\":0}},\"vacation_rentals\":{\"party\":{\"total\":2,\"adults\":2,\"children\":0}},\"flights\":{\"class_of_service\":\"ECONOMY\",\"is_one_way\":true,\"dates\":{\"start\":\"2025-03-24\",\"end\":\"2025-03-31\",\"source\":\"user\",\"length_in_days\":7,\"day_of_week_of_start\":\"Mon\",\"day_of_week_of_end\":\"Mon\"},\"party\":{\"total\":1,\"adults\":1,\"children\":0,\"seniors\":0}}},\"path\":\"/Search?q=" + city + "&geo=1&ssrc=A&searchNearby=false&searchSessionId=000ad8b47968cf0e.ssid&offset=" + str(30*page) + "\",\"referrer\":\"https://www.tripadvisor.com/Search?q=" + city + "&geo=1&ssrc=A&searchNearby=false&searchSessionId=000ad8b47968cf0e.ssid&offset=" + str(30*page) + "\",\"request\":{\"locale\":\"en-US\",\"session\":\"fdded094-2aa3-48ac-b99e-0df9f1b2ba2f\",\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15\"},\"client_timestamp\":\"2025-03-10T22:18:28.262Z\",\"user_device\":{\"os\":\"unknown\",\"kind\":\"desktop\",\"app_kind\":\"web\",\"browser\":\"safari\",\"browser_version\":\"18\"},\"identifiers\":{},\"consent\":{\"ta\":{}}}"}]},"extensions":{"preRegisteredQueryId":"636d0b9184b2fc29"}},{"variables":{"page":"Search","pos":"en-US","parameters":[{"key":"q","value":city},{"key":"geo","value":"1"},{"key":"ssrc","value":"A"},{"key":"searchNearby","value":"false"},{"key":"searchSessionId","value":"000ad8b47968cf0e.ssid"},{"key":"offset","value":str(30*page)},{"key":"blockRedirect","value":"undefined"}],"factors":["TITLE","META_DESCRIPTION","MASTHEAD_H1","MAIN_H1","IS_INDEXABLE","RELCANONICAL"],"route":{"page":"Search","params":{"q":city,"geo":"1","ssrc":"A","searchNearby":"false","searchSessionId":"000ad8b47968cf0e.ssid","offset":str(30*page)}},"currencyCode":"USD"},"extensions":{"preRegisteredQueryId":"18d4572907af4ea5"}},{"variables":{"params":{"q":city,"geo":"1","ssrc":"A","searchNearby":"false","searchSessionId":"000ad8b47968cf0e.ssid","offset":str(30*page)},"page":"Search","fragment":""},"extensions":{"preRegisteredQueryId":"a26bffd43d0e25b6"}},{"variables":{"request":{"filters":{"dataTypes":["LOCATION"],"locationTypes":["ATTRACTION","ATTRACTION_PRODUCT"]},"locale":"en-US","query":city,"offset":page*30,"scope":{"locationId":1,"center":None},"locationIdsToExclude":[],"categoryFilterIds":["DESTINATIONS","HOTELS","ATTRACTIONS","RESTAURANTS","ACTIVITIES","VACATION_RENTALS","AIRLINE"],"additionalFields":["SNIPPET","MENTION_COUNT"],"limit":30}},"extensions":{"preRegisteredQueryId":"d65d51b7e2ed4f40"}}]

        try:
            results = requests.post(url, headers=headers, json=data)

            if results.status_code == 200:
                results_json = json.loads(str(results.content, 'utf-8'))
                    
                # Extract relevant info from JSON
                raw_listings = results_json[4]['data']['SERP_getSearchResultsList']['clusters'][0]['sections'][1]['results']
                listings = [
                    {
                        'name': listing.get('details', {}).get('localizedName', None),
                        'location': listing.get('details', {}).get('locationV2', {}).get('names', {}).get('longOnlyHierarchyTypeaheadV2', ''),
                        'url': 'https://www.tripadvisor.com' + listing.get('details', {}).get('defaultUrl', ""),
                        'rating': listing.get('details', {}).get('reviewSummary', {}).get('rating', -1),
                        'review_count': listing.get('details', {}).get('reviewSummary', {}).get('count', -1),
                        'thumbnail_url': listing.get('details', {}).get('thumbnail', {}).get('photoSizeDynamic', {}).get('urlTemplate', ''),
                        'thumbnail_max_width': listing.get('details', {}).get('thumbnail', {}).get('photoSizeDynamic', {}).get('maxWidth', -1),
                        'thumbnail_max_height': listing.get('details', {}).get('thumbnail', {}).get('photoSizeDynamic', {}).get('maxHeight', -1),
                        'query_city': city
                    }
                    for listing in raw_listings
                ]
                
                # Need to format url
                for listing in listings:
                    listing['thumbnail_url'] = listing['thumbnail_url'].replace('{width}', str(listing['thumbnail_max_width'])).replace('{height}', str(listing['thumbnail_max_height']))
                
                # Write to file
                output_file = f'output/{city_str}_{page:03d}_results.json'
                with open(output_file, 'w') as file:
                    json.dump(listings, file, indent=4)
                    
                # Add to aggregated results
                aggregated_results += listings
                
                print(f"{city} | Page {page} | {len(listings)} Results")
            else:
                raise Exception("Non-passing status code for page {page}. Got {results.status_code}")
        except Exception as e:
            print(f"{city} | Exception for page {page} | {e}")
        
        time.sleep(random.uniform(1.5, 3.0))
    # END page loop
# END city loop
output_file = 'output/aggregated_results.json'
with open(output_file, 'w') as file:
    json.dump(aggregated_results, file, indent=4)