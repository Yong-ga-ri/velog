<h1 id="data--information">Data &amp; Information</h1>
<h2 id="data">Data</h2>
<blockquote>
<p>💡 관찰의 결과. <strong>정량적 혹은 정성적 실제 값</strong>
ex) 2024년 전세사기 피해자 수: 5000명</p>
</blockquote>
<h2 id="information">Information</h2>
<blockquote>
<p>💡 데이터를 기반으로 <strong>의미를 부여</strong>된 것
ex) 최근 전세사기 피해자 수가 증가하는 추세이다.</p>
</blockquote>
<hr />
<h1 id="database">Database</h1>
<blockquote>
<p>💡 한 조직에 필요한 정보를 여러 응용 시스템에서 공용으로 사용할 수 있도록 논리적으로 연관된 데이터를 모으고, 중복되는 데이터를 최소화하여 <strong>구조적으로 통합/저장</strong>해 놓은 것.
구조화된 데이터의 집합으로 컴퓨터에서 쉽게 접근, 관리, 업데이트 가능.</p>
</blockquote>
<h2 id="data-정의">DATA 정의</h2>
<blockquote>
<ol>
<li><strong>운영 데이터(Operational Data)</strong>: 조직의 목적을 위해 사용되는 데이터</li>
<li><strong>공용 데이터(Shared Data)</strong>: 공동으로 사용되는 데이터</li>
<li><strong>통합 데이터(Integrated Data)</strong>: 중복을 최소화하여 중복으로 인한 데이터 불일치 현상 제거</li>
<li><strong>저장 데이터(Stored Data)</strong>: 컴퓨터 저장 장치에 저장된 데이터<blockquote>
<p>저장 데이터 -&gt; <code>영속성 데이터</code>: 보조기억장치(SSD, HDD)에 저징되는 데이터</p>
</blockquote>
</li>
</ol>
</blockquote>
<h2 id="database-특징">Database 특징</h2>
<blockquote>
<ol>
<li><strong>실시간 접근성(Real Time Accessibility)</strong>: 사용자의 데이터 요청 시, 실시간으로 결과 제공.</li>
<li><strong>계속적인 변화(Continuous Change)</strong>: 데이터 값은 시간에 따라 계속 바뀜.</li>
<li><strong>동시 공유(Concurrent Sharing)</strong>: 데이터베이스는 서로 다른 업무 또는 여러 사용자에게 동시 공유됨.</li>
<li><strong>내용에 따른 참조(Reference By Content):</strong> 데이터베이스에 저장된 데이터는 데이터의 물리적 위치가 아니라 데이터 값에 따라 참조됨.</li>
</ol>
</blockquote>
<hr />
<h1 id="dbmsbrdatabase-management-system">DBMS(Database Management System)</h1>
<h2 id="dbms">DBMS</h2>
<blockquote>
<p>💡 데이터베이스에서 데이터를 <code>추출</code>, <code>조작</code>, <code>정의</code>, <code>제어</code> 등을 할 수 있게 해주는 <strong>데이터베이스 전용 관리 프로그램</strong>들</p>
<p>데이터베이스와 개발자가 소통하는 매개체
<img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/1945b89f-4939-4176-bd9e-6a8230627084/image.png" /></p>
</blockquote>
<h2 id="dbms의-기능">DBMS의 기능</h2>
<table>
<thead>
<tr>
<th>주요 기능</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>데이터 추출(Retrieval)</td>
<td>사용자가 조회하는 데이터 혹은 응용 프로그램의 데이터를 추출</td>
</tr>
<tr>
<td>데이터 조작(Manipulation)</td>
<td>데이터를 조작하는 소프트웨어(응용 프로그램)가 요청하는 데이터의 <strong>삽입</strong>, <strong>수정</strong>, <strong>삭제</strong> 작업을 지원</td>
</tr>
<tr>
<td>데이터 정의(Definition)</td>
<td>데이터의 구조를 정의하고 데이터 구조에 대한 삭제 및 변경 기능을 수행</td>
</tr>
<tr>
<td>데이터 제어(Control)</td>
<td>데이터베이스 사용자를 생성하고 모니터링하며 접근을 제어백업과 회복, 동시성 제어 등의 기능을 지원</td>
</tr>
</tbody></table>
<h2 id="dbms의-사용-이점">DBMS의 사용 이점</h2>
<table>
<thead>
<tr>
<th>주요 이점</th>
<th>내용</th>
</tr>
</thead>
<tbody><tr>
<td>데이터 중복최소화</td>
<td>데이터와 응용 프로그램을 분리시켜, 상호 영향을 줄일 수 있음.</td>
</tr>
<tr>
<td>쿼리 언어</td>
<td>DBMS는 SQL(Structured Query Language)과 같은 쿼리 언어를 제공,복잡한 검색 및 분석 작업을 쉽게 수행가능.</td>
</tr>
<tr>
<td>데이터 무결성</td>
<td>DBMS는 데이터의 무결성을 보장하기 위해 다양한 제약 조건과 규칙을 설정 가능.이로부터 데이터의 품질과 정확성을 보장.</td>
</tr>
<tr>
<td>데이터백업 및 복구</td>
<td>DBMS는 데이터의 백업과 복구를 지원.  시스템 장애나 데이터 손상 시에도 데이터를 복원 가능.</td>
</tr>
<tr>
<td>표준화</td>
<td>DBMS는 표준화된 방법을 통해 데이터를 관리.데이터의 구조와 접근 방법이 일괄적. 따라서 애플리케이션 개발 및 유지보수가 용이.</td>
</tr>
</tbody></table>
<h2 id="dbms의-종류와-특징">DBMS의 종류와 특징</h2>
<table>
<thead>
<tr>
<th></th>
<th>SQL Server</th>
<th>Oracle</th>
<th>MySQL</th>
<th>MariaDB</th>
<th>DB2</th>
<th>SQLite</th>
</tr>
</thead>
<tbody><tr>
<td>제조사</td>
<td>MS</td>
<td>Oracle</td>
<td>Oracle</td>
<td>MariaDB재단</td>
<td>IBM</td>
<td>D.Richard Hipp(오픈소스)</td>
</tr>
<tr>
<td>기반운영체제</td>
<td>윈도우</td>
<td>윈도우유닉스리눅스</td>
<td>윈도우유닉스리눅스</td>
<td>윈도우유닉스리눅스</td>
<td>유닉스</td>
<td>모바일OS(안드로이드, IOS 등)</td>
</tr>
<tr>
<td>용도</td>
<td>윈도우기반기업용</td>
<td>대용량데이터베이스</td>
<td>소용량데이터베이스</td>
<td>소용량데이터베이스</td>
<td>대용량데이터베이스</td>
<td>모바일전용데이터베이스</td>
</tr>
</tbody></table>
<h2 id="database의-변천-과정">Database의 변천 과정</h2>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/e1ad70f3-f07e-4802-951f-8caf07bf29c6/image.png" /></p>
<ul>
<li><p><strong>파일시스템(File System)</strong></p>
<ul>
<li>데이터를 파일 형태로 저장</li>
<li>가장 기본적인 데이터 저장 방식<ul>
<li>👍: 복잡하지 않음</li>
<li>👎: 효율적인 데이터 관리 기능 부족</li>
</ul>
</li>
</ul>
</li>
<li><p><strong>계층 데이터 모델(Hierarchical Data Model)</strong></p>
<ul>
<li>데이터를 계층적 트리 구조로 조직화</li>
<li>각 레벨의 데이터 항목은 상위 레벨의 하나의 항목에 연결.</li>
<li>부모-자식 관계를 사용하여 데이터 관계를 표현</li>
<li>주로 문서 관리 시스템이나 XML 데이터베이스에서 사용</li>
</ul>
</li>
<li><p><strong>네트워크 데이터 모델(Network Data Model)</strong></p>
<ul>
<li>계층 모델과 유사하지만 하나의 데이터 항목이 여러 상위 항목과 연결될 수 있어 복잡한 관계와 데이터 구조를 나타내는 데 적합</li>
<li>각 노드는 여러 부모노드를 가질 수 있어 더 유연한 관계 표현이 가능</li>
</ul>
</li>
<li><p><strong>관계 데이터 모델(Relational Data Model)</strong></p>
<ul>
<li>데이터를 테이블 형태로 구성(행과 열로 구성)</li>
<li>서로 다른 테이블 간의 관계는 키를 통해 정의</li>
<li>데이터의 무결성을 유지하고 SQL을 사용하여 복잡한 쿼리와 데이터 조작을 용이하게 함</li>
</ul>
</li>
<li><p><strong>객체 데이터 모델(Object Data Model)</strong></p>
<ul>
<li>객체 지향 프로그래밍의 개념을 데이터 모델링에 적용</li>
<li>데이터에 연관된 동작을 객체로 캡슐화하고 복잡한 데이터 구조와 상속, 다형성 등 객체 지향 개념을 지원하여 <strong>개발자가 더 자연스러운 방식</strong>으로 데이터를 처리할 수 있게 함.</li>
</ul>
</li>
<li><p><strong>객체-관계 데이터 모델(Object-Relational Data Model)</strong></p>
<ul>
<li>객체 데이터 모델과 관계 데이터 모델의 특징을 결합</li>
<li>데이터를 객체로 관리하면서도 관계형 데이터베이스의 기능을 제공.</li>
<li>복잡한 데이터 유형과 관계를 처리할 수 있음</li>
<li>상속과 다형성 같은 객체 지향 특성을 관계형 데이터베이스 내에서 사용할 수 있게 함</li>
</ul>
</li>
</ul>
<h2 id="database의-유형">Database의 유형</h2>
<h3 id="계층형-데이터베이스-vs-네트워크형-데이터베이스">계층형 데이터베이스 vs 네트워크형 데이터베이스</h3>
<h4 id="계층형-데이터베이스hierarchical-database"><strong>계층형 데이터베이스(Hierarchical Database)</strong></h4>
<blockquote>
<p>💡 트리 구조를 가짐. 각 노드는 한 개 이상의 자식 노드를 가질 수 있지만 <strong>한 개의 부모 노드만 가질 수 있다</strong>.
데이터는 <strong>&quot;부모-자식&quot;</strong> 관계를 통해 연결 됨. 이런 특성은 특히 조직 구조나 파일 시스템과 같이 자연스럽게 계층 구조를 가지는 데이터를 표현하는데 적합.</p>
</blockquote>
<ul>
<li><p>👍:</p>
<ul>
<li>계층적인 구조는 직관적이고 이해하기 쉬움.</li>
<li>부모-자식 관계에 의한 데이터 접근이 빠름.</li>
</ul>
</li>
<li><p>👎:</p>
<ul>
<li>복잡한 많은 many to many 관계를 표현하는 것이 어려움.</li>
<li>유연성이 부족, 구조 변경 어려움.</li>
</ul>
</li>
</ul>
<h4 id="네트워크형-데이터베이스network-database"><strong>네트워크형 데이터베이스(Network Database)</strong></h4>
<blockquote>
<p>💡 그래프 구조를 가짐. 각 노드는 여러 부모 노드를 가질 수 있어, 계층형보다 복잡한 관계를 표현 가능.
데이터는 &quot;주인-멤버&quot; 관계를 통해 연결됨.
특히 이는 많은 M:N 관계를 가지는 데이터를 표현하는데 적합.</p>
</blockquote>
<ul>
<li><p>👍:</p>
<ul>
<li>복잡한 관계를 표현 가능.</li>
<li>데이터 무결성을 유지하는데 효과적.</li>
</ul>
</li>
<li><p>👎:</p>
<ul>
<li>구조가 복잡. 이해하기 어려움.</li>
<li>데이터 검색 및 관리에 높은 수준의 처리능력이 필요.</li>
</ul>
</li>
</ul>
<h4 id="관계형-데이터베이스rdbms-relational-database-management-system"><strong>관계형 데이터베이스(RDBMS, Relational Database Management System)</strong></h4>
<blockquote>
<p>💡 데이터를 테이블의 형태로 저장. 각 테이블은 행(레코드)과 열(필드)로 구성. 테이블 간의 관계는 공통 필드를 통해 형성.
SQL(Structured Query Language)은 RDBMS에서 데이터를 조작하고 쿼리하는데 주로 사용되는 언어로 엄격한 데이터 무결성 규칙을 가짐.
ACID(Atomicity, Consistency, Isolation, Durability) 트랜잭션 속성을 지원.</p>
<blockquote>
<p><strong>Atomicity(원자성)</strong>
: 트랜잭션 내의 모든 연산은 하나의 단위로 간주되어야 한다.
<strong>Consistency(일관성)</strong>
: 트랜잭션의 실행이 완료되면, 데이터베이스는 일관된 상태를 유지해야 한다. (무결성 제약조건을 만족함을 보증)
<strong>Isolation(고립성)</strong>
: 동시에 실행되는 여러 트랜잭션이 서로 영향을 주지 않도록 관리해서 동시성을 관리해야 한다.
<strong>Durability(지속성)</strong>
: 트랙잭션이 성공적으로 완료되면 시스템에 장애가 발생하더라도 영구적으로 반영되어야한다.(커밋 되면 안전하게 저장됨을 보증)</p>
</blockquote>
</blockquote>
<ul>
<li>👍:<ul>
<li>데이터 무결성을 유지하는데 효과적.</li>
<li>강력한 쿼리 언어(SQL)로 복잡한 데이터 조작 가능.</li>
<li>데이터의 정규화를 통해 중복성을 최소화.</li>
</ul>
</li>
<li>👎:<ul>
<li>복잡한 객체 관계를 표현하는데 한계.</li>
<li>스키마 변경이 어렵고 비용이 많이 듦.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/220a8cb9-1598-4823-b3e2-b8b033fb8563/image.png" /></p>
<h4 id="객체-관계형-데이터베이스ordbms-object-relational-database-management-system"><strong>객체-관계형 데이터베이스(ORDBMS, Object-Relational Database Management System)</strong></h4>
<blockquote>
<p>💡 관계형 데이터베이스의 기능을 확장하여 객체 지향 데이터 모델을 지원.
이를 통해 ORDBMS는 복잡한 데이터 타입(예: 배열, 딕셔너리 등)과 메소드, 상속 등의 객체 지향 기능을 활용 가능.
ORDBMS는 RDBMS의 테이블 구조와 SQL의 강력한 쿼리 기능을 유지하면서, 객체 지향 프로그래밍의 유연성과 복잡한 데이터 구조를 지원하는 것이 특징.</p>
</blockquote>
<ul>
<li>👍:<ul>
<li>복잡한 데이터 타입과 객체 지향 프로그래밍을 지원.</li>
<li>관계형 데이터베이스의 강력한 쿼리 기능과 데이터 무결성을 유지.</li>
</ul>
</li>
<li>👎:<ul>
<li>구현이 복잡하며, 관리가 어렵다.</li>
<li>모든 상황에 적합한 솔루션은 아니므로 일반적인 업무용 애플리케이션에는 RDBMS가 더 적합할 수 있다.
  -&gt; 사실 현재는 ORDBM과 RDBM을 구분하는 큰 의미는 없다.</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/rlfgks97/post/597140fd-bac6-4b16-9c4f-1423e4395ea3/image.png" /></p>
<hr />
<details>
🎯 학습 목표
<div>

<h4 id="데이터와-정보">데이터와 정보</h4>
<p>데이터와 정보의 차이점을 명확하게 설명할 수 있다.
예시를 통해 데이터와 정보의 관계를 설명할 수 있다.</p>
<h4 id="데이터베이스">데이터베이스</h4>
<p>데이터베이스의 정의와 목적을 이해한다.
데이터베이스의 주요 특징을 설명할 수 있다.</p>
<h4 id="데이터베이스-관리-시스템-dbms">데이터베이스 관리 시스템 (DBMS)</h4>
<p>DBMS의 정의와 역할을 이해한다.
DBMS의 주요 기능과 사용 이점을 설명할 수 있다.
주요 DBMS의 종류와 각 DBMS의 특징을 이해한다.</p>
<h4 id="데이터베이스의-변천-과정">데이터베이스의 변천 과정</h4>
<p>파일 시스템, 계층 데이터 모델, 네트워크 데이터 모델, 관계 데이터 모델, 객체 데이터 델, 객체-관계 데이터 모델의 차이점을 이해한다.</p>
<h4 id="데이터베이스의-유형">데이터베이스의 유형</h4>
<p>계층형 데이터베이스, 네트워크형 데이터베이스, 관계형 데이터베이스, 객체-관계형 데이터베이스의 정의와 특징을 이해한다.</p>
</div>
</details>

<hr />
<details>
체크리스트
<div>


<h4 id="데이터와-정보-1">데이터와 정보</h4>
<ul>
<li><input disabled="" type="checkbox" /> 데이터란 무엇인가?</li>
<li><input disabled="" type="checkbox" /> 정보란 무엇인가?</li>
<li><input disabled="" type="checkbox" /> 데이터와 정보의 차이를 설명하시오.</li>
</ul>
<h4 id="데이터베이스-1">데이터베이스</h4>
<ul>
<li><input disabled="" type="checkbox" /> 데이터베이스란 무엇인가?</li>
<li><input disabled="" type="checkbox" /> 데이터베이스의 주요 특징 4가지를 설명하시오.</li>
</ul>
<h4 id="데이터베이스-관리-시스템-dbms-1">데이터베이스 관리 시스템 (DBMS)</h4>
<ul>
<li><input disabled="" type="checkbox" /> DBMS란 무엇인가?(데이터베이스와 분리하여 설명)</li>
<li><input disabled="" type="checkbox" /> DBMS의 주요 기능 4가지를 설명하시오.</li>
<li><input disabled="" type="checkbox" /> DBMS를 사용할 때의 이점 3가지를 설명하시오.</li>
<li><input disabled="" type="checkbox" /> SQL Server, Oracle, MySQL, MariaDB, DB2, SQLite의 특징을 비교하시오.</li>
</ul>
<h4 id="데이터베이스의-변천-과정-1">데이터베이스의 변천 과정</h4>
<ul>
<li><input disabled="" type="checkbox" /> 파일 시스템과 계층 데이터 모델의 차이점을 설명하시오.</li>
<li><input disabled="" type="checkbox" /> 네트워크 데이터 모델과 관계 데이터 모델의 차이점을 설명하시오.</li>
<li><input disabled="" type="checkbox" /> 객체 데이터 모델과 객체-관계 데이터 모델의 차이점을 설명하시오.</li>
</ul>
<h4 id="데이터베이스의-유형-1">데이터베이스의 유형</h4>
<ul>
<li><input disabled="" type="checkbox" /> 계층형 데이터베이스의 장단점을 설명하시오.</li>
<li><input disabled="" type="checkbox" /> 네트워크형 데이터베이스의 장단점을 설명하시오.</li>
<li><input disabled="" type="checkbox" /> 관계형 데이터베이스의 특징과 장단점을 설명하시오.</li>
<li><input disabled="" type="checkbox" /> 객체-관계형 데이터베이스의 특징과 장단점을 설명하시오.</li>
</ul>
</div>
</details>