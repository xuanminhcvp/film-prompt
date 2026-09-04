#!/usr/bin/env python3
"""Tra cứu Mẫu Thumbnail từ kho mẫu Thumbnail template.xlsx.

Mục đích: Trích xuất và hiển thị đúng 2 prompt mẫu Thumbnail từ kho sfboard/thumbnail-templates.json
(được trích xuất từ /Users/may1/Downloads/Thumbnail template.xlsx) dựa theo Keyword hoặc Tên Sheet + Hàng.

Cú pháp:
    python3 sfboard/tim-thumbnail.py <keyword1> [keyword2 ...]
    python3 sfboard/tim-thumbnail.py <Tên_Sheet> <Số_Hàng>

Ví dụ:
    python3 sfboard/tim-thumbnail.py "Diner" 2
    python3 sfboard/tim-thumbnail.py "Máy bay" 3
    python3 sfboard/tim-thumbnail.py xé vé cựu chiến binh
"""

import json
import os
import sys

PATH_DB = os.path.join(os.path.dirname(__file__), "thumbnail-templates.json")


def load_db():
    if not os.path.exists(PATH_DB):
        print(f"✗ Không thấy kho mẫu {PATH_DB}")
        sys.exit(1)
    with open(PATH_DB, "r", encoding="utf-8") as f:
        return json.load(f)


def tim_theo_sheet_hang(data, sheet_name, row_num):
    sheet_name_clean = sheet_name.lower().strip()
    for cat in data.get("categories", []):
        if cat.get("sheet", "").lower().strip() == sheet_name_clean:
            for tpl in cat.get("templates", []):
                if tpl.get("row") == int(row_num):
                    return (cat.get("sheet"), tpl)
    # Tìm gần đúng nếu không trùng khớp 100%
    for cat in data.get("categories", []):
        if sheet_name_clean in cat.get("sheet", "").lower():
            for tpl in cat.get("templates", []):
                if tpl.get("row") == int(row_num):
                    return (cat.get("sheet"), tpl)
    return None


def tim_theo_keywords(data, keywords):
    results = []
    kw_set = {k.lower().strip() for k in keywords if k.strip()}

    for cat in data.get("categories", []):
        sheet = cat.get("sheet", "")
        for tpl in cat.get("templates", []):
            tpl_kws = {k.lower() for k in tpl.get("keywords", [])}
            tpl_prompt = tpl.get("prompt", "").lower()
            
            # Tính điểm khớp: keyword trùng trong tag hoặc xuất hiện trong prompt/sheet
            match_score = 0
            for kw in kw_set:
                if any(kw in tk for tk in tpl_kws):
                    match_score += 3
                elif kw in sheet.lower():
                    match_score += 2
                elif kw in tpl_prompt:
                    match_score += 1

            if match_score > 0:
                results.append((match_score, sheet, tpl))

    results.sort(key=lambda x: x[0], reverse=True)
    return results[:2]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    data = load_db()
    args = sys.argv[1:]

    # Kiểm tra xem có phải gõ tên Sheet + Số Hàng không (vd: "Diner" 2)
    if len(args) == 2 and args[1].isdigit():
        sheet_name, row_num = args[0], int(args[1])
        matched = tim_theo_sheet_hang(data, sheet_name, row_num)
        if matched:
            sheet, tpl = matched
            print(f"═══ MẪU THUMBNAIL CHÍNH XÁC [Sheet: {sheet} | Hàng {tpl['row']}] ═══\n")
            print(f"Keywords: {tpl.get('keyword_raw', '')}")
            print(f"Prompt thô gốc ({len(tpl['prompt'])} ký tự):\n{tpl['prompt']}\n")
            return
        else:
            print(f"✗ Không thấy mẫu ở Sheet '{sheet_name}' hàng {row_num}. Chuyển sang tìm theo keyword...")

    # Tra cứu theo Keywords
    matches = tim_theo_keywords(data, args)
    if not matches:
        print("✗ Không tìm thấy mẫu thumbnail nào phù hợp với keyword.")
        sys.exit(1)

    print(f"═══ TÌM THẤY {len(matches)} MẪU THUMBNAIL PHÙ HỢP NHẤT ═══\n")
    for idx, (score, sheet, tpl) in enumerate(matches, 1):
        print(f"--- MẪU #{idx} [Sheet: {sheet} | Hàng {tpl['row']} | Keywords: {tpl.get('keyword_raw', '')}] ---")
        print(f"Prompt thô gốc ({len(tpl['prompt'])} ký tự):\n{tpl['prompt']}\n")


if __name__ == "__main__":
    main()
