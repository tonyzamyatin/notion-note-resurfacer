import random
import requests
import json
import re

""" Config data """

INTEGRATION_TOKEN = ""
NOTION_DATABASE_ID = ""
NUM_RANDOM_PAGES = 3
PROP_NAME = "Today's idea"

""" Functions. Do not change anything below unless you want to change the logic """


def query_database(database_id, token):
    has_more = None
    next_cursor = None
    url = f"https://api.notion.com/v1/databases/{database_id}/query"

    while has_more is None or has_more:
        if next_cursor is None:
            db = get_database_section(url, token)
        else:
            db_section = get_database_section(url, token, next_cursor)
            db["results"].extend(db_section["results"])
            db["has_more"] = db_section["has_more"]
            db["next_cursor"] = db_section["next_cursor"]

        has_more = db["has_more"]
        if has_more:
            next_cursor = db["next_cursor"]

    return db


def get_database_section(url, token, next_cursor=None):
    payload = {"page_size": 100}
    if next_cursor:
        payload["start_cursor"] = next_cursor

    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "Notion-Version": "2023-04-27",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def update_pages(token, db, num_random_pages):
    for page in db["results"]:
        if page["properties"][PROP_NAME]["checkbox"]:
            update_page(token, page["id"], False)

    n = len(db["results"])
    rand_indices = random.sample(range(n), num_random_pages)

    for index in rand_indices:
        page_id = db["results"][index]["id"]
        update_page(token, page_id, True)


def update_page(token, page_id, value):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {
        "properties": {
            PROP_NAME: {
                "type": "checkbox",
                "checkbox": value
            }
        }
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json",
        "Notion-Version": "2023-04-27",
        "content-type": "application/json"
    }
    response = requests.patch(url, json=payload, headers=headers)


def validate_token(token):
    return bool(re.match(r"^secret_[a-zA-Z0-9]{43}$", token))


def validate_database_id(database_id):
    return bool(re.match(r"^[a-zA-Z0-9]{32}$", database_id))


'''Main program'''

if not validate_token(INTEGRATION_TOKEN):
    raise ValueError("Invalid token")
if not validate_database_id(NOTION_DATABASE_ID):
    raise ValueError("Invalid database id")
if not (isinstance(NUM_RANDOM_PAGES, int) and 0 < NUM_RANDOM_PAGES <= 100):
    raise ValueError("Invalid number of pages to update. Please enter a number between 1 and 100.")

database = query_database(NOTION_DATABASE_ID, INTEGRATION_TOKEN)
update_pages(INTEGRATION_TOKEN, database, NUM_RANDOM_PAGES)
