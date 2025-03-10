import requests
import json
import time
import random

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Length': '5145',
    'Content-Type': 'application/json',
    'Cookie': 'ATGSESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJ3d3cuZHN3LmNvbSIsInN1YiI6IjIxNDUwOTcxMjU4IiwidXNlclN0YXR1cyI6IkFOT05ZTU9VUyIsImlzcyI6IkFURyIsImV4cCI6MTc0MTY0MDIzMCwiaWF0IjoxNzQxNjM4NDMwfQ.BlpNWqzjEsYRuZLMGbeQTDnA2vpQ1KrQOefeG4ipFP3L7sgVExV_kmAZUxyvsam1BpShV1RhZD0AkGmhsgYO_g; __rpck=0!eyJwcm8iOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsIkMiOnt9LCJOIjp7fX0~; __rpckx=0!eyJ0NyI6eyIyIjoxNzQxNjM4NDI5NTg1fSwidDd2Ijp7IjIiOjE3NDE2Mzg0Mjk1ODV9LCJlYyI6NX0~; bm_sv=8D84B0F65DE024DF49E20F25D0BE68BA~YAAQiZTYFw4f/2eVAQAAPW+9gRtLve18bMr2XvaPOXalILWZ4Y1qZNmXZhh/Z1RS8+4igZ2NAAFYuZSYN9IxFZs0wFPjkAEanUXPiBU1lh9PabWT29kVvbf8EJYB6FjFrXUo59QPgwWpjuYYGuv82p4jHLxnssCGTzPZZWd0htRcxY4sX+xqepE6sQdiAVjfSZs34ZrDBlqqwxfwJD7xCY/jHOpMBhZc886TwXpHTlUk/UsWmUQ0u/CSLkVTuw==~1; __rcmp=0!bj1ydzEsZj1ydyxzPTAsYz0yNzY5LHQ9MjAyMTA1MDMuMjAyMQ~~; __ruid=262300170-7b-tu-4j-1p-2v2ju081f8s0il9i5wuq-1741638393946; __rutma=262300170-7b-tu-4j-1p-2v2ju081f8s0il9i5wuq-1741638393946.1741638393946.1741638393946.1.2.2; _abck=FB2F017427A72F17B126F8B79E89FC8D~0~YAAQiZTYF6Ie/2eVAQAAGmu9gQ1jhEVrcKP1Mf1upxnIHdXEwhock00t1PlUOByQHdz/aAN6Oft4iWaD1lfwg5r/adoY+Ucso8XVpTplRZ97PxAxfYr6VMWZn7CATxRP0n/VsZLkW37KrIBR6wzsT2j7l+j38o4rHZZzmNNdf4Z6+clqbXpKVlB6fGmslLA/3Tgv8EXVzdGnle3RxoKFHaSDm42yHVTYdIXA+Lk8UM/zRNQi6uYL61cGfw70EmlsiN4bjVSf8SYfl1pXABIuA9mVqNSoNoBMgUYbPQyWQ/BUHT3zlI8YbWEVAN/b1CYHP6UruE/ekISGPxsM/h/Mq0i1FWVO0Pe9Mk3MDKYNmwtpfiFFoY/K0FUaw+dt+HNBrqoC4O8WivULGFMuJaE3BUXbHRTDn8Q8NtzoLfz4CJLBKr3rN6JbC5l2ZxqcSS9YTDgfRTuWKf0hU+ynp3f+GhJ3gPrqa6BecQru+B2YWWIq0ZyygizE1VI=~-1~-1~-1; bm_sz=3E35210F00EDB7E024A525830702B6ED~YAAQiZTYF5ge/2eVAQAA0Wq9gRsKtQImAqTYguVG39FCdlSlcVt3l0XrIRQLiCPW5M6Hm5SfR9zXh78vWosJiG/0+l90MH2K+SE1OTN9g6E5/1fL15r48hU5y0a6el1po/o/eK2VZ3sDaodnpjHfXm7wjLs/Ll3MCst+jOnhhzIZ5nVbPwYtNyiT4PF8WvHNxY19FMzlpMAbaiofsVnZwCCwpzyrVRp+0Ng8LQ2BlELoQSZOPqJCBJv0vnB2V444MwmSjf5cqud3Gbirp3D05tI+4veapQgIpgDd/e4k4dzx07JeDxowLlT8/mlndRCa/Sk9Y7RAi5zJRlD3CcHtUVRuWEVbsiHk4mdxJdKc2/6/R0D3AFOzYO3LOveVI0JS8SQl6yZMC6hIUyfEh589TA==~3225904~4536631; IR_4837=1741638395997%7C0%7C1741638395997%7C%7C; IR_PI=f6d782dd-fded-11ef-86d0-a717e8352fe8%7C1741638395997; _fbp=fb.1.1741638396533.726706923285712093; _gcl_aw=GCL.1741638397.Cj0KCQjwm7q-BhDRARIsACD6-fXddCk_O64YYQwhYX2kY88GVN0KQY9BQ4322dvA8d5bybmAj-KJY0saAhdNEALw_wcB; _gcl_dc=GCL.1741638397.Cj0KCQjwm7q-BhDRARIsACD6-fXddCk_O64YYQwhYX2kY88GVN0KQY9BQ4322dvA8d5bybmAj-KJY0saAhdNEALw_wcB; _sp_id.77b1=9c8a2c5e-3762-4007-8325-45d001b1b477.1741638396.1.1741638411.1741638396.11fb0d8e-04f5-417c-aa84-0abf1888f2f1; _sp_ses.77b1=*; _uetsid=f6d40a70fded11ef92a9d98f40140287; _uetvid=f6d423f0fded11ef840ff5e9af257631; dtm_token=AQAIUnK27rd66gEVedBAAQBJjwABAQCUgL3powEBAJSAvemj; dtm_token_sc=AQAIUnK27rd66gEVedBAAQBJjwABAQCUgL3powEBAJSAvemj; utag_main=v_id:019581bce76d001b8d3ab301bfa405075010606d00b35$_sn:1$_ss:0$_st:1741640210991$ses_id:1741638395758%3Bexp-session$_pn:1%3Bexp-session$vapi_domain:dsw.com$dc_visit:1$dc_event:2%3Bexp-session$dc_region:us-west-2%3Bexp-session; prev_page_name=category:men:shoes:mens shoes; prev_page_name_2=dsw home page; prev_page_type=category; smtrrmkr=638772352014608766%5E019581bc-fdb4-4c91-bc52-aac377b25807%5E019581bc-fdb4-40a4-b36a-fcef612d41eb%5E0%5E96.74.77.21; AMCV_A8683BC75245AF560A490D4D%40AdobeOrg=1176715910%7CMCIDTS%7C20158%7CMCMID%7C79328908520571050772048518084159454645%7CMCAID%7CNONE%7CMCOPTOUT-1741645596s%7CNONE%7CMCAAMLH-1742243196%7C9%7CMCAAMB-1742243196%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-20165%7CvVersion%7C5.4.0; __idcontext=eyJjb29raWVJRCI6IjJ1OG02QjI4TGJOTHFTQ2o3anRxdlRjdnFTQSIsImRldmljZUlEIjoiMnU4bTZCUGFWWnM0WU45a3o5T21ESE1YVDF0IiwiaXYiOiIiLCJ2IjoiIn0%3D; _rdt_uuid=1741638397032.c5e0d93a-ff5b-48d1-843f-060ddcfa7ac3; _sctr=1%7C1741590000000; cto_bundle=JGu74F90JTJGYnQ3b2NYQk95JTJCNHl4R0NvWG5Nbm4yNXl1YnpEVCUyQjJlVlZaS1NrOCUyRiUyRiUyRjJFY2cyJTJGZVRUVmlLYTkxdWFhODJSaSUyQkx5WU1ES1FnUkMySmZNUzhZdk50JTJGam1rS1h3JTJCS091NG5ob0pIU2pZJTNE; AMCVS_A8683BC75245AF560A490D4D%40AdobeOrg=1; _gcl_au=1.1.1329397911.1741638396; _gcl_gs=2.1.k1$i1741638392$u253152284; _pin_unauth=dWlkPU5ETmxNRE5tTVdFdE56UmlNUzAwT1RSakxXRmpZbVl0TWpNNVpESTFORFEzTVRBNQ; _scid=sc_szH35cNuFhQGb9Usuh3bUqEkL46sT; _scid_r=sc_szH35cNuFhQGb9Usuh3bUqEkL46sT; _screload=; _tt_enable_cookie=1; _ttp=01JP0VSTB53X8P9E3FG4Q3E7NG_.tt.1; s_ecid=MCMID%7C79328908520571050772048518084159454645; IR_gbd=dsw.com; _group=Group A; JSESSIONID=9K-BvOD2GnCskMiS8tBV2nmoTMvc_UCFDNnpD2IpfLN8BmZDR-wJ!1789312116; MOUS=7; ROUTEID=.ps030; ak_bmsc=A461D5F863A0EF0AC9F592ED91D8117A~000000000000000000000000000000~YAAQiZTYF4MN/2eVAQAA/OC8gRuIDLgh2t/xQwL4ps9mY7JkTKTUrJlQAqhPavPJBJfj+VLfFuWqUHuVdoU4zhCax/sasP8SUS8XzeUJAjed9xTddZJBWvyUGvBwTkmxoSgCZYcnwa2YOL0Q4UoWZTLqCMRfX5TRSSA5g8QN0NPaXMtrUlbeqIvK9QEih2Up9XQh3dbdus0UM4Pj8kSD1IqHmdPinKcP/UiAEfRZj41QZMwabgRbcNzfpvfumEZpqY2tF6PEoSa7CJmez15kJQ6c6ZXU8Z11Lp3UytrK2HCqmqJRB8oMKbt23uzJA9O0Rh8yiEIS+13RtT/tRWRqq9pgwWqo+mhzXbEGZyUOi/MXA/smS8ErZBz/Xacjq7/+dhlB9eCl6f5yCsb8MkZwF7fG/nQVVxpgsUOUKPXFCw1Y/+VgNV3jxVFOSqtfdqFEgCRKhCOnNw==; __rutmb=262300170',
    'Origin': 'https://www.dsw.com',
    'Priority': 'u=3, i',
    'Referer': 'https://www.dsw.com/category/mens/shoes',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15'
}
url = 'https://api.dsw.com/content/api/v3/page?rfk_account=dswus_prod&banner=dswus&uri=%2Fcategory%2Fmens%2Fshoes'

running_product_list = []
pages = range(88)

for page in pages:
    print(f"Querying for page {page}")
    try:
        # Build query for current page
        query = {"widgets":[{"id":"list_products","type":"search","parameters":{"include_ad_banners":True,"include_ad_products":True,"copy_format":"html"},"content":{"products":{}}},{"id":"content_funnel","type":"content","content":{"products":{}}},{"id":"content_feature","type":"content","parameters":{"copy_format":"html"},"content":{"products":{}}},{"id":"content_banner","type":"content","parameters":{"copy_format":"html"},"content":{"products":{}}},{"id":"content_editorial","type":"content","content":{"products":{}}},{"id":"content_copy","type":"content","parameters":{"copy_format":"html"},"content":{"products":{}}},{"id":"content_marketing_capture","type":"content","parameters":{"copy_format":"html"},"content":{"products":{}}},{"id":"content_seo","type":"content","content":{"products":{}}},{"id":"recs_plp_*","type":"recommendations","parameters":{"copy_format":"html"},"content":{"products":{"page_size":20,"page_number":1}}},{"id":"content_ugc","type":"content","content":{"products":{}}},{"id":"content_product_messaging","type":"content","content":{"products":{}}},{"id":"content_site_banner","type":"content","content":{"products":{}}},{"id":"content_custom_breadcrumbs","type":"content","content":{"products":{}}},{"id":"content_header","type":"content","content":{"products":{}}},{"id":"content_dont_forgets","type":"content","content":{"products":{}}},{"id":"content_shoppable_video","type":"content","content":{"products":{}}},{"id":"content_ad_banner","type":"content","content":{"products":{}}}],"context":{"user":{"atg_profile_id":"21450971258","ad_tracking_id":"AQAIUnK27rd66gEVedBAAQBJjwABAQCUgL3powEBAJSAvemj","rfk_uuid":"262300170-7b-tu-4j-1p-2v2ju081f8s0il9i5wuq-1741638393946","segments":[]},"device":{"app_type":"browser","device_type":"desktop","app_version":"2.0.0","geo_country_code":"US","geo_region_code":"CA","geo_dma_code":"807","geo_zip_code":["94102","94103","94104","94105","94107","94108","94109","94110","94111","94112","94114","94115","94116","94117","94118","94119","94120","94121","94122","94123","94124","94125","94126","94127","94128","94129","94130","94131","94132","94133","94134","94137","94139","94140","94141","94142","94143","94144","94145","94146","94147","94151","94153","94154","94156","94159","94160","94161","94162","94163","94164","94171","94172","94177","94188"],"geo_timezone_code":"pacific"},"page":{"referrer":"https://www.google.com/"},"campaign":{},"ads":{}},"content":{"products":{"page_size":60,"page_number":page,"fields":["id","name","category_list","gender","brand","default_sku","default_color_code","color_code","release_date","color_code_list","color_list","web_type","is_image_animated","is_any_clearance","is_show_price_in_cart","review_rating","review_count","price_min","price_max","clearance_price_min","clearance_price_max","msrp_list","stock_quantity","is_brand_logo_card_available","is_brand_logo_tile_available","price","clearance_price","fulfillment_mode","badges","is_drop_ship_none","message_content_id"]},"facets":{"include_product_count":True,"keys":{"brand":{"include_product_count":True,"max_results":1000,"sort":{"type":"text_case_insensitive","order":"asc"}},"calf_width":{"include_product_count":True,"sort":{"type":"text","order":"asc"}},"category_tree":{"hierarchy_level":2,"hierarchy_depth":4,"max_results":100,"sort":{"type":"text","order":"asc"}},"color_family":{"include_product_count":True,"max_results":20,"sort":{"type":"text","order":"asc"}},"dimension":{"include_product_count":True,"max_results":10,"sort":{"type":"dimension","order":"asc"}},"discount":{"include_product_count":True,"max_results":10},"discount_label":{"include_product_count":True,"max_results":10},"features":{"include_product_count":True,"max_results":100,"sort":{"type":"text","order":"asc"}},"filter_size":{"include_product_count":True,"max_results":100,"sort":{"type":"size","order":"asc"}},"gender":{"include_product_count":True,"max_results":10,"sort":{"type":"gender","order":"asc"}},"heel_height":{"include_product_count":True,"max_results":10,"sort":{"type":"heel_height","order":"asc"}},"item_type":{"include_product_count":True,"max_results":100,"sort":{"type":"text","order":"asc"}},"materials":{"include_product_count":True,"max_results":100},"occasion":{"include_product_count":True,"max_results":100,"sort":{"type":"text","order":"asc"}},"price_label":{"include_product_count":True,"max_results":10},"price":{"include_product_count":True},"shaft_height":{"include_product_count":True,"max_results":10,"sort":{"type":"shaft_height","order":"asc"}},"shop_promotions":{"include_product_count":True,"sort":{"type":"text","order":"asc"}},"special_attributes":{"include_product_count":True,"max_results":100,"sort":{"type":"text","order":"asc"}},"style":{"include_product_count":True,"max_results":200,"sort":{"type":"text","order":"asc"}},"toe_shape":{"include_product_count":True,"max_results":10,"sort":{"type":"toe_shape","order":"asc"}},"trends":{"include_total_count":True,"include_product_count":True,"max_results":100,"sort":{"type":"text","order":"asc"}}}}},"include_matched_context":{"visitor_context":["profile_segment"]},"debug":{"load_test_product_messaging":False}}
        results = requests.post(url, headers=headers, json=query)

        if results.status_code == 200:
            print("Query success")
            results_json = results.json()
            
            # Work through JSON structure
            widgets = results_json.get('widgets', {})
            products = [data for data in widgets if data.get('id', None) == 'list_products']
            
            if not products:
                raise Exception("No product container")
            products = products[0]
            
            products = products.get('products', {}).get('value', [])
            if not products:
                raise Exception("No products inside container")
            
            # Add extracted products to master list
            running_product_list += products
            print(f"Got {len(products)} products | Current total: {len(running_product_list)}")
            
            # Write products from current page
            output_file = f'output/page_{page:03d}_results.json'
            print(f"Writing results to {output_file}")
            with open(output_file, 'w') as file:
                json.dump(products, file, indent=4)
        else:
            print(f"Got non-passing response for page {page}")
    except Exception as e:
        print(f"Exception for page {page}: {e}")
        
    # Random sleep to avoid getting blocked
    time.sleep(random.uniform(2.0, 4.0))

# Write total aggregated list
output_file = 'output/results.json'
print(f"Writing aggregated results to {output_file}")
with open(output_file, 'w') as file:
    json.dump(running_product_list, file, indent=4)
