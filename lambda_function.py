import requests

def lambda_handler(event, context):
    info_data = requests.get("https://gdacs.org/xml/rss.xml")
    return info_data.text
    
    # print(event)
    # return 'Hello from Lambda!'