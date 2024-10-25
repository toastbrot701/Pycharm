import json
import requests
from requests import head
import pandas as pd
import _json


pageID = "f184a448f3984a2f9dd7aa89b54eaf6b"
token = 'secret_2sJc3jBgpm1Wps9aDx8mvKon5QtdVjOhaC9wIkQozzk'
databaseID ="772ed84f92474c0a9683a30de5e4c1fe?v=46f36971964447119947581c3bf4b24e"
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}

# Response a Database
def responseDatabase(databaseID,headers):
    #URL
    readUrl=f"https://api.notion.com/v1/databases/{databaseID}"
    #Request
    res=requests.request("GET",readUrl,headers=headers)
    #Status Code Anzeigen
    print(res.status_code)

def readDatabase(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseID}/query"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('../full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)
    return data


# Update a Page
def updatePage(headers,pageID):
    updateUrl = f"https://api.notion.com/v1/pages/{pageID}"
    #Json file/Data um Seite zu aktualisieren
    updateData = {
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "THIENQCCCCCC"
                        }
                    }
                ]
            },
            "Text": {
                    "rich_text": [
                        {
                            "text": {
                                "content": "My name is Thienqc"
                            },
                        }
                    ]
                },
            "Checkbox": {
                    "checkbox": False
                },
            "Number": {
                    "number": 2004
            },
            "Select": {
                    "select": {
                        "name": "Mickey",
                    }
                },
            "Multi-select": {
                    "multi_select": [
                        {
                            "name": "Coconut",
                        },
                        {
                            "name": "Banana",
                        }
                    ]
                },
            "Date": {
                    "date": {
                        "start": "2022-08-04",
                        "end": "2022-08-09",
                    }
                },
            "URL": {
                    "url": "ipsum.com"
                },
            "Email": {
                    "email": "thienqc@ipsum.com"
                },
            "Phone": {
                    "phone_number": "32323232"
                },
            "Person": {
                    "people": [
                        {
                            "id": "4af42d2d-a077-4808-b4f7-e960a93fd945",
                        }
                    ]
                },
            "Relation": {
                    "relation": [
                        {
                            "id": "6c320979581b44819d84f941f7eddc41"
                        }
                    ]
                }
            }
        }
    data = json.dumps(updateData)
    response = requests.request("PATCH", updateUrl, headers=headers, data=data)
    print(response.status_code)


def eigeneAPi():
    Url = requests.get("https://www.notion.so/772ed84f92474c0a9683a30de5e4c1fe?v=46f36971964447119947581c3bf4b24e")
    result = json.loads(Url)
    df = pd.DataFrame(result)
    print(df)



updatePage(headers, pageID)
readDatabase(databaseID, headers)
responseDatabase(databaseID, headers)
