<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6396e9b4-b3e0-4c3b-a2e0-271fd0483941/image.png" /></p>
<h1 id="운영체제">운영체제</h1>
<blockquote>
<p>💡 컴퓨터 시스템의 자원들을 효율적으로 관리하며, 사용자가 컴퓨터를 편리하고 효과적으로 사용할 수 있도록 환경을 제공하는 여러 프로그램들의 모임이다.</p>
<p>운영체제는 컴퓨터 하드웨어와 사용자 간의 인터페이스로서 동작하는 시스템 소프트웨어의 일종으로, 다른 응용프로그램에 유용한 작업을 할 수 있도록 환경을 제공해 준다.</p>
</blockquote>
<blockquote>
<p><strong>프로그램</strong>
: 하드디스크와 같은 보조기억장치에서 아무런 동작을 하지 않는 상태</p>
<blockquote>
<p><strong>프로세스</strong>
: RAM과 같은 메인 메모리(주기억장치)에서 실행중인 프로그램(program in execution) </p>
</blockquote>
</blockquote>
<h2 id="운영체제의-구조">운영체제의 구조</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/534ebe6c-c43e-465b-b207-a036f3525653/image.png" /></p>
<blockquote>
<p>💡 운영체제는 크게는 <strong>커널</strong>과 <strong>인터페이스</strong>로 나뉜다.</p>
</blockquote>
<ul>
<li><strong>인터페이스</strong></li>
</ul>
<blockquote>
<p>💡 컴퓨터에 대한 많은 지식을 가지지 않은 사용자가 시스템 호출을 직접 이용하지 않아도 간단한 명령 혹은 조작을 해서 시스템 호출을 통해 운영체제 커널 기능을 이용할 수 있도록 만든 소프트웨어이다.
그래픽 기반 사용자 인터페이스(GUI)와 명령줄 기반 사용자 인터페이스(CLI)로 나누어 진다.</p>
</blockquote>
<ul>
<li><strong>시스템 호출</strong></li>
</ul>
<blockquote>
<p>💡 커널이 자신을 보호하기 위한 인터페이스이다.
시스템 관련 서비스를 모아 함수 형태로 제공하며 사용자나 응용 프로그램으로부터 컴퓨터의 자원을 보호하기 위해 자원에 직접 접근하는 것을 차단했다.</p>
</blockquote>
<ul>
<li><strong>커널</strong></li>
</ul>
<blockquote>
<p>💡 하드웨어와 소프트웨어 컴포넌트 사이의 중요한 인터페이스 역할을 하고 있으며 아래와 같은 여러 주요 기능을 담당한다.
운영체제의 가장 낮은 수준에서 실행되어 운영 체제의 다른 모든 부분들이 커널을 통해 하드웨어와 직/간접적으로 상호작용한다.
리눅스, 윈도우, macOS 등 다양한 운영체제가 각각의 고유한 커널을 가지고 있으며 운영체제의 특성과 성능을 결정 짓게 된다.(대부분의 운영체제는 계층형 구조 커널로 되어 있다.)</p>
</blockquote>
<pre><code>1. **리소스 관리**
    : CPU, 메모리, 디스크 공간 등을 관리한다.
2. **프로세스 관리**
    : 다양한 프로세스들 사이에 CPU 시간을 분배하고 프로세스의 생성과 종료를 관리한다.
3. **메모리 관리**
    : 프로그램들이 필요로 하는 메모리를 할당하거나 해제하여 메모리 누수나 오버플로우 같은 문제를 방지한다.
4. **장치 드라이버와의 인터페이스**
    : 키보드, 마우스, 프린터, 디스플레이와 같은 하드웨어 장치를 효과적으로 제어할 수 있다.</code></pre><ul>
<li><strong>드라이버</strong></li>
</ul>
<blockquote>
<p>💡 커널과 하드웨어의 인터페이스를 담당한다.
키보드와 마우스 같은 일반적이고 복잡하지 않은 디바이스 드라이버는 커널에 포함되어 있지만 프린터나 그래픽 카드와 같은 크기가 크고 복잡한 디바이스 드라이버는 사용자가 직접 설치해야 한다.</p>
</blockquote>
<h1 id="리눅스">리눅스</h1>
<blockquote>
<p>💡 오픈 소스 운영 체제로 컴퓨터 하드웨어와 소프트웨어 리소스의 관리 및 사용자와 프로그램 간의 인터페이스를 제공한다. 
안정성, 보안성, 유연성 측면에서 우수하여 웹서버, 애플리케이션 서버, 데이터베이스 서버와 같은 다양한 용도로 사용된다.</p>
</blockquote>
<ul>
<li>리눅스를 다양한 서버로 사용하는 이유</li>
</ul>
<p><strong>1. 무료 오픈 소스</strong>
: 리눅스 배포판은 대부분 무료이며 오픈 소스이기 때문에 사용자가 필요에 따라 소스 코드를 수정하고 배포할 수 있다.</p>
<p><strong>2. 안정성 및 신뢰성</strong>
: 매우 안정적인 운영체제로 오랜 시간 동안 재부팅 없이 실행 될 수 있다. 이는 서버 운영에 있어 중요한 요소이다.</p>
<p><strong>3. 보안</strong>
: 기본적으로 보안이 강화된 설계를 가지고 있고 정기적인 업데이트와 커뮤니티의 지원을 통해 높은 보안성이 지속적으로 유지된다.</p>
<p><strong>4. 성능</strong>
: 자원을 효율적으로 사용하여 시스템의 성능을 최적화 한다. 이 역시 서버 운영에서 중요하다.</p>
<p><strong>5. 다양한 배포판</strong>
: 다양한 배포판이 있어 서버 용도에 맞게 선택할 수 있다.
(Ubuntu, CentOS, Debian 등)</p>
<h2 id="리눅스의-역사">리눅스의 역사</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e36ad711-129b-4fad-b2c4-3411dd6d1d91/image.png" /></p>
<blockquote>
<p>💡 1991년, 핀란드 헬싱키 대학교의 컴퓨터과학 학생이었던 리누스 토발즈(Linux Tovalds)에 의해 처음 개발되었다.</p>
<p>처음에는 MINIX(작은 유닉스 시스템)를 사용하였는데 제한적인 시스템에 실망해 자신만의 운영체제를 만들기로 결정하여 만들었던 것으로 알려져 있다.</p>
<p>공개 이후 많은 개발자들이 참여하면서 안정성과 효율성이 뛰어난 리눅스 커널을 갖추게 되었으며 이후 현재까지도 무료 오픈소스로써 전세계 수많은 개발자들이 수정 및 기능 추가를 해 오고 있다.</p>
<p>유닉스 클론(clone)이었던 리눅스는 리눅스 커널을 기반으로 다양한 배포판이 등장하였고 다양한 대기업의 투자 및 서버, 데스크톱, 모바일 장치, 임베디드 시스템 등 다양한 분야에서 사용되고 있다.</p>
</blockquote>
<blockquote>
<p>GNU 프로젝트
: 컴퓨터 프로그램에 대한 저작권을 없애는 것으로 모두가 공유할 수 있는 소프트웨어를 제작하고 프로그램의 복제, 변경, 소스 코드의 제한을 철폐하는 것에 진정한 가치를 둔다.</p>
<p>자유 소프트웨어 재단(FSF, Free Software Foundation)의 리처드 스톨만(Richard Stallman)이 주축이 되어 설립된 재단에서 GNU 프로젝트를 지원하고 모든 프로그램의 라이센스를 GPL 라이선스로 규정하여 자유 소프트웨어 개념을 도입했다.</p>
<blockquote>
<p>자유 소프트웨어
: 소스 코드를 공개, 사용, 수정, 재배포의 자유, 수정한 소프트웨어의 판매 자유를 말한다.</p>
</blockquote>
</blockquote>
<h2 id="리눅스의-종류">리눅스의 종류</h2>
<blockquote>
<p>💡 리눅스는 다양한 배포판을 통해 제공되며 특정한 목적, 사용자, 기능에 맞춰 설계되어 있다.</p>
</blockquote>
<ul>
<li><p><strong>리눅스의 종류 및 설명</strong></p>
<p>  <a href="https://w3techs.com/technologies/history_details/os-linux/all/q">Historical quarterly trends in the usage statistics of Linux subcategories, July 2024</a></p>
<p>  <img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/bae293dc-b8fc-470f-8d06-58169e630304/image.png" /></p>
</li>
</ul>
<pre><code>| 계열 | 종류 | 설명 |
| --- | --- | --- |
| Debian 계열 | Ubuntu | 가장 인기있는 데스크탑 리눅스 배포판 중 하나로, 사용자 친화적이며 초보자에게 적합하다. |
| Debian 계열 | Debian | 안정성과 보안에 중점을 둔 배포판으로, 다양한 아키텍처를 지원한다. |
| Debian 계열 | Mint  | Ubuntu를 기반으로 하며, 향상된 사용자 경험을 제공한다. 초보자에게 적합하다. |
| Redhat 계열 | Fedora | 최신 기술을 빠르게 채택하는 것으로 알려져 있으며, 개발자와 고급 사용자에게 인기가 있다. |
| Redhat 계열 | CentOS | 엔터프라이즈 수준의 안정성을 제공하는 서버용 배포판으로, 무료 대체제로 Red Hat Enterprise Linux(RHEL)와 호환된다. |
| Slackware 계열 | openSUSE | 안정적이고 다기능적인 배포판으로, 서버와 데스크톱 양쪽에서 모두 사용한다. |</code></pre>