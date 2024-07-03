<h1 id="join">JOIN</h1>
<blockquote>
<p>💡 JOIN은 두 개 이상의 테이블을 관련있는 컬럼을 통해 결합하는데 사용된다.</p>
<p>두 개 이상의 테이블은 반드시 연관있는 컬럼이 존재해야 하며 이를 통해 JOIN된 테이블들의 컬럼을 모두 활용할 수 있다.
<img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/65195755-eb5d-486f-9ed1-9a0961eae597/image.png" /></p>
</blockquote>
<h2 id="alias">ALIAS</h2>
<ul>
<li><p>SQL문의 컬럼 또는 테이블에 별칭을 달아줄 수 있다.</p>
</li>
<li><p><strong>컬럼 별칭</strong></p>
<ul>
<li>resultSet의 컬럼명이 별칭으로 바뀜</li>
<li>별칭에 띄어쓰기나 특수기호가 없다면 홑따옴표(')와 AS는 생략 가능하다.</li>
</ul>
</li>
<li><p><strong>테이블 별칭</strong></p>
<ul>
<li><p>테이블에 별칭을 작성할 수 있으며 어떤 테이블 소속인지를 쉽게 알 수 있게 한다.</p>
</li>
<li><p>테이블 별칭은 AS를 써도 되고 생략도 가능하다.</p>
<p>```sql
SELECT</p>
<pre><code> a.category_code</code></pre><p>   , a.menu_name</p>
</li>
<li><ul>
<li>FROM tbl_menu AS a
FROM tbl_menu a
ORDER BY a.category_code, a.menu_name;<pre><code></code></pre></li>
</ul>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/7ebef028-6a58-45a8-80c3-d89b36bb9852/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h2 id="join의-종류">JOIN의 종류</h2>
<h3 id="inner-join">INNER JOIN</h3>
<ul>
<li><p>두 테이블의 교집합을 반환하는 SQL JOIN 유형</p>
</li>
<li><p>INNER JOIN에서 INNER 키워드는 생략이 가능하다.</p>
<ul>
<li><p>ON을 활용한 JOIN</p>
<ul>
<li>컬럼명이 같거나 다를 경우 ON으로 서로 연관있는 컬럼에 대한 조건을 작성하여 JOIN하는 경우</li>
</ul>
<p>```sql
SELECT</p>
<pre><code> a.menu_name</code></pre><p>   , b.category_name</p>
<p>FROM tbl_menu a</p>
</li>
<li><ul>
<li>INNER JOIN tbl_category b ON a.category_code = b.category_code;
JOIN tbl_category b ON a.category_code = b.category_code;<pre><code></code></pre></li>
</ul>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/8ac7ab6c-e410-4e0f-a0f8-2e6cc003fb1c/image.png" /></p>
</blockquote>
</li>
<li><p>USING을 활용한 JOIN</p>
<ul>
<li>컬럼명이 같을 경우 USING으로 서로 연관있는 컬럼에 대한 조건을 작성하여 JOIN하는 경우</li>
</ul>
<p>```sql
SELECT</p>
<pre><code> a.menu_name</code></pre><p>   , b.category_name
FROM tbl_menu a</p>
</li>
<li><ul>
<li>INNER JOIN tbl_category b USING (category_code);
JOIN tbl_category b USING (category_code);<pre><code></code></pre></li>
</ul>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/80a25cb0-b369-4538-93af-f25dff705559/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h3 id="left-join">LEFT JOIN</h3>
<ul>
<li><p>첫 번째(왼쪽) 테이블의 모든 레코드와 두 번째(오른쪽) 테이블에서 일치하는 레코드를 반환하는 SQL JOIN 유형</p>
<pre><code class="language-sql">  SELECT
         a.menu_name
       , b.category_name
    FROM tbl_menu a
    LEFT JOIN tbl_category b ON a.category_code = b.category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f6f5887b-efaf-4747-bf83-5eefbded67da/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="right-join">RIGHT JOIN</h3>
<ul>
<li><p>두 번째(오른쪽) 테이블의 모든 레코드와 첫 번째(왼쪽) 테이블에서 일치하는 레코드를 반환하는 SQL JOIN 유형</p>
<pre><code class="language-sql">  SELECT                                                          
         a.menu_name                                              
       , b.category_name                                          
    FROM tbl_menu a                                               
   RIGHT JOIN tbl_category b ON a.category_code = b.category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ab82fba4-47ee-4a47-8dc6-3348f76c1c6f/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="cross-join">CROSS JOIN</h3>
<ul>
<li><p>두 테이블의 모든 가능한 조합을 반환하는 SQL JOIN 유형</p>
<pre><code class="language-sql">  SELECT
         a.menu_name
       , b.category_name
    FROM tbl_menu a
   CROSS JOIN tbl_category b;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/800b8196-91ef-4346-a259-6675d066f95c/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="self-join">SELF JOIN</h3>
<ul>
<li><p>같은 테이블 내에서 행과 행 사이의 관계를 찾기 위해 사용되는 SQL JOIN 유형</p>
</li>
<li><p>카테고리별 대분류 확인을 위한 SELF JOIN 조회</p>
<pre><code class="language-sql">  SELECT
         a.category_name
       , b.category_name
    FROM tbl_category a
    JOIN tbl_category b ON a.ref_category_code = b.category_code
   WHERE a.ref_category_code IS NOT NULL;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/906b470e-15a3-42c8-9358-63d4abeed97f/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="join-알고리즘">JOIN 알고리즘</h2>
<ul>
<li><p>MariaDB 5.3 버전까지는 네스티드 루프(Nested Loop) 알고리즘 형태밖에 없었지만 현재는 다양해 졌다.</p>
<ul>
<li>단순 네스티드 루프(Simple Nested Loop)<ul>
<li>가장 기본적인 조인 알고리즘으로 한 테이블의 각 행에 대해 다른 테이블의 모든 행을 순회하면서 조인 조건을 만족하는지 확인한다.</li>
<li>매우 단순하지만 큰 데이터 세트에서는 비효율적일 수 있다.</li>
</ul>
</li>
<li>블록 네스티드 루프(Block Nested Loop)<ul>
<li>단순 네스티드 루프를 개선한 버전으로 데이터를 테이블(드라이빙 테이블)로부터 블록 단위로 불러와서 한 블록의 모든 행을 다른 테이블(드리븐 테이블)의 블록과 비교한다.</li>
<li>I/O  작업을 줄여 성능을 향상시킬 수 있다.</li>
</ul>
</li>
<li>블록 네스티드 루프 해쉬(Block Nested Loop Hash)<ul>
<li>블록 네스티드 루프와 유사하지만 해쉬 테이블을 사용하여 조인 조건을 만족하는 행을 더 효율적으로 찾는다.</li>
<li>해쉬 함수를 사용하여 조인 키를 빠르게 매칭할 수 있어 성능이 더욱 향상된다.</li>
</ul>
</li>
<li>블록 인덱스(Block Index Join, Batched Key Access)<ul>
<li>인덱스를 활용하여 조인을 수행한다.</li>
<li>인덱스를 사용하여 필요한 행만을 효율적으로 액세스하고, 불필요한 행의 검색을 최소화하여 성능을 개선한다.</li>
</ul>
</li>
<li>블록 인덱스 해쉬(Block Index Hash Join, Batched Key Access Hash)<ul>
<li>블록 인덱스 조인에 해쉬 기능이 추가된 것이다.</li>
<li>해쉬 테이블을 활용하여 인덱스의 조인 성능을 더욱 향상시켜 빠른 매칭이 필요한 경우 유용하다.</li>
</ul>
</li>
</ul>
</li>
<li><p>조인 캐시 레벨(join_cache_level)</p>
<p>  <img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0b2c5cb8-59e7-4f2e-a892-af63da102a4e/image.png" /></p>
<ul>
<li>MariaDB 10.0에서는 4가지 형태의 블록 기반 조인 알고리즘을 제공하고 있는데, 이들은 모두 조인 버퍼에 예전 방식으로 레코드 필드를 복사하는 플랫(flat)방식과 중복값 없이 포인터만 조인 버퍼에 저장하는 인크리멘탈(incremental)방식이 있다.</li>
<li>BNL<ul>
<li>블록 네스티드 루프(Block Nested Loop - Flat)</li>
<li>블록 네스티드 루프(Block Nested Loop - Incremental)</li>
</ul>
</li>
<li>BNLH<ul>
<li>블록 네스티드 루프 해쉬(Block Nested Loop Hash - Flat)</li>
<li>블록 네스티드 루프 해쉬(Block Nested Loop Hash - Incremental)</li>
</ul>
</li>
<li>BKA<ul>
<li>배치 키 액세스(Batched Key Access - Flat)</li>
<li>배치 키 액세스(Batched Key Access - Incremental)</li>
</ul>
</li>
<li>BKAH<ul>
<li>배치 키 액세스 해쉬(Batched Key Access Hash - Flat)</li>
<li>배치 키 액세스 해쉬(Batched Key Access Hash - Incremental)</li>
</ul>
</li>
</ul>
</li>
<li><p>join_cache_level을 통해 알고리즘을 고를 수 있다.</p>
<p>  <a href="https://mariadb.com/kb/en/server-system-variables/">Server System Variables</a></p>
</li>
</ul>
<pre><code class="language-sql">DROP TABLE t1;
DROP TABLE t2;

CREATE TABLE t1 (
id int(10) NOT NULL AUTO_INCREMENT ,
c1 int(10) NOT NULL DEFAULT '0',
c2 int(10) NOT NULL DEFAULT '0',
PRIMARY KEY (id),
KEY idx_c1 (c1)
) ENGINE=InnoDB;

CREATE TABLE t2 (
id int(10) NOT NULL AUTO_INCREMENT ,
c1 int(10) NOT NULL DEFAULT '0',
c2 int(10) NOT NULL DEFAULT '0',
PRIMARY KEY (id),
KEY idx_c1 (c1)
) ENGINE=InnoDB;

insert into t1 select null,round(rand()*100),round(rand()*1000)
from information_schema.columns a1, information_schema.columns b1  
LIMIT 100;

insert INTO t2 select null,round(rand()*100),round(rand()*1000)
from information_schema.columns a1, information_schema.columns b1  
LIMIT 100;

SELECT * FROM t1;
SELECT * FROM t2;</code></pre>
<h3 id="block-nested-loopbnl">BLOCK NESTED LOOP(BNL)</h3>
<ul>
<li><p>MariaDB(MySQL)은 기본적으로 BLOCK NESTED LOOP JOIN을 사용한다.</p>
</li>
<li><p>두 개 이상의 테이블에서 하나의 집합을 기준으로 순차적으로 상대방 Row를 결합하여 조합하는 방식</p>
</li>
<li><p>중첩 반복문처럼 첫번 째 테이블의 Row와 관련된 두번째 테이블에 대한 Row를 검색하고 이후 첫 번째 테이블의 다음 Row에 대해 두번째 테이블에 대한 것을 검색하며 이후 이와 같은 방식을 반복한다.</p>
<pre><code class="language-sql">  SET SESSION optimizer_switch='join_cache_incremental=on';
  SET SESSION optimizer_switch='join_cache_hashed=on';
  SET SESSION optimizer_switch='join_cache_bka=on';
  SET SESSION join_cache_level=2;

  select count(*) from t1 join t2 on t1.c2 = t2.c2;
  explain select count(*) from t1 join t2 on t1.c2 = t2.c2;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6d98e6c0-83a4-4630-a90e-a8a80bfef29c/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="block-nested-loop-hashbnlh">Block Nested Loop Hash(BNLH)</h3>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c64ebaa6-6db4-4311-8c9b-184fb8bc6c8f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/49a0b966-5a28-452a-9595-7b2047390fb7/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a27db5ef-993d-460e-bb55-a533bbbde1b9/image.png" /></p>
<ul>
<li><p>MySQL8.0.18버전 이후 지원하게 되었다.</p>
</li>
<li><p>대규모 데이터 세트에 대한 조인 연산을 효과적으로 진행할 수 있다.</p>
</li>
<li><p>빌드 단계(Build phase): 해싱 단계에서 조인을 수행하는 두 테이블 중 작은 쪽을 선택하여 해시 테이블을 만들어 메모리(PGA 영역)에 저장하고 해시 함수를 사용해서 각 행을 특정 &quot;해시 버킷&quot;에 할당한다.</p>
</li>
<li><p>프로브 단계(Probe phase): 조인 단계에서 다른 테이블을 순회하며 각 행에 대해 동일한 해시 함수를 사용하여 해당 행이 어떤 버킷에 속하는지 결정하고 이 버킷의 모든 행과 해당 행을 비교하여 조인 조건을 만족한다.</p>
</li>
<li><p>이 방법은 조인할 테이블 중 하나가 메모리에 적합할 만큼 충분히 작아야 한다. 그렇지 않으면 해시 테이블이 메모리를 넘어서 디스크로까지 넘어가고 이는 성능 저하를 초래한다.</p>
</li>
<li><p>HASH JOIN은 등가 조인('=' 연산자를 사용하는 조인)에만 사용할 수 있고 비등가 조인에는 사용할 수 없다.</p>
<pre><code class="language-sql">  SET SESSION optimizer_switch='join_cache_incremental=on';
  SET SESSION optimizer_switch='join_cache_hashed=on';
  SET SESSION optimizer_switch='join_cache_bka=on';
  SET SESSION join_cache_level=3;

  select count(*) from t1 join t2 on t1.c2 = t2.c2;
  explain select count(*) from t1 join t2 on t1.c2 = t2.c2;

  -- join_cache_hashed를 off로 하면 BNL 결과가 나온다.
  -- SET SESSION optimizer_switch='join_cache_hashed=on';
  -- explain select count(*) from t1 join t2 on t1.c2 = t2.c2;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ea489a42-816e-4bf9-8dd8-5c073d1c1a1d/image.png" /></p>
</blockquote>
</li>
</ul>
<h1 id="grouping">GROUPING</h1>
<blockquote>
<p>💡 GROUP BY절은 결과 집합을 특정 열의 값에 따라 그룹화하는데 사용된다.</p>
<p>HAVING은 GROUP BY 절과 함께 사용해야 하며 그룹에 대한 조건을 적용하는데 사용된다.</p>
</blockquote>
<h2 id="group-by">GROUP BY</h2>
<ul>
<li><p>GROUP BY를 활용한 메뉴가 존재하는 카테고리 그룹 조회</p>
<pre><code class="language-sql">  SELECT
         category_code
    FROM tbl_menu
   GROUP BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0bbfa2d7-574d-4822-903a-8c4d1842de0a/image.png" /></p>
</blockquote>
</li>
<li><p>COUNT 함수 활용</p>
<pre><code class="language-sql">  SELECT
         category_code
       , COUNT(*)
    FROM tbl_menu
   GROUP BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/593ccd97-7857-4236-8342-82769d927e7c/image.png" /></p>
</blockquote>
</li>
<li><p>SUM 함수 활용</p>
<pre><code class="language-sql">  SELECT
         category_code
       , SUM(menu_price)
    FROM tbl_menu
   GROUP BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/da1e3bc7-5d68-4cd1-ae1c-4d0731d83ba4/image.png" /></p>
</blockquote>
</li>
<li><p>AVG 함수 활용</p>
<pre><code class="language-sql">  SELECT
         category_code
       , AVG(menu_price)
    FROM tbl_menu
   GROUP BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/694a4811-a085-47d5-a721-b812dfe4dea4/image.png" /></p>
</blockquote>
</li>
<li><p>2개 이상의 그룹 생성</p>
<pre><code class="language-sql">  SELECT
         menu_price
       , category_code
    FROM tbl_menu
   GROUP BY menu_price, category_code; </code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2f79aff4-8823-4126-b145-bab54d8b5c65/image.png" /></p>
</blockquote>
</li>
<li><p>join과 함께 사용</p>
<pre><code class="language-sql">  SELECT
         a.category_code
       , b.category_name
       , AVG(menu_price)
    FROM tbl_menu a
    JOIN tbl_category b ON (a.category_code = b.category_code)
   GROUP BY a.category_code, b.category_name;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/30ac87f2-dc19-4051-95b4-7574083b2730/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="having">HAVING</h2>
<ul>
<li><p>HAVING을 활용해 5번(중식) 카테고리부터 8번(커피) 카테고리까지의 메뉴 카테고리 번호 조회</p>
<pre><code class="language-sql">  SELECT                               
         category_code                 
    FROM tbl_menu                      
   GROUP BY category_code              
  HAVING category_code BETWEEN 5 AND 8;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/356d3ca1-e4b5-4398-b789-eb5f85f57e4d/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="rollup">ROLLUP</h2>
<ul>
<li><p>컬럼 한 개를 활용한 ROLLUP(카테고리별 총합)</p>
<pre><code class="language-sql">  SELECT
         category_code
       , SUM(menu_price)
    FROM tbl_menu
   GROUP BY category_code
    WITH ROLLUP;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/39967330-85da-4f69-8955-4f4bd02d3e52/image.png" /></p>
</blockquote>
</li>
<li><p>컬럼 두 개를 활용한 ROLLUP(같은 메뉴 가격별 총합 및 해당 메뉴 가격별 같은 카테고리의 총합과 전체 )</p>
<ul>
<li><p>ROLLUP을 통해 먼저 나온 컬럼의 총합을 구하고 이후 나오는 컬럼과의 합도 구하는 방식이다.</p>
<pre><code class="language-sql">SELECT
     menu_price
   , category_code
   , SUM(menu_price)
FROM tbl_menu
GROUP BY menu_price, category_code
WITH ROLLUP;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d52ae7c2-9f31-4e31-bc0f-48a8aa548106/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
<li><p>연도별, 월별, 상품별 합계를 구할 수도 있다.</p>
<pre><code class="language-sql">  CREATE TABLE sales (
      code INT AUTO_INCREMENT,
      year VARCHAR(4),
      month VARCHAR(2),
      product VARCHAR(50),
      amount DECIMAL(10,2),
      PRIMARY KEY(code)
  );

  INSERT INTO sales (code, year, month, product, amount) VALUES
  (null, '2023', LPAD('1', 2, '0'), 'Product A', 1000.00),
  (null, '2023', LPAD('1', 2, '0'), 'Product B', 1500.00),
  (null, '2023', LPAD('2', 2, '0'), 'Product A', 2000.00),
  (null, '2023', LPAD('2', 2, '0'), 'Product B', 2500.00),
  (null, '2023', LPAD('3', 2, '0'), 'Product A', 1200.00),
  (null, '2024', LPAD('3', 2, '0'), 'Product B', 1700.00);

  SELECT
         year
         , month
         , product
         , SUM(amount) AS total_sales
    FROM sales
   GROUP BY year, month, product WITH ROLLUP;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2fbb8a67-beb0-4784-9b6c-c7ec35c66d46/image.png" /></p>
</blockquote>
</li>
</ul>
<h1 id="subqueries">SUBQUERIES</h1>
<blockquote>
<p>💡 SUBQUERY는 다른 쿼리 내에서 실행되는 쿼리이다.</p>
<p>SUBQUERY의 결과를 활용해서 복잡한 MAINQUERY를 작성해 한번에 여러 작업을 수행할 수 있다.</p>
</blockquote>
<h2 id="subquery-활용">SUBQUERY 활용</h2>
<ul>
<li><p>서브쿼리와 메인 쿼리를 활용한 다중열 결과 조회</p>
<ul>
<li><p>서브쿼리</p>
<pre><code class="language-sql">SELECT
     category_code
FROM tbl_menu
WHERE menu_name = '민트미역국';</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1e883b74-8c62-44fe-b7a5-388499f8e3eb/image.png" /></p>
</blockquote>
</li>
<li><p>메인쿼리</p>
<pre><code class="language-sql">SELECT
     menu_code
   , menu_name
   , menu_price
   , category_code
   , orderable_status
FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9e39c5dd-fe9a-4185-983d-4ecce938efa2/image.png" /></p>
</blockquote>
</li>
<li><p>서브쿼리를 활용한 메인 쿼리</p>
<pre><code class="language-sql">SELECT                                                   
     menu_code                                         
   , menu_name                                         
   , menu_price                                        
   , category_code                                     
   , orderable_status                                  
FROM tbl_menu                                          
WHERE category_code = (SELECT category_code             
                        FROM tbl_menu                  
                       WHERE menu_name = '민트미역국');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9335670e-7289-4173-9382-247265e05479/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
<li><p>SUBQUERY를 활용해 가장 많은 메뉴가 포함된 카테고리 조회</p>
<ul>
<li><p>서브쿼리</p>
<pre><code class="language-sql">SELECT
     COUNT(*) AS 'count'
FROM tbl_menu
GROUP BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f46d8961-1699-48f9-9f16-f0b9cd81a3d4/image.png" /></p>
</blockquote>
</li>
<li><p>서브쿼리를 활용한 메인 쿼리</p>
<ul>
<li>FROM 절에 쓰인 서브쿼리(derived table, 파생 테이블)는 반드시 자신의 별칭이 있어야 한다.(feat. 이러한 서브쿼리를 ‘인라인 뷰’라고 한다.)</li>
</ul>
<pre><code class="language-sql">SELECT
     MAX(count)
FROM (SELECT COUNT(*) AS 'count'
        FROM tbl_menu
       GROUP BY category_code) AS countmenu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f84a30e0-798c-476f-ad69-d88c30c4fae1/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h2 id="상관-서브쿼리">상관 서브쿼리</h2>
<ul>
<li><p>메인 쿼리가 서브쿼리의 결과에 영향을 주는 경우 상관 서브쿼리라고 한다.</p>
</li>
<li><p>SUBQUERY를 활용해 카테고리별 평균 가격보다 높은 가격의 메뉴 조회</p>
<ul>
<li><p>서브쿼리</p>
<pre><code class="language-sql">SELECT
     AVG(menu_price)
FROM tbl_menu
WHERE category_code = 4;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2f31de67-eb0e-4117-8b5a-ba0f9f1917fe/image.png" /></p>
</blockquote>
</li>
<li><p>서브쿼리를 활용한 메인 쿼리</p>
<pre><code class="language-sql">SELECT                                                   
     menu_code                                         
   , menu_name                                         
   , menu_price                                        
   , category_code                                     
   , orderable_status                                  
FROM tbl_menu a     

WHERE menu_price &gt; (SELECT AVG(menu_price)
                     FROM tbl_menu                  
                    WHERE category_code = a.category_code);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/883e00c9-12b2-4db3-98f6-6a033e27d69d/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h2 id="exists">EXISTS</h2>
<ul>
<li><p>조회 결과가 있을 때 true 아니면 false</p>
</li>
<li><p>EXISTS와 SUBQUERY를 활용한 메뉴가 있는 카테고리 조회</p>
<pre><code class="language-sql">  SELECT
         category_name
    FROM tbl_category a
   WHERE EXISTS(SELECT 1
                  FROM tbl_menu b
                  WHERE b.category_code = a.category_code)
       ORDER BY 1;</code></pre>
</li>
</ul>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/278662cf-bac5-459d-8e4c-786ea9a0a9ae/image.png" /></p>
</blockquote>
<ul>
<li>파생 테이블과 비슷한 개념이며 코드의 가독성과 재사용성을 위해 파생 테이블 대신 사용하게 된다.)</li>
</ul>
<h2 id="ctecommon-table-expressions">CTE(Common Table Expressions)</h2>
<ul>
<li><p>FROM절에서만 사용 됨(JOIN일 시 JOIN 구문에서도 가능)</p>
</li>
<li><p>인라인 뷰로 쓰인 서브쿼리(FROM 절에 쓰인 서브쿼리)를 미리 정의하고 메인쿼리가 심플해 질 수 있도록 사용하는 문법</p>
<pre><code class="language-sql">  WITH menucate AS (
      SELECT menu_name
           , category_name
        FROM tbl_menu a
        JOIN tbl_category b ON a.category_code = b.category_code
  )
  SELECT
         *
    FROM menucate
   ORDER BY menu_name;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/59d77d16-3609-4a67-bf8d-af982e848506/image.png" /></p>
</blockquote>
</li>
</ul>
<h1 id="set-operators">SET OPERATORS</h1>
<blockquote>
<p>💡 SET 연산자는 두 개 이상의 SELECT문의 결과 집합을 결합하는데 사용한다.</p>
<p>SET 연산자를 통해 결합하는 결과 집합의 컬럼이 동일해야 한다.</p>
</blockquote>
<h2 id="union">UNION</h2>
<ul>
<li><p>두 개 이상의 SELECT 문의 결과를 결합하여 중복된 레코드를 제거한 후 반환하는 SQL 연산자이다.</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , menu_name
       , menu_price
       , category_code
       , orderable_status
    FROM tbl_menu
   WHERE category_code = 10
   UNION
  SELECT
         menu_code
       , menu_name
       , menu_price
       , category_code
       , orderable_status
    FROM tbl_menu
   WHERE menu_price &lt; 9000;</code></pre>
</li>
</ul>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/91fc7180-4b64-4b28-b9f1-009696cf9361/image.png" /></p>
</blockquote>
<h2 id="union-all">UNION ALL</h2>
<ul>
<li><p>두 개 이상의 SELECT 문의 결과를 결합하며 중복된 레코드를 제거하지 않고 모두 반환하는 SQL 연산자이다.</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , menu_name
       , menu_price
       , category_code
       , orderable_status
    FROM tbl_menu
   WHERE category_code = 10
   UNION ALL
  SELECT
         menu_code
       , menu_name
       , menu_price
       , category_code
       , orderable_status
    FROM tbl_menu
   WHERE menu_price &lt; 9000;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/7190f60d-cf07-4322-907e-5a7894863707/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="intersect">INTERSECT</h2>
<ul>
<li><p>두 SELECT 문의 결과 중 공통되는 레코드만을 반환하는 SQL 연산자이다.</p>
</li>
<li><p>MySQL은 본래 기본적으로 INTERSECT를 제공하지 않는다. 하지만 INNER JOIN 또는 IN 연산자 활용해서 구현하는 것은 가능하다.</p>
<ul>
<li><p>INNER JOIN 활용</p>
<pre><code class="language-sql">SELECT
     a.menu_code
   , a.menu_name
   , a.menu_price
   , a.category_code
   , a.orderable_status
FROM tbl_menu a
INNER JOIN (SELECT menu_code
                , menu_name
                , menu_price
                , category_code
                , orderable_status
             FROM tbl_menu
            WHERE menu_price &lt; 9000) b ON (a.menu_code = b.menu_code)
WHERE a.category_code = 10;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2da232cf-44c4-4667-b684-08a2248d0db2/image.png" /></p>
</blockquote>
</li>
<li><p>IN 연산자 활용</p>
<pre><code class="language-sql">SELECT
     a.menu_code
   , a.menu_name
   , a.menu_price
   , a.category_code
   , a.orderable_status
FROM tbl_menu a
WHERE category_code = 10 
 AND menu_code IN (SELECT menu_code
                     FROM tbl_menu
                    WHERE menu_price &lt; 9000);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/541f0788-366a-4517-b591-a75b82f7c528/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h2 id="minus">MINUS</h2>
<ul>
<li><p>첫 번째 SELECT 문의 결과에서 두 번째 SELECT 문의 결과가 포함하는 레코드를 제외한 레코드를 반환하는 SQL 연산자이다.</p>
</li>
<li><p>MySQL은 MINUS를 제공하지 않는다. 하지만 LEFT JOIN을 활용해서 구현하는 것은 가능하다.</p>
<pre><code class="language-sql">  SELECT
         a.menu_code
       , a.menu_name
       , a.menu_price
       , a.category_code
       , a.orderable_status
    FROM tbl_menu a
    LEFT JOIN (SELECT menu_code
                    , menu_name
                    , menu_price
                    , category_code
                    , orderable_status
                 FROM tbl_menu b
                WHERE menu_price &lt; 9000) b ON (a.menu_code = b.menu_code)
   WHERE a.category_code = 10
     AND b.menu_code IS NULL;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e47e0dfc-3b69-4e11-a13e-2e701eb6bc01/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="6가지-절의-종류와-실행-순서">6가지 절의 종류와 실행 순서</h2>
<p>ex)</p>
<blockquote>
<pre><code class="language-sql">select                            -- 5th
from (join)                       -- 1st
where (한 행 씩 조건을 분별)        -- 2nd
group by                          -- 3rd
having (그룹별로 조건)              -- 4th
order by (limit)                  -- 6th</code></pre>
</blockquote>
<ul>
<li>활용 데이터셋
```sql</li>
<li><ul>
<li>테이블 삭제
DROP TABLE IF EXISTS tbl_payment_order CASCADE;
DROP TABLE IF EXISTS tbl_payment CASCADE;
DROP TABLE IF EXISTS tbl_order_menu CASCADE;
DROP TABLE IF EXISTS tbl_order CASCADE;
DROP TABLE IF EXISTS tbl_menu CASCADE;
DROP TABLE IF EXISTS tbl_category CASCADE;</li>
</ul>
</li>
</ul>
<p>-- 테이블 생성
-- category 테이블 생성
CREATE TABLE IF NOT EXISTS tbl_category
(
    category_code    INT AUTO_INCREMENT COMMENT '카테고리코드',
    category_name    VARCHAR(30) NOT NULL COMMENT '카테고리명',
    ref_category_code    INT COMMENT '상위카테고리코드',
    CONSTRAINT pk_category_code PRIMARY KEY (category_code),
    CONSTRAINT fk_ref_category_code FOREIGN KEY (ref_category_code) REFERENCES tbl_category (category_code)
) ENGINE=INNODB COMMENT '카테고리';</p>
<p>CREATE TABLE IF NOT EXISTS tbl_menu
(
    menu_code    INT AUTO_INCREMENT COMMENT '메뉴코드',
    menu_name    VARCHAR(30) NOT NULL COMMENT '메뉴명',
    menu_price    INT NOT NULL COMMENT '메뉴가격',
    category_code    INT NOT NULL COMMENT '카테고리코드',
    orderable_status    CHAR(1) NOT NULL COMMENT '주문가능상태',
    CONSTRAINT pk_menu_code PRIMARY KEY (menu_code),
    CONSTRAINT fk_category_code FOREIGN KEY (category_code) REFERENCES tbl_category (category_code)
) ENGINE=INNODB COMMENT '메뉴';</p>
<p>CREATE TABLE IF NOT EXISTS tbl_order
(
    order_code    INT AUTO_INCREMENT COMMENT '주문코드',
    order_date    VARCHAR(8) NOT NULL COMMENT '주문일자',
    order_time    VARCHAR(8) NOT NULL COMMENT '주문시간',
    total_order_price    INT NOT NULL COMMENT '총주문금액',
    CONSTRAINT pk_order_code PRIMARY KEY (order_code)
) ENGINE=INNODB COMMENT '주문';</p>
<p>CREATE TABLE IF NOT EXISTS tbl_order_menu
(
    order_code INT NOT NULL COMMENT '주문코드',
    menu_code    INT NOT NULL COMMENT '메뉴코드',
    order_amount    INT NOT NULL COMMENT '주문수량',
    CONSTRAINT pk_comp_order_menu_code PRIMARY KEY (order_code, menu_code),
    CONSTRAINT fk_order_menu_order_code FOREIGN KEY (order_code) REFERENCES tbl_order (order_code),
    CONSTRAINT fk_order_menu_menu_code FOREIGN KEY (menu_code) REFERENCES tbl_menu (menu_code)
) ENGINE=INNODB COMMENT '주문별메뉴';</p>
<p>CREATE TABLE IF NOT EXISTS tbl_payment
(
    payment_code    INT AUTO_INCREMENT COMMENT '결제코드',
    payment_date    VARCHAR(8) NOT NULL COMMENT '결제일',
    payment_time    VARCHAR(8) NOT NULL COMMENT '결제시간',
    payment_price    INT NOT NULL COMMENT '결제금액',
    payment_type    VARCHAR(6) NOT NULL COMMENT '결제구분',
    CONSTRAINT pk_payment_code PRIMARY KEY (payment_code)
) ENGINE=INNODB COMMENT '결제';</p>
<p>CREATE TABLE IF NOT EXISTS tbl_payment_order
(
    order_code    INT NOT NULL COMMENT '주문코드',
    payment_code    INT NOT NULL COMMENT '결제코드',
    CONSTRAINT pk_comp_payment_order_code PRIMARY KEY (payment_code, order_code),
    CONSTRAINT fk_payment_order_order_code FOREIGN KEY (order_code) REFERENCES tbl_order (order_code),
    CONSTRAINT fk_payment_order_payment_code FOREIGN KEY (order_code) REFERENCES tbl_payment (payment_code)
) ENGINE=INNODB COMMENT '결제별주문';</p>
<p>-- 데이터 삽입
INSERT INTO tbl_category VALUES (null, '식사', null);
INSERT INTO tbl_category VALUES (null, '음료', null);
INSERT INTO tbl_category VALUES (null, '디저트', null);
INSERT INTO tbl_category VALUES (null, '한식', 1);
INSERT INTO tbl_category VALUES (null, '중식', 1);</p>
<p>INSERT INTO tbl_category VALUES (null, '일식', 1);
INSERT INTO tbl_category VALUES (null, '퓨전', 1);
INSERT INTO tbl_category VALUES (null, '커피', 2);
INSERT INTO tbl_category VALUES (null, '쥬스', 2);
INSERT INTO tbl_category VALUES (null, '기타', 2);</p>
<p>INSERT INTO tbl_category VALUES (null, '동양', 3);
INSERT INTO tbl_category VALUES (null, '서양', 3);</p>
<p>INSERT INTO tbl_menu VALUES (null, '열무김치라떼', 4500, 8, 'Y');
INSERT INTO tbl_menu VALUES (null, '우럭스무디', 5000, 10, 'Y');
INSERT INTO tbl_menu VALUES (null, '생갈치쉐이크', 6000, 10, 'Y');
INSERT INTO tbl_menu VALUES (null, '갈릭미역파르페', 7000, 10, 'Y');
INSERT INTO tbl_menu VALUES (null, '앙버터김치찜', 13000, 4, 'N');</p>
<p>INSERT INTO tbl_menu VALUES (null, '생마늘샐러드', 12000, 4, 'Y');
INSERT INTO tbl_menu VALUES (null, '민트미역국', 15000, 4, 'Y');
INSERT INTO tbl_menu VALUES (null, '한우딸기국밥', 20000, 4, 'Y');
INSERT INTO tbl_menu VALUES (null, '홍어마카롱', 9000, 12, 'Y');
INSERT INTO tbl_menu VALUES (null, '코다리마늘빵', 7000, 12, 'N');</p>
<p>INSERT INTO tbl_menu VALUES (null, '정어리빙수', 10000, 10, 'Y');
INSERT INTO tbl_menu VALUES (null, '날치알스크류바', 2000, 10, 'Y');
INSERT INTO tbl_menu VALUES (null, '직화구이젤라또', 8000, 12, 'Y');
INSERT INTO tbl_menu VALUES (null, '과메기커틀릿', 13000, 6, 'Y');
INSERT INTO tbl_menu VALUES (null, '죽방멸치튀김우동', 11000, 6, 'N');</p>
<p>INSERT INTO tbl_menu VALUES (null, '흑마늘아메리카노', 9000, 8, 'Y');
INSERT INTO tbl_menu VALUES (null, '아이스가리비관자육수', 6000, 10, 'Y');
INSERT INTO tbl_menu VALUES (null, '붕어빵초밥', 35000, 6, 'Y');
INSERT INTO tbl_menu VALUES (null, '까나리코코넛쥬스', 9000, 9, 'Y');
INSERT INTO tbl_menu VALUES (null, '마라깐쇼한라봉', 22000, 5, 'N');</p>
<p>INSERT INTO tbl_menu VALUES (null, '돌미나리백설기', 5000, 11, 'Y');</p>
<p>COMMIT;</p>
<pre><code></code></pre>