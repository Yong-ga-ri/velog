import os
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


def main():
    repo = Repo('.')  # 현재 디렉토리의 Git 저장소를 로드

    # Velog의 RSS 피드에서 포스트 정보 가져오기
    feed = feedparser.parse(RSS_FEED_URL)
    for entry in feed.entries:
        post_title = entry.title
        post_title = post_title.replace('/', '-')
        post_title = post_title.replace('\\', '-')
        post_title += '.md'
        date = datetime(*entry.updated_parsed[:6])
        file_path = os.path.join(posts_dir, post_title)

        # 파일이 이미 존재하지 않으면 생성
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(entry.description)  # 글 내용을 파일에 작성


            # 깃허브 커밋
            repo.git.add(file_path)
            repo.git.commit('-m', f'add title:{entry.title} updated at {date}')
    
    # 푸시 설정
    repo.git.push('origin', 'master')

if __name__ == "__main__":
    main()
