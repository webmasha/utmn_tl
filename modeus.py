import requests
import json

class Modeus:
  url = "https://utmn.modeus.org"

  def __init__(self):
    with open('modeus/tmp/jwt.txt') as f:
      self.jwt = f.read()

  def search(self):
    url_search = Modeus.url + "/schedule-calendar-v2/api/calendar/events/search?tz=Asia/Tyumen"
    query = {"size":1000,"timeMin":"2024-11-17T19:00:00Z","timeMax":"2024-11-24T19:00:00Z","attendeePersonId":["8213e6a1-12e4-46ca-a047-407eb9872f87"]}

    j = requests.post(url_search, json=query, headers={'authorization': f"Bearer {self.jwt}", 'content-type': 'application/json'})
    if j.status_code == 200:
      d = j.json()
      with open('tmp/search.json', 'w', encoding='utf8') as f:
        json.dump(d, f, indent=4, ensure_ascii=False)
      self.data = d["_embedded"]
      return True

  def get_events(self):
    return [e["name"] for e in self.data["events"]]


if __name__ == '__main__':
    m = Modeus()
    m.search()
    e = m.get_events()
    print(f"Получено событий: {len(e)}")
    print("\n".join(e))
