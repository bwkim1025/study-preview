import json,re
from pathlib import Path
B=Path(__file__).resolve().parent.parent/'briefings'
fs=sorted(p.name for p in B.glob('*.md') if re.match(r'^\d{4}-\d{2}-\d{2}-day[123]\.md$',p.name))
json.dump({"generatedAt":"2026-11-24T12:00:00+09:00","count":len(fs),"files":[{"date":f[:10],"day":int(f[14]),"file":f} for f in fs]},open(B/'index.json','w'),ensure_ascii=False,indent=2)
print(len(fs))
