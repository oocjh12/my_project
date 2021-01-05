from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    category = '전신스트레칭'
    search_response = youtube.search().list(
        q=category,  # 변수 처리
        part="snippet",
        maxResults=50
    ).execute()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            doc = {
                'category': category,
                'videoId': search_result["id"]["videoId"],
                'title': search_result["snippet"]["title"],
                'description': search_result["snippet"]["description"],
                'thumbnail': search_result["snippet"]["thumbnails"]["medium"]["url"],
                'channelTitle': search_result["snippet"]["channelTitle"],
                'publishTime': search_result["snippet"]["publishTime"]
            }

            db.myproject.insert_one(doc)
            print('완료!')


if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="Google")
argparser.add_argument("--max-results", help="Max results", default=25)
args = argparser.parse_args()

try:
    youtube_search(args)
except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
