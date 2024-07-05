<h1 id="gui--cli">GUI &amp; CLI</h1>
<h2 id="guigraphical-user-interface">GUI(Graphical User Interface)</h2>
<blockquote>
<p>💡 그래픽 기반 사용자 인터페이스를 말한다.
사용자가 컴퓨터 애플리케이션을 조작하기 위해 마우스, 키보드, 터치 스크린 등을 사용하는 방식이다.</p>
<p>예시로는 Windows, macOS, Linux의 GNOME 또는 KDE 환경 등이 있다.</p>
</blockquote>
<h3 id="gui-특징">GUI 특징</h3>
<ul>
<li>GUI는 그래픽 요소를 사용하여 사용자에게 정보를 시각적으로 전달하며, 사용자가 버튼, 아이콘, 창, 메뉴 등과 상호 작용하도록 도와준다.</li>
<li>GUI는 일반적으로 비숙련자에게 더 쉽게 접근 가능하며 시각적으로 직관적이라 대부분의 사용자에게 친숙하다.</li>
</ul>
<h2 id="clicommand-line-interface">CLI(Command Line Interface)</h2>
<blockquote>
<p>💡 명령 줄 인터페이스를 말한다.
사용자가 명령어를 입력하여 컴퓨터에 지시하는 방식이다.</p>
<p>예시로는 Window의 Command Prompt, macOS 및 Linux의 터미널, Git 명령어, Phython 인터프리터 등이 있다.</p>
</blockquote>
<h3 id="cli-특징">CLI 특징</h3>
<ul>
<li>CLI는 텍스트 기반으로 동작하며, 사용자가 명령어와 옵션을 직접 입력하여 작업을 수행한다.</li>
<li>CLI는 숙련된 사용자나 개발자에게 유용하며, 자동화 및 스크립팅 작업에 많이 사용된다.</li>
</ul>
<h1 id="쉘shell">쉘(Shell)</h1>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6c8ac8b1-3456-42b6-9466-c37b7f7f9e84/image.png" /></p>
<blockquote>
<p>💡 사용자와 운영체제 간의 중간 계층을 형성하는 프로그램 또는 환경을 말한다.
사용자가 키보드와 같은 입력 장치를 통해 명령어를 입력하면 쉘이 해당 명령어를 해석하고 커널에 전달한다.
(커널의 인터페이스에 해당한다.)
(커널을 감싸는 껍데기 역할을 하여 조개 껍질에 해당하는 shell이라는 이름이 붙여졌다.)</p>
<p>쉘은 명령어 실행, 파일 및 디렉토리 관리, 환경 변수 설정, 프로세스 관리 등 다양한 작업을 수행할 수 있다.</p>
<blockquote>
<p><strong>커널(Kernel)</strong>
: 운영체제의 핵심 부분(본체)으로 하드웨어와 소프트웨어 간의 통신을 관리하고 시스템 자원을 효율적으로 관리한다. 실질적으로 하드웨어 자원인 CPU나 메모리, 디스크, 네트워크 장치에 접근하고 제어하는 역할을 한다.
커널은 보안과 안정성 및 성능 유지에 중요한 역할을 한다.</p>
</blockquote>
</blockquote>
<h2 id="쉘의-프롬프트">쉘의 프롬프트</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/eb52882f-0add-4b70-847e-a67ffc33bbf6/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/69e12d74-2106-4339-b7af-8d7eaf06bb16/image.png" /></p>
<blockquote>
<p>💡 ‘@’를 기준으로 앞(ohgirafffers)은 사용자 이름, 뒤(ohgiraffers-VirtualBox)는 호스트 이름에 해당한다.</p>
<p>일반 사용자의 프롬프트는 $으로 끝나고 슈퍼 사용자(root)는 #으로 끝나게 되며 리눅스 공식 문서 뿐 아니라 모든 책에서도 일반사용자는 $, 슈퍼사용자는 #로 ‘<strong>프롬프트</strong>’를 표시한다.</p>
<p>$나 # 이후의 명령어 입력 부분은 ‘<strong>커맨드 라인</strong>’이라고 한다.</p>
</blockquote>
<ul>
<li><p><strong>명령어에서 커서 움직이기</strong></p>
<table>
<thead>
<tr>
<th>위치</th>
<th>단축키</th>
</tr>
</thead>
<tbody><tr>
<td>한칸 앞</td>
<td>ctrl + b</td>
</tr>
<tr>
<td>한칸 뒤</td>
<td>ctrl + f</td>
</tr>
<tr>
<td>맨 처음</td>
<td>ctrl + a</td>
</tr>
<tr>
<td>맨 끝</td>
<td>ctrl + e</td>
</tr>
</tbody></table>
</li>
<li><p><strong>로그아웃</strong></p>
</li>
</ul>
<blockquote>
<p>💡 로그인의 반대 개념으로 작업이 끝났는데도 로그아웃을 하지 않으면 컴퓨터 자원이 불필요하게 사용되며 누군가가 몰래 계정을 탈취 할 수 있다.</p>
</blockquote>
<pre><code class="language-bash">## 쉘이 종료되는 명령어이자 자동적으로 로그아웃 된다.
$ exit</code></pre>
<ul>
<li><strong>셧다운</strong></li>
</ul>
<blockquote>
<p>💡 컴퓨터의 전원을 끄려고 OS를 완전히 정지시키는 것
(실무에서는 로그아웃은 한 상태로 OS는 몇 년간도 켜 놓기 때문에 실제로 쓸 일은 많지 않다.)</p>
</blockquote>
<pre><code class="language-bash">## 슈퍼 사용자로 변환하기($ -&gt; #)
## /root 경로의 디렉토리
$ sudo su

## 현재 사용자의 홈 디렉토리
$ sudo -s  

## 셧다운 실행
# shutdown -h now

## 재부팅(reboot) 실행
# shutdown -r now

## 일반 사용자로 변환하기
## 현재 사용자를 로그아웃 하지 않은 상태에서 다른 사용자의 계정으로 전환
# su &lt;계정명&gt;

## 완전히 다른 사용자 계정으로 전환하고 전환한 사용자의 환경설정을 불러온다.(logout 가능)
# su - &lt;계정명&gt;</code></pre>
<ul>
<li>‘su 계정명’과 ‘su - 계정명’의 차이</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/85030161-bea9-4139-9c50-d0a3da55282b/image.png" /></p>
<h2 id="쉘의-종류">쉘의 종류</h2>
<ul>
<li><p><strong>로그인 쉘</strong></p>
<ul>
<li><p>로그인과 동시에 사용자의 입력을 대기하는 쉘을 로그인 쉘이라고 부른다.</p>
</li>
<li><p>로그인 쉘 확인하기</p>
<pre><code class="language-bash">  $ echo $SHELL</code></pre>
<p>  <img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/77743d4a-373d-4a4f-9d63-6c630ee66399/image.png" /></p>
</li>
<li><p>변경 가능한 일반 쉘들 확인하기</p>
<pre><code class="language-bash">  $ cat /etc/shells</code></pre>
<p>  <img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6aca7add-d7f3-4fde-860b-19b71c5fcb9c/image.png" /></p>
</li>
</ul>
</li>
</ul>
<ul>
<li><p><strong>쉘의 종류</strong></p>
<table>
<thead>
<tr>
<th>쉘의 종류</th>
<th>실행명령</th>
<th>운영체제</th>
<th>특징</th>
</tr>
</thead>
<tbody><tr>
<td>sh (Bourne Shell)</td>
<td>유닉스 계열</td>
<td>유닉스 시스템의 초기 쉘, 기본적인 스크립팅 및 명령 실행 기능</td>
<td>sh</td>
</tr>
<tr>
<td>csh (C Shell)</td>
<td>유닉스 계열</td>
<td>C 프로그래밍 언어와 유사한 문법 구조, 사용자 친화적인 기능</td>
<td>csh</td>
</tr>
<tr>
<td>bash (Bourne-Again Shell)</td>
<td>유닉스 계열</td>
<td>가장 일반적으로 사용되는 쉘, GNU 프로젝트의 일부, 고급 스크립팅 기능</td>
<td>bash</td>
</tr>
<tr>
<td>tcsh (TENEX C Shell)</td>
<td>유닉스 계열</td>
<td>C Shell의 확장, 향상된 사용자 인터페이스 및 프로그래밍 기능</td>
<td>tcsh</td>
</tr>
<tr>
<td>zsh (Z Shell)</td>
<td>유닉스 계열</td>
<td>Bash의 확장 기능을 포함, 테마와 플러그인 지원으로 맞춤화 가능</td>
<td>zsh</td>
</tr>
</tbody></table>
</li>
<li><p>일시적으로 일반 쉘(비로그인 쉘) 바꾸기</p>
</li>
</ul>
<pre><code class="language-bash">## sh 쉘로 바꾸기
$ sh

## sh 쉘에서 bash 쉘 실행
$ bash

## bash -&gt; sh -&gt; bash쉘로 기동한 상태에서 다시 원래의 로그인 쉘로 돌아오려면 exit를 두번 실행한다.
$ exit
$ exit</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/4d55f95b-3c1e-4e15-8e62-4b975a7a34d0/image.png" /></p>
<h2 id="터미널">터미널</h2>
<blockquote>
<p>💡 터미널은 하드웨어 또는 소프트웨어 기반의 입력 및 출력 장치이다.
원래는 컴퓨터에 직접 연결된 입/출력 장치를 가르켰으나 현대에는 소프트웨어 기반의 터미널 에뮬레이터를 의미한다.
사용자는 터미널을 통해 쉘에 접근하고 명령을 입력할 수 있다.</p>
<p>쉘과 달리 명령 해석 기능은 없이 사용자의 입력을 컴퓨터에 전달하고 컴퓨터의 출력을 사용자에게 표시만 한다.</p>
<p>PuTTY, GNOME Terminal, macOS의 Terminal 앱 등이 있다.</p>
</blockquote>
<h1 id="우분투-개발-환경-세팅">우분투 개발 환경 세팅</h1>
<h2 id="apt">apt</h2>
<blockquote>
<p>💡 Debian 시스템에 포함된 핵심 도구들의 집합체로 우분투에서는 패키지를 관리하는 툴로 사용된다. 주로 apt-get과 apt-cache를 사용해 왔다.
요즘은 두 명령어를 통합하여 apt로 사용한다. apt는 apt-get/apt-cache를 완전히 통합하는 툴은 아니다. 사용자 편의성을 위해 주요 기능만 통합한 툴이다.</p>
<p>하지만, 전문가가 아니라면 apt로도 충분하다.</p>
</blockquote>
<h3 id="apt-install">apt install</h3>
<blockquote>
<p>💡 패키지 설치 하는 명령어이다. 패키지 명을 여러 개 지정해서 한번에 설치도 가능하다.
패키지명 사이사이는 공백으로 띄어주어야 한다.</p>
</blockquote>
<pre><code class="language-bash">$ sudo apt install &lt;package_name&gt; [&lt;package_name&gt;]</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c4df7dff-ddc8-4ce7-b14b-be81dd862e22/image.png" /></p>
<h3 id="apt-remove">apt remove</h3>
<blockquote>
<p>💡 패키지를 제거하는 명령이다.
remove 명령은 저장한 패키지만을 제거한다.</p>
</blockquote>
<pre><code class="language-bash">$ sudo apt remove &lt;package_name&gt;</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/19ef5104-9ead-4ca3-a9e1-443df896bb64/image.png" /></p>
<h3 id="apt-purge">apt purge</h3>
<blockquote>
<p>💡 패키지와 설정파일까지 제거하는 명령어이다.
purge 명령은 remove와 달리 패키지와 설정 파일 모두 제거하는 명령어다.</p>
</blockquote>
<pre><code class="language-bash">$ sudo apt purge &lt;package_name&gt;</code></pre>
<h3 id="apt-autoremove">apt autoremove</h3>
<blockquote>
<p>💡 사용하지 않는 패키지 제거하는 명령어이다. 
해당 명령을 사용하면 현재 사용되지 않는 패키지를 제거한다.</p>
</blockquote>
<pre><code class="language-bash">$ sudo apt autoremove</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0f524a97-4306-4314-b7d8-98b402663303/image.png" /></p>
<h3 id="apt-search">apt search</h3>
<blockquote>
<p>💡 패키지 검색할 수 있는 명령어이다.
apt 툴을 이용하여 설치할 수 있는 패키지 검색 명령이다.</p>
</blockquote>
<pre><code class="language-bash">$ apt search &lt;package_name&gt;</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d98756fc-0d13-4c92-adfc-869d4535075e/image.png" /></p>
<h3 id="apt-list">apt list</h3>
<blockquote>
<p>💡 패키지 목록 조회하는 명령어이다.
apt list는 레포지토리에 등록된 패키지 목록을 조회하는 명령어다.</p>
</blockquote>
<pre><code class="language-bash">$ apt list</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/93bc5005-7ebc-4b6c-85cc-632572890173/image.png" /></p>
<h3 id="apt-update">apt update</h3>
<blockquote>
<p>💡 현재 사용 가능한 패키지 리스트를 업데이트 해주는 명령어이다.</p>
<p>우분투의 /etc/apt/sources.list 파일이나 /etc/apt/sources.list.d 디렉토리에 별도로 구성된 파일에 구성되어 활성화된 소스들의 최신 패키지 정보를 다운로드하는데에 사용한다.</p>
</blockquote>
<pre><code class="language-bash">$ sudo apt update</code></pre>
<h2 id="vim-편집기-설치">Vim 편집기 설치</h2>
<pre><code class="language-bash">## apt 명령을 이용해 vim 설치를 진행한다.
$ sudo apt install vim</code></pre>
<p><a href="https://iamfreeman.tistory.com/entry/vi-vim-%ED%8E%B8%EC%A7%91%EA%B8%B0-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%A0%95%EB%A6%AC-%EB%8B%A8%EC%B6%95%ED%82%A4-%EB%AA%A8%EC%9D%8C-%EB%AA%A9%EB%A1%9D">vi /vim 편집기 명령어 정리 (단축키 모음 / 목록)</a></p>