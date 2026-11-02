# keyring.jpg 갤러리에 표시하는 방법

1. `MAKER_LAB_advanced/gallery/keyring.jpg` 또는 `MAKER_LAB_advanced/galley/keyring.jpg`에 사진을 넣습니다. 두 철자 모두 지원합니다.
2. `start_windows.bat`를 더블클릭합니다. Python 3 설치 필요.
3. 브라우저에서 `http://localhost:8000` 접속 후 **작품 갤러리** 메뉴를 선택합니다.
4. **갤러리 새로고침**을 눌러 사진을 확인합니다.
5. 작품명과 소개는 사진을 넣은 폴더의 `works.json`에 같은 파일명으로 등록합니다. 예시:

```json
{
  "works": {
    "keyring.jpg": {
      "title": "나만의 키링",
      "description": "AI 디자인과 레이저 각인으로 만든 작품입니다.",
      "category": "디지털 굿즈"
    }
  }
}
```

**진단 방법**: `http://localhost:8000/gallery-manifest.json`에 접속해서 `keyring.jpg`가 목록에 있는지 확인하세요. `gallery`에 넣었으면 `folder`가 `gallery`, `galley`에 넣었으면 `galley`여야 합니다.

**주의**: `index.html` 더블클릭(`file://`)은 브라우저 보안 제한으로 자동 탐색이 되지 않습니다. 서버로 실행해야 합니다. 정적 웹호스팅이라면 이미지 추가 후 `python refresh_images.py` 실행과 갱신된 `gallery-manifest.json` 업로드가 필요합니다.

**파일명**: `keyring.jpg`, `keyring-01.png`, `keyring-02.webp`처럼 영문/숫자/하이픈 사용을 추천합니다. 확장자 및 대소문자 일치 확인.
