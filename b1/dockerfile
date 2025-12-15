# 1. 베이스 이미지로 Node.js 18-alpine 버전을 사용
FROM node:18-alpine

# 2. 컨테이너 내부에 /app 이라는 작업 디렉터리 생성
WORKDIR /app

# 3. package.json과 package-lock.json 파일을 먼저 복사 (의존성 캐싱을 위함)
COPY package*.json ./

# 4. 의존성 패키지 설치
RUN npm install

# 5. 현재 디렉터리(a1)의 모든 소스코드를 컨테이너의 /app 디렉터리로 복사
COPY . .

# 6. 컨테이너가 시작될 때 실행할 명령어 (package.json의 scripts에 맞게 수정)
CMD ["npm", "start"]
