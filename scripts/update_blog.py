import os
import json
import feedparser
from datetime import datetime
from git import Repo
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# GitHub 액세스 토큰과 저장소 정보 설정
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_NAME = os.getenv('REPO_NAME')
RSS_FEED_URL = 'https://v2.velog.io/rss/@rlfgks97'


# 'velog-posts' 폴더 경로
posts_dir = os.path.join('.', 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 무시 키워드 로드
with open(os.path.join(posts_dir, 'ignore_keyword.json'), 'r', encoding='utf-8') as f:
    ignore_keywords = json.load(f)


def main():
    repo = Repo('.')  # 현재 디렉토리의 Git 저장소를 로드
    origin = repo.remote(name='origin')
    new_url = f'https://{GITHUB_TOKEN}@github.com/Yong-ga-ri/velog.git'
    origin.set_url(new_url)
    print("Loaded the Git repository.")

    # Velog의 RSS 피드에서 포스트 정보 가져오기
    feed = feedparser.parse(RSS_FEED_URL)
    print("Fetched RSS feed.")

    commit_msg_body = ""

    for entry in feed.entries:
        entry_title_on_commit = entry.title
        post_title = entry.title.replace(
            '/', '-').replace('\\', '-') + '.md'
        date = datetime(*entry.updated_parsed[:6])
        file_path = os.path.join(posts_dir, post_title)

        if all(basic not in post_title for basic in ignore_keywords):
            print("post_title: ", post_title[:-3])

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(entry.description)  # 글 내용을 파일에 작성
            # print(f"Created file: {file_path}")
            commit_msg_body += f"- title: {
                entry_title_on_commit} uploaded at {date}\n"

    # 깃허브 커밋
    commit_message = f"Update posts from RSS feed\n\n{commit_msg_body}"
    print("commit_message: ", commit_message)
    # repo.git.add(file_path)
    # repo.index.commit(commit_message)
    # print(f"Committed changes for: {file_path}")

    # 깃허브에 변경 사항을 푸시
    # origin.push()
    # print("committed compeleted")


if __name__ == "__main__":
    main()
