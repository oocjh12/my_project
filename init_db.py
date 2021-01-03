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

    search_response = youtube.search().list(
        q='전신스트레칭',
        part="snippet",
        maxResults=30
    ).execute()

    videoId = []  # VideoID
    title = []  # 영상 제목
    description = []  # 영살 설명
    thumbnail = []  # 영상 썸네일
    channelTitle = []  # 채널 이름
    publishTime = []  # 영상 발행 시간

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videoId.append("%s" % (search_result["id"]["videoId"],))
            title.append("%s" % (search_result["snippet"]["title"],))
            description.append("%s" % (search_result["snippet"]["description"],))
            thumbnail.append("%s" % (search_result["snippet"]["thumbnails"]["medium"]["url"]))
            channelTitle.append("%s" % (search_result["snippet"]["channelTitle"],))
            publishTime.append("%s" % (search_result["snippet"]["publishTime"],))

            print("\n\nVideoId:\n\n", "\n".join(videoId), "\n")
            print("\n\ntitle:\n\n", "\n".join(title), "\n")
            print("\n\ndescription:\n\n", "\n".join(description), "\n")
            print("\n\nthumbnail:\n\n", "\n".join(thumbnail), "\n")
            print("\n\nchannelTitle:\n\n", "\n".join(channelTitle), "\n")
            print("\n\npublishTime:\n\n", "\n".join(publishTime), "\n")

            doc = {
                'videoId': videoId,
                'title': title,
                'description': description,
                'thumbnail': thumbnail,
                'channelTitle': channelTitle,
                'publishTime': publishTime
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
