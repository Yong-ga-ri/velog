<h1 id="data-types">DATA TYPES</h1>
<blockquote>
<p>💡 MySQL은 여러 가지 데이터 유형을 지원(문자열, 숫자, 날짜, 시간)한다.</p>
<p>적절한 데이터 유형을 정의하면 데이터 저장 공간을 효율적으로 사용하고 데이터 입력의 유효성 검사에도 도움이 된다.</p>
</blockquote>
<h2 id="데이터-형식의-종류">데이터 형식의 종류</h2>
<h3 id="숫자-데이터-형식">숫자 데이터 형식</h3>
<ul>
<li>정수 또는 실수 등의 숫자를 표현한다.</li>
<li>FLOAT이나 DOUBLE형은 큰 범위의 숫자를 저장할 수 있지만 정확하지 않은 근사치를 저장한다. 따라서 실수 형을 저장하고 싶어도 DECIMAL을 사용하는 것이 바람직하다.</li>
</ul>
<table>
<thead>
<tr>
<th>데이터 형식</th>
<th>바이트 수</th>
<th>숫자 범위</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>BIT(N)</td>
<td>N/B</td>
<td></td>
<td>1~64Bit 표현, b'0000'형식으로 표현</td>
</tr>
<tr>
<td>TINYINT</td>
<td>1</td>
<td>-128 ~ 127</td>
<td>정수</td>
</tr>
<tr>
<td>SMALLINT</td>
<td>2</td>
<td>-32,768 ~ 32,767</td>
<td>정수</td>
</tr>
<tr>
<td>MEDIUMINT</td>
<td>3</td>
<td>-8,388,608 ~ 8,388,607</td>
<td>정수</td>
</tr>
<tr>
<td>INT INTEGER</td>
<td>4</td>
<td>약-21억 ~ +21억</td>
<td>정수</td>
</tr>
<tr>
<td>BIGINT</td>
<td>8</td>
<td>약 -900경 ~ +900경</td>
<td>정수</td>
</tr>
<tr>
<td>FLOAT</td>
<td>4</td>
<td>3.40E+38 ~ -1.17E-38</td>
<td>소수점 아래 7자리까지 표현</td>
</tr>
<tr>
<td>DOUBLE</td>
<td>8</td>
<td>-1.22E-308 ~ 1.79E+308</td>
<td>소수점 아래 15자리까지 표현</td>
</tr>
<tr>
<td>DECIMAL(m,[d]) NUMBER(m,[d])</td>
<td>5~17</td>
<td>-10^38+1 ~ 10^38-1</td>
<td>전체 자릿수(m)와 소수점 이하 자릿수(d)를 가진</td>
</tr>
</tbody></table>
<h3 id="문자-데이터-형식">문자 데이터 형식</h3>
<ul>
<li>CHAR는 고정길이 문자형으로 자릿수가 불변이다.</li>
<li>VARCHAR는 가변길이 문자형으로 자릿수가 가변이다.
(큰 자릿수를 설정해도 저장할 공간을 효율적으로 사용할 수 있다.)</li>
<li>CHAR 형식으로 설정하는 것이 INSERT/UPDATE 시에 일반적으로 더 좋은 성능을 발휘한다.</li>
<li>대용량 데이터는 TEXT계열의 데이터 형식으로 저장한다.</li>
<li>BLOB(Binary Large Object)은 사진 파일, 동영상 파일, 문서 파일 등의 대용량 이진 데이터를 저장한다.</li>
<li>ENUM은 열거형 데이터를 사용(요일이나 카테고리 등) 시 활용되는 방식이다.</li>
<li>SET은 최대 64개를 준비한 후에 2개씩 세트로 데이터를 저장하는 방식을 사용 시 활용되는 방식이다.</li>
<li>LONGTEXT는 대용량 문서 데이터, LONGBLOB은 동영상 파일과 같은 큰 바이너리 파일 저장 시에 활용할 수 있다.</li>
</ul>
<table>
<thead>
<tr>
<th>데이터 형식</th>
<th>데이터 형식</th>
<th>바이트 수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td></td>
<td>CHAR(n)</td>
<td>1 ~ 255</td>
<td>고정길이 문자형 n을 1부터 255까지 지정  그냥 CHAR만 쓰면 CHAR(1)과 동일</td>
</tr>
<tr>
<td></td>
<td>VARCHAR(n)</td>
<td>1 ~ 65535</td>
<td>가변길이 문자형 n을 사용하면 1부터 65535까지 지정</td>
</tr>
<tr>
<td></td>
<td>BINARY(n)</td>
<td>1 ~ 255</td>
<td>고정길이의 이진 데이터 값</td>
</tr>
<tr>
<td></td>
<td>VARBINARY(n)</td>
<td>1 ~ 255</td>
<td>가변길이의 이진 데이터 값</td>
</tr>
<tr>
<td>TEXT</td>
<td>TINYTEXT</td>
<td>1 ~ 255</td>
<td>255 크기의 TEXT 데이터 값</td>
</tr>
<tr>
<td>TEXT</td>
<td>TEXT</td>
<td>1 ~ 65535</td>
<td>N 크기의 TEXT 데이터 값</td>
</tr>
<tr>
<td>TEXT</td>
<td>MEDIUMTEXT</td>
<td>1 ~ 16777215</td>
<td>16777215 크기의 TEXT 데이터 값</td>
</tr>
<tr>
<td>TEXT</td>
<td>LONGTEXT</td>
<td>1 ~ 4294967295</td>
<td>최대 4GB 크기의 TEXT 데이터 값</td>
</tr>
<tr>
<td>BLOB</td>
<td>TINYBLOB</td>
<td>1 ~ 255</td>
<td>255 크기의 BLOB 데이터 값</td>
</tr>
<tr>
<td>BLOB</td>
<td>BLOB</td>
<td>1 ~ 65535</td>
<td>N 크기의 BLOB 데이터 값</td>
</tr>
<tr>
<td>BLOB</td>
<td>MEDIUMBLOB</td>
<td>1 ~ 16777215</td>
<td>16777215 크기의 BLOB 데이터 값</td>
</tr>
<tr>
<td>BLOB</td>
<td>LONGBLOB</td>
<td>1 ~ 4294967295</td>
<td>최대 4GB 크기의 BLOB 데이터 값</td>
</tr>
<tr>
<td></td>
<td>ENUM(값들...)</td>
<td>1 또는 2</td>
<td>최대 65535개의 열거형 데이터 값</td>
</tr>
<tr>
<td></td>
<td>SET(값들...)</td>
<td>1, 2, 3, 4, 8</td>
<td>최대 64개의 서로 다른 데이터 값</td>
</tr>
</tbody></table>
<h3 id="날짜와-시간-데이터-형식">날짜와 시간 데이터 형식</h3>
<table>
<thead>
<tr>
<th>데이터 형식</th>
<th>바이트 수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>DATE</td>
<td>3</td>
<td>날짜는 1001-01-01 ~ 9999-12-31 까지 저장되며 날짜 형식만 사용 'YYYY-MM-DD' 형식으로 사용됨</td>
</tr>
<tr>
<td>TIME</td>
<td>3</td>
<td>-838:59:59.000000 ~ 838:59:59.000000 까지 저장되며 'HH:MM:SS' 형식으로 사용</td>
</tr>
<tr>
<td>DATETIME</td>
<td>8</td>
<td>날짜는 1001-01-01 00:00:00 ~ 9999-12-31 23:59:59 까지 저장되며 형식은 'YYYY-MM-DD HH:MM:SS' 형식으로 사용</td>
</tr>
<tr>
<td>TIMESTAMP</td>
<td>4</td>
<td>날짜는 1001-01-01 00:00:00 ~ 9999-12-31 23:59:59 까지 저장되며 형식은 'YYYY-MM-DD HH:MM:SS' 형식으로 사용 time_zone 시스템 변수와 관련이 있고 UTC 시간대 변환하여 저장</td>
</tr>
<tr>
<td>YEAR</td>
<td>1(tiny_int?)</td>
<td>1901 ~ 2155까지 저장 'YYYY' 형식으로 사용</td>
</tr>
</tbody></table>
<h3 id="기타-데이터-형식">기타 데이터 형식</h3>
<table>
<thead>
<tr>
<th>데이터 형식</th>
<th>바이트 수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>GEOMETRY</td>
<td>N/A</td>
<td>공간 데이터 형식으로 선, 점 및 다각형 같은 공간 데이터 개체를 저장하고 조작</td>
</tr>
<tr>
<td>JSON</td>
<td>8</td>
<td>JSON 문서를 저장</td>
</tr>
</tbody></table>
<h2 id="형변환">형변환</h2>
<ul>
<li>SQL 데이터의 형변환에는 명시적 형변환과 암시적 형변환이 있다.</li>
</ul>
<h3 id="명시적-형변환explicit-conversion">명시적 형변환(Explicit Conversion)</h3>
<ul>
<li><p><code>CAST (expression AS 데이터형식 [(길이)])</code></p>
</li>
<li><p><code>CONVERT (expression, 데이터형식 [(길이)])</code></p>
</li>
<li><p>데이터 형식으로 가능한 것은 BINARY, CHAR, DATE, DATETIME, DECIMAL, JSON, SIGNED INTEGER, TIME, UNSIGNED INTEGER 등이 있다.</p>
<pre><code class="language-sql">  SELECT AVG(menu_price) FROM tbl_menu;
  SELECT CAST(AVG(menu_price) AS SIGNED INTEGER) AS '평균 메뉴 가격' FROM tbl_menu;
  SELECT CONVERT(AVG(menu_price), SIGNED INTEGER) AS '평균 메뉴 가격' FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/181cc229-2b24-400b-8486-793c8ab16281/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/449e8591-8250-4236-837d-ca7a610a150a/image.png" /></p>
</blockquote>
</li>
</ul>
<pre><code class="language-sql">SELECT CAST('2023$5$30' AS DATE);
SELECT CAST('2023/5/30' AS DATE);
SELECT CAST('2023%5%30' AS DATE);
SELECT CAST('2023@5@30' AS DATE);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9466eae7-379e-461e-bc2b-7c58cebbcea8/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d9bc3373-6cf7-47c3-8aa2-19a851dccedc/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/525c95b0-0a63-4cf7-b4ca-98f552791140/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/00192dd9-6944-42e2-8755-d05a9e84123c/image.png" /></p>
</blockquote>
<ul>
<li><p>메뉴 가격 구하기</p>
<pre><code class="language-sql">  SELECT CAST(menu_price AS CHAR(5)) FROM tbl_menu;
  SELECT CONCAT(CAST(menu_price AS CHAR(5)), '원') FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/fe60a566-fd0e-41ac-8d8b-c128f774d08a/image.png" /></p>
</blockquote>
</li>
<li><p>카테고리별 메뉴 가격 합계 구하기</p>
<pre><code class="language-sql">  SELECT category_code, CONCAT(CAST(SUM(menu_price) AS CHAR(10)), '원') FROM tbl_menu GROUP BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/77cc58f1-0660-4070-82e6-1183e944df9d/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="암시적-형변환implicit-conversion">암시적 형변환(Implicit Conversion)</h3>
<ul>
<li><p>따로 처리하지 않아도 내부적으로 자동으로 형변환이 이루어진다.</p>
<pre><code class="language-sql">  SELECT '1' + '2';    -- 각 문자가 정수로 변환됨
  SELECT CONCAT(menu_price, '원') FROM tbl_menu;    -- menu_price가 문자로 변환됨
  SELECT 3 &gt; 'MAY';    -- 문자는 0으로 변환된다.</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9890ced1-5bba-4e7b-a236-f5539b5dfe24/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/fa02af62-20c4-4a68-999a-6894c32def97/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/7261343c-a4f3-47fd-b94a-554269ab1000/image.png" /></p>
</blockquote>
<pre><code class="language-sql">  SELECT 5 &gt; '6MAY';   -- 문자에서 첫번째로 나온 숫자는 정수로 전환된다.
  SELECT 5 &gt; 'M6AY';   -- 숫자가 뒤에 나오면 문자로 인식되어 0으로 변환된다.
  SELECT '2023-5-30';  -- 날짜형으로 바뀔 수 있는 문자는 DATE형으로 변환된다.</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/b67579af-45cd-4cdf-b0e7-3e9d9f7402a2/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0b28d94b-ec15-4ea3-a6d3-5fcc7748522c/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c2af17aa-289d-430a-ae2b-998af021717c/image.png" /></p>
</blockquote>
</li>
</ul>