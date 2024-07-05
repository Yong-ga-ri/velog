<h1 id="select">SELECT</h1>
<blockquote>
<p>💡 SELECT절은 MariaDB의 가장 기본적인 명령어로 특정 테이블에서 원하는 데이터를 조회해서 가져오는데 사용 된다.</p>
</blockquote>
<h2 id="select-clause">SELECT CLAUSE</h2>
<ul>
<li><p>SELECT 문을 사용하여 모든 열에서 데이터 검색</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , menu_name
       , menu_price
       , category_code
       , orderable_status
    FROM tbl_menu;</code></pre>
<pre><code class="language-sql">  SELECT 
         *
    FROM tbl_menu;</code></pre>
</li>
</ul>
<h2 id="selectonly">SELECT(only)</h2>
<ul>
<li><p>SELECT는 FROM절 없이 단순 테스트를 위한 단독으로 사용 할 수 있는 절이다.</p>
</li>
<li><p>연산자 결과 확인</p>
<pre><code class="language-sql">  SELECT 7 + 3;   
  SELECT 7 * 3;
  SELECT 7 % 3;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d26825e6-82ca-436d-a72d-209a4f33ec5e/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/015695ff-d38f-45c4-8d5c-7a9fa767a655/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3a774093-fd00-42df-88ca-3ad98673a4e9/image.png" /></p>
</blockquote>
</li>
<li><p>내장함수 결과 확인</p>
<pre><code class="language-sql">  SELECT NOW();
  SELECT CONCAT('홍',' ','길동');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/01545b49-cc71-41db-8e7a-445fb2b15217/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/b668f4b7-0c34-4a73-a7ee-175025d2af49/image.png" /></p>
</blockquote>
</li>
</ul>
<h1 id="order_by-clause">ORDER_BY CLAUSE</h1>
<blockquote>
<p>💡 ORDER BY절은 select문과 함께 사용하며 결과 집합을 특정 열이나 열들의 값에 따라 정렬하는 데 사용한다.</p>
</blockquote>
<h2 id="order-by">ORDER BY</h2>
<ul>
<li><p>ORDER BY 절을 사용하여 결과 집합을 하나의 열로 정렬</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , menu_name
       , menu_price
    FROM tbl_menu
  --  ORDER BY menu_price ASC;    -- 오름차순(default)
  --  ORDER BY menu_price DESC;    -- 내림차순
   ORDER BY menu_price;</code></pre>
<blockquote>
<p><code>실행결과</code>
<img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d4ce9b2b-f6ad-469f-aa82-fb554b9a23e7/image.png" /></p>
</blockquote>
</li>
<li><p>ORDER BY 절을 사용하여 결과 집합을 여러 열로 정렬</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , menu_name
       , menu_price
    FROM tbl_menu
   ORDER BY menu_price DESC, menu_name ASC;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/60d1a0d7-872c-4d86-95fe-1ce9cdfb7747/image.png" /></p>
</blockquote>
</li>
<li><p>별칭을 달아줄 수도 있다.</p>
<pre><code class="language-sql">  SELECT
         menu_code AS '메뉴코드'
       , menu_price AS '메뉴가격'
       , menu_code * menu_price AS '연산결과'
    FROM tbl_menu
   ORDER BY 연산결과 DESC;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ffc1e81b-1f5a-4b7e-886f-db07419bb93f/image.png" /></p>
</blockquote>
</li>
<li><p>ORDER BY 절을 사용하여 사용자 지정 목록을 사용하여 데이터 정렬</p>
<ul>
<li><p>맨 왼쪽의 값이 2번째 인자 이후의 값과 일치하면 해당 위치 값을 반환함
(이렇게 반환된 값은 정렬 우선순위를 나타낸다.)</p>
<pre><code class="language-sql">SELECT FIELD('A', 'A', 'B', 'C');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f402c1cc-4e80-4bf5-b095-f7e6cd2eec2a/image.png" /></p>
</blockquote>
<pre><code class="language-sql">SELECT 
     FIELD(orderable_status, 'N', 'Y')
FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/cd7fa52a-6ea2-4aee-872a-97c0cb1bf2db/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
<li><p>field 함수를 이용하여 특정한 값을 우선적으로 정렬할 수 있다.</p>
<pre><code class="language-sql">  SELECT
         menu_name
       , orderable_status
    FROM tbl_menu
   ORDER BY FIELD(orderable_status, 'N', 'Y');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3f1bdb8d-5f3f-4333-b435-6a086a4a1d76/image.png" /></p>
</blockquote>
</li>
<li><p>null값이 있는 컬럼에 대한 정렬</p>
<ul>
<li><p>오름차순 시 NULL 처음으로(DEFAULT)</p>
<p>```sql
SELECT</p>
<pre><code> category_code</code></pre><p>   , category_name
   , ref_category_code
FROM tbl_category</p>
</li>
<li><ul>
<li>ORDER BY ref_category_code ASC;
ORDER BY ref_category_code;    -- ASC 생략 가능<pre><code></code></pre></li>
</ul>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a5d37406-256b-4857-9098-6d4c5b50dadd/image.png" /></p>
</blockquote>
</li>
<li><p>오름차순 시 NULL 마지막으로(IS NULL ASC)</p>
<pre><code class="language-sql">SELECT
     category_code
   , category_name
   , ref_category_code
FROM tbl_category
ORDER BY -ref_category_code DESC;    -- 마이너스(-)부호를 붙이고 DESC를 적용해 주면 된다.
                                  -- 마이너스 부호는 null을 제외하고 정렬을 반대로 뒤집는 것이다.</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a97a7a0e-7bd3-4853-b48c-80055a96ff3c/image.png" /></p>
</blockquote>
</li>
<li><p>내림차순 시 NULL 마지막으로(DEFAULT)</p>
<pre><code class="language-sql">SELECT
     category_code
   , category_name
   , ref_category_code
FROM tbl_category
ORDER BY ref_category_code DESC;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a99bbbe1-0cf0-415d-b0e9-b3d7e4d19697/image.png" /></p>
</blockquote>
</li>
<li><p>내림차순 시 NULL 처음으로(IS NULL DESC)</p>
<pre><code class="language-sql">SELECT
     category_code
   , category_name
   , ref_category_code
FROM tbl_category
ORDER BY -ref_category_code ASC;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/89148132-7866-4fbd-afb8-4ccf399b3fa4/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h1 id="where-clause">WHERE CLAUSE</h1>
<blockquote>
<p>💡 WHERE절은 특정 조건에 맞는 레코드만을 선택하는데 사용되며 다양한 방법으로 조건을 설정할 수 있다.</p>
</blockquote>
<h2 id="비교-연산자-활용">비교 연산자 활용</h2>
<ul>
<li>같음(=) 연산자 예제와 함께 WHERE절 사용</li>
</ul>
<pre><code class="language-sql">SELECT
       menu_name
     , menu_price
     , orderable_status
  FROM tbl_menu
 WHERE menu_price = 13000;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/552a598a-0d8d-49fc-9c71-bf8d1750cd63/image.png" /></p>
</blockquote>
<ul>
<li><p>같지 않음(!=, &lt;&gt;) 연산자와 함께 WHERE절 사용</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , menu_name
       , orderable_status
    FROM tbl_menu
  --  WHERE orderable_status &lt;&gt; 'Y';
   WHERE orderable_status != 'Y';</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d207bcc0-e98c-43df-863d-3536127bf25b/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="and-operator">AND OPERATOR</h2>
<ul>
<li>AND 연산자와 함께 WHERE절 사용<ul>
<li>0과 NULL이 아닌 값들일 경우 1이다.</li>
<li>하나라도 0이거나 둘 다 0일 경우 0을 반환한다.(이미 0이면 뒤를 연산하지 않는다.)</li>
<li>0이 아닌 값과 NULL이거나 둘 다 NULL일 경우 NULL을 반환한다.</li>
<li>AND 결과 표</li>
</ul>
</li>
</ul>
<pre><code>|  | TRUE | FALSE | NULL |
| --- | --- | --- | --- |
| TRUE | TRUE | FALSE | NULL |
| FALSE | FALSE | FALSE | FALSE |
| NULL | NULL | FALSE | NULL |

  - 0이 아닌 값은 TRUE
  - 0인 값은 FALSE
  - NULL 값은 NULL

```sql
SELECT 1 AND 2;
SELECT 1 AND 0, 0 AND 1, 0 AND 0, 0 AND NULL;
SELECT 1 AND NULL, NULL AND NULL;
```

&gt; `실행결과`
&gt; 
&gt; 
&gt; ![](https://velog.velcdn.com/images/rlfgks97/post/dd81fd39-fe54-46c9-a7c8-71d64e31a8e0/image.png)
&gt; 
&gt; ![](https://velog.velcdn.com/images/rlfgks97/post/66f1be24-c614-4a22-a32d-1b8f491e8bce/image.png)
&gt; 
&gt; ![](https://velog.velcdn.com/images/rlfgks97/post/9001a1a6-938f-4de3-8a9b-f628616eae56/image.png)
&gt; </code></pre><pre><code class="language-sql">SELECT
       menu_name
     , menu_price
     , category_code
     , orderable_status
  FROM tbl_menu
 WHERE orderable_status = 'Y'
   AND category_code = 10;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/8a33bb0b-4819-48fb-add8-4c955ca7585c/image.png" /></p>
</blockquote>
<h2 id="or-operator">OR OPERATOR</h2>
<ul>
<li>OR 연산자와 함께 WHERE절 사용<ul>
<li>둘 다 NULL이 아니면서 하나라도 0이 아닌 값이 있을 경우 1을 반환한다.(이미 1이면 뒤를 연산하지 않는다.)</li>
<li>둘 다 0일 경우 0을 반환한다.</li>
<li>1을 제외한 값들에서 하나라도 NULL이거나 둘 다 NULL일 경우 NULL을 반환한 다.</li>
<li>OR 결과 표</li>
</ul>
</li>
</ul>
<pre><code>|  | TRUE | FALSE | NULL |
| --- | --- | --- | --- |
| TRUE | TRUE | TRUE | TRUE |
| FALSE | TRUE | FALSE | NULL |
| NULL | TRUE | NULL | NULL |
    - 0이 아닌 값은 TRUE
    - 0인 값은 FALSE
    - NULL 값은 NULL

```sql
SELECT 1 OR 1, 1 OR 0, 0 OR 1;
SELECT 0 OR 0;
SELECT 1 OR NULL, 0 OR NULL, NULL or NULL;
```

&gt; `실행결과`
&gt; 
&gt; 
&gt; ![](https://velog.velcdn.com/images/rlfgks97/post/9cf43b95-a92b-4bf9-83ea-f647a6c0eb1d/image.png)
&gt; 
&gt; ![](https://velog.velcdn.com/images/rlfgks97/post/e4e8c096-85a9-4873-a60c-a8678aea83a2/image.png)
&gt; 
&gt; ![](https://velog.velcdn.com/images/rlfgks97/post/4342a43b-7390-4fe5-a6c2-5ff22ca85ea0/image.png)
&gt; </code></pre><pre><code class="language-sql">SELECT
       menu_name
     , menu_price
     , category_code
     , orderable_status
  FROM tbl_menu
 WHERE orderable_status = 'Y'
    OR category_code = 10
 ORDER BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f572434e-371c-4919-8b2c-012f23d6e48e/image.png" /></p>
</blockquote>
<ul>
<li><p>AND와 OR의 우선순위</p>
<ul>
<li><p>AND가 OR보다 우선순위가 높다.</p>
</li>
<li><p>OR의 우선순위를 높이고 싶다면 소괄호(())를 사용한다.</p>
<pre><code class="language-sql">SELECT 1 OR 0 AND 0;
SELECT (1 OR 0) AND 0;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9d538f86-979c-42ce-8b7e-765781956043/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/7a0161c4-ed29-4072-9707-ede49668ab86/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<pre><code class="language-sql">SELECT
       menu_code
     , menu_name
     , menu_price
     , category_code
     , orderable_status
  FROM tbl_menu
 WHERE category_code = 4
    OR menu_price = 9000
   AND menu_code &gt; 10;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e625b3e0-a745-498b-b52d-2ad5987bf96e/image.png" /></p>
</blockquote>
<h2 id="between-operator">BETWEEN OPERATOR</h2>
<ul>
<li><p>BETWEEN 연산자 예제와 함께 WHERE절 사용</p>
<pre><code class="language-sql">  SELECT
         menu_name
       , menu_price
       , category_code
    FROM tbl_menu
   WHERE menu_price &gt;= 10000
     AND menu_price &lt;= 25000
   ORDER BY menu_price;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/be8ba5ec-855a-4c5d-86a7-0d27a0326b6d/image.png" /></p>
</blockquote>
</li>
</ul>
<pre><code class="language-sql">SELECT
       menu_name
     , menu_price
     , category_code
  FROM tbl_menu
 WHERE menu_price BETWEEN 10000 AND 25000
 ORDER BY menu_price;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3df6c6b3-8a85-4e42-bca5-1bfa8372f608/image.png" /></p>
</blockquote>
<ul>
<li><p>부정 표현</p>
<pre><code class="language-sql">  SELECT
         menu_name
       , menu_price
       , category_code
    FROM tbl_menu
   WHERE menu_price NOT BETWEEN 10000 AND 25000
   ORDER BY menu_price;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0e45d560-d747-410c-85e5-b6c3517a46a5/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="like-operator">LIKE OPERATOR</h2>
<ul>
<li><p>LIKE 연산자 예제와 함께 MySQL WHERE절 사용</p>
<pre><code class="language-sql">  SELECT
          menu_name
        , menu_price
     FROM tbl_menu
    WHERE menu_name LIKE '%마늘%'
    ORDER BY menu_name;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/89cdbc72-4c1f-486f-9e1e-319aea1468a2/image.png" /></p>
</blockquote>
</li>
</ul>
<pre><code class="language-sql">SELECT
       menu_code
     , menu_name
     , menu_price
     , category_code
     , orderable_status
  FROM tbl_menu
 WHERE menu_price &gt; 5000
   AND category_code = 10
    AND menu_name LIKE '%갈치%';</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/88f52b85-4716-4a64-aaaa-aafbce8a23ea/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/cbc0172b-a5cc-4aa8-87dd-5afb64a045ce/image.png" /></p>
</blockquote>
<ul>
<li><p>부정 표현</p>
<pre><code class="language-sql">  SELECT
          menu_name
        , menu_price
     FROM tbl_menu
    WHERE menu_name NOT LIKE '%마늘%'
    ORDER BY menu_name;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/30a8c829-2321-4bd3-acda-433b4707193e/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="in-operator">IN OPERATOR</h2>
<ul>
<li>IN 연산자 예제와 함께 WHERE절 사용</li>
</ul>
<pre><code class="language-sql">SELECT 
        menu_name
      , category_code
   FROM tbl_menu
  WHERE category_code IN (4, 5, 6)
  ORDER BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/174588c2-5ee9-46ec-9817-16dceb2c6b93/image.png" /></p>
</blockquote>
<ul>
<li><p>부정 표현</p>
<pre><code class="language-sql">  SELECT 
          menu_name
        , category_code
     FROM tbl_menu
    WHERE category_code NOT IN (4, 5, 6)
    ORDER BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/8e4887c0-6fde-4a32-9f44-ffe5490a55e1/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="is-null-operator">IS NULL OPERATOR</h2>
<ul>
<li><p>IS NULL 연산자와 함께 WHERE절 사용</p>
</li>
<li><p>IS NOT NULL로 부정 표현 사용 가능</p>
<pre><code class="language-sql">  SELECT 
         category_code, 
         category_name, 
         ref_category_code
    FROM tbl_category
   -- WHERE ref_category_code IS NOT NULL;
   WHERE ref_category_code IS NULL;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/b99877f3-362c-4cdf-9398-2db3915ae71f/image.png" /></p>
</blockquote>
</li>
</ul>
<h1 id="distinct">DISTINCT</h1>
<blockquote>
<p>💡 DISTINCT는 중복된 값을 제거하는데 사용된다.
컬럼에 있는 컬럼값들의 종류를 쉽게 파악할 수 있다.</p>
</blockquote>
<ul>
<li><p>단일열 DISTINCT 사용</p>
<pre><code class="language-sql">  SELECT 
         category_code
    FROM tbl_menu
   ORDER BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3fd1dfd7-135d-498e-97e5-5fe838b406ba/image.png" /></p>
</blockquote>
</li>
</ul>
<pre><code class="language-sql">-- 메뉴가 존재하는 카테고리의 종류를 뽑을 때 Distinct를 쓸 수 있다.
SELECT 
       DISTINCT category_code
  FROM tbl_menu
 ORDER BY category_code;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/50706503-27e9-4f1e-a097-544a5df2718d/image.png" /></p>
</blockquote>
<ul>
<li><p>NULL값을 포함한 열의 DISTINCT 사용</p>
<pre><code class="language-sql">  SELECT
         ref_category_code
    FROM tbl_category;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9fafadcd-1a10-406a-8368-0cdb395cf86f/image.png" /></p>
</blockquote>
</li>
</ul>
<pre><code class="language-sql">SELECT
       DISTINCT ref_category_code
  FROM tbl_category;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/40e09824-21ee-4bec-8e85-31e045ed65a1/image.png" /></p>
</blockquote>
<ul>
<li><p>다중열 DISTINCT 사용</p>
<ul>
<li><p>다중열의 값들이 모두 동일하면 중복된 것으로 판별한다.</p>
<pre><code class="language-sql">SELECT 
     category_code
   , orderable_status
FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/29182f4a-9fbf-4a73-9bb2-bf742c680ff7/image.png" /></p>
</blockquote>
<pre><code class="language-sql">SELECT 
     DISTINCT category_code
   , orderable_status
FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/b72515ab-5eed-4866-baed-78a33a4bf340/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h1 id="limit">LIMIT</h1>
<blockquote>
<p>💡 LIMIT 키워드는 SELECT문의 결과 집합에서 반환할 행의 수를 제한하는데 사용된다.</p>
<pre><code class="language-.sql">   SELECT
       select_list
   FROM
       table_name
   LIMIT [offset,] row_count;</code></pre>
<p>offset: 시작할 행의 번호(인덱스 체계)
row_count: 이후 행부터 반환 받을 행의 개수</p>
</blockquote>
<h2 id="limit-활용">LIMIT 활용</h2>
<ul>
<li><p>전체 행 조회</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , menu_name
       , menu_price
    FROM tbl_menu
  ORDER BY
      menu_price DESC;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a957f0be-bb7d-4b9f-af0c-374ad825d8a6/image.png" /></p>
</blockquote>
</li>
<li><p>2번 행부터 5번 행까지 조회</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , menu_name
       , menu_price
    FROM tbl_menu
   ORDER BY menu_price DESC
   LIMIT 1, 4;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6102da1c-eb1f-477d-b30a-7dc569d48721/image.png" /></p>
</blockquote>
</li>
<li><p>상위 다섯줄의 행만 조회</p>
<pre><code class="language-sql">  SELECT 
         menu_code
       , menu_name
       , menu_price
  FROM tbl_menu
  ORDER BY menu_price DESC, menu_name ASC
  LIMIT 5;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e7d6a6b0-0245-47ab-8901-dba6d3345964/image.png" /></p>
</blockquote>
</li>
<li><p>활용 데이터셋
```sql</p>
</li>
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