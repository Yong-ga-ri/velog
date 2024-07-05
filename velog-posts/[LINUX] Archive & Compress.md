<h1 id="파일-압축-방식">파일 압축 방식</h1>
<h2 id="아카이브archive와-압축compress">아카이브(Archive)와 압축(Compress)</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6dc8de70-2e27-4f87-a99c-8f28268c2754/image.png" /></p>
<blockquote>
<p>💡 <strong>윈도우</strong>에서는 <strong>압축(zip)을 하면 파일이나 폴더들을 한번에 묶으면서 동시에 압축</strong>한다. 반면 <strong>리눅스</strong>는 <strong>파일이나 폴더를 하나의 파일로 묶는 것(아카이빙(Archiving))과 압축을 진행해 용량을 줄이는 과정이 구분되어 있다.(gz)</strong></p>
<blockquote>
<ul>
<li><strong>Archiving</strong>: 하나의 파일에 파일과 폴더를 넣고 묶는 것으로 용량은 줄어들지 않음
(<strong>파일과 폴더를 묶어서 하나로 만들어 진 것</strong>을 <strong>아카이브</strong>라고 한다.)</li>
<li><strong>Compression</strong>: 파일이나 아카이빙 된 아카이브를 알고리즘을 활용해 압축해서 용량을 줄이는 것</li>
</ul>
</blockquote>
</blockquote>
<h3 id="파일-아카이브">파일 아카이브</h3>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6ee38b34-131b-41f5-8d04-c45d3aac9c79/image.png" /></p>
<blockquote>
<p>💡 <strong>TAR(Tape ARchives)</strong></p>
<p><strong>테이프 아카이버(Tape Archiver)</strong> 를 줄인 말로 <strong>저장 장치로 백업하기 위해 하나의 파일로 합치는 프로그램을 의미</strong>한다.
용량은 줄어들지 않지만 여러 폴더와 파일을 하나로 관리하기 위해 존재한다.</p>
<ul>
<li>하나로 묶이기 전의 링크나 폴더 구조를 그대로 가져갈 수 있다.</li>
<li>리눅스 용 프로그램이나 데이터, 소스 및 라이브러리 등을 배포하는 용도로 많이 사용한다.</li>
</ul>
</blockquote>
<pre><code class="language-bash">$ tar [OPTION] [아카이브FILE명] [FILE|PATH]</code></pre>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-f</td>
<td>파일 지정. tar 명령에서 -f 옵션 다음에 아카이브 파일의 이름을 지정할 때 쓰임.</td>
</tr>
<tr>
<td>-c</td>
<td>새 아카이브 생성. 파일이나 디렉토리를 아카이브 파일로 만들 때 사용함.</td>
</tr>
<tr>
<td>-x</td>
<td>아카이브에서 파일 추출. 이미 생성된 아카이브 파일에서 파일을 꺼내고 싶을 때 사용함.</td>
</tr>
<tr>
<td>-v</td>
<td>자세한 정보 표시. tar 작업 중에 어떤 파일이 처리되고 있는지 보여줌.</td>
</tr>
<tr>
<td>-z</td>
<td>압축 및 압축 해제. 아카이브를 생성하거나 추출할 때 gzip 형식의 압축 또는 압축 해제를 수행함.</td>
</tr>
<tr>
<td>-j</td>
<td>압축 및 압축 해제. 이 옵션은 bzip2 형식으로 압축하거나 압축 해제할 때 사용함.</td>
</tr>
<tr>
<td>-t</td>
<td>아카이브 내용 나열. 아카이브 안에 어떤 파일들이 있는지 보고 싶을 때 사용함.</td>
</tr>
<tr>
<td>-C</td>
<td>디렉토리 변경. tar를 실행할 때 특정 디렉토리로 이동하고 싶을 때 사용함.</td>
</tr>
<tr>
<td>-A</td>
<td>아카이브 병합. 두 개 이상의 tar 아카이브 파일을 하나로 합칠 때 쓰임.</td>
</tr>
<tr>
<td>-d</td>
<td>차이점 확인. 아카이브 파일과 파일 시스템 사이의 차이점을 확인할 때 사용함.</td>
</tr>
<tr>
<td>-r</td>
<td>아카이브에 파일 추가. 이미 존재하는 tar 아카이브 파일에 새로운 파일을 추가할 때 쓰임.</td>
</tr>
<tr>
<td>-u</td>
<td>아카이브 업데이트. 아카이브에 있는 파일보다 더 최근에 수정된 파일로 아카이브를 업데이트할 때 사용함.</td>
</tr>
<tr>
<td>-k</td>
<td>덮어쓰기 방지. 이미 존재하는 파일을 추출할 때 덮어쓰기를 방지함.</td>
</tr>
<tr>
<td>-U</td>
<td>압축 해제 시 덮어쓰기. 이미 존재하는 파일을 압축 해제할 때 강제로 덮어쓰게 함.</td>
</tr>
<tr>
<td>-w</td>
<td>대화형 확인. tar 작업을 수행하기 전에 사용자에게 확인을 요구함.</td>
</tr>
<tr>
<td>-e</td>
<td>오류 발생 시 즉시 종료. 오류가 발생하면 tar 작업을 즉시 중단함.</td>
</tr>
</tbody></table>
<pre><code class="language-bash"># 현재 디렉토리의 모든 파일과 디렉토리를 tar로 묶기
$ tar cvf 파일명.tar * 

# 대상 디렉토리를 포함한 모든 파일과 디렉토리를 tar로 묶기
$ tar cvf 파일명.tar [PATH] 

# 파일을 지정하여 tar 아카이브로 묶기
$ tar cvf 파일명.tar [FILE_1] [FILE_2]

# tar 아카이브의 내용 확인하기
$ tar tvf 파일명.tar 

# tar 아카이브를 현재 디렉토리에 풀기
$ tar xvf 파일명.tar 

# tar 아카이브를 지정된 디렉토리에 풀기
$ tar xvf 파일명.tar -C [PATH]

# tar 아카이브 묶거나 풀 때 파일 별 진행 여부 확인하기
$ tar cvfw 파일명.tar *

# 현재 디렉토리를 tar로 묶고 gzip으로 압축하기
$ tar zcvf 파일명.tar.gz * 

# gzip으로 압축된 tar 아카이브를 현재 디렉토리에 풀기
$ tar zxvf 파일명.tar.gz 

# 현재 디렉토리를 tar로 묶고 bzip2로 압축하기
$ tar jcvf 파일명.tar.bz2 * 

# bzip2로 압축된 tar 아카이브를 현재 디렉토리에 풀기
$ tar jxvf 파일명.tar.bz2</code></pre>
<h3 id="파일-압축"><strong>파일 압축</strong></h3>
<ul>
<li><strong>압축 형식</strong></li>
</ul>
<table>
<thead>
<tr>
<th>압축형태</th>
<th>확장자 기본</th>
<th>확장자 축약</th>
<th>설명</th>
<th>압축률</th>
<th>압축 및 해제 시간</th>
</tr>
</thead>
<tbody><tr>
<td>gzip</td>
<td>.tar.gz</td>
<td>.tgz</td>
<td>zip과 같은 알고리즘 사용.  다른 파일 간 중복 부분을 하나로 압축해서 용량을 줄일 수 있음.  일반적인 용도에 적합하고 널리 사용됨.</td>
<td>4</td>
<td>1</td>
</tr>
<tr>
<td>xzip</td>
<td>.tar.xz</td>
<td>.txz</td>
<td>LZMA2압축 알고리즘 사용.  윈도우의 7-zip과 유사하지만 유닉스 시스템을 위해 설계됨.  압축률이 가장 좋음.</td>
<td>1</td>
<td>6</td>
</tr>
<tr>
<td>bzip2</td>
<td>.tar.bz2</td>
<td>.tb2  .tbz  .tbz2</td>
<td>큰 용량의 파일에 사용하기 좋음. gzip보다 압축률은 좋지만, 압축과 해제 속도가 느림.</td>
<td>3</td>
<td>3</td>
</tr>
<tr>
<td>Z</td>
<td>.tar.Z</td>
<td>.tZ</td>
<td>ASCII나 바이너리 파일을 의미. 오래된 압축 형식이고, 현재는 더 효율적인 압축 방식이 많이 사용됨.</td>
<td>6</td>
<td>2</td>
</tr>
<tr>
<td>lzma</td>
<td>.tar.lzma</td>
<td>.tlz</td>
<td>bzip2보다 더 높은 압축률 제공. 최대 4GB까지 압축 가능.</td>
<td>2</td>
<td>5</td>
</tr>
<tr>
<td>lz</td>
<td>.tar.lz</td>
<td></td>
<td>LZMA 알고리즘 기반. 무결성 확인을 위한 CRC 체크섬 지원. 데이터 손상을 방지하고 정확성을 유지하는 데 유용함.</td>
<td>5</td>
<td>4</td>
</tr>
</tbody></table>
<blockquote>
<p>💡 <strong>compress 명령어란?</strong></p>
<p>유닉스에서 많이 썼던 압축 프로그램으로 현재는 압축률이 낮아 거의 사용되지 않는다.</p>
</blockquote>
<pre><code class="language-bash"># ncompress 설치
$ sudo apt-get install ncompress

# 압축하기
$ compress [아카이브 FILE명]

# 압축풀기
$ uncompress [아카이브 FILE명]</code></pre>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-d</td>
<td>압축된 파일의 압축을 해제하기 위한 옵션으로 uncompress와 효과가 동일</td>
</tr>
</tbody></table>
<blockquote>
<p>💡 <strong>gzip/gunzip 명령어란?</strong></p>
<p>tar 명령어로 파일을 묶고 tar 명령어로 만들어진 아카이브 파일을 압축하게 되어 단독으로는 잘 쓰이지 않는다.</p>
</blockquote>
<pre><code class="language-bash"># gzip설치
$ sudo apt-get install gzip 

# 압축하기
$ gzip [옵션] [아카이브FILE명] 

# 압축풀기
$ gzip -d [아카이브FILE명]
$ gunzip [아카이브FILE명] 

# 압축된 파일의 내용 확인
$ gzip -l [아카이브FILE명]
$ zcat [아카이브FILE명]</code></pre>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-d</td>
<td>압축을 해제하기 위한 옵션</td>
</tr>
<tr>
<td>-l</td>
<td>압축 내용 확인</td>
</tr>
</tbody></table>
<blockquote>
<p>💡 <strong>bzip2/bunzip2 명령어란?</strong></p>
<p>블록 정렬 알고리즘을 활용한 압축 프로그램으로 gzip, xzip과 더불어 많이 사용되는 압축 프로그램이다. 다소 무난한 압축률을 가지고 있으나 압축 및 해제 시간은 다소 소요된다.</p>
</blockquote>
<pre><code class="language-bash"># bzip2설치
$ sudo apt-get install bzip2

#압축
$ bzip2 text.txt

# 압축 해제
$ bunzip2 text.txt.bz2</code></pre>
<blockquote>
<p>💡 <strong>xz/unxz 명령어란?</strong></p>
<p>LZMA2 알고리즘으로 데이터 손실 없이(무손실) 압축 시킬 수 있는 프로그램이다. 상대적으로 매우 높은 압축률을 가지고 있으며 사이트에서 압축 포맷 파일 배포 용도로 많이 사용되고 있다.</p>
<blockquote>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-d</td>
<td>압축을 해제하기 위한 옵션</td>
</tr>
</tbody></table>
</blockquote>
</blockquote>
<pre><code class="language-bash"># 압축
$ xz [옵션] [아카이브 FILE명]

# 압축풀기
$ xz -d [아카이브 FILE명]
$ unxz [옵션] [아카이브 FILE명]</code></pre>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-d</td>
<td>압축을 풀기 위해 사용하는 옵션</td>
</tr>
</tbody></table>
<blockquote>
<p>💡 <strong>zip/unzip 명령어란?</strong></p>
<p>이전 압축 명령어와 달리 원본 파일이 사라지지 않고 그대로 남아 있고 압축 파일은 별도로 생성된다. 윈도우에서의 압축처럼 아카이빙과 압축이 함께 일어난다.</p>
</blockquote>
<pre><code class="language-bash">$ sudo apt-get install zip # zip 설치

$ zip [압축할 FILE명].zip [아카이브 또는 FILE명]

$ unzip [압축할 FILE명]

# mylog.log를 mylog.zip으로 압축하기(단일 파일 압축)
$ zip mylog.zip mylog.log 

# mylog1.log, mylog2.log, mylog3.log를 mylog.zip으로 압축하기(다중 파일 압축)
$ zip mylog.zip mylog1.log mylog2.log mylog3.log 

# 현 위치 디렉토리와 하위 디렉토리를 모두 test.zip으로 압축
$ zip -r test.zip ./*

# test.zip 압축 해제
$ unzip test.zip</code></pre>
<ul>
<li><strong>zip 명령어 옵션</strong></li>
</ul>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-r</td>
<td>하위 폴더나 파일까지 포함하여 압축</td>
</tr>
</tbody></table>
<ul>
<li><strong>unzip 명령어 옵션</strong></li>
</ul>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>-n</td>
<td>파일 추출 시 파일을 덮어쓰지 않음</td>
</tr>
</tbody></table>