## 클래스101 2차 프로젝트 Back-end 소개

- 국내 최대 교육 프로그램 [클래스101](https://class101.net/) 모티브 프로젝트
- 짧은 프로젝트 기간동안 개발에 집중해야 하므로 디자인/기획 부분만 모티브로 했습니다.
- 개발은 초기 세팅부터 전부 직접 구현했으며 프론트앤드와 연결하여 실제 사용할 수 있는 서비스 수준으로 개발한 것입니다.

### 개발 인원 및 기간

- 개발기간 : 2021/3/29~ 2021/4/9
- 개발 인원 : 프론트엔드 4명, 백엔드 3명
- [백엔드 github 링크](https://github.com/wecode-bootcamp-korea/18-2nd-class200ok-backend)

### 프로젝트 선정이유

- 이 사이트는 여태 해왔던 소셜 커머스 사이트가 아닌 교육 사이트로, 크리에이터가 자유롭게 사이트 내에서 강좌를 개설하면서 동시에 소비할 수 있는 형태가 인상적이었습니다. 또한 인스타그램처럼 스토리 형식으로 데이터를 출력할 수 있는 부분이 흥미로웠습니다.

<br>
## 적용 기술 및 구현 기능

### 적용 기술

> - Back-End : Python, Django web framework, Bcrypt, , JWT, Transaction, MySQL
> - Common : AWS(EC2,RDS), RESTful API, S3

### 구현 기능

#### 소셜 로그인 (내가 한 부분)

- 회원가입 / 로그인을 소셜 로그인(카카오) 통해 구현 
- python request 이해 통한 카카오 소셜 로그인 로직 구현
- 카카오 API 통한 access token을 통해 유저 정보 획득 뒤 다시 new_token 부여하여 유저 관리
- 유닛테스트 중 발견된 1071 error 디버깅 통한 모델링 시 컬럼 설정에 대한 주의 및 용량 이해


#### 메인페이지

- 오픈 예정 사이트 필터링 및 솔팅으로 구현 
- 같은 변수의 쿼리스트링 여러 개가 오도록 getlist사용
- 처음에 if문 사용해서 솔팅했던 것을 filter와 order_by사용해서 코드 줄임

#### S3를 통한 이미지 삽입

- AWS 정책생성기를 활용하여 객체에 대한 엑세스 권한을 제공하는 버킷 정책 작성
<업로드 관련 사항 정리>
- 가상환경에 boto3, django-storages 설치
- 이때 setting.py 의 INSTALLED_APP 에 'storages'추가
- 파일과 텍스트를 multipart/form-data 형식으로 한번에 수신
- request.FILES 를 통해 파일을, 
- request.POST 를 통해 텍스트를 수신
- 만약 다수의 파일/텍스트를 전달 받을 경우 python의 getlist method 를 사용
- 전달받은 파일은 랜덤한 값을 붙여  S3로 저장
- 전달받은 텍스트와 s3 에 저장한 파일의 url 을 테이블에 저장



#### 데이터 입력 및 배포
- RDS DB 통해 멤버 데이터베이스 일원화
- csv 파일 제작 후 api 구성하여 데이터 한 번에 입력
- AWS 배포 통한 데이터베이스 배포 완료

### 리팩토리 예정

#### 오픈 예정 강좌 바로 수강으로 넘기는 로직 구현 논의

<br>

## Reference

- 이 프로젝트는 [클래스101](https://class101.net/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
