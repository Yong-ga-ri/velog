<h1 id="우분투-계정과-권한-명령어">우분투 계정과 권한 명령어</h1>
<h3 id="superuser">Superuser</h3>
<ul>
<li>시스템 운영 관리자 계정이다.</li>
<li>일반적으로 리눅스에선 root 유저를 의미한다.</li>
<li>일반 사용자 계정의 권한과 슈퍼유저의 권한을 구분하여 사용해야 한다.</li>
<li>우분투의 경우 기본적으로 root 사용자를 비활성화한다.</li>
</ul>
<h3 id="whoami">whoami</h3>
<blockquote>
<p>💡 <strong>현재 로그인</strong> 되어 있는 <strong>사용자 계정</strong>을 <strong>확인</strong>하는 명령어이다.</p>
</blockquote>
<h3 id="id">id</h3>
<blockquote>
<p>💡 현재 사용자가 가지고 있는 권한(그룹 포함)을 확인하는 명령어이다.
UID는 사용자의 아이디를 나타내며 0 ~ 32767 사이의 숫자로 나타내고 0은 슈퍼(root) 유저를 나타낸다.</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/519f3491-11e2-4ae4-b22f-71efd341f162/image.png" /></p>
<table>
<thead>
<tr>
<th>UID</th>
<th>의미</th>
</tr>
</thead>
<tbody><tr>
<td>0</td>
<td>root</td>
</tr>
<tr>
<td>1 ~ 99</td>
<td>predefined</td>
</tr>
<tr>
<td>100 ~ 999</td>
<td>administrative and System accounts</td>
</tr>
<tr>
<td>1000 ~</td>
<td>user</td>
</tr>
</tbody></table>
<h3 id="접근-권한-간단-정리">접근 권한 간단 정리</h3>
<blockquote>
<p>💡 접근 권한은 크게 유저 본인, GROUP, OTHER에 대해 설정할 수 있다.</p>
<p>맨 앞 d를 제외하고 차례대로 3단어씩 소유자의 권한, 소유주가 속한 그룹의 권한, 그 외 모든 이들의 권한이다.</p>
<ul>
<li>r : read 권한(파일 리스트 취득 가능)</li>
<li>w : write 권한(디렉토리 하위 파일 및 디렉토리에 작성 및 삭제 가능)</li>
<li>x : executable 권한(디렉토리로 이동 가능)</li>
</ul>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/bf5a7cea-040a-4a7a-a692-fb9c0334118c/image.png" /></p>
<ul>
<li><strong>drwxr-xr-x</strong><ul>
<li><strong>1필드</strong><ul>
<li><ul>
<li>: 파일</li>
</ul>
</li>
<li>d : 디렉토리</li>
<li>l : 다른 파일을 가리키는 링크</li>
<li>p : pipe. 두 개의 프로그램을 연결하는 파이프 파일</li>
<li>b : block device. 블럭 단위로 하드웨어와 반응하는 파일</li>
<li>c : character device. 스트림 단위로 하드웨어와 반응하는 파일</li>
</ul>
</li>
<li><strong>2~4필드</strong><ul>
<li>소유주(User) 권한</li>
</ul>
</li>
<li><strong>5~7필드</strong><ul>
<li>그룹(Group) 권한</li>
</ul>
</li>
<li><strong>8~10필드</strong><ul>
<li>나머지(Others) 권한</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="권한-대여">권한 대여</h3>
<ul>
<li>su [-] [username]</li>
</ul>
<blockquote>
<p>💡 사용자의 권한을 대여하는 명령어이다. (즉, 사용자로 로그인한 효과를 나타낸다.)</p>
<ul>
<li>su ohgiraffers : ohgiraffers의 ID로 로그인(해당 유저의 PW 입력해야함)</li>
<li>su - ohgiraffers : ohgiraffers의 ID로 로그인, ohgiraffers 계정의 home 디렉토리도 사용</li>
<li>sudo su - : 우분투에서도 root로 로그인(위험하니 자제할 것)</li>
<li>권한 대여 종료는 exit로 할 수 있다.</li>
</ul>
</blockquote>
<h2 id="계정-관련-명령어">계정 관련 명령어</h2>
<h3 id="adduser">adduser</h3>
<blockquote>
<p>💡 사용자 계정을 추가하는 명령어이다.
패스워드는 필수로 입력한 후 이후 정보는 enter로 skip이 가능하다.</p>
</blockquote>
<pre><code class="language-bash">$ sudo adduser [OPTIONS] {username}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ede40f78-e5ac-4b16-842e-ad837d9ac388/image.png" /></p>
<h3 id="userdel">userdel</h3>
<blockquote>
<p>💡 사용자 계정을 삭제하는 명령어이다.</p>
</blockquote>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-f</td>
<td>사용자라 로그인 중이라도 강제 삭제</td>
</tr>
<tr>
<td>-r</td>
<td>사용자와 함께 사용자 디렉토리, 사용자 메일함도 삭제</td>
</tr>
</tbody></table>
<pre><code class="language-bash">$ sudo userdel [OPTIONS] {username}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/22073e96-fcf3-4169-b932-6f930ce0fbd9/image.png" /></p>
<h2 id="그룹-관련-명령어">그룹 관련 명령어</h2>
<h3 id="groupadd">groupadd</h3>
<blockquote>
<p>💡 그룹을 추가하는 명령어이다.
그룹에는 보통 GID가 부여되며 기존의 마지막 그룹 번호에 +1이 추가되어 생성된다.</p>
</blockquote>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-g</td>
<td>그룹번호를 지정할 수 있다.(기존 그룹번호와 중복 불가)</td>
</tr>
</tbody></table>
<pre><code class="language-bash">$ sudo groupadd [OPTIONS] [GROUP NUMBER] {groupname}</code></pre>
<h3 id="groupdel">groupdel</h3>
<blockquote>
<p>💡 그룹을 삭제하는 명령어이다.</p>
</blockquote>
<pre><code class="language-bash">$ sudo groupdel {groupname}</code></pre>
<h3 id="유용한-group-관련-명령어">유용한 Group 관련 명령어</h3>
<table>
<thead>
<tr>
<th>명령어</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>cat /etc/group</td>
<td>GID와 함께 Group List 조회</td>
</tr>
<tr>
<td>groups</td>
<td>GID 제외하고 Group List 조회</td>
</tr>
<tr>
<td>gpasswd -a {username} {groupname}</td>
<td>특정 유저를 특정 그룹에 추가</td>
</tr>
<tr>
<td>gpasswd -A {username} {groupname}</td>
<td>그룹 멤버 중 특정 유저를 관리자로 설정</td>
</tr>
<tr>
<td>gpasswd -d {username} {groupname}</td>
<td>유저를 특정 그룹에서 제거</td>
</tr>
<tr>
<td>gpasswd {groupname}</td>
<td>특정 그룹의 패스워드 설정/변경</td>
</tr>
<tr>
<td>gpasswd -r {groupname}</td>
<td>특정 그룹의 패스워드 제거</td>
</tr>
<tr>
<td>useradd -G {groupname} {username}</td>
<td>계정 생성 시 그룹에 추가</td>
</tr>
</tbody></table>
<h2 id="파일-관한-관련-명령어">파일 관한 관련 명령어</h2>
<h3 id="chmod">chmod</h3>
<blockquote>
<p>💡 파일 또는 디렉토리의 권한을 변경하는 명령어이다. 권한 변경은 슈퍼 유저나 파일/디렉토리 소유주만 가능하다.</p>
</blockquote>
<ul>
<li>mode 종류(누구에게, 어떻게, 무엇을)</li>
</ul>
<table>
<thead>
<tr>
<th>구분</th>
<th>기호</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>사용자</td>
<td>u</td>
<td>user의 약자, 소유자</td>
</tr>
<tr>
<td>사용자</td>
<td>g</td>
<td>group의 약자, 그룹</td>
</tr>
<tr>
<td>사용자</td>
<td>o</td>
<td>other의 약자, 그 외</td>
</tr>
<tr>
<td>사용자</td>
<td>a</td>
<td>all의 약자, 모든 사용자</td>
</tr>
<tr>
<td>사용자</td>
<td></td>
<td>문자가 없으면 a와 동일하게 적용</td>
</tr>
<tr>
<td>수행할 연산</td>
<td>+</td>
<td>권한 추가</td>
</tr>
<tr>
<td>수행할 연산</td>
<td>-</td>
<td>권한 제거</td>
</tr>
<tr>
<td>수행할 연산</td>
<td>=</td>
<td>권한 부여</td>
</tr>
<tr>
<td>접근권한</td>
<td>r</td>
<td>읽기</td>
</tr>
<tr>
<td>접근권한</td>
<td>w</td>
<td>쓰기</td>
</tr>
<tr>
<td>접근권한</td>
<td>x</td>
<td>실행</td>
</tr>
</tbody></table>
<pre><code class="language-bash">$ chmod [OPTIONS] [MODE] {file/directory}</code></pre>
<ul>
<li>예시<ul>
<li>ug+r : 소유자와 그룹에 읽기 권한 추가</li>
<li>+rw : 모든 사용자에게 읽기/쓰기 권한 추가</li>
<li>u=rwx : 소유자에게 읽기, 쓰기, 실행 권한 부여</li>
<li>u-x : 소유주에게 실행 권한 제거</li>
<li>g+x,o+x : 그룹과 기타 사용자에게 실행권한 추가</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e779cfca-b66a-4315-9953-1f18872e7b88/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a1ac068d-6f47-4ea6-98b4-ce91aae187a1/image.png" /></p>
<h3 id="chown">chown</h3>
<blockquote>
<p>💡 파일 또는 디렉토리의 소유권을 변경하는 명령어이다.</p>
<ul>
<li>-R 옵션: 하위 디렉토리까지 모든 소유권 적용</li>
</ul>
</blockquote>
<pre><code class="language-bash">$ sudo chown [OPTIONS] {바꾸고 싶은 username}:{바꾸고 싶은 groupname} {소유권을 변경하고자 하는 파일/디렉토리}</code></pre>
<ul>
<li><p>특정 파일 소유권 변경</p>
<p>  <img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3298a46f-6b30-4097-8019-0058e0b7e864/image.png" /></p>
</li>
<li><p>하위 모든 파일/디렉토리 소유권 변경</p>
<p>  <img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a367c135-2e1e-47a6-8ef1-cfc256b252eb/image.png" /></p>
</li>
</ul>