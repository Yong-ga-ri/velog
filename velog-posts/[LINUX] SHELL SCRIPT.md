<h1 id="텍스트-처리-명령어">텍스트 처리 명령어</h1>
<ul>
<li>텍스트 처리 명령어를 위해 아래 두 파일(number.txt와 fruit.txt)과 같은 내용이 들어 있도록 파일을 생성 후 수정한다.</li>
</ul>
<pre><code class="language-bash">$ mkdir sortDir

$ touch ./sortDir/number.txt

$ touch sortDir/fruit.txt

$ cd sortDir

$ vim number.txt

$ vim fruit.txt</code></pre>
<ul>
<li>number.txt</li>
</ul>
<pre><code>9
4
2
7
6
5
10
20
11
21</code></pre><ul>
<li>fruit.txt</li>
</ul>
<pre><code>mango banana pineapple
kiwi
orange
strawberry grape
watermelon
cherry
pear
peach
grape kiwi
banana
banana
mango
grape
grape
mango
cherry</code></pre><h2 id="wc">wc</h2>
<blockquote>
<p>💡 wc 명령어를 통해 파일의 행 수, 단어 수, 바이트 수를 출력할 수 있다.</p>
</blockquote>
<pre><code class="language-bash">## 행수, 단어수, 바이트 수, 파일 이름
$ wc fruit.txt

## 행만 표시
$ wc -l fruit.txt

## 단어만 표시
$ wc -w fruit.txt

## 바이트 수만 표시
$ wc -c fruit.txt</code></pre>
<ul>
<li>파이프라인을 통해 루트 디렉토리의 파일과 디렉토리가 총 몇 개인지도 알 수 있다.</li>
</ul>
<pre><code class="language-bash">## 루트 디렉토리
$ ls / | wc -l</code></pre>
<blockquote>
<p><strong>파이프라인(Pipeline)</strong>
: ‘|’ 기호를 사용하여 구성하며 왼쪽 명령어의 출력을 오른쪽 명령어의 입력으로 전달한다.
다양한 명령어를 조합하여 복잡한 작업을 수행하기 위한 데이터 처리 및 변환에 사용된다.</p>
</blockquote>
<h2 id="sort">sort</h2>
<h3 id="숫자-값으로-정렬">숫자 값으로 정렬</h3>
<blockquote>
<p>💡 -n 옵션을 추가하면 내용이 문자열이 아닌 숫자로 판단한다.</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d28fa744-fc63-4986-85c5-6fc53aa22e7e/image.png" /></p>
<h3 id="역순으로-정렬">역순으로 정렬</h3>
<blockquote>
<p>💡 -r 옵션을 추가하면 역순으로 정렬된다.</p>
</blockquote>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3731fc56-4162-4006-a503-c95511454ede/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c220c767-8d92-4dc7-8221-7a933d61ec61/image.png" /></p>
<h2 id="head와-tail">head와 tail</h2>
<blockquote>
<p>💡 head 명령어를 사용하면 파일의 처음 부분을, tail 명령어를 사용하면 파일의 마지막 부분을 출력할 수 있다.</p>
</blockquote>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-n number</td>
<td>number 수 만큼 출력한다.</td>
</tr>
<tr>
<td>-c number</td>
<td>number 바이트 만큼 출력한다.</td>
</tr>
<tr>
<td>-q</td>
<td>여러 개의 파일을 출력할 때 제목을 출력하지 않는다.</td>
</tr>
<tr>
<td>-f</td>
<td>내용이 변경될 때마다 실시간으로 출력해주며 로그파일 모니터링 등에 활용된다.(tail만 해당)</td>
</tr>
</tbody></table>
<pre><code class="language-bash">## 마지막 4행만 보여준다.
$ tail -n 4 /etc/passwd
$ cat /etc/passwd | tail -n 4

## 처음 4행만 보여준다.
$ head -n 4 /etc/passwd
$ cat /etc/passwd | head -n 4</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/34842e04-dd8b-4f00-be64-e8a82898b601/image.png" /></p>
<h2 id="uniq-명령어">uniq 명령어</h2>
<blockquote>
<p>💡 같은 내용이 연속되어 있는 경우에만 중복을 제거한다.</p>
</blockquote>
<pre><code class="language-bash">## 연속된 중복 데이터 제거
$ uniq fruit.txt

## 연속된 중복 데이터 제거 후 정렬(연속되지 않은 중복은 제거 되지 않음을 확인)
$ uniq fruit.txt | sort</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/7784b77f-bb28-44d6-8b2d-8ab558e50fa6/image.png" /></p>
<blockquote>
<p>💡 -c 옵션을 주어 중복 데이터 개수를 셀 수도 있다.</p>
</blockquote>
<pre><code class="language-bash">## 연속된 중복 데이터 카운팅
$ uniq -c fruit.txt

## 정렬 후 연속된 중복 데이터 카운팅(정렬 후에 중복을 카운팅하면 중복 값을 모두 확인할 수 있다.)
$ sort fruit.txt | uniq -c</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/41532fc9-3585-4aa4-a715-2f7f4498311e/image.png" /></p>
<h2 id="diff-명령어">diff 명령어</h2>
<blockquote>
<p>💡 diff 명령어를 통해 두 파일의 차이점을 출력할 수 있다.</p>
</blockquote>
<pre><code class="language-bash">$ diff [옵션] &lt;비교 파일 1&gt; &lt;비교 파일 2&gt;</code></pre>
<ul>
<li>다음 명령어를 실행하고 아래 파일과 같은 내용이 들어 있도록 파일을 생성하고 수정한다.</li>
</ul>
<pre><code class="language-bash">$ touch fruit2.txt

$ vim fruit2.txt</code></pre>
<ul>
<li><p>fruit2.txt</p>
<pre><code>  mango banana pineapple
  kiwi
  orange
  strawberry grape
  watermelon
  cherry
  pear
  peach
  grape kiwi
  banana
  banana
  chocolate
  candy
  marshmallow</code></pre></li>
</ul>
<ul>
<li>diff 명령어를 통해 fruit.txt와 fruit2.txt의 차이를 확인한다.</li>
</ul>
<pre><code class="language-bash">## fruit.txt와 fruit2.txt의 차이를 비교한다.
$ diff fruit.txt fruit2.txt

## 결과는 fruit.txt의 12번째 줄부터 16번째 행이 fruit2.txt의 12번째 줄부터 14번째 줄로 변경되었음을 나타낸다.</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/18ffbdfc-f501-4d65-80b3-24a896bdcb87/image.png" /></p>
<h1 id="쉘-스크립트-개요">쉘 스크립트 개요</h1>
<blockquote>
<p>💡 리눅스를 사용하다 보면 일련의 명령어를 반복적으로 실행해야 될 때가 있다. 이 때마다 길고 복잡한 커맨드 라인을 손으로 직접 입력하는 것은 번거롭기 때문에 미리 파일에 입력해 놓고 해당 파일을 쉘이 실행하도록 할 수 있다.</p>
<p>쉘에서 실행될 커맨드 라인을 입력해 놓은 파일을 쉘 스크립트라고 한다. 단순히 명령어 나열 뿐 아니라 복잡한 조건문이나 반복문과 같은 제어 구조도 활용할 수 있다.</p>
</blockquote>
<h2 id="쉘-스크립트의-장점">쉘 스크립트의 장점</h2>
<ul>
<li>쉘 스크립트를 작성해 두면 쉽게 재사용할 수 있다.</li>
<li>다른 사람에게 쉘 스크립트를 공유할 수 있다.</li>
<li>명령어 입력 실수를 줄일 수 있다.</li>
</ul>
<h1 id="쉘-스크립트의-기본">쉘 스크립트의 기본</h1>
<h2 id="shell-관련-명령어">shell 관련 명령어</h2>
<pre><code class="language-bash"># 기본 shell 목록 확인
$ cat /etc/shells</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/27a288b7-0267-448b-ae43-a304dac12329/image.png" /></p>
<pre><code class="language-bash"># 현재 쉘 확인
echo $SHELL</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0742394c-e95b-46fc-a4af-c3721403c216/image.png" /></p>
<blockquote>
<p>💡 기본 shell 목록에서 명령어를 통해 원하는 계정의 원하는 쉘로 변경이 가능하다.</p>
</blockquote>
<pre><code class="language-bash">## 기본 shell 변경
$ chsh -s /bin/dash 

## 특정 user의 shell을 변경할 수도 있다.
$ chsh -s /bin/dash username

## 아래 명령어로 계정별 shell들을 확인할 수 있다.
$ vim /etc/passwd</code></pre>
<h2 id="셔뱅">셔뱅</h2>
<blockquote>
<p>💡 아래와 같은 쉘 스크립트를 작성하여 실행해 보자.</p>
</blockquote>
<pre><code class="language-bash">## vim 편집기를 활용한 sh파일 생성 및 수정
$ vim test.sh</code></pre>
<ul>
<li><p>test.sh</p>
<pre><code class="language-bash">  #!/bin/bash

  echo 'ohgiraffers directory'
  cd /home/ohgiraffers
  ls -l</code></pre>
</li>
</ul>
<pre><code class="language-bash">## 실행 권한 부여
$ chmod +x test.sh

## 셔뱅을 활용한 test.sh 쉘 스크립트 실행
$ ./test.sh</code></pre>
<blockquote>
<p>💡 첫 줄의 #!로 시작하는 행을 <strong>셔뱅</strong>이라고 하며 해시 기호와 느낌표(#!) 로 이루어진 문자 시퀀스로, 스크립트의 맨 처음에 온다.</p>
<p>#!/bin/bash는 /bin/bash를 사용한다고 명시적으로 선언한 것으로 /bin/bash를 입력하지 않아도 되고, 또한 사용중인 쉘이 bash가 아니어도 자동으로 /bin/bash가 스크립트를 실행하게 한다.</p>
</blockquote>