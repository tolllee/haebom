#!/usr/bin/env python3
"""이미지 목록을 갱신합니다. 웹 호스팅에 올릴 때 사용."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
folder=root/'images'
allowed={'.jpg','.jpeg','.png','.webp','.gif','.avif'}
images=sorted(p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file() and p.suffix.lower() in allowed and not p.name.startswith('.'))
(root/'images-manifest.json').write_text(json.dumps({'images':images},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'이미지 {len(images)}개 등록 완료: images-manifest.json')

# 작품 갤러리 목록 생성
folders=[root/'gallery']
works=sorted(({'file':p.relative_to(folder).as_posix(),'folder':folder.name} for folder in folders for p in folder.rglob('*') if p.is_file() and p.suffix.lower() in allowed and not p.name.startswith('.')),key=lambda v:(v['folder'],v['file'].casefold()))
(root/'gallery-manifest.json').write_text(json.dumps({'images':works},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'작품 {len(works)}개 등록 완료: gallery-manifest.json')

# 음악 플레이리스트 목록 생성 (정적 호스팅 용도)
music_dir=root/'music'
allowed_music={'.mp3','.wav','.ogg','.m4a','.aac'}
tracks=sorted((v.relative_to(music_dir).as_posix() for v in music_dir.rglob('*') if v.is_file() and v.suffix.lower() in allowed_music and not v.name.startswith('.')),key=str.casefold)
(root/'music-manifest.json').write_text(json.dumps({'tracks':tracks},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'음악 {len(tracks)}곡 등록 완료: music-manifest.json')
