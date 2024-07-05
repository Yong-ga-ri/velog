<h1 id="dmldata-manipulation-language">DML(Data Manipulation Language)</h1>
<blockquote>
<p>💡 데이터 조작언어, 테이블에 값을 삽입하거나 수정하거나  삭제하는(데이터베이스 내의 데이터를 조작하는데 사용하는) SQL의 한 부분이다.</p>
</blockquote>
<h2 id="insert">INSERT</h2>
<ul>
<li><p>새로운 행을 추가하는 구문이다.</p>
</li>
<li><p>테이블의 행의 수가 증가한다.</p>
<pre><code class="language-sql">  INSERT 
    INTO tbl_menu
  VALUES 
  (
    NULL, '바나나해장국'
  , 8500, 4
  , 'Y'
  );</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/616ad968-19c3-44d3-b361-2fa03afda0ad/image.png" /></p>
</blockquote>
</li>
<li><p>NULL 허용 가능한(NULLABLE) 컬럼이나 AUTO_INCREMENT가 있는 컬럼을 제외하고 INSERT하고 싶은 데이터 컬럼을 지정해서 INSERT 가능하다.(default 속성이 있다면 default값이 들어감)</p>
<blockquote>
<p><code>실행결과</code></p>
<pre><code class="language-sql">INSERT 
  INTO tbl_menu
(
  menu_name, menu_price
, category_code, orderable_status
)
VALUES 
(
  '초콜릿죽', 6500
, 7, 'Y'
);</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2a82efcc-68b1-41ef-9d83-29e2a98d4609/image.png" /></p>
</blockquote>
</li>
<li><p>컬럼을 명시하면 INSERT 시 데이터의 순서를 바꾸는 것도 가능하다.</p>
<pre><code class="language-sql">  INSERT 
    INTO tbl_menu
  (orderable_status, menu_price, menu_name, category_code)
  VALUES 
  ('Y', 5500, '파인애플탕', 4);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c656232a-f13b-4e2b-a5ae-f20d99501e58/image.png" /></p>
</blockquote>
</li>
</ul>
<pre><code class="language-sql">SELECT * FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d276094d-80a1-471d-bd1b-1ea6cc92f719/image.png" /></p>
</blockquote>
<ul>
<li><p>MULTI INSERT</p>
<pre><code class="language-sql">  INSERT 
    INTO tbl_menu 
  VALUES 
  (null, '참치맛아이스크림', 1700, 12, 'Y'),
  (null, '멸치맛아이스크림', 1500, 11, 'Y'),
  (null, '소시지맛커피', 2500, 8, 'Y');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a1aacbef-8e2c-42c1-b0a1-52310c28810f/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="update">UPDATE</h2>
<ul>
<li><p>테이블에 기록된 컬럼의 값을 수정하는 구문이다.</p>
</li>
<li><p>테이블의 전체 행 갯수는 변화가 없다.</p>
<pre><code class="language-sql">  SELECT
         menu_code
       , category_code
    FROM tbl_menu
   WHERE menu_name = '파인애플탕';</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3d5a7196-1a49-4f75-b793-c638109bb7be/image.png" /></p>
</blockquote>
</li>
</ul>
<pre><code class="language-sql">UPDATE tbl_menu
   SET category_code = 7
     , menu_name = '딸기맛붕어빵'
 WHERE menu_code = 24;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ae8d4295-e5af-4d7a-93ad-179d71ecb210/image.png" /></p>
</blockquote>
<ul>
<li><p>SUBQUERY를 활용할 수도 있다.</p>
</li>
<li><p>다만 MySQL은 Oracle과 달리 update나 delete 시 자기 자신 테이블의 데이터를 사용 시 1093 에러가 발생한다.</p>
<pre><code class="language-sql">  UPDATE tbl_menu
     SET category_code = 6
   WHERE menu_code = (SELECT menu_code
                        FROM tbl_menu 
                       WHERE menu_name = '파인애플탕');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d9bb8c2b-dc14-4612-a48f-40f9cb13b121/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="delete">DELETE</h2>
<ul>
<li><p>테이블의 행을 삭제하는 구문이다.</p>
</li>
<li><p>테이블의 행의 갯수가 줄어든다.</p>
</li>
<li><p>LIMIT을 활용한 행 삭제(offset 지정은 안됨)</p>
<pre><code class="language-sql">  DELETE FROM tbl_menu
  ORDER BY menu_price
  LIMIT 2;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2b66155b-00c0-4626-a74b-f6c56526406c/image.png" /></p>
</blockquote>
</li>
<li><p>WHERE절을 활용한 단일 행 삭제</p>
<pre><code class="language-sql">  DELETE
    FROM tbl_menu
   WHERE menu_code = 24;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c02f81f4-7200-4b34-8530-d48e4b7ffedc/image.png" /></p>
</blockquote>
</li>
<li><p>해당 테이블 전체 행 삭제</p>
<pre><code class="language-sql">  DELETE FROM tbl_menu;

  -- (경고문구를 안 띄우고 싶다면)
  DELETE FROM tbl_menu WHERE 1 = 1;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e11064d9-2693-47a3-a6e0-87d4d1bd41bd/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="replace">REPLACE</h2>
<ul>
<li><p>INSERT 시 PRIMARY KEY 또는 UNIQUE KEY가 충돌이 발생할 수 있다면</p>
</li>
<li><p>REPLACE를 통해 중복 된 데이터를 덮어 쓸 수 있다.</p>
<pre><code class="language-sql">  -- INSERT INTO tbl_menu VALUES (17, '참기름소주', 5000, 10, 'Y'); -- 에러 발생
  REPLACE INTO tbl_menu VALUES (17, '참기름소주', 5000, 10, 'Y');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a78f89ab-ab7b-47b1-aa25-94a23e88f243/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/7d679a6d-261e-4274-8f87-0399a0ecb545/image.png" /></p>
</blockquote>
</li>
<li><p>INTO는 생략 가능 하다.</p>
<pre><code class="language-sql">  REPLACE tbl_menu VALUES (17, '참기름소주', 6500, 10, 'Y');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a1e0c187-015d-480b-ab1c-b2eb5abf3c90/image.png" /></p>
</blockquote>
</li>
<li><p>UPDATE 시 WHERE 구문 없이 UPDATE가 가능하다.</p>
<pre><code class="language-sql">  REPLACE tbl_menu
      SET menu_code = 2
        , menu_name = '우럭쥬스'
        , menu_price = 2000
        , category_code = 9
        , orderable_status = 'N';</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/16e7d525-558e-4d01-9f21-452375f2a3d1/image.png" /></p>
</blockquote>
</li>
<li><p><strong>DML 작업이 끝나면 db_script를 다시 전체 실행해서 테이블 및 데이터 정보를 초기화 한다.</strong></p>
</li>
</ul>
<h1 id="transaction">TRANSACTION</h1>
<blockquote>
<p>💡 TRANSACTION은 데이터 베이스에서 한 번에 수행되는 작업의 단위이다.</p>
<p>시작, 진행, 종료 단계를 가지며 만약 중간에 오류가 발생하면 롤백(시작 이전 단계로 되돌리는 작업)을 수행하고 데이터 베이스에 제대로 반영하기 위해서는 커밋(이후 롤백이 되지 않음)을 진행한다.</p>
<p>MySQL은 기본적으로 자동 커밋 설정이 되어 있어(롤백이 안됨). 롤백을 하기 위해서는 자동 커밋 설정을 해제해 주어야 한다.</p>
</blockquote>
<h2 id="transaction-활용">Transaction 활용</h2>
<ul>
<li><p>MySQL은 기본적으로 commit이 자동으로 되므로 수동으로 조절하고 싶다면 autocommit 설정을 바꿔 주어야 한다.</p>
</li>
<li><p>autocommit 활성화</p>
<pre><code class="language-sql">  SET autocommit = 1; 
  -- 또는 
  SET autocommit = ON;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/88499c0e-71ea-4707-bad5-59ffc2491def/image.png" /></p>
</blockquote>
</li>
<li><p>autocommit 비활성화</p>
<pre><code class="language-sql">  SET autocommit = 0; 
  -- 또는 
  SET autocommit = OFF;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0a94641f-fcf3-49a8-9217-f8bf67c8e61e/image.png" /></p>
</blockquote>
</li>
<li><p>START TRANSACTION 구문을 작성하고 DML 작업 수행 후 COMMIT 또는 ROLLBACK을 하면 된다.</p>
</li>
<li><p>COMMIT 이후에는 ROLLBACK을 해도 ROLLBACK이 적용되지 않는다.</p>
<pre><code class="language-sql">  START TRANSACTION;

  SELECT * FROM tbl_menu;
  INSERT INTO tbl_menu VALUES (null, '바나나해장국', 8500, 4, 'Y');
  UPDATE tbl_menu SET menu_name = '수정된 메뉴' WHERE menu_code = 5;
  DELETE FROM tbl_menu WHERE menu_code = 7;

  -- COMMIT; 
  ROLLBACK;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
</blockquote>
<p>  <img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/5cb17dbd-74da-444b-8382-7b449c4e7ff4/image.png" /></p>
</li>
</ul>