import os
import feedparser
from datetime import datetime
from git import Repo

# GitHub 액세스 토큰과 저장소 정보 설정
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = 'Yong-ga-ri'
REPO_NAME = 'velog'
FEED_URL = 'https://velog.io/rss/your_feed_url'

def fetch_posts():
    # Velog의 RSS 피드에서 포스트 정보 가져오기
    feed = feedparser.parse(FEED_URL)
    posts = []
    for entry in feed.entries:
        post_title = entry.title
        post_content = entry.description  # 또는 entry.content[0].value 사용 가능
        post_updated = datetime(*entry.updated_parsed[:6])
        posts.append((post_title, post_content, post_updated))
    return posts

def main():
    posts = fetch_posts()
    repo = Repo('.')  # 현재 디렉토리의 Git 저장소를 로드

    for post_title, post_content, post_updated in posts:
        file_name = f"posts/{post_title.replace(' ', '_')}.md"
        file_path = os.path.join(repo.working_tree_dir, file_name)

        # 파일 생성 또는 업데이트
        if os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(post_content)
            repo.index.add([file_name])
            repo.index.commit(f"Update post: {post_title}")
        else:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(post_content)
            repo.index.add([file_name])
            repo.index.commit(f"Add post: {post_title}")

    # GitHub에 푸시
    origin = repo.remote(name='origin')
    origin.push()

if __name__ == "__main__":
    main()