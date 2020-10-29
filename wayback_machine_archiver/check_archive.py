import requests
import argparse

def raw_to_request_url (raw_url):
    # Given a site URL, convert it to request format for the Wayback Availability JSON API
    return f'http://archive.org/wayback/available?url={raw_url}'

def already_archived (raw_url):
    # url -> status

    formatted_url = raw_to_request_url(raw_url)
    r = requests.get(formatted_url).json()

    return 'archived_snapshots' in r and r['archived_snapshots']!={}

'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str,
                        help='a single url to process')
    parser.add_argument('urls',
 '''   
