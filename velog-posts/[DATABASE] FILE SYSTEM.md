<h1 id="파일시스템">파일시스템</h1>
<h2 id="파일-시스템-개요">파일 시스템 개요</h2>
<blockquote>
<p>💡 파일 시스템은 파일에 이름을 붙이고 저장, 탐색을 위해 파일을 어디에 위치 시킬 것인지 나타내는 체계이다. 즉, 컴퓨터에서 자료들을 쉽게 발견하고 관리할 수 있게 하는 구조적인 시스템을 말한다.</p>
<p>사용자 영역이 아닌 커널 영역에서 동작한다. 파일을 빠르게 읽기, 쓰기, 삭제 등 기본적인 기능을 원활히 수행하기 위한 목적이다. 이는 리눅스 뿐만 아니라 거의 모든 OS(Operating System)가 지원하고 있다.</p>
</blockquote>
<h3 id="리눅스-파일-구조-및-대표적인-디렉토리">리눅스 파일 구조 및 대표적인 디렉토리</h3>
<p><a href="http://www.pathname.com/fhs/">Filesystem Hierarchy Standard</a></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/320bef9e-1866-466e-8efb-a27e6b776828/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/8068e81b-0572-405b-a93b-5d2fe619323f/image.png" /></p>
<blockquote>
<p>💡 리눅스는 모든 정보(데이터)가 파일로 보존된다.
문서, 이미지, 영상, 프로그램들이 이에 해당한다.</p>
<p>또한, 사용자의 데이터 뿐 아니라 시스템을 구성하는 장치 조차도 파일로 다룬다.
하드 디스크, 키보드, 프린터 같은 입출력 장치도 모두 파일로 다룬다.</p>
<p>리눅스 커널 뿐 아니라 시스템 설정 마저도 파일로 기록된다.</p>
<p>최상위에 /디렉토리(루트 디렉토리)가 있고 아래에 디렉토리와 파일이 있는 계층 구조를 가지고 있다.(트리 혹은 디렉토리 트리로 표현)</p>
<p>리눅스는 시스템 전체에 단 하나의 트리만 가지게 된다.</p>
<p>리눅스에서는 모든 것을 파일로 다루기 때문에 파일 조작 방법을 익히는 것이 중요하다.</p>
</blockquote>
<ul>
<li><strong>/</strong><ul>
<li>리눅스 파일 체제의 최상의 디렉토리</li>
<li>모든 디렉토리들의 시작점으로 일반적인 데이터를 저장하지 않는다.</li>
</ul>
</li>
<li><strong>/bin</strong><ul>
<li>시스템을 부팅하거나 복구 모드로 운영할 때 필요한 필수적인 바이너리 실행 파일들이 들어있다.</li>
<li>ls, cp, mv, cat과 같은 기본적인 명령어들이 여기 포함된다.</li>
</ul>
</li>
<li><strong>/dev</strong><ul>
<li>‘device’의 약자로, 시스템의 장치 파일이 위치하는 곳이다.</li>
<li>하드 드라이브, USB 드라이브, 터미널, 키보드 등 다양한 하드웨어 장치를 나타내는 파일들이 포함된다.</li>
</ul>
</li>
<li><strong>/etc</strong><ul>
<li>시스템 전반에 걸쳐 사용되는 설정 파일들이 저장되는 위치이다.</li>
<li>부팅 스크립트, 네트워크 설정 파일, 사용자 계정 정보 등이 포함된다.</li>
</ul>
</li>
<li><strong>/home</strong><ul>
<li>사용자의 개인 데이터와 설정 파일이 저장되는 디렉토리이다.</li>
<li>시스템에 있는 각 사용자 계정은 여기에 자신의 홈 디렉토리를 가지며, 사용자의 문서, 사진, 설정 파일 등이 이곳에 저장된다.</li>
</ul>
</li>
<li><strong>/sbin</strong><ul>
<li>‘system binary’의 약자로, 시스템 관리와 관련된 실행 파일들이 들어있는 디렉토리이다.</li>
<li>주로 시스템 관리자(root)에 의해 사용되며, 시스템 부팅, 복구, 관리 등에 필요한 명령어들이 포함된다.</li>
</ul>
</li>
<li><strong>/tmp</strong><ul>
<li>임시 파일을 저장하는 곳으로, 시스템이나 사용자가 일시적으로 사용하는 파일들을 위한 공간이다.</li>
<li>이 디렉토리의 내용은 보통 재부팅 시에 지워질 수 있다.</li>
</ul>
</li>
<li><strong>/usr</strong><ul>
<li>‘Unix System Resources’의 약자로, 사용자들에 의해 사용되는 응용 프로그램과 파일들이 위치하는 디렉토리이다.</li>
<li>/usr/bin, /usr/lib, /usr/local등과 같은 하위 디렉토리들을 포함하고 있다.</li>
</ul>
</li>
<li><strong>/var</strong><ul>
<li>‘variable’의 약자로, 자주 변하는 데이터를 저장하는 곳이다.</li>
<li>이곳에는 로그 파일, 메일 박스, 임시 파일 등이 저장되며 시스템 운영 중에 지속적으로 변할 수 있다.</li>
</ul>
</li>
</ul>
<h3 id="window폴더와-간단-비교">window폴더와 간단 비교</h3>
<table>
<thead>
<tr>
<th>기능</th>
<th>Windows</th>
<th>Linux</th>
</tr>
</thead>
<tbody><tr>
<td>root</td>
<td>C:\</td>
<td>/</td>
</tr>
<tr>
<td>사용자 폴더</td>
<td>C:\Users{username}</td>
<td>/home/{username}</td>
</tr>
<tr>
<td>설정</td>
<td>폴더는 숨겨져 있지만 제어판으로 접근</td>
<td>/etc</td>
</tr>
<tr>
<td>시스템 파일</td>
<td>C:\Windows\</td>
<td>/bin, /sbin</td>
</tr>
<tr>
<td>설치 프로그램</td>
<td>C:\Program Files</td>
<td>/usr</td>
</tr>
</tbody></table>
<h1 id="파일-관련-명령어">파일 관련 명령어</h1>
<h3 id="절대-경로">절대 경로</h3>
<blockquote>
<p>💡 루트 디렉토리부터 해당 파일에 이르는 경로를 표시하는 것을 절대 경로라고 한다.</p>
</blockquote>
<h3 id="상대-경로">상대 경로</h3>
<blockquote>
<p>💡 현재 디렉토리의 위치를 기준으로 표기하는 경로를 상대 경로라고 한다.</p>
</blockquote>
<ul>
<li><p>현재 경로가 아래 그림과 같을 때</p>
<p>  <img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a5501b93-062f-4e5c-9e50-f3a559c8f4e6/image.png" /></p>
<table>
<thead>
<tr>
<th>상대 경로</th>
<th>절대 경로</th>
</tr>
</thead>
<tbody><tr>
<td>../ ../</td>
<td>/</td>
</tr>
<tr>
<td>..</td>
<td>/home</td>
</tr>
<tr>
<td>.</td>
<td>/home/ohgiraffers</td>
</tr>
</tbody></table>
</li>
</ul>
<h2 id="디렉토리-이동">디렉토리 이동</h2>
<blockquote>
<p>💡 현재 디렉토리와 현재 디렉토리 변경 및 디렉토리 안의 디렉토리 및 파일을 출력</p>
</blockquote>
<ul>
<li><p>pwd, cd, ls 활용</p>
<ul>
<li><p>~(틸트)를 사용하면 계정의 홈 디렉토리로 이동한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/115cc690-6695-433a-ab18-6375139a159c/image.png" /></p>
<table>
<thead>
<tr>
<th>명령어</th>
<th>기능</th>
</tr>
</thead>
<tbody><tr>
<td>pwd</td>
<td>현재 디렉토리 출력</td>
</tr>
<tr>
<td>cd</td>
<td>현재 디렉토리 변경</td>
</tr>
<tr>
<td>ls</td>
<td>디렉토리 안의 파일 출력</td>
</tr>
</tbody></table>
</li>
</ul>
</li>
</ul>
<h2 id="ls">ls</h2>
<blockquote>
<p>💡 ls 명령어를 통해 디렉토리 내의 파일 및 디렉토리 목록을 출력해 준다.</p>
</blockquote>
<pre><code class="language-bash">## 시간순으로 나열하기
ls -lt

## 큰 사이즈 우선
ls -lSh

## 작은 사이즈 우선
ls -lSrh

## 인간이 보기 쉬운 용량
ls -lh</code></pre>
<table>
<thead>
<tr>
<th>옵션</th>
<th>단어</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>-r</td>
<td>reverse</td>
<td>거꾸로 나열한다.</td>
</tr>
<tr>
<td>-R</td>
<td>recursive</td>
<td>하위 디렉토리도 검색한다.</td>
</tr>
<tr>
<td>-h</td>
<td>human</td>
<td>사이즈를 인간이 보기 쉽게 K, M, G 단위로 표시한다.</td>
</tr>
<tr>
<td>-t</td>
<td>time</td>
<td>시간 순서로 나열한다.</td>
</tr>
<tr>
<td>-a</td>
<td>all</td>
<td>숨겨진 파일이나 디렉토리도 전부 표시한다.</td>
</tr>
<tr>
<td>-l</td>
<td>long</td>
<td>자세한 내용을 출력한다.  권한: 포함된파일수 : 소유자 : 그룹 : 파일크기 : 수정일자 : 파일이름</td>
</tr>
<tr>
<td>-S</td>
<td>size</td>
<td>파일의 크기 순으로 표시한다.</td>
</tr>
</tbody></table>
<h1 id="파일-조작">파일 조작</h1>
<h2 id="mkdir-명령어">mkdir 명령어</h2>
<blockquote>
<p>💡 mkdir 명령어를 통해 디렉토리를 만들 수 있다.</p>
</blockquote>
<pre><code class="language-bash">mkdir [옵션] &lt;작성할 디렉토리 이름&gt;</code></pre>
<pre><code class="language-bash">## 현재 디렉토리 확인
$ pwd

## testDir 디렉토리 만들기
$ mkdir testDir

## 디렉토리 확인
$ ls

## 만들어진 testDir로 이동
$ cd testDir</code></pre>
<ul>
<li>중간 경로가 없을 시에는 -p 옵션을 준다.</li>
</ul>
<pre><code class="language-bash">$ mkdir -p 디렉토리1/디렉토리2/...</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/33efdbb0-d665-4302-9b2e-ce720302a5e5/image.png" /></p>
<h2 id="touch-명령어">touch 명령어</h2>
<blockquote>
<p>💡 touch 명령어로 파일을 만들 수 있다.</p>
</blockquote>
<pre><code class="language-bash">$ touch &lt;생성할 파일1&gt; &lt;생성할 파일2&gt; ...</code></pre>
<ul>
<li>testDir에서 파일 만들기</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/361abfa7-7814-4dde-aed2-5b02426a2292/image.png" /></p>
<h2 id="rm-명령어">rm 명령어</h2>
<blockquote>
<p>💡 rm 명령어로 파일 및 디렉토리를 지울 수 있다.</p>
</blockquote>
<ul>
<li>파일 삭제</li>
</ul>
<pre><code class="language-bash">## 파일 삭제
$ rm [옵션] &lt;삭제할 파일1&gt; &lt;삭제할 파일2&gt; ...</code></pre>
<ul>
<li>rm 명령어로 파일 삭제하기</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d89a2a23-4aa1-4039-bacc-49cd48e80c8c/image.png" /></p>
<ul>
<li>디렉토리 삭제</li>
</ul>
<pre><code class="language-bash">## -r 옵션을 주어 디렉토리를 삭제할 수 있다.
$ rm -r &lt;삭제할 디렉토리1&gt; &lt;삭제할 디렉토리2&gt; ...

## 추가 질문 없이 내용물이 삭제되므로 확인 문구를 띄우고 싶으면 -i 옵션을 준다.
$ rm -r -i &lt;삭제할 디렉토리1&gt; &lt;삭제할 디렉토리2&gt; ...

## 비어있는 디렉토리는 rmdir로도 지울 수 있다.
$ rmdir &lt;삭제할 디렉토리1&gt; &lt;삭제할 디렉토리2&gt; ...</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/313ebff8-68df-44fb-8cca-ed8ecdc7137b/image.png" /></p>
<h2 id="cat-명령어">cat 명령어</h2>
<blockquote>
<p>💡 cat 명령어로 파일 내용을 출력할 수 있다.</p>
</blockquote>
<pre><code class="language-bash">$ cat [옵션] &lt;파일 이름1&gt; &lt;파일 이름2&gt; ...</code></pre>
<ul>
<li>/etc/hostname 파일 출력하기</li>
</ul>
<pre><code class="language-bash">## 파일 하나 출력하기
$ cat /etc/hostname

## 파일 여러개 한번에 출력하기
$ cat /etc/hostname /etc/crontab

## 행번호 붙여 출력하기
$ cat -n /etc/crontab</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/dbebbebb-f75f-4ac8-bce9-ac8e59efa32d/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/da622b91-f486-44a1-9fe1-4b0e02e8338c/image.png" /></p>
<h2 id="cp-명령어">cp 명령어</h2>
<blockquote>
<p>💡 cp 명령어를 활용해 파일을 복사할 수 있다.</p>
</blockquote>
<pre><code class="language-bash">$ cp [옵션] &lt;복사할 파일&gt; ... &lt;복사할 위치&gt;</code></pre>
<ul>
<li>파일을 다른 이름으로 복사하기</li>
</ul>
<pre><code class="language-bash">## test1 파일 만들기
$ touch test1.txt

## test1.txt을 test2.txt로 복사하기
$ cp test1.txt test2.txt

## 복사된 파일 확인
$ ls</code></pre>
<ul>
<li>파일을 특정 디렉토리 안에 복사하기</li>
</ul>
<pre><code class="language-bash">## dir1 디렉토리 생성하기
$ mkdir dir1

## test1.txt를 dir1 디렉토리로 복사하기
$ cp test1.txt dir1

## dir1 폴더에 복사된 것을 확인
$ ls dir1 </code></pre>
<ul>
<li>기존 파일에 복사하면 말없이 덮어쓴다. 그럴 땐 i옵션을 사용하면 확인 질문이 뜨게 된다.</li>
</ul>
<pre><code class="language-bash">## test1.txt를 기존 파일에 덮어쓸 때 확인하기
$ cp -i test1.txt test2.txt</code></pre>
<ul>
<li>디렉토리 역시 cp로 복사가 가능하다. (단, 재귀 옵션인 -r을 주어야 한다.)</li>
</ul>
<pre><code class="language-bash">$ cp -r dir1 dir2</code></pre>
<h2 id="mv-명령어">mv 명령어</h2>
<blockquote>
<p>💡 mv 명령어를 이용해 파일 위치를 옮길 수 있다.</p>
</blockquote>
<pre><code class="language-bash">$ mv [옵션] &lt;이동할 파일&gt; ... &lt;이동할 위치&gt;</code></pre>
<ul>
<li>새로운 디렉토리 생성 후 파일 만들기</li>
</ul>
<pre><code class="language-bash">## 새로운 디렉토리 생성
$ mkdir testDir1

## 생성된 디렉토리 내부로 이동
$ cd testDir1

## test1.txt 파일 생성
$ touch test1.txt</code></pre>
<ul>
<li>파일 이름 바꾸기</li>
</ul>
<pre><code class="language-bash">## test1.txt에서 test2.txt로 파일명 변경
$ mv test1.txt test2.txt

## 변경된 파일명 확인
$ ls</code></pre>
<ul>
<li>파일을 디렉토리 안으로 옮기기</li>
</ul>
<pre><code class="language-bash">## testDir2 디렉토리 생성
$ mkdir testDir2

## test2.txt 파일을 testDir2 디렉토리로 이동
$ mv test2.txt testDir2

## 이동된 파일 확인
$ ls testDir2</code></pre>
<ul>
<li>여러 파일 옮기기</li>
</ul>
<pre><code class="language-bash">## 파일 두개 더 생성
$ touch test3.txt test4.txt

## testDir2 디렉토리로 한번에 이동
$ mv test3.txt test4.txt testDir2

## 이동된 파일들 확인
$ ls testDir2</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f0e79c3c-9fb4-4830-9664-263ae51d2cc3/image.png" /></p>
<ul>
<li>디렉토리 이동하기</li>
</ul>
<pre><code class="language-bash">## testDir2 디렉토리를 상위 디렉토리로 이동
$ mv testDir2 ..

## 상위 디렉토리로 전환
$ cd ..

## 옮겨진 디렉토리 확인
$ ls</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1b68c21b-8f69-4143-bd76-aeb935a21122/image.png" /></p>