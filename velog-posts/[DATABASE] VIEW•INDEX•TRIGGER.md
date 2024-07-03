<h1 id="view">VIEW</h1>
<blockquote>
<p>💡 SELECT 쿼리문을 저장한 객체로 가상테이블이라고 불린다. 
실질적인 데이터를 물리적으로 저장하고 있지 않고 쿼리만 저장했지만 테이블을 사용하는 것과 동일하게 사용할 수 있다.</p>
<p>VIEW는 데이터를 쉽게 읽고 이해할 수 있도록 돕는 동시에, 원본 데이터의 보안을 유지하는데 도움이 된다.</p>
</blockquote>
<h2 id="view-생성">VIEW 생성</h2>
<ul>
<li><p>VIEW 생성 후 조회</p>
<pre><code class="language-sql">  SELECT * FROM tbl_menu;

  -- VIEW 생성
  CREATE VIEW hansik AS
  SELECT 
         menu_code 
       , menu_name
       , menu_price
       , category_code
       , orderable_status
    FROM tbl_menu 
   WHERE category_code = 4;

  -- 생성된 VIEW 조회
  SELECT * FROM hansik;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/163513c1-2005-4867-bb3a-b1e73bd9646b/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/db876bbc-03ea-4227-8bec-12422dc2e944/image.png" /></p>
</blockquote>
</li>
<li><p>베이스 테이블의 정보가 변경되면 VIEW의 결과도 같이 변경된다.</p>
<pre><code class="language-sql">  INSERT 
    INTO tbl_menu 
  VALUES (null, '식혜맛국밥', 5500, 4, 'Y');
  SELECT * FROM hansik;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/42b4feee-37f3-425d-bfd8-7df68667b811/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="view를-통한-dml">VIEW를 통한 DML</h2>
<ul>
<li>VIEW를 통한 DML 작업은 베이스 테이블에도 영향을 주게 된다.</li>
</ul>
<h3 id="view를-통한-insert">VIEW를 통한 INSERT</h3>
<ul>
<li><p>VIEW는 AUTO_INCREMENT가 없으므로 pk 컬럼의 값을 지정해 주어야 한다.</p>
</li>
<li><p>VIEW를 통한 INSERT 이후 VIEW 조회 및 베이스 테이블 조회</p>
<pre><code class="language-sql">  -- INSERT INTO hansik VALUES (null, '식혜맛국밥', 5500, 4, 'Y');    -- 에러 발생
  INSERT 
    INTO hansik
  VALUES (99, '수정과맛국밥', 5500, 4, 'Y');   
  SELECT * FROM hansik;
  SELECT * FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6a8e3a9e-7171-4d0e-a62a-416e99acc8bf/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/fb21f963-4f55-464a-8fd6-8cafd7bf6d36/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="view를-통한-update">VIEW를 통한 UPDATE</h3>
<ul>
<li><p>VIEW를 통한 UPDATE 이후 VIEW 조회 및 베이스 테이블 조회</p>
<pre><code class="language-sql">  UPDATE hansik
     SET menu_name = '버터맛국밥', menu_price = 5700 
   WHERE menu_code = 99;
  SELECT * FROM hansik;
  SELECT * FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ce12a090-ea10-42f0-8e31-afd34e9c7bdf/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/97090227-3a4a-4561-899b-7d29be49280a/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="view를-통한-delete">VIEW를 통한 DELETE</h3>
<ul>
<li><p>VIEW를 통한 DELETE 이후 VIEW 조회 및 베이스 테이블 조회</p>
<pre><code class="language-sql">  DELETE FROM hansik WHERE menu_code = 99;
  SELECT * FROM hansik;
  SELECT * FROM tbl_menu;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/0e05e766-bea2-488e-a40c-53ae98b1df16/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e0d69233-5293-4c54-9473-656848a3daf0/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="view로-dml-명령어로-조작이-불가능한-경우">VIEW로 DML 명령어로 조작이 불가능한 경우</h3>
<ul>
<li>사용된 SUBQUERY에 따라 DMB 명령어로 조작이 불가능할 수 있다.<ol>
<li>뷰 정의에 포함되지 않은 컬럼을 조작하는 경우</li>
<li>뷰에 포함되지 않은 컬럼 중에 베이스가 되는 테이블 컬럼이 NOT NULL 제약조건이 지정된 경우t</li>
<li>산술 표현식이 정의된 경우</li>
<li>JOIN을 이용해 여러 테이블을 연결한 경우</li>
<li>DISTINCT를 포함한 경우</li>
<li>그룹함수나 GROUP BY 절을 포함한 경우</li>
</ol>
</li>
</ul>
<h3 id="view-삭제">VIEW 삭제</h3>
<ul>
<li><p>VIEW에 쓰인 SUBQUERY 안에 연산 결과 컬럼도 사용 가능하다.</p>
<pre><code class="language-sql">  DROP VIEW hansik;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6536f517-5bed-4005-968f-583f170b95fc/image.png" /></p>
</blockquote>
</li>
<li><p>OR REPLACE 옵션</p>
<ul>
<li><p>테이블을 DROP하지 않고 기존의 VIEW를 새로운 VIEW로 쉽게 다룰 수 있다.</p>
<pre><code class="language-sql">CREATE OR REPLACE VIEW hansik AS
SELECT 
     menu_code AS '메뉴코드'
   , menu_name '메뉴명'
   , category_name '카테고리명'
FROM tbl_menu a
JOIN tbl_category b ON a.category_code = b.category_code
WHERE b.category_name = '한식';

SELECT * FROM hansik;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/5c3bc21c-7f1d-45c6-883c-b88680cc8635/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h1 id="index">INDEX</h1>
<blockquote>
<p>💡 인덱스(Index)는 데이터 검색 속도를 향상시키는 데이터 구조로 데이터를 빠르게 조회할 수 있는 포인터를 제공한다.</p>
<p>데이터베이스에서 데이터를 찾을 때 전체 테이블을 검색하는 대신 인덱스를 통해 검색을 하므로 속도가 더 빨라지게 된다.</p>
<p>인덱스는 주로 WHERE절의 조건이나 JOIN 연산에 사용되는 컬럼에 생성한다.</p>
<p>다만 인덱스도 데이터 저장 공간을 차지하고 데이터가 변경될 때마다 인덱스 역시 갱신해야 하기 때문에 어떤 컬럼에 인덱스를 생성할지는 신중히 결정해야 한다.</p>
</blockquote>
<h2 id="인덱스-생성">인덱스 생성</h2>
<ul>
<li><p>PRIMARY KEY 제약조건을 지닌 기본 테이블 생성 후 기본 데이터 INSERT 후 조회</p>
<pre><code class="language-sql">  CREATE TABLE phone (
      phone_code INT PRIMARY KEY,
      phone_name VARCHAR(100),
      phone_price DECIMAL(10, 2)
  );

  INSERT 
    INTO phone (phone_code , phone_name , phone_price )
  VALUES 
  (1, 'galaxyS23', 1200000),
  (2, 'iPhone14pro', 1433000),
  (3, 'galaxyZfold3', 1730000);

  SELECT * FROM phone;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/21964271-e4de-4b71-b7c5-ba723fb617cb/image.png" /></p>
</blockquote>
</li>
<li><p>인덱스가 없는 컬럼을 WHERE절의 조건으로 활용한 조회 진행 시 EXPLAIN으로 쿼리 실행 계획 확인</p>
<pre><code class="language-sql">  EXPLAIN SELECT * FROM phone WHERE phone_name = 'galaxyS23';</code></pre>
<blockquote>
<p><code>실행결과</code>
<img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/78d38bb6-2153-445c-98d0-c0824e66cb89/image.png" /></p>
</blockquote>
</li>
<li><p>phone_name 컬럼에 idx_name이라는 이름의 인덱스 생성 후 확인</p>
<pre><code class="language-sql">  CREATE INDEX idx_name ON phone (phone_name);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e926402f-bdcb-4d65-a4a1-f632f235a2dd/image.png" /></p>
</blockquote>
</li>
<li><p>2개 이상의 컬럼을 한번에 하나의 인덱스로 설정해서 생성할 수 있다.</p>
</li>
<li><p>복합 인덱스 생성</p>
<pre><code class="language-sql">  CREATE INDEX idx_name_price ON phone (phone_name, phone_price);

  SHOW INDEX FROM phone;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/fbd6daae-e8d4-4f9c-bf9d-580e836274c7/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="인덱스-활용">인덱스 활용</h2>
<ul>
<li><p>테이블에 인덱스가 설정 된 컬럼을 활용해 조회를 진행</p>
<pre><code class="language-sql">  SELECT * FROM phone WHERE phone_name = 'iPhone14pro';</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/bc7850ca-ee44-4e6f-97cd-d810d9f8b723/image.png" /></p>
</blockquote>
</li>
<li><p>EXPLAIN 명령어로 쿼리 실행 계획 확인(인덱스 사용 여부 및 사용 컬럼 확인)</p>
<pre><code class="language-sql">  EXPLAIN SELECT * FROM phone WHERE phone_name = 'iPhone14pro';</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/853e6153-b0d5-4927-8d81-dbfb6cb708fd/image.png" /></p>
</blockquote>
</li>
<li><p>인덱스 최적화(재구성)</p>
<ul>
<li><p>인덱스 최적화(재구성)은 인덱스가 파편화되었거나, 데이터의 대부분이 변경된 경우에 유용하다.</p>
</li>
<li><p>이는 인덱스의 성능을 개선하고, 디스크 공간을 더 효율적으로 사용하게 해준다.</p>
</li>
<li><p>단, 인덱스를 재구성하는 동안 해당 테이블은 잠길 수 있으므로, 이 작업은 주의해서 수행해야 한다.</p>
</li>
<li><p>'ALTER TABLE' 명령어를 사용해서 재구성한다.</p>
<pre><code class="language-sql">ALTER TABLE phone DROP INDEX idx_name;
ALTER TABLE phone ADD INDEX idx_name(phone_name);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/017d13c5-bb6a-4def-b2b0-16ae674486f2/image.png" /></p>
</blockquote>
</li>
<li><p>또한, MySQL의 InnoDB 엔진을 사용하는 경우에는 OPTIMIZE TABLE 명령을 사용하여 테이블과 인덱스를 최적화할 수도 있다.</p>
<pre><code class="language-sql">OPTIMIZE TABLE phone;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ed952d8f-050b-41e3-adba-8d54364a25be/image.png" /></p>
</blockquote>
</li>
</ul>
</li>
</ul>
<h2 id="인덱스-삭제">인덱스 삭제</h2>
<ul>
<li><p>인덱스 삭제 후 테이블에 존재하는 인덱스 확인</p>
<pre><code class="language-sql">  DROP INDEX idx_name ON phone;
  SHOW INDEX FROM phone;</code></pre>
</li>
</ul>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1cc3fc64-eb23-4f13-8f9f-0c875860f4cf/image.png" /></p>
</blockquote>
<h1 id="trigger">TRIGGER</h1>
<blockquote>
<p>💡 트리거란 데이터베이스 테이블에서 발생하는 특정 이벤트(INSERT, UPDATE, DELETE)가 발생했을 때 자동으로 실행되는 데이터베이스 객체이다.</p>
<p>주요 사용 목적은 데이터의 무결성을 유지하고 복잡한 비즈니스 로직을 처리하기 위함이다.</p>
<p>다만 트리거를 남용할 시 성능 문제나 복잡성 증가와 같은 부정적인 영향을 줄 수 있다.</p>
</blockquote>
<ul>
<li>트리거의 종류<ul>
<li>BEFORE 트리거<ul>
<li>이벤트가 발생하기 전에 실행되며 데이터의 유효성 검사나 변형에 주로 사용된다.</li>
</ul>
</li>
<li>AFTER 트리거<ul>
<li>이벤트가 발생한 후에 실행되며 로깅, 알림 전송 등의 작업에 적합하다.</li>
</ul>
</li>
</ul>
</li>
<li>트리거 작성법</li>
</ul>
<pre><code class="language-sql">DELIMITER // 

CREATE OR REPLACE TRIGGER [트리거명]
    BEFORE|AFTER [이벤트 타입]
    ON [테이블명]
    FOR EACH ROW
BEGIN
END//

DELIMITER ;</code></pre>
<h2 id="트리거-생성">트리거 생성</h2>
<ul>
<li>주문 메뉴(tbl_order_menu) 테이블에 INSERT가 되고 나서 주문(tbl_order) 테이블의 총 합계가 UPDATE 될 수 있는 트리거 생성</li>
</ul>
<pre><code class="language-sql">DELIMITER //

CREATE OR REPLACE TRIGGER after_order_menu_insert
    AFTER INSERT
    ON tbl_order_menu
    FOR EACH ROW
BEGIN
    UPDATE tbl_order
    SET total_order_price = total_order_price + NEW.order_amount * (SELECT menu_price FROM tbl_menu WHERE menu_code = NEW.menu_code)
    WHERE order_code = NEW.order_code;
END//

DELIMITER ;</code></pre>
<h2 id="트리거-활용">트리거 활용</h2>
<ul>
<li>주문 테이블과 주문 메뉴 테이블에 INSERT 작업 이후 주문 테이블의 총 합계가 UPDATE 되는 것 확인</li>
</ul>
<pre><code class="language-sql">-- 주문 테이블 INSERT
INSERT
  INTO tbl_order
(
  order_code
, order_date
, order_time
, total_order_price
)
VALUES
(
  NULL
, CONCAT(CAST(YEAR(NOW()) AS VARCHAR(4))
        , CAST(LPAD(MONTH(NOW()), 2, 0) AS VARCHAR(2))
        , CAST(LPAD(DAY(NOW()), 2, 0) AS VARCHAR(2)))
, CONCAT(CAST(LPAD(HOUR(NOW()), 2, 0) AS VARCHAR(2))
       , CAST(LPAD(MINUTE(NOW()), 2, 0) AS VARCHAR(2))
       , CAST(LPAD(SECOND(NOW()), 2, 0) AS VARCHAR(2)))
, 0            
);

-- 주문 메뉴 테이블 INSERT 1
INSERT
  INTO tbl_order_menu
(
  order_code
, menu_code
, order_amount
)
VALUES
(
  1
, 3
, 2
);

-- 주문 메뉴 테이블 INSERT 2
INSERT
  INTO tbl_order_menu
(
  order_code
, menu_code
, order_amount
)
VALUES
(
  1
, 6
, 3
);

SELECT * FROM tbl_order;
SELECT * FROM tbl_order_menu;

-- 다시 되돌려 테스트 해보고자 할 경우
-- 1) rollback하기
ROLLBACK;
-- 2) 기존 데이터 지우기
DELETE FROM tbl_order WHERE 1 = 1;
DELETE FROM tbl_order_menu WHERE 1 = 1;

-- 이후 AUTO_INCREMENT도 다시 초기화 해 준다.
ALTER TABLE tbl_order AUTO_INCREMENT = 1;</code></pre>