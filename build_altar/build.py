# -*- coding: utf-8 -*-
"""Ráp sf-board.json cho PIPELINE-ALTAR từ các module scene đã viết."""
import importlib, json, os, sys, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib, ref_nv, ref_prop, ref_dd1, ref_dd2, ref_dd3

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',
                   'PIPELINE-ALTAR.project', 'sf-board.json')

FILM = ("ABANDONED AT THE ALTAR, SHE MARRIED A STRANGER IN A WHEELCHAIR — "
        "UNAWARE HE IS A SECRET BILLIONAIRE")

def them_lenh_cat(sfs):
    """Lệnh Cắt Tham Chiếu — mỗi khung gọi tên người BỊ GẠT khỏi lô ref.

    Cả một địa điểm dùng chung một đoạn chat, nên ảnh ref của các khung trước
    vẫn nằm trong ngữ cảnh; không gọi tên người thừa thì model kéo họ vào khung
    sau, thành chật khung và sai cast. Dàn diễn viên lấy từ chính `pose.who` của
    scene nên không thể khai sót hay khai thừa. SF nào đã tự mang `cut` (Scene 1)
    thì giữ nguyên, và các thẻ REF không có `pose` thì bỏ qua.
    """
    dan = []
    for x in sfs:
        for t in (x.get('pose') or {}).get('who', {}):
            if t not in dan:
                dan.append(t)
    for x in sfs:
        if 'THAM CHIẾU:' in x['prompt']:
            continue
        co = list((x.get('pose') or {}).get('who', {}))
        bo = [t for t in dan if t not in co]
        if not co or not bo:
            continue
        x['prompt'] += (f"\n\nTHAM CHIẾU: CHỈ tham chiếu {' và '.join(co)}. "
                        f"KHÔNG tham chiếu và KHÔNG vẽ {', '.join(bo)}.")


scenes = [{
    "id": "REF",
    "name": "REF — nhân vật · đạo cụ · bối cảnh",
    "sfs": ref_nv.R + ref_prop.R + ref_dd1.R + ref_dd2.R + ref_dd3.R,
    "shots": [],
    "script": "",
}]

for n in range(1, 26):
    mod = f"s{n:02d}"
    try:
        m = importlib.import_module(mod)
    except ModuleNotFoundError:
        continue
    sid = f"S{n}"
    them_lenh_cat(m.SFS)
    scenes.append({
        "id": sid,
        "name": lib.KB[sid][0],
        "sfs": m.SFS,
        "shots": m.SHOTS,
        "script": lib.script(sid),
    })

board = {"film": FILM,
         "updated_at": datetime.datetime.now().isoformat(timespec='seconds'),
         "scenes": scenes}

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(board, f, ensure_ascii=False, indent=1)

nsf = sum(len(s['sfs']) for s in scenes)
nsh = sum(len(s['shots']) for s in scenes)
giay = sum(x['dur'] for s in scenes for x in s['shots'])
print(f"✓ {os.path.abspath(OUT)}")
print(f"  {len(scenes)-1} scene · {nsf} SF · {nsh} shot · {giay//60}:{giay%60:02d}")
