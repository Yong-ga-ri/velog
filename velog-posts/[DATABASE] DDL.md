<h1 id="ddldata-definition-language">DDL(Data Definition Language)</h1>
<blockquote>
<p>💡 DDL(Data Definition Language)는 데이터베이스의 스키마를 정의하거나 수정하는 데 사용되는 SQL의 한 부분이다.</p>
</blockquote>
<blockquote>
<p><strong>스키마(schema)</strong>
: 테이블의 구조(컬럼명, 자료형, 자료형 크기, 테이블명 등) 및 제약조건(unique, primary key, not null, check, foreign key 등) 전반을 아울러 지칭하는 말</p>
</blockquote>
<h2 id="create">CREATE</h2>
<ul>
<li><p>테이블 생성을 위한 구문</p>
</li>
<li><p>IF NOT EXISTS를 적용하면 기존에 존재하는 테이블이라도 에러가 발생하지 않는다.</p>
</li>
<li><p>테이블의 컬럼 설정 방법</p>
<ul>
<li>column_name data_type(length) [NOT NULL] [DEFAULT value] [AUTO_INCREMENT] column_constraint</li>
</ul>
</li>
<li><p>tb1 테이블 생성</p>
<pre><code class="language-sql">  CREATE TABLE IF NOT EXISTS tb1 (
      pk INT PRIMARY KEY, -- 컬럼 레벨에서  제약조건 추가
      fk INT,
      col1 VARCHAR(255),
      CHECK(col1 IN ('Y', 'N')) -- 테이블 레벨에서 제약조건 추가
  ) ENGINE=INNODB;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f60c74e9-a35e-45c7-879a-a5dfa77344ea/image.png" /></p>
</blockquote>
</li>
<li><p>테이블 구조 확인</p>
<pre><code class="language-sql">  DESCRIBE tb1;

  -- 줄여서 쓸 수도 있다.
  DESC tb1;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/d553e8fd-37fe-4bd7-86f5-332140034f77/image.png" /></p>
</blockquote>
</li>
<li><p>INSERT 테스트</p>
<pre><code class="language-sql">  INSERT INTO tb1 VALUES (1, 10, 'Y');

  SELECT * FROM tb1;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/af48031e-79b9-415b-9c6d-c0f63d4f73e9/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="auto_increment">AUTO_INCREMENT</h2>
<ul>
<li><p>INSERT 시 PRIMARY키에 해당하는 컬럼에 자동으로 번호를 발생(중복되지 않게)시켜 저장할 수 있다.</p>
</li>
<li><p>tb2 테이블 생성</p>
<pre><code class="language-sql">  CREATE TABLE IF NOT EXISTS tb2 (
      pk INT AUTO_INCREMENT PRIMARY KEY,
      fk INT,
      col1 VARCHAR(255),
      CHECK(col1 IN ('Y', 'N'))
  ) ENGINE=INNODB;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/b713e82d-0b3f-47f3-9141-f47c1994f8dd/image.png" /></p>
</blockquote>
</li>
<li><p>INSERT 테스트</p>
<pre><code class="language-sql">  INSERT INTO tb2 VALUES (null, 10, 'Y');
  INSERT INTO tb2 VALUES (null, 20, 'Y');

  SELECT * FROM tb2;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/2bc8d790-1d5d-4c5b-9f8f-204f30d876d7/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="alter">ALTER</h2>
<ul>
<li>테이블에 추가/변경/수정/삭제하는 모든 것은 ALTER 명령어를 사용해 적용한다.</li>
<li>종류가 너무 많고 복잡하므로 대표적인 것만 살펴보도록 하자.</li>
</ul>
<h3 id="열-추가">열 추가</h3>
<ul>
<li><p><code>ALTER TABLE 테이블명 ADD 컬럼명 컬럼정의</code></p>
</li>
<li><p>col2 컬럼 추가(INT형, NOT NULL 제약조건 존재)</p>
<pre><code class="language-sql">  ALTER TABLE tb2
  ADD col2 INT NOT NULL;

  DESCRIBE tb2;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ca15206d-19ed-44e2-8aab-dc84bbc6d46b/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="열-삭제">열 삭제</h3>
<ul>
<li><p><code>ALTER TABLE 테이블명 DROP COLUMN 컬럼명</code></p>
</li>
<li><p>col2 컬럼 삭제</p>
<pre><code class="language-sql">  ALTER TABLE tb2
  DROP COLUMN col2;

  DESCRIBE tb2;</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/8d31a678-cbb9-439c-aec4-137569e1d170/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="열-이름-및-데이터-형식-변경">열 이름 및 데이터 형식 변경</h3>
<ul>
<li><p><code>ALTER TABLE 테이블명 CHANGE COLUMN 기존컬럼명 바꿀 컬럼명 컬럼정의</code></p>
</li>
<li><p>fk 컬럼을 change_fk 컬럼으로 변경(NOT NULL 제약조건 존재)</p>
<pre><code class="language-sql">  ALTER TABLE tb2
  CHANGE COLUMN fk change_fk INT NOT NULL;

  DESCRIBE tb2;</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/5b5be241-f16c-47f8-afbe-d563e3765322/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="열-제약-조건-추가-및-삭제">열 제약 조건 추가 및 삭제</h3>
<ul>
<li><p><code>ALTER TABLE 테이블명 drop 제약조건</code></p>
</li>
<li><p>tb2 테이블의 PRIMARY KEY 제약조건 제거</p>
<pre><code class="language-sql">  ALTER TABLE tb2
  DROP PRIMARY KEY;    -- 에러 발생</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ea6af711-15e2-475d-baa2-1649b358d736/image.png" /></p>
</blockquote>
</li>
<li><p>AUTO_INCREMENT가 걸려 있는 컬럼은 PRIMARY KEY 제거가 안되므로 AUTO_INCREMENT를 MODIFY 명령어로 제거한다.(MODIFY는 컬럼의 정의를 바꾸는 것이다.)</p>
<pre><code class="language-sql">  ALTER TABLE tb2
  MODIFY pk INT;

  DESCRIBE tb2;</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1289502b-b03b-4bb3-9a3d-eb9aef42c71c/image.png" /></p>
</blockquote>
</li>
<li><p>이제 다시 PRIMARY KEY 제약조건 제거</p>
<pre><code class="language-sql">  ALTER TABLE tb2
  DROP PRIMARY KEY;

  DESCRIBE tb2;</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/02922186-b9cb-4533-96fb-ae9b4aee6f85/image.png" /></p>
</blockquote>
</li>
<li><p>tb2 테이블의 pk 컬럼에 다시 PRIMARY KEY 제약조건 추가하기</p>
<pre><code class="language-sql">  ALTER TABLE tb2
  ADD PRIMARY KEY(pk);

  DESCRIBE tb2;</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/f9fe8baa-73af-4325-8a05-71164187bb74/image.png" /></p>
</blockquote>
</li>
</ul>
<h3 id="컬럼-여러개-추가하기">컬럼 여러개 추가하기</h3>
<ul>
<li><p>한번에 여러 컬럼을 추가할 수 있다.</p>
<pre><code class="language-sql">  ALTER TABLE tb2
  ADD col3 DATE NOT NULL,            
  ADD col4 TINYINT NOT NULL; 

  DESC tb2;</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/423ba8f3-cf52-4916-8505-9f18ac47ca56/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="drop">DROP</h2>
<ul>
<li><p>테이블을 삭제하기 위한 구문</p>
</li>
<li><p>tb3 테이블 생성 후 삭제</p>
<pre><code class="language-sql">  -- tb3 테이블 생성
  CREATE TABLE IF NOT EXISTS tb3 (
    pk INT AUTO_INCREMENT PRIMARY KEY,
    fk INT,
    col1 VARCHAR(255),
    CHECK(col1 IN ('Y', 'N'))
  ) ENGINE=INNODB;

  -- tb3 테이블 삭제
  DROP TABLE IF EXISTS tb3;</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c5030f1f-61cb-4ae3-8b29-b5ded6f02b2e/image.png" /></p>
</blockquote>
</li>
<li><p>두 개 이상의 테이블 생성(tb4, tb5) 후 한번에 삭제</p>
<pre><code class="language-sql">  -- tb4 테이블 생성
  CREATE TABLE IF NOT EXISTS tb4 (
    pk INT AUTO_INCREMENT PRIMARY KEY,
    fk INT,
    col1 VARCHAR(255),
    CHECK(col1 IN ('Y', 'N'))
  ) ENGINE=INNODB;

  -- tb5 테이블 생성
  CREATE TABLE IF NOT EXISTS tb5 (
    pk INT AUTO_INCREMENT PRIMARY KEY,
    fk INT,
    col1 VARCHAR(255),
    CHECK(col1 IN ('Y', 'N'))
  ) ENGINE=INNODB;

  -- 한번에 2개의 테이블 삭제
  DROP TABLE IF EXISTS tb4, tb5;</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/aed6d08f-3623-4ad7-ae71-18c52ba3e577/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="truncate">TRUNCATE</h2>
<ul>
<li><p>논리적으로는 WHERE절이 없는 DELETE 구문과 큰 차이가 없어 보인다.</p>
</li>
<li><p>하지만 어차피 데이터를 다 삭제할 경우 행마다 하나씩 지워지는 DELETE보다 DROP이후 바로 테이블을 재생성 해주는 TRUNCATE가 훨씬 효율적으로 한번에 테이블을 초기화 시켜준다.</p>
</li>
<li><p>또한 AUTO_INCREMENT 컬럼이 있는 경우 시작 값도 0으로 초기화가 된다.</p>
<pre><code class="language-sql">  -- tb6 테이블 생성
  CREATE TABLE IF NOT EXISTS tb6 (
    pk INT AUTO_INCREMENT PRIMARY KEY,
    fk INT,
    col1 VARCHAR(255),
    CHECK(col1 IN ('Y', 'N'))
  ) ENGINE=INNODB;

  -- 4개 행 데이터 INSERT
  INSERT INTO tb6 VALUES (null, 10, 'Y');
  INSERT INTO tb6 VALUES (null, 20, 'Y');
  INSERT INTO tb6 VALUES (null, 30, 'Y');
  INSERT INTO tb6 VALUES (null, 40, 'Y');

  -- 제대로 INSERT 되었는지 확인
  SELECT * FROM tb6;

  -- 테이블 초기화 하기
  -- TRUNCATE TABLE tb6;
  TRUNCATE tb6;    -- TABLE 키워드 생략 가능</code></pre>
<blockquote>
<p><strong><code>실행결과</code></strong></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1780a25c-0ff6-4a0a-b089-b55e78dfbaa2/image.png" /></p>
</blockquote>
</li>
</ul>
<h1 id="constraints">CONSTRAINTS</h1>
<blockquote>
<p>💡 CONSTRAINT는 제약조건으로 테이블에 데이터가 입력되거나 수정될 때의 규칙을 정의한다.</p>
<p>데이터 무결성을 보장하는데 도움이 된다.</p>
</blockquote>
<h2 id="not-null">NOT NULL</h2>
<ul>
<li><p>NULL값을 허용하지 않는 제약조건</p>
</li>
<li><p>제약조건 확인용 테이블 생성 및 테스트 데이터 INSERT 후 조회하기</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS user_notnull;
  CREATE TABLE IF NOT EXISTS user_notnull (
      user_no INT NOT NULL,
      user_id VARCHAR(255) NOT NULL,
      user_pwd VARCHAR(255) NOT NULL,
      user_name VARCHAR(255) NOT NULL,
      gender VARCHAR(3),
      phone VARCHAR(255) NOT NULL,
      email VARCHAR(255)
  ) ENGINE=INNODB;

  INSERT 
    INTO user_notnull
  (user_no, user_id, user_pwd, user_name, gender, phone, email)
  VALUES
  (1, 'user01', 'pass01', '홍길동', '남', '010-1234-5678', 'hong123@gmail.com'),
  (2, 'user02', 'pass02', '유관순', '여', '010-777-7777', 'yu77@gmail.com');

  SELECT * FROM user_notnull;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/63a0bdbf-09ad-4690-933c-8be68f63bc6e/image.png" /></p>
</blockquote>
</li>
<li><p>not null 제약조건 에러 발생(null 값 적용)</p>
<pre><code class="language-sql">  INSERT
    INTO user_notnull
  (user_no, user_id, user_pwd, user_name, gender, phone, email)
  VALUES
  (3, 'user03', null, '이순신', '남', '010-222-2222', 'lee222@gmail.com');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/4f078117-527e-4fcf-9ce8-6bdb9cdb2cec/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="unique">UNIQUE</h2>
<ul>
<li><p>중복값 허용하지 않는 제약조건</p>
</li>
<li><p>제약조건 확인용 테이블 생성 및 테스트 데이터 INSERT 후 조회하기</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS user_unique;
  CREATE TABLE IF NOT EXISTS user_unique (
      user_no INT NOT NULL UNIQUE,
      user_id VARCHAR(255) NOT NULL,
      user_pwd VARCHAR(255) NOT NULL,
      user_name VARCHAR(255) NOT NULL,
      gender VARCHAR(3),
      phone VARCHAR(255) NOT NULL,
      email VARCHAR(255),
      UNIQUE (phone)
  ) ENGINE=INNODB;

  INSERT
    INTO user_unique
  (user_no, user_id, user_pwd, user_name, gender, phone, email)
  VALUES
  (1, 'user01', 'pass01', '홍길동', '남', '010-1234-5678', 'hong123@gmail.com'),
  (2, 'user02', 'pass02', '유관순', '여', '010-777-7777', 'yu77@gmail.com');

  SELECT * FROM user_unique;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/9c08d15e-2d8a-4e0b-9ebc-3d4e652753fa/image.png" /></p>
</blockquote>
</li>
<li><p>unique 제약조건 에러 발생(전화번호 중복값 적용)</p>
<pre><code class="language-sql">  INSERT 
    INTO user_unique
  (user_no, user_id, user_pwd, user_name, gender, phone, email)
  VALUES
  (3, 'user03', 'pass03', '이순신', '남', '010-777-7777', 'lee222@gmail.com');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ec88db56-599b-452b-81d8-fc793e70a04e/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="primary-key">PRIMARY KEY</h2>
<ul>
<li><p>테이블에서 한 행의 정보를 찾기 위해 사용 할 컬럼을 의미한다.</p>
</li>
<li><p>테이블에 대한 식별자 역할을 한다.(한 행씩 구분하는 역할을 한다.)</p>
</li>
<li><p>NOT NULL + UNIQUE 제약조건의 의미</p>
</li>
<li><p>한 테이블당 한 개만 설정할 수 있음</p>
</li>
<li><p>컬럼 레벨, 테이블 레벨 둘 다 설정 가능함</p>
</li>
<li><p>한 개 컬럼에 설정할 수도 있고, 여러 개의 컬럼을 묶어서 설정할 수도 있음(복합키)(테이블 레벨 설정만 가능함)</p>
</li>
<li><p>제약조건 확인용 테이블 생성 및 테스트 데이터 INSERT 후 조회하기</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS user_primarykey;
  CREATE TABLE IF NOT EXISTS user_primarykey (
  --     user_no INT PRIMARY KEY,
      user_no INT,
      user_id VARCHAR(255) NOT NULL,
      user_pwd VARCHAR(255) NOT NULL,
      user_name VARCHAR(255) NOT NULL,
      gender VARCHAR(3),
      phone VARCHAR(255) NOT NULL,
      email VARCHAR(255),
      PRIMARY KEY (user_no)
  ) ENGINE=INNODB;

  INSERT 
    INTO user_primarykey
  (user_no, user_id, user_pwd, user_name, gender, phone, email)
  VALUES
  (1, 'user01', 'pass01', '홍길동', '남', '010-1234-5678', 'hong123@gmail.com'),
  (2, 'user02', 'pass02', '유관순', '여', '010-777-7777', 'yu77@gmail.com');

  SELECT * FROM user_primarykey;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/af429dbd-86c4-44d7-a0ce-e8a87a64d4bd/image.png" /></p>
</blockquote>
</li>
<li><p>primary key 제약조건 에러 발생(null값 적용)</p>
<pre><code class="language-sql">  INSERT 
    INTO user_primarykey
  (user_no, user_id, user_pwd, user_name, gender, phone, email)
  VALUES
  (null, 'user03', 'pass03', '이순신', '남', '010-777-7777', 'lee222@gmail.com');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/37d0cfed-305c-4e51-85e9-ff2a8d431269/image.png" /></p>
</blockquote>
</li>
<li><p>primary key 제약조건 에러 발생(중복값 적용)</p>
<pre><code class="language-sql">  INSERT 
    INTO user_primarykey
  (user_no, user_id, user_pwd, user_name, gender, phone, email)
  VALUES
  (2, 'user03', 'pass03', '이순신', '남', '010-777-7777', 'lee222@gmail.com');</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3a6ccc7d-c117-41a6-bad3-e90a0047d7d7/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="foreign-key">FOREIGN KEY</h2>
<ul>
<li><p>삭제룰 관련 링크</p>
<p>  <a href="https://mariadb.com/kb/en/foreign-keys/">Foreign Keys</a></p>
</li>
<li><p>참조 무결성을 위배하지 않기 위해 사용</p>
</li>
<li><p>참조(REFERENCES)된 다른 테이블에서 제공하는 값만 사용할 수 있음</p>
</li>
<li><p>FOREIGN KEY 제약조건에 의해서 테이블 간의 관계(RELATIONSHIP)가 형성 됨</p>
</li>
<li><p>제공되는 값 외에는 NULL을 사용할 수 있음</p>
</li>
<li><p>제약조건 확인용 테이블 생성 및 테스트 데이터 INSERT 후 조회하기(부모 테이블)</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS user_grade;
  CREATE TABLE IF NOT EXISTS user_grade (
      grade_code INT NOT NULL UNIQUE,
      grade_name VARCHAR(255) NOT NULL
  ) ENGINE=INNODB;

  INSERT 
    INTO user_grade
  VALUES 
  (10, '일반회원'),
  (20, '우수회원'),
  (30, '특별회원');

  SELECT * FROM user_grade;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/7194b857-d836-46cf-a9db-e214d6b1bd3b/image.png" /></p>
</blockquote>
</li>
<li><p>제약조건 확인용 테이블 생성 및 테스트 데이터 INSERT 후 조회하기2  (자식 테이블 - DELETE 삭제룰 없을 시 )</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS user_foreignkey1;
  CREATE TABLE IF NOT EXISTS user_foreignkey1 (
      user_no INT PRIMARY KEY,
      user_id VARCHAR(255) NOT NULL,
      user_pwd VARCHAR(255) NOT NULL,
      user_name VARCHAR(255) NOT NULL,
      gender VARCHAR(3),
      phone VARCHAR(255) NOT NULL,
      email VARCHAR(255),
      grade_code INT ,
      FOREIGN KEY (grade_code) 
          REFERENCES user_grade (grade_code)
  ) ENGINE=INNODB;

  INSERT 
    INTO user_foreignkey1
  (user_no, user_id, user_pwd, user_name, gender, phone, email, grade_code)
  VALUES
  (1, 'user01', 'pass01', '홍길동', '남', '010-1234-5678', 'hong123@gmail.com', 10),
  (2, 'user02', 'pass02', '유관순', '여', '010-777-7777', 'yu77@gmail.com', 20);

  SELECT * FROM user_foreignkey1;
</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/a9931d91-ba3e-4538-abae-f3e334871677/image.png" /></p>
</blockquote>
</li>
<li><p>foreign key 제약조건 에러 발생(참조 컬럼에 없는 값 적용)</p>
<pre><code class="language-sql">  INSERT 
    INTO user_foreignkey1
  (user_no, user_id, user_pwd, user_name, gender, phone, email, grade_code)
  VALUES
  (3, 'user03', 'pass03', '이순신', '남', '010-777-7777', 'lee222@gmail.com', 50);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/ee6e188f-5187-4454-bb3c-84d2438217b4/image.png" /></p>
</blockquote>
</li>
<li><p>제약조건 확인용 테이블 생성 및 테스트 데이터 INSERT 후 조회하기3  (자식 테이블 - DELETE 삭제룰 있을 시 )</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS user_foreignkey2;
  CREATE TABLE IF NOT EXISTS user_foreignkey2 (
      user_no INT PRIMARY KEY,
      user_id VARCHAR(255) NOT NULL,
      user_pwd VARCHAR(255) NOT NULL,
      user_name VARCHAR(255) NOT NULL,
      gender VARCHAR(3),
      phone VARCHAR(255) NOT NULL,
      email VARCHAR(255),
      grade_code INT ,
      FOREIGN KEY (grade_code) 
          REFERENCES user_grade (grade_code)
          ON UPDATE SET NULL
          ON DELETE SET NULL
  ) ENGINE=INNODB;

  INSERT 
    INTO user_foreignkey2
  (user_no, user_id, user_pwd, user_name, gender, phone, email, grade_code)
  VALUES
  (1, 'user01', 'pass01', '홍길동', '남', '010-1234-5678', 'hong123@gmail.com', 10),
  (2, 'user02', 'pass02', '유관순', '여', '010-777-7777', 'yu77@gmail.com', 20);

  SELECT * FROM user_foreignkey2;
</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/3eaa150b-3a68-4dcd-a6f8-50ea40ab6031/image.png" /></p>
</blockquote>
</li>
<li><p>1) 부모 테이블의 grade_code 수정  (user_foreignkey1 테이블 DROP하고 진행할 것(user_foreignkey에는 foreign key 제약조건에 수정 및 삭제룰 적용이 되지 않았기 때문)</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS user_foreignkey1;

  UPDATE user_grade
     SET grade_code = null
   WHERE grade_code = 10;

  -- 자식 테이블의 grade_code가 10이 었던 회원의 grade_code값이 NULL이 된 것을 확인
  SELECT * FROM user_foreignkey2;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1b30711e-b5a7-487b-b4fe-fb033ec2115e/image.png" /></p>
</blockquote>
</li>
<li><p>2) 부모 테이블의 행 삭제  (user_foreignkey1 테이블 DROP하고 진행할 것(user_foreignkey에는 foreign key 제약조건에 수정 및 삭제룰 적용이 되지 않았기 때문)</p>
<pre><code class="language-sql">  DELETE 
    FROM user_grade
   WHERE grade_code = 20;

  -- 자식 테이블의 grade_code가 20이 었던 회원의 grade_code값이 NULL이 된 것을 확인
  SELECT * FROM user_foreignkey2;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/6c85b92a-5cad-4d48-8708-222f61626e09/image.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="1-5-check">1-5. CHECK</h2>
<ul>
<li><p>check 제약 조건 위반시 허용하지 않는 제약조건</p>
</li>
<li><p>제약조건 확인용 테이블 생성 및 테스트 데이터 INSERT 후 조회하기</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS user_check;
  CREATE TABLE IF NOT EXISTS user_check (
      user_no INT AUTO_INCREMENT PRIMARY KEY,
      user_name VARCHAR(255) NOT NULL,
      gender VARCHAR(3) CHECK(gender IN ('남','여')),
      age INT CHECK(age &gt;= 19)
  ) ENGINE=INNODB;

  INSERT 
    INTO user_check
  VALUES 
  (null, '홍길동', '남', 25),
  (null, '이순신', '남', 33);

  SELECT * FROM user_check;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="Untitled" src="https://v2.velog.io/rss/CONSTRAINTS%2054e32962d1064690b8021c135f63b7bd/Untitled%2013.png" /></p>
</blockquote>
</li>
<li><p>gender 컬럼의 CHECK 제약 조건 에러 발생(성별이 두 글자)</p>
<pre><code class="language-sql">  INSERT 
    INTO user_check
  VALUES (null, '안중근', '남성', 27);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="Untitled" src="https://v2.velog.io/rss/CONSTRAINTS%2054e32962d1064690b8021c135f63b7bd/Untitled%2014.png" /></p>
</blockquote>
</li>
<li><p>age 컬럼의 CHECK 제약 조건 에러 발생(나이가 19세 미만)</p>
<pre><code class="language-sql">  INSERT 
    INTO user_check
  VALUES (null, '유관순', '여', 17);</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="Untitled" src="https://v2.velog.io/rss/CONSTRAINTS%2054e32962d1064690b8021c135f63b7bd/Untitled%2015.png" /></p>
</blockquote>
</li>
</ul>
<h2 id="default">DEFAULT</h2>
<ul>
<li><p>컬럼에 null 대신 기본 값 적용</p>
</li>
<li><p>컬럼 타입이 DATE일 시 current_date만 가능</p>
</li>
<li><p>컬럼 타입이 DATETIME일 시 current_time과 current_timestamp, now() 모두 사용 가능</p>
</li>
<li><p>제약조건 확인용 테이블 생성 및 테스트 데이터 INSERT 후 조회하기</p>
<pre><code class="language-sql">  DROP TABLE IF EXISTS tbl_country;
  CREATE TABLE IF NOT EXISTS tbl_country (
      country_code INT AUTO_INCREMENT PRIMARY KEY,
      country_name VARCHAR(255) DEFAULT '한국',
      population VARCHAR(255) DEFAULT '0명',
      ****add_day DATE DEFAULT (current_date),
      add_time DATETIME DEFAULT (current_time)
  ) ENGINE=INNODB;

  SELECT * FROM tbl_country;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1fe18449-1a06-44ac-98f3-59518e0376f3/image.png" /></p>
</blockquote>
</li>
<li><p>default 설정이 되어 있는 컬럼들에 default 값이 들어가도록 INSERT 진행 후 조회</p>
<pre><code class="language-sql">  INSERT 
    INTO tbl_country
  VALUES (null, default, default, default, default);

  SELECT * FROM tbl_country;</code></pre>
<blockquote>
<p><code>실행결과</code></p>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/c043e329-acef-4f2b-857c-85d987ce993c/image.png" /></p>
</blockquote>
</li>
</ul>