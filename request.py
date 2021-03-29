import requests
import json
import sys

params = {"state": "open"}
headers = {
  'Authorization': f'token 23e894f6eb3d765adb03b6374a8f2ddc1c090eac',
  'accept' : 'application/vnd.github.v3+json',
  'Content-Type' : 'application/json'
}
heads = ["LEETCODE", "GENERATOR", "ITERATOR","HEXNUMBER", "TRIANGLE", "REQUESTS", "CLA"]
groups = ["1021", "1022"]
actions = ["Added", "Refactored", "Deleted", "Moved", "Fixed"]
data = {
  'body': f'Your title is incorrect',
  'path': '',
  'position': 1,
  'commit_id': ''
}


def get_pulls(name):
    link = "https://api.github.com/repos/{}/python_au/pulls".format(name)
    pulls_req=requests.get(link, headers=headers, params=params)
    return pulls_req.json()


def check_name(name):
    parts = name.split()
    parts[0] = parts[0].split("-")
    if len(parts) != 3 or len(parts[0]) != 2:
        return False
    if parts[0][0] not in heads:
        return False
    if parts[0][1] not in groups:
        return False
    if parts[1] not in actions:
        return False
    return True


def isReviewed(pull, reviewer):
    comments = requests.get(pull['review_comments_url'], headers=headers,params=params).json()
    for comm in comments:
        if comm['body'] == f'Your title is incorrect':
            if comm['created_at'] > last_commit_date(pull):
                if comm['user']['login'] == reviewer:
                    return True
    return False


def last_commit_date(pull):
    commits = requests.get(pull['commits_url'], headers=headers,params=params).json()
    return commits[-1]['commit']['author']['date']


def review(pull, reviewer):
  if not isReviewed(pull, reviewer):
    commit = requests.get(pull['url']+'/files',headers=headers,params=params).json()[0]
    data['path'] = commit['filename']
    data['commit_id'] = pull['head']['sha']
    requests.post(pull['url']+'/comments', data=json.dumps(data).encode('utf8'),headers=headers).json()
  pass


def get_all_commits(pull):
    commits = requests.get(pull['commits_url'], headers=headers, params=params)
    return commits.json()


def verify(pull, reviewer):
    names = [pull['title']]
    for commit in get_all_commits(pull):
        names.append(commit['commit']['message'])
    for name in names:
        if not check_name(name):
            review(pull, reviewer)
            break




def main():
    username = input('username: ')
    reviewer = input('reviewer: ')
    for pull in get_pulls(username):
        verify(pull, reviewer)


if __name__ == '__main__':
    main()




