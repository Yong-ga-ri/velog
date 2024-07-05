<h1 id="build-in-functions">BUILD IN FUNCTIONS</h1>
<blockquote>
<p>💡 MySQL은 문자열, 숫자, 날짜, 시간에 관한 다양한 작업 수행에 많은 내장 함수를 제공한다.</p>
</blockquote>
<h2 id="문자열-관련-함수">문자열 관련 함수</h2>
<ul>
<li><p>ASCII(아스키 코드), CHAR(숫자)</p>
</li>
<li><p><code>ASCII: 아스키 코드 값 추출</code>  <code>CHAR: 아스키 코드로 문자 추출</code></p>
</li>
<li><p>Workbench의 버그로 CHAR(65)의 결과가 'BLOB'으로 보일 수 있는데 일반 명령형 모드에서는 정상적으로 'A'로 출력된다. 'BLOB' 글자에서 마우스 오른쪽 버튼 클릭하고 'Open Value in Viewer' 선택 후 Text 탭에서 확인할 수 있다.</p>
<pre><code class="language-sql">  SELECT ASCII('A'), CHAR(65);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/313dc111-f1cb-4a49-ab4b-2cf39b7194f8/image.png" /></p>
</blockquote>
</li>
<li><p>BIT_LENGTH(문자열), CHAR_LENGTH(문자열), LENGTH(문자열)</p>
</li>
<li><p>BIT_LENGTH: 할당된 비트 크기 반환</p>
</li>
<li><p>CHAR_LENGTH: 문자열의 길이 반환</p>
</li>
<li><p>LENGTH: 할당된 BYTE 크기 반환`</p>
<pre><code class="language-sql">  SELECT BIT_LENGTH('pie'), CHAR_LENGTH('pie'), LENGTH('pie');
  SELECT menu_name, BIT_LENGTH(menu_name), CHAR_LENGTH(menu_name), LENGTH(menu_name) from tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/4befc47a-bff5-4158-b003-c997284ca6f2/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/4f5d1504-2aa8-4291-b676-95ae1286360c/image.png" /></p>
</blockquote>
</li>
<li><p>CONCAT(문자열1, 문자열2, ...), CONCAT_WS(구분자, 문자열1, 문자열2, ...)</p>
</li>
<li><p><code>CONCAT: 문자열을 이어붙임</code>  <code>CONCAT_WS: 구분자와 함께 문자열을 이어붙임</code></p>
<pre><code class="language-sql">  SELECT CONCAT('호랑이', '기린', '토끼');
  SELECT CONCAT_WS(',', '호랑이', '기린', '토끼');
  SELECT CONCAT_WS('-', '2023', '05', '31');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3b244c0a-5ac4-4f00-9c99-8de035e202d9/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/de430822-48b0-429c-b9a4-2a5133c25b77/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/8d7baf9d-6614-41ff-acf2-37d228b6c95f/image.png" /></p>
</blockquote>
</li>
<li><p>ELT(위치, 문자열1, 문자열2, ...), FIELD(찾을 문자열, 문자열1, 문자열2, ...), FIND_IN_SET(찾을 문자열, 문자열 리스트), INSTR(기준 문자열, 부분 문자열), LOCATE(부분 문자열, 기준 문자열)</p>
</li>
<li><p><code>ELT: 해당 위치의 문자열 반환</code>  <code>FIELD: 찾을 문자열 위치 반환</code>  <code>FIND_IN_SET: 찾을 문자열의 위치 반환</code>  <code>INSTR: 기준 문자열에서 부분 문자열의 시작 위치 반환</code>  <code>LOCATE: INSTR과 동일하고 순서는 반대</code></p>
<pre><code class="language-sql">  SELECT 
         ELT(2, '사과', '딸기', '바나나')
       , FIELD('딸기', '사과', '딸기', '바나나')
       , FIND_IN_SET('바나나', '사과,딸기,바나나')
       , INSTR('사과딸기바나나', '딸기') 
       , LOCATE('딸기', '사과딸기바나나');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a3442e25-9b79-47dc-ad27-ba0b961753f9/image.png" /></p>
</blockquote>
</li>
<li><p>FORMAT(숫자, 소수점 자릿수)</p>
</li>
<li><p><code>FORMAT: 1000단위마다 콤마(,) 표시를 해 주며 소수점 아래 자릿수(반올림)까지 표현한다.</code></p>
<pre><code class="language-sql">  SELECT FORMAT(123142512521.5635326, 3);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1abfbb3a-64be-4d84-b6f7-f207a6f8329d/image.png" /></p>
</blockquote>
</li>
<li><p>BIN(숫자), OCT(숫자), HEX(숫자)</p>
</li>
<li><p><code>BIN: 2진수 표현</code>  <code>OCT: 8진수 표현</code>  <code>HEX: 16진수 표현</code></p>
<pre><code class="language-sql">  SELECT BIN(65), OCT(65), HEX(65);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6f7d6d26-7d47-48a3-b7cc-724b17079dc6/image.png" /></p>
</blockquote>
</li>
<li><p>INSERT(기준 문자열, 위치, 길이, 삽입할 문자열)</p>
</li>
<li><p><code>INSERT: 기준 문자열의 위치부터 길이만큼을 지우고 삽입할 문자열을 끼워 넣는다.</code></p>
<pre><code class="language-sql">  SELECT INSERT('내 이름은 아무개입니다.', 7, 3, '홍길동');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/7f9a5b1a-5e66-4597-9382-76c4f9fc964f/image.png" /></p>
</blockquote>
</li>
<li><p>LEFT(문자열, 길이), RIGHT(문자열, 길이)</p>
</li>
<li><p><code>LEFT: 왼쪽에서 문자열의 길이만큼을 반환</code>  <code>RIGHT: 오른쪽에서 문자열의 길이만큼을 반환</code></p>
<pre><code class="language-sql">  SELECT LEFT('Hello World!', 3), RIGHT('Hello World!', 3);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f6adf845-0f7c-4d80-a102-f8f8539c0f8b/image.png" /></p>
</blockquote>
</li>
<li><p>UPPER(문자열), LOWER(문자열)</p>
</li>
<li><p><code>UPPER: 소문자를 대문자로 변경</code>  <code>LOWER: 대문자를 소문자로 변경</code></p>
<pre><code class="language-sql">  SELECT LOWER('Hello World!'), UPPER('Hello World!');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a99c2ca7-0558-4320-a02a-9cdaee5610c0/image.png" /></p>
</blockquote>
</li>
<li><p>LPAD(문자열, 길이, 채울 문자열), RPAD(문자열, 길이, 채울 문자열)</p>
</li>
<li><p><code>LPAD: 문자열을 길이만큼 왼쪽으로 늘린 후에 빈 곳을 문자열로 채운다.</code>  <code>RPAD: 문자열을 길이만큼 오른쪽으로 늘린 후에 빈 곳을 문자열로 채운다.</code></p>
<pre><code class="language-sql">  SELECT LPAD('왼쪽', 6, '@'), RPAD('오른쪽', 6 ,'@');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/fc328d64-52bf-4a56-af02-4873c21a7357/image.png" /></p>
</blockquote>
</li>
<li><p>LTRIM(문자열), RTRIM(문자열)</p>
</li>
<li><p><code>LTRIM: 왼쪽 공백 제거</code>  <code>RTRIM: 오른쪽 공백 제거</code></p>
<pre><code class="language-sql">  SELECT LTRIM('    왼쪽'), RTRIM('오른쪽    ');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/5c803c47-f6c6-4c75-a5b1-15c7f59ac9ef/image.png" /></p>
</blockquote>
</li>
<li><p>TRIM(문자열), TRIM(방향 자를_문자열 FROM 문자열)</p>
</li>
<li><p><code>TRIM: TRIM은 기본적으로 앞뒤 공백을 제거하지만 방향(LEADING(앞), BOTH(양쪽), TRAILING(뒤))이 있으면 해당 방향에 지정한 문자열을 제거할 수 있다.</code></p>
<pre><code class="language-sql">  SELECT TRIM('    MySQL    '), TRIM(BOTH '@' FROM '@@@@MySQL@@@@');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0883e1a9-b64c-4e57-acd9-cccbef6d279a/image.png" /></p>
</blockquote>
</li>
<li><p>REPEAT(문자열, 횟수)</p>
</li>
<li><p><code>REPEAT: 문자열을 횟수만큼 반복</code></p>
<pre><code class="language-sql">  SELECT REPEAT('재밌어', 3);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/8ca0060f-5ccc-4dcf-b209-69a6537876a8/image.png" /></p>
</blockquote>
</li>
<li><p>REPLACE(문자열, 찾을 문자열, 바꿀 문자열)</p>
</li>
<li><p><code>REPLACE: 문자열에서 문자열을 찾아 치환</code></p>
<pre><code class="language-sql">  SELECT REPLACE('마이SQL', '마이', 'My');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e4760ddc-9709-4fa8-95a2-faa5ec718706/image.png" /></p>
</blockquote>
</li>
<li><p>REVERSE(문자열)</p>
</li>
<li><p><code>REVERSE: 문자열의 순서를 거꾸로 뒤집음</code></p>
<pre><code class="language-sql">  SELECT REVERSE('stressed');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a275ccf9-9361-44ef-b5b6-618512e8b32e/image.png" /></p>
</blockquote>
</li>
<li><p>SPACE(길이)</p>
</li>
<li><p><code>SPACE: 길이 만큼의 공백을 반환</code></p>
<pre><code class="language-sql">  SELECT CONCAT('제 이름은', SPACE(5), '이고 나이는', SPACE(3), '세입니다.');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/5a3f05a2-2e93-4eeb-8eec-cc33c4cc5a3f/image.png" /></p>
</blockquote>
</li>
<li><p>SUBSTRING(문자열, 시작위치, 길이)</p>
</li>
<li><p><code>SUBSTRING: 시작 위치부터 길이만큼의 문자를 반환(길이를 생략하면 시작 위치부터 끝까지 반환)</code></p>
<pre><code class="language-sql">  SELECT SUBSTRING('안녕하세요 반갑습니다.', 7, 2), SUBSTRING('안녕하세요 반갑습니다.', 7);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e44ca729-d8d2-47e8-84ce-adc8c5250107/image.png" /></p>
</blockquote>
</li>
<li><p>SUBSTRING_INDEX(문자열, 구분자, 횟수)</p>
</li>
<li><p><code>SUBSTRING_INDEX: 구분자가 왼쪽부터 횟수 번쨰 나오면 그 이후의 오른쪽은 버린다. 횟수가 음수일 경우 오른쪽부터 세고 왼쪽을 버린다.</code></p>
<pre><code class="language-sql">  SELECT SUBSTRING_INDEX('hong.test@gmail.com', '.', 2), SUBSTRING_INDEX('hong.test@gmail.com', '.', -2);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3521d2df-49b9-4cc2-86e1-b3cebb39483a/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="숫자-관련-함수">숫자 관련 함수</h2>
<ul>
<li><p>ABS(숫자)</p>
</li>
<li><p><code>ABS: 절대값 반환</code></p>
<pre><code class="language-sql">  SELECT ABS(-123);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/fa9e3f35-a4e8-4350-bae6-db00a5c8c4fb/image.png" /></p>
</blockquote>
</li>
<li><p>CEILING(숫자), FLOOR(숫자), ROUND(숫자)</p>
</li>
<li><p><code>CEILING: 올림값 반환</code>  <code>FLOOR: 버림값 반환</code>  <code>ROUND: 반올림값 반환</code></p>
<pre><code class="language-sql">  SELECT CEILING(1234.56), FLOOR(1234.56), ROUND(1234.56);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/01900741-3a21-4436-9b85-8c9e56b067a2/image.png" /></p>
</blockquote>
</li>
<li><p>CONV(숫자, 원래 진수, 변환할 진수)</p>
</li>
<li><p><code>CONV: 원래 진수에서 변환하고자 하는 진수로 변환</code></p>
<pre><code class="language-sql">  SELECT CONV('A', 16, 10), CONV('A', 16, 2), CONV(1010, 2, 8);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d5642fed-220c-408c-9474-f6277477a3f1/image.png" /></p>
</blockquote>
</li>
<li><p>MOD(숫자1, 숫자2) 또는 숫자1 % 숫자2 또는 숫자1 MOD 숫자2</p>
</li>
<li><p><code>MOD: 숫자 1을 숫자 2로 나눈 나머지 추출</code></p>
<pre><code class="language-sql">  SELECT MOD(75, 10), 75 % 10, 75 MOD 10;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ce8e5be3-804d-46e2-8d92-c90504d90bc7/image.png" /></p>
</blockquote>
</li>
<li><p>POW(숫자1, 숫자2), SQRT(숫자)</p>
</li>
<li><p><code>POW: 거듭제곱값 추출</code>  <code>SQRT: 제곱근을 추출</code></p>
<pre><code class="language-sql">  SELECT POW(2, 4), SQRT(16);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="Untitled" src="https://v2.velog.io/rss/BUILD_IN_FUNCTIONS%20013eb6767e0a4b93a97f6b91f2ce4cc2/Untitled%2025.png" /></p>
</blockquote>
</li>
<li><p>RAND()</p>
</li>
<li><p><code>RAND: 0이상 1 미만의 실수를 구한다.</code>  <code>'m &lt;= 임의의 정수 &lt; n'을 구하고 싶다면 FLOOR((RAND() * (n - m) + m)을 사용한다.</code>  <code>1부터 10까지 난수 발생: FLOOR(RAND() * (11 - 1) + 1)</code></p>
<pre><code class="language-sql">  SELECT RAND(), FLOOR(RAND() * (11 - 1) + 1);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9901c918-6792-49c2-b887-cfed753f1b3d/image.png" /></p>
</blockquote>
</li>
<li><p>SIGN(숫자)</p>
</li>
<li><p><code>SIGN: 양수면 1, 0이면 0, 음수면 -1을 반환</code></p>
<pre><code class="language-sql">  SELECT SIGN(10.1), SIGN(0), SIGN(-10.1);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c95631f1-157c-4f87-b880-dc97642d5c1c/image.png" /></p>
</blockquote>
</li>
<li><p>TRUNCATE(숫자, 정수)</p>
</li>
<li><p><code>TRUNCATE: 소수점을 기준으로 정수 위치까지 구하고 나머지는 버림</code></p>
<pre><code class="language-sql">  SELECT TRUNCATE(12345.12345, 2), TRUNCATE(12345.12345, -2);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/b6fab86f-6511-49b2-89b8-f5746925bf1c/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="날짜-및-시간-관련-함수">날짜 및 시간 관련 함수</h2>
<ul>
<li><p>ADDDATE(날짜, 차이), SUBDATE(날짜, 차이)</p>
</li>
<li><p><code>ADDDATE: 날짜를 기준으로 차이를 더함</code>  <code>SUBDATE: 날짜를 기준으로 날짜를 뺌</code></p>
<pre><code class="language-sql">  SELECT ADDDATE('2023-05-31', INTERVAL 30 DAY), ADDDATE('2023-05-31', INTERVAL 6 MONTH);
  SELECT SUBDATE('2023-05-31', INTERVAL 30 DAY), SUBDATE('2023-05-31', INTERVAL 6 MONTH);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e879ca8d-d7fa-461d-b7bb-7817c8099e69/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/08b7c820-ba7e-4410-89db-bf33367c42cd/image.png" /></p>
</blockquote>
</li>
<li><p>ADDTIME(날짜/시간, 시간), SUBTIME(날짜/시간, 시간)</p>
</li>
<li><p><code>ADDTIME: 날짜 또는 시간을 기준으로 시간을 더함</code>  <code>SUBTIME: 날짜 또는 시간을 기준으로 시간을 뺌</code></p>
<pre><code class="language-sql">  SELECT ADDTIME('2023-05-31 09:00:00', '1:0:1'), SUBTIME('2023-05-31 09:00:00', '1:0:1');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ba14acd2-d241-4391-9123-6c248815105f/image.png" /></p>
</blockquote>
</li>
<li><p>CURDATE(), CURTIME(), NOW(), SYSDATE()</p>
</li>
<li><p><code>CURDATE: 현재 연-월-일 추출</code>  <code>CURTIME: 현재 시:분:초 추출</code>  <code>NOW() 또는 SYSDATE(): 현재 연-월-일 시:분:초 추출</code></p>
<pre><code class="language-sql">  SELECT CURDATE(), CURTIME(), NOW(), SYSDATE();

  -- CURDATE(), CURRENT_DATE(), CURRENT_DATE는 동일
  SELECT CURDATE(), CURRENT_DATE(), CURRENT_DATE;

  -- CURTIME(), CURRENT_TIME(), CURRENT_TIME은 동일 
  SELECT CURTIME(), CURRENT_TIME(), CURRENT_TIME;

  -- NOW(), LOCALTIME, LOCALTIME(), LOCALTIMESTAMP, LOCALTIMESTAMP()는 동일
  SELECT NOW(), LOCALTIME, LOCALTIME(), LOCALTIMESTAMP, LOCALTIMESTAMP();</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/67cd72b2-90c2-43bf-ad2d-0580c2a162a0/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/54250737-2ea9-4164-b8b2-d900f90c1bdb/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/590bb74c-d65b-4d79-a532-3c2614b6498e/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6dca8fd2-5cba-434d-ae99-4c6c7407201f/image.png" /></p>
</blockquote>
</li>
<li><p>YEAR(날짜), MONTH(날짜), DAYOFMONTH(날짜),</p>
</li>
<li><p><code>HOUR(시간), MINUTE(시간), SECOND(시간), MICROSECOND(시간)</code>  <code>날짜 또는 시간에서 연, 월, 일, 시, 분, 초, 밀리초를 추출</code></p>
<pre><code class="language-sql">  SELECT YEAR(CURDATE()), MONTH(CURDATE()), DAYOFMONTH(CURDATE());
  SELECT HOUR(CURTIME()), MINUTE(CURTIME()), SECOND(CURRENT_TIME), MICROSECOND(CURRENT_TIME);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/20919205-7302-4849-af0d-bbc386bd708a/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/89c7e107-982d-48e6-a30e-c6001170bb98/image.png" /></p>
</blockquote>
</li>
<li><p>DATE(), TIME()</p>
</li>
<li><p><code>DATE: 연-월-일만 추출</code>  <code>TIME: 시:분:초만 추출</code></p>
<pre><code class="language-sql">  SELECT DATE(NOW()), TIME(NOW());</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/61cac7b9-a65e-427d-bfad-779e03904021/image.png" /></p>
</blockquote>
</li>
<li><p>DATEDIFF(날짜1, 날짜2), TIMEDIFF(날짜1 또는 시간1, 날짜1 또는 시간2)</p>
</li>
<li><p><code>DATEDIFF: 날짜1 - 날짜2의 일수를 반환</code>  <code>TIMEDIFF: 시간1 - 시간2의 결과를 구함</code></p>
<pre><code class="language-sql">  SELECT DATEDIFF('2023-05-31', '2023-02-27'), TIMEDIFF('17:07:11', '13:06:10');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/11ac5f2d-16b3-46e4-a87d-34d5c3ff9b1f/image.png" /></p>
</blockquote>
</li>
<li><p>DAYOFWEEK(날짜), MONTHNAME(), DAYOFYEAR(날짜)</p>
</li>
<li><p><code>DAYOFWEEK: 요일 반환(1이 일요일)</code>  <code>MONTHNAME: 해당 달의 이름 반환</code>  <code>DAYOFYEAR: 해당 년도에서 몇 일이 흘렀는지 반환</code></p>
<pre><code class="language-sql">  SELECT DAYOFWEEK(CURDATE()), MONTHNAME(CURDATE()), DAYOFYEAR(CURDATE());</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/92a4c6c5-be07-428b-bb5a-32c14ad5e005/image.png" /></p>
</blockquote>
</li>
<li><p>LAST_DAY(날짜)</p>
</li>
<li><p><code>LAST_DAY: 해당 날짜의 달에서 마지막 날의 날짜를 구한다.</code></p>
<pre><code class="language-sql">  SELECT LAST_DAY('20230201');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2adba376-5f89-428a-9ec5-adfccd546528/image.png" /></p>
</blockquote>
</li>
<li><p>MAKEDATE(연도, 정수)</p>
</li>
<li><p><code>MAKEDATE: 해당 연도의 정수만큼 지난 날짜를 구한다.</code></p>
<pre><code class="language-sql">  SELECT MAKEDATE(2023, 32);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/47959ab7-d98f-4ecc-92f0-94740c5df3fd/image.png" /></p>
</blockquote>
</li>
<li><p>MAKETIME(시, 분, 초)</p>
</li>
<li><p><code>MAKETIME: 시, 분, 초를 이용해서 '시:분:초'의 TIME 형식을 만든다.</code></p>
<pre><code class="language-sql">  SELECT MAKETIME(17, 03, 02);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/4a925e04-8f79-4795-be2e-08ff8255edbe/image.png" /></p>
</blockquote>
</li>
</ul>
<ul>
<li><p>QUARTER(날짜)</p>
</li>
<li><p><code>QUARTER: 해당 날짜의 분기를 구함</code></p>
<pre><code class="language-sql">  SELECT QUARTER('2023-05-31');</code></pre>
</li>
</ul>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9b446ea6-9e1c-495e-a39b-e3ef3048e9cc/image.png" /></p>
</blockquote>
<ul>
<li><p>TIME_TO_SEC(시간)</p>
</li>
<li><p><code>TIME_TO_SEC: 시간을 초 단위로 구함</code></p>
<pre><code class="language-sql">  SELECT TIME_TO_SEC('1:1:1');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2b9a7f7c-b879-405a-9e6a-de7e7c56ec61/image.png" /></p>
</blockquote>
</li>
</ul>