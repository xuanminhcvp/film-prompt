#!/usr/bin/env python3
"""Hoàn thiện sf-board của FILM-WILLA từ KICH-BAN.md theo skills-film."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROJECT = ROOT / "FILM-WILLA--BA-TRAM-CHIEC-HARLEY.project"
SCRIPT_PATH = PROJECT / "KICH-BAN.md"
BOARD_PATH = PROJECT / "sf-board.json"


AGES = {
    "WILLA": (28, "Black American woman"),
    "ODESSA": (75, "Black American woman"),
    "NOLAN": (34, "white American man"),
    "CROSS": (45, "white American man"),
    "EARL": (68, "Black American man"),
    "GARRETT": (50, "white American woman"),
    "SAWYER": (55, "white American man"),
    "GORDON": (40, "American man"),
    "KID": (11, "American child"),
    "INSPECTOR": (35, "American man"),
    "REYNOLDS": (50, "American state investigator"),
    "BIKER": (45, "American man"),
    "NEIGHBOR 1": (45, "American adult"),
    "NEIGHBOR 2": (50, "American adult"),
    "NEIGHBOR 3": (60, "American adult"),
    "CREDITOR": (48, "American man"),
}

BASE_REFS = {
    "EARL": "REF_EARL_ANCHOR_FULL",
    "GARRETT": "REF_GARRETT_ANCHOR_FULL",
    "SAWYER": "REF_SAWYER_ANCHOR_FULL",
    "GORDON": "REF_GORDON_ANCHOR_FULL",
    "KID": "REF_KID_ANCHOR_FULL",
    "INSPECTOR": "REF_INSPECTOR_ANCHOR_FULL",
    "REYNOLDS": "REF_REYNOLDS_ANCHOR_FULL",
    "BIKER": "REF_BIKER_ANCHOR_FULL",
    "NEIGHBOR 1": "REF_NEIGHBOR1_ANCHOR_FULL",
    "NEIGHBOR 2": "REF_NEIGHBOR2_ANCHOR_FULL",
    "NEIGHBOR 3": "REF_NEIGHBOR3_ANCHOR_FULL",
    "CREDITOR": "REF_CREDITOR_ANCHOR_FULL",
}

PORTRAITS = {
    "WILLA": "REF_WILLA_PORTRAIT",
    "ODESSA": "REF_ODESSA_PORTRAIT",
    "NOLAN": "REF_NOLAN_PORTRAIT",
    "CROSS": "REF_CROSS_PORTRAIT",
}

WARDROBE = {
    "WILLA": {
        (1, 6, 7, 8, 9, 10): "REF_WILLA_NIGHT_OLIVE_FULL",
        (2, 3): "REF_WILLA_WORK_TEAL_FULL",
        (4,): "REF_WILLA_CITYHALL_FULL",
        (5,): "REF_WILLA_WORK_RUST_FULL",
        (11, 12, 13): "REF_WILLA_WORK_DENIM_FULL",
        (15, 16, 17): "REF_WILLA_WORK_PLUM_FULL",
        (18, 19, 20): "REF_WILLA_WORK_GRAY_FULL",
        (22,): "REF_WILLA_NIGHT_CARDIGAN_FULL",
        (23, 24, 25, 26, 27): "REF_WILLA_WORK_MUSTARD_FULL",
        (30, 31, 32, 33, 34, 35, 36, 37): "REF_WILLA_NIGHT_TEALKNIT_FULL",
        (38,): "REF_WILLA_FINAL_CREAM_FULL",
    },
    "ODESSA": {
        (2, 3): "REF_ODESSA_WORK_LILAC_FULL",
        (5,): "REF_ODESSA_WORK_BLUE_FULL",
        (6, 10): "REF_ODESSA_ROBE_FULL",
        (11, 12, 13): "REF_ODESSA_WORK_MINT_FULL",
        (15,): "REF_ODESSA_WORK_BROWN_FULL",
        (17,): "REF_ODESSA_WORK_OCHRE_FULL",
        (18, 19, 20, 21): "REF_ODESSA_WORK_CORAL_FULL",
        (23, 25, 26): "REF_ODESSA_WORK_OLIVE_FULL",
        (31, 34, 35, 36): "REF_ODESSA_NIGHT_SHAWL_FULL",
        (38,): "REF_ODESSA_FINAL_YELLOW_FULL",
    },
    "NOLAN": {
        (1, 6, 7, 9): "REF_NOLAN_BIKER_BEATEN_FULL",
        (16, 21, 22): "REF_NOLAN_TSHIRT_REST_FULL",
        (23, 24): "REF_NOLAN_WORK_GRAY_FULL",
        (26, 27): "REF_NOLAN_HIDE_FULL",
        (31, 34): "REF_NOLAN_JACKET_ON_FULL",
        (35, 36): "REF_NOLAN_DAWN_FULL",
    },
    "CROSS": {
        (5,): "REF_CROSS_UNIFORM_DAY_FULL",
        (8,): "REF_CROSS_UNIFORM_NIGHT_FULL",
        (14, 15): "REF_CROSS_UNIFORM_JACKET_FULL",
        (17,): "REF_CROSS_CIVIL_FULL",
        (28,): "REF_CROSS_CRUISER_FULL",
        (32, 33, 37): "REF_CROSS_FINAL_FULL",
    },
    "EARL": {
        (2, 5): "REF_EARL_ANCHOR_FULL",
        (12, 13, 14): "REF_EARL_GRAY_FULL",
        (29,): "REF_EARL_MEETING_FULL",
        (31, 37, 38): "REF_EARL_NIGHT_FULL",
    },
    "GARRETT": {
        (4,): "REF_GARRETT_ANCHOR_FULL",
        (29, 30, 36): "REF_GARRETT_NIGHT_FULL",
    },
}

BG = {
    1: "REF_BG_DINER_NIGHT", 2: "REF_BG_DINER_DAY", 3: "REF_BG_KITCHEN_DAY",
    4: "REF_BG_CITYHALL_OFFICE", 5: "REF_BG_DINER_DAY", 6: "REF_BG_DINER_NIGHT",
    7: "REF_BG_DINER_NIGHT", 8: "REF_BG_DINER_NIGHT", 9: "REF_BG_STORAGE",
    10: "REF_BG_DINER_NIGHT", 11: "REF_BG_DINER_DAY", 12: "REF_BG_DINER_DAY",
    13: "REF_BG_DINER_DAY", 14: "REF_BG_DINER_DAY", 15: "REF_BG_DINER_DAY",
    16: "REF_BG_STORAGE", 17: "REF_BG_DINER_DAY", 18: "REF_BG_DINER_DAY",
    19: "REF_BG_DINER_DAY", 20: "REF_BG_KITCHEN_DAY", 21: "REF_BG_STORAGE",
    22: "REF_BG_BACKDOOR", 23: "REF_BG_KITCHEN_DAY", 24: "REF_BG_DINER_DAY",
    25: "REF_BG_KITCHEN_DAY", 26: "REF_BG_KITCHEN_DAY", 27: "REF_BG_BASEMENT",
    28: "REF_BG_CRUISER_NIGHT", 29: "REF_BG_COMMUNITY_HALL", 30: "REF_BG_DINER_NIGHT",
    31: "REF_BG_DINER_NIGHT", 32: "REF_BG_DINER_NIGHT", 33: "REF_BG_DINER_NIGHT",
    34: "REF_BG_DINER_NIGHT", 35: "REF_BG_DINER_DAWN", 36: "REF_BG_DINER_DAWN",
    37: "REF_BG_DINER_DAWN", 38: "REF_BG_DINER_DAY",
}

ZONES = {
    1: "booth nearest the storage-room passage", 2: "main counter and three occupied booths",
    3: "kitchen worktable beside the fryer", 4: "Garrett's desk inside City Hall",
    5: "main counter facing the entrance", 6: "front booth and counter after closing",
    7: "front windows facing the street", 8: "locked front doorway and counter",
    9: "storage room behind the flour bags", 10: "counter at two in the morning",
    11: "counter and locked storage-room passage", 12: "Earl's usual counter stool",
    13: "counter beside the kitchen pass-through", 14: "Earl's counter stool",
    15: "front door and near end of the counter", 16: "storage room beside the flour bags",
    17: "near end of the counter; Odessa remains at the far end", 18: "empty lunch counter",
    19: "bright afternoon counter with the front door open", 20: "kitchen aisle and worktable",
    21: "storage-room doorway beside Nolan's cot", 22: "open back doorway and service alley",
    23: "kitchen fryer and breakfast pass-through", 24: "quiet afternoon counter",
    25: "kitchen worktable", 26: "kitchen freezer, storage door, and basement hatch",
    27: "basement landing below the floor hatch", 28: "driver's seat of Cross's parked cruiser",
    29: "community-hall chair circle and rear wall", 30: "locked late-night counter",
    31: "counter used as a planning table", 32: "locked front door at night",
    33: "same doorway immediately after the ultimatum", 34: "counter and front window at four a.m.",
    35: "front window, doorway, and dawn street", 36: "counter, front sidewalk, and repair activity",
    37: "counter with the cruiser visible through the window", 38: "repaired morning counter",
}

BROLL_SCENES = {
    2, 3, 4, 5, 6, 9, 10, 11, 13, 14, 16, 17, 18, 20, 21, 22, 23,
    24, 25, 26, 27, 28, 29, 30, 32, 34, 35, 36, 38,
}

PUBLIC_BG = {
    2: "Three quiet morning customers remain naturally seated; nobody looks at camera.",
    4: "Two municipal staff silhouettes work beyond the glass partition.",
    5: "Two local patrons remain soft and unobtrusive in distant booths.",
    11: "A small morning flow of regulars stays outside the narrow focus cone.",
    12: "Two regulars sit quietly in distant booths, maintaining the same seated posture.",
    13: "The diner is closing; one last blurred customer exits naturally.",
    14: "A few morning patrons remain seated and do not watch the camera.",
    15: "Two patrons pause their meals and glance toward the tense doorway.",
    18: "The room is genuinely empty because every regular has stopped coming.",
    19: "The room remains empty except for Willa, Odessa, and the child; daylight and the open door keep it safe.",
    23: "No customers have arrived yet; the family breakfast happens before opening.",
    24: "The afternoon diner is quiet and nearly empty.",
    29: "Neighbors fill the hall in stable seated rows; reactions stay restrained and nobody looks at camera.",
    35: "Hundreds of riders and parked motorcycles fill the dawn street in ordered rows; headlights stay on.",
    36: "Riders work in small practical teams outside while others queue calmly for coffee.",
    37: "Riders and parked motorcycles remain visible outside, small through the window.",
    38: "Only Earl occupies his usual stool; the quiet street beyond has normal light traffic.",
}

SHIRT_COLORS = {
    "WILLA": {1: "muted olive", 2: "teal", 3: "teal", 4: "navy", 5: "rust",
              6: "muted olive", 7: "muted olive", 8: "muted olive", 9: "muted olive", 10: "muted olive",
              11: "denim blue", 12: "denim blue", 13: "denim blue", 15: "deep plum", 16: "deep plum",
              17: "deep plum", 18: "soft gray", 19: "soft gray", 20: "soft gray", 22: "brown cardigan",
              23: "mustard", 24: "mustard", 25: "mustard", 26: "mustard", 27: "mustard",
              30: "dark teal", 31: "dark teal", 32: "dark teal", 33: "dark teal", 34: "dark teal",
              35: "dark teal", 36: "dark teal", 37: "dark teal", 38: "warm cream"},
    "ODESSA": {2: "lilac", 3: "lilac", 5: "soft blue", 6: "burgundy", 10: "burgundy",
               11: "mint", 12: "mint", 13: "mint", 15: "warm brown", 17: "ochre",
               18: "coral", 19: "coral", 20: "coral", 21: "coral", 23: "olive",
               25: "olive", 26: "olive", 31: "charcoal shawl", 34: "charcoal shawl",
               35: "charcoal shawl", 36: "charcoal shawl", 38: "sunny yellow"},
    "NOLAN": {1: "black", 6: "black", 7: "black", 9: "black", 16: "faded gray", 21: "faded gray",
              22: "faded gray", 23: "work gray", 24: "work gray", 26: "dark gray", 27: "dark gray",
              31: "black", 34: "black", 35: "black", 36: "black"},
    "CROSS": {5: "sheriff tan", 8: "sheriff tan", 14: "sheriff tan", 15: "sheriff tan",
              17: "plain charcoal", 28: "sheriff tan", 32: "sheriff tan", 33: "sheriff tan", 37: "sheriff tan"},
    "EARL": {2: "brown", 5: "brown", 12: "heather gray", 13: "heather gray", 14: "heather gray",
             29: "deep blue", 31: "dark brown", 37: "dark brown", 38: "dark brown"},
    "GARRETT": {4: "forest green", 29: "burgundy", 30: "burgundy", 36: "burgundy"},
    "SAWYER": {35: "black", 36: "black"}, "GORDON": {18: "navy"}, "KID": {19: "sky blue"},
    "INSPECTOR": {26: "white"}, "REYNOLDS": {36: "slate blue"}, "BIKER": {36: "black"},
    "NEIGHBOR 1": {29: "brick red"}, "NEIGHBOR 2": {29: "sage green"},
    "NEIGHBOR 3": {29: "golden brown"}, "CREDITOR": {28: "dark maroon"},
}

PROPS = {
    "letter": "REF_PROP_LETTER_OPEN", "violations": "REF_PROP_LETTER_OPEN",
    "phone": "REF_PROP_PHONE", "video": "REF_PROP_PHONE", "wristband": "REF_PROP_WRISTBAND",
    "badge": "REF_PROP_BADGE", "fryer": "REF_PROP_FRYER", "envelope": "REF_PROP_ENVELOPE_CASH",
}

MASTER_PROPS = {
    (3, 1): ["REF_PROP_LETTER_OPEN"],
    (23, 1): ["REF_PROP_FRYER"],
    (36, 1): ["REF_PROP_PHONE"],
    (36, 2): ["REF_PROP_FRYER"],
    (37, 2): ["REF_PROP_BADGE"],
    (38, 1): ["REF_PROP_WRISTBAND"],
}


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:['’][A-Za-z0-9]+)?", text))


def parse_script() -> list[dict]:
    raw = SCRIPT_PATH.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^## SCENE (\d+):\s*(.+)$", raw, flags=re.M))
    scenes = []
    for idx, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[idx + 1].start() if idx + 1 < len(matches) else raw.find("\n## HỒ SƠ", match.end())
        body = raw[match.end():end].strip()
        purpose_match = re.search(r"\[SCENE PURPOSE\]\s*(.+?)(?=\n[A-Z][A-Z0-9 ]*:)", body, flags=re.S)
        purpose = re.sub(r"\s+", " ", purpose_match.group(1)).strip() if purpose_match else "Advance the dramatic beat faithfully."
        entries, pending = [], []
        dialogue_line_id = 0
        for line in body.splitlines():
            line = line.strip()
            if not line:
                continue
            dm = re.match(r"^([A-Z][A-Z0-9 ]*):\s*(.+)$", line)
            if dm:
                speaker, dialogue = dm.group(1), dm.group(2)
                dialogue_line_id += 1
                parts = dialogue.split()
                for part_index, part in enumerate(parts):
                    entries.append({
                        "speaker": speaker,
                        "text": part,
                        "context": " ".join(pending) if part_index == 0 else "",
                        "line_id": dialogue_line_id,
                        "word_pos": part_index,
                        "word_end": part_index,
                        "word_total": len(parts),
                    })
                pending = []
            elif line.startswith("[") and not line.startswith("[SCENE CONTEXT]") and not line.startswith("[END STATE]"):
                pending.append(line)
        scenes.append({"number": number, "title": match.group(2).strip(), "body": body, "purpose": purpose, "entries": entries})
    return scenes


def partition(entries: list[dict]) -> list[list[dict]]:
    """Chia tại biên câu thoại, ưu tiên 34–42 từ và không quá 4 người/clip."""
    total_all = sum(word_count(x["text"]) for x in entries)
    speakers_all = {x["speaker"] for x in entries if x["speaker"] != "VOICE"}
    if total_all <= 42 and len(speakers_all) <= 4:
        return [entries]
    n = len(entries)
    best: list[tuple[int, int, float, list[list[dict]]] | None] = [None] * (n + 1)
    best[n] = (0, 0, 0.0, [])
    for i in range(n - 1, -1, -1):
        total = 0
        speakers: set[str] = set()
        for j in range(i, n):
            total += word_count(entries[j]["text"])
            if entries[j]["speaker"] != "VOICE":
                speakers.add(entries[j]["speaker"])
            if total > 42 or len(speakers) > 4:
                break
            if j + 1 < n and entries[j].get("line_id") == entries[j + 1].get("line_id"):
                used = entries[j].get("word_pos", 0) + 1
                remain = entries[j].get("word_total", used) - used
                # Nếu buộc phải cắt giữa một câu dài, không để lại mảnh vụn
                # dưới bốn từ ở đầu clip kế.
                if used < 4 or remain < 4:
                    continue
            if total >= 24 and best[j + 1] is not None:
                penalty = (38 - total) ** 2 + (0 if total >= 34 else 30)
                tail = best[j + 1]
                cand = (1 + tail[0], tail[1] - int(total >= 39), penalty + tail[2], [entries[i:j + 1]] + tail[3])
                if best[i] is None or cand[:3] < best[i][:3]:
                    best[i] = cand
    if best[0] is None:
        raise ValueError("Không thể chia thoại thành clip hợp lệ")
    return best[0][3]


def partition_scene(scene: dict) -> list[list[dict]]:
    """Giữ hard boundary ở các blocking shift không được phép nằm chung một SF."""
    entries = scene["entries"]
    breaks: set[int] = set()
    number = scene["number"]
    for i, entry in enumerate(entries):
        context = entry.get("context", "")
        if number == 6 and "Nolan crashes through the front door" in context:
            breaks.add(i)
        if number == 37 and "Cross gets out of the cruiser" in context:
            breaks.add(i)
        if number == 36 and entry["speaker"] == "WILLA" and not any(x < i for x in breaks):
            breaks.add(i)
        if number == 26 and "moves Nolan to the basement hatch" in context:
            breaks.add(i)
            for k in range(i, len(entries)):
                if entries[k]["speaker"] == "NOLAN":
                    breaks.add(k + 1)
                    break
        if number == 26 and "danger is over" in context:
            breaks.add(i + 1)
    points = [0] + sorted(x for x in breaks if 0 < x < len(entries)) + [len(entries)]
    chunks = []
    for a, b in zip(points, points[1:]):
        chunks.extend(partition(entries[a:b]))
    merged_chunks = []
    for chunk in chunks:
        merged = []
        for entry in chunk:
            if (merged and merged[-1]["speaker"] == entry["speaker"]
                    and merged[-1].get("line_id") == entry.get("line_id")
                    and not entry.get("context")):
                merged[-1]["text"] += " " + entry["text"]
                merged[-1]["word_end"] = entry.get("word_end", entry.get("word_pos", 0))
            else:
                merged.append(dict(entry))
        merged_chunks.append(merged)
    return merged_chunks


def split_three(entries: list[dict]) -> list[list[dict]]:
    if len(entries) == 1:
        return [entries, [], []]
    if len(entries) == 2:
        return [[entries[0]], [entries[1]], []]
    weights = [word_count(x["text"]) for x in entries]
    total = sum(weights)
    target = total / 3
    a, b = min(
        ((a, b) for a in range(1, len(entries) - 1) for b in range(a + 1, len(entries))),
        key=lambda ab: (
            (sum(weights[:ab[0]]) - target) ** 2
            + (sum(weights[ab[0]:ab[1]]) - target) ** 2
            + (sum(weights[ab[1]:]) - target) ** 2
        ),
    )
    return [entries[:a], entries[a:b], entries[b:]]


def split_two(entries: list[dict]) -> list[list[dict]]:
    if len(entries) == 1:
        return [entries, []]
    weights = [word_count(x["text"]) for x in entries]
    cut = min(
        range(1, len(entries)),
        key=lambda i: abs(sum(weights[:i]) - sum(weights[i:])),
    )
    return [entries[:cut], entries[cut:]]


def wardrobe_ref(name: str, scene: int) -> str:
    for scene_set, ref in WARDROBE.get(name, {}).items():
        if scene in scene_set:
            return ref
    return BASE_REFS[name]


def refs_for(name: str, scene: int) -> list[str]:
    if name == "VOICE":
        name = "CREDITOR"
    refs = []
    if name in PORTRAITS:
        refs.append(PORTRAITS[name])
    refs.append(wardrobe_ref(name, scene))
    return refs


def scene_speakers(scene: dict) -> list[str]:
    result = []
    for entry in scene["entries"]:
        speaker = "CREDITOR" if entry["speaker"] == "VOICE" else entry["speaker"]
        if speaker not in result:
            result.append(speaker)
    return result


def cluster_numbers(scene: dict, chunks: list[list[dict]]) -> list[int]:
    number = scene["number"]
    if number == 6:
        return [1] + [2] * (len(chunks) - 1)
    if number == 35:
        return [1] + [2] * (len(chunks) - 1)
    if number == 36:
        return [1 if i == 0 else 2 if i < 5 else 3 for i in range(len(chunks))]
    if number == 37:
        return [1] + [2] * (len(chunks) - 1)
    if number == 26:
        result, aftermath = [], False
        for chunk in chunks:
            context = " ".join(x.get("context", "") for x in chunk)
            if aftermath:
                result.append(3)
            elif "moves Nolan to the basement hatch" in context:
                result.append(2)
            else:
                result.append(1)
            if "danger is over" in context:
                aftermath = True
        return result
    return [1] * len(chunks)


def cluster_cast(scene: dict, cluster: int) -> list[str]:
    plans = {
        6: {1: ["ODESSA", "WILLA"], 2: ["WILLA", "NOLAN"]},
        26: {1: ["INSPECTOR", "WILLA", "ODESSA"], 2: ["WILLA", "NOLAN"], 3: ["WILLA", "ODESSA"]},
        35: {1: ["WILLA", "NOLAN", "ODESSA"], 2: ["WILLA", "SAWYER", "ODESSA", "NOLAN"]},
        36: {1: ["SAWYER", "NOLAN", "REYNOLDS", "GARRETT"], 2: ["WILLA", "SAWYER", "ODESSA", "BIKER"], 3: ["WILLA", "NOLAN"]},
        37: {1: ["EARL", "WILLA"], 2: ["WILLA", "CROSS", "EARL"]},
    }
    if scene["number"] in plans:
        return plans[scene["number"]][cluster]
    return [x for x in scene_speakers(scene) if x != "CREDITOR"][:4]


def visible_cast(scene: dict, chunk: list[dict], focus: str | None = None) -> list[str]:
    number = scene["number"]
    speakers = []
    for entry in chunk:
        if entry["speaker"] == "VOICE":
            continue
        if entry["speaker"] not in speakers:
            speakers.append(entry["speaker"])
    if focus and focus not in speakers and focus != "VOICE":
        speakers.insert(0, focus)
    for name in scene_speakers(scene):
        if name != "CREDITOR" and name not in speakers:
            speakers.append(name)
        if len(speakers) == 4:
            break
    # Các scene đông người được chẻ nón quan sát theo nhóm thật sự đang thoại.
    if number in {29, 36}:
        actual = []
        for entry in chunk:
            if entry["speaker"] != "VOICE" and entry["speaker"] not in actual:
                actual.append(entry["speaker"])
        if focus and focus not in actual and focus != "VOICE":
            actual.insert(0, focus)
        speakers = actual[:4]
    return speakers[:4]


def refs_for_cast(cast: list[str], scene: int) -> list[str]:
    refs = []
    for name in cast:
        for ref in refs_for(name, scene):
            if ref not in refs:
                refs.append(ref)
    return refs[:8]


def props_for(scene_no: int, chunk: list[dict]) -> list[str]:
    text = " ".join(x["text"] + " " + x.get("context", "") for x in chunk).lower()
    allowed = {
        3: {"letter": "REF_PROP_LETTER_OPEN"},
        4: {"letter": "REF_PROP_LETTER_OPEN"},
        16: {"phone": "REF_PROP_PHONE"},
        23: {"fryer": "REF_PROP_FRYER"},
        31: {"phone": "REF_PROP_PHONE"},
        36: {"phone": "REF_PROP_PHONE", "fryer": "REF_PROP_FRYER", "envelope": "REF_PROP_ENVELOPE_CASH", "wristband": "REF_PROP_WRISTBAND"},
        37: {"badge": "REF_PROP_BADGE"},
        38: {"wristband": "REF_PROP_WRISTBAND", "fryer": "REF_PROP_FRYER"},
    }.get(scene_no, {})
    found = []
    for needle, ref in allowed.items():
        if re.search(rf"\b{re.escape(needle)}\b", text) and ref not in found:
            found.append(ref)
    return found[:2]


def pose_for(cast: list[str], scene: int, focus: str | None = None) -> dict:
    who = {}
    for idx, name in enumerate(cast):
        if name == focus:
            who[name] = "chủ thể nét chính, giữ đúng vị trí đã thiết lập trong Master"
        elif idx == 0:
            who[name] = "ở lớp tiền-trung cảnh, rõ mặt"
        else:
            who[name] = "đối diện hoặc kề chủ thể theo đúng trục hội thoại, miệng khép khi lắng nghe"
    return {
        "zone": ZONES[scene],
        "who": who,
        "dist": "camera giữ trong không gian đã khóa, không khám phá vùng ngoài ảnh neo",
        "hands": {name: "hai tay tự nhiên, trạng thái trước hành động của clip" for name in cast},
    }


def sf_object(sf_id: str, label: str, desc: str, prompt: str, refs_chars: list[str], refs_bg: str,
              goc: str, pose: dict) -> dict:
    return {
        "id": sf_id, "label": label, "desc": desc, "goc": goc, "pose": pose,
        "prompt": prompt, "status": "proposed", "notes": "", "usedBy": [],
        "refs": {"chars": refs_chars, "bg": refs_bg}, "picked": "",
    }


def master_prompt(scene: dict, cast: list[str]) -> str:
    number = scene["number"]
    names = ", ".join(cast)
    bg_note = PUBLIC_BG.get(number, "Không thêm người lạ vào nón quan sát nếu kịch bản không yêu cầu.")
    prompt = (
        f"ẢNH THAM CHIẾU: lấy đúng nhân dạng, trang phục và bối cảnh từ toàn bộ ảnh đã đính.\n\n"
        f"Tạo MỘT ẢNH TĨNH photorealistic 16:9, cinematic wide shot ngang tầm mắt, bao quát 70–100% "
        f"không gian tại {ZONES[number]}. Đây là Master SF khóa trục cho Scene {number}.\n\n"
        f"CHỦ THỂ: {names}. Giữ từng người ở một vị trí đọc được, đúng quan hệ khoảng cách; mọi gương mặt chính "
        f"đều nhận diện được nhưng không nhồi cùng cỡ mặt. Tư thế đang chờ trước hành động và câu thoại đầu.\n\n"
        f"HẬU CẢNH: giữ nguyên 100% kiến trúc, đồ đạc và ánh sáng của thẻ địa điểm. {bg_note} "
        f"Không tự dựng lại layout, không nhân bản nhân vật.\n\nKHUNG NGANG 16:9"
    )
    if len(prompt) > 1400:
        raise ValueError(f"Master prompt quá dài S{number}: {len(prompt)}")
    return prompt


def normal_sf_prompt(scene: dict, cast: list[str], focus: str, angle: str, chunk: list[dict], master_id: str) -> str:
    number = scene["number"]
    bg_note = PUBLIC_BG.get(number, "Hậu cảnh chỉ giữ các dáng người thật sự nằm trong nón quan sát.")
    if "Close-Up" in angle or "ECU" in angle:
        bg_note = "Hậu cảnh xóa mờ mạnh, tối đa một dáng người mờ sát sau lưng; không nhồi đám đông."
    prop_refs = props_for(number, chunk)
    prop_note = ""
    if prop_refs:
        prop_note = " Đạo cụ tham chiếu phải lộ đúng mặt thông tin, không bị che hoặc lật úp trong Start Frame."
    safety = ""
    if number == 19:
        safety = " Khung đủ sáng, cửa trước mở, tương tác dịu và an toàn; đứa trẻ lễ phép, không sợ hãi."
    context = " ".join(x.get("context", "") for x in chunk if x.get("context"))
    prompt = (
        f"ẢNH THAM CHIẾU: dùng đúng Master {master_id} và các thẻ nhân vật/đạo cụ đã đính.\n\n"
        f"Tạo MỘT ẢNH TĨNH photorealistic 16:9, {angle}, camera ở {ZONES[number]}. "
        f"{focus} là chủ thể nét chính; {', '.join(cast)} giữ nguyên vị trí tương đối và hướng nhìn theo Master. "
        f"Miệng khép tự nhiên, tay ở trạng thái chờ trước hành động của clip.{safety}\n\n"
        f"HẬU CẢNH: {bg_note} Kế thừa nguyên layout và ánh sáng từ Master, không thiết lập lại bàn hay quầy.{prop_note}"
    )
    if context:
        clean = re.sub(r"\[[^\]]+\]", "", context).strip()
        prompt += f" Khoảnh khắc tâm lý: {clean[:180]}."
    prompt += "\n\nKHUNG NGANG 16:9"
    if len(prompt) >= 1000:
        raise ValueError(f"SF prompt quá dài {number}/{focus}: {len(prompt)}")
    return prompt


def broll_sf_prompt(scene: dict, subject: str, master_id: str, angle: str) -> str:
    number = scene["number"]
    safety = " Khung đủ sáng, cửa mở và mọi tư thế đều an toàn cho trẻ nhỏ." if number == 19 else ""
    return (
        f"ẢNH THAM CHIẾU: dùng đúng Master {master_id} và thẻ của {subject}.\n\n"
        f"Tạo MỘT ẢNH TĨNH photorealistic 16:9, {angle}, tại {ZONES[number]}. "
        f"{subject} hiện diện rõ trong một khoảnh khắc chuyển cảnh tĩnh, miệng khép, tay ở trạng thái chờ; "
        f"không dựng hành động đã hoàn tất.{safety}\n\n"
        f"HẬU CẢNH: kế thừa nguyên layout từ Master. {PUBLIC_BG.get(number, 'Chỉ giữ hoạt động nền tự nhiên đúng thời điểm.')}\n\n"
        f"KHUNG NGANG 16:9"
    )


def angle_for(index: int, scene_no: int, focus: str, cast: list[str], prop_refs: list[str]) -> str:
    slot = index % 25
    insert_ref = {
        3: "REF_PROP_LETTER_OPEN",
        36: "REF_PROP_ENVELOPE_CASH",
        37: "REF_PROP_BADGE",
        38: "REF_PROP_WRISTBAND",
    }.get(scene_no)
    if insert_ref and insert_ref in prop_refs:
        return f"Extreme Close-Up (ECU) on a story prop with {focus}'s face or hand still visible"
    if slot < 14:
        return f"Medium Close-Up (MCU) on {focus}"
    if slot < 23 and len(cast) >= 2:
        return f"3/4 Two-Shot on {cast[0]} and {cast[1]}"
    if slot == 23 and len(cast) >= 2:
        return f"Clean Two-Shot on {cast[0]} and {cast[1]}"
    return f"Close-Up on {focus}"


def character_line(name: str, scene: int, position: str) -> str:
    age, identity = AGES[name]
    color = SHIRT_COLORS.get(name, {}).get(scene, "distinct neutral")
    return f"{name} — {age}-year-old {identity}, wearing {color}, anchored in place."


def clip_prompt(scene: dict, chunk: list[dict], cast: list[str], angle: str, dur: int) -> str:
    number = scene["number"]
    groups = split_two(chunk) if dur == 10 else split_three(chunk)
    focus_order = []
    for group in groups:
        candidate = next((x["speaker"] for x in group if x["speaker"] != "VOICE"), None)
        focus_order.append(candidate or (cast[0] if cast else "CROSS"))
    dialogue_order = " → ".join(x["speaker"] for x in chunk)
    char_block = "\n".join(character_line(name, number, "in the exact anchored position") for name in cast)
    safety = " Child-safe, bright, calm, and gentle." if number == 19 else ""
    continuity = []
    if chunk[0].get("word_pos", 0) > 0:
        continuity.append("Continue the previous sentence seamlessly; do not restart it.")
    if chunk[-1].get("word_end", chunk[-1].get("word_pos", 0)) < chunk[-1].get("word_total", 1) - 1:
        continuity.append("Leave the sentence unfinished for the next clip; no closing cadence.")
    continuity_note = " ".join(continuity)
    shot_sections = []
    camera_summaries = []
    camera_types = [
        ("MEDIUM WIDE / TWO-SHOT", "VERY SLOW PUSH-IN", "Slow smooth push-in only within the anchored space."),
        ("MEDIUM CLOSE-UP", "SUBTLE LATERAL DOLLY", "Tiny lateral drift; keep the face primary."),
        ("CLOSE-UP / SHARED REACTION", "STATIC OR VERY SLOW PUSH-IN", "Fixed framing or a minimal push-in."),
    ]
    last_lines = []
    for idx, group in enumerate(groups, 1):
        shot_name, move, camera = camera_types[idx - 1]
        focus = focus_order[idx - 1]
        lines = []
        if group:
            for entry in group:
                emotion = "controlled and truthful"
                if number == 19:
                    emotion = "gentle, calm, and non-threatening"
                lines.append(f'{entry["speaker"]} — {emotion}: "{entry["text"]}"')
            last_lines.append(group[-1]["text"])
        else:
            lines.append("No dialogue in this brief reaction beat; every mouth remains closed.")
            last_lines.append("")
        action = "Use small listening reactions; preserve hand and body continuity."
        group_context = re.sub(r"\s+", " ", " ".join(x["context"] for x in group if x.get("context")))[:80]
        if group_context:
            action += f" Honor this direction without speaking or displaying it: {group_context}."
        shot_sections.append(
            f"SHOT {idx} — {shot_name} ON {focus} — {move}\n"
            f"Camera: {camera}\n{action}\n" + "\n".join(lines)
        )
        camera_summaries.append(f"SHOT {idx} = {shot_name.lower()} on {focus}, {move.lower()}.")
    listeners = []
    for speaker in sorted(set(x["speaker"] for x in chunk)):
        listeners.append(f"When {speaker} speaks, every other character stays silent with mouth closed.")
    cuts = []
    for idx in range(len(groups) - 1):
        anchor = last_lines[idx] or "the silent reaction beat ends"
        cuts.append(f'CUT {idx + 1}: Immediately after "{anchor}".')
    prompt = (
        "Use the uploaded image as the anchor for appearance, wardrobe, layout, lighting, props, and spatial relationships.\n\n"
        f"{dur}-SECOND VIDEO. EXACTLY {'TWO' if dur == 10 else 'THREE'} SHOTS. EXACTLY {'ONE' if dur == 10 else 'TWO'} HARD CUT{'S' if dur != 10 else ''}.\n\n"
        f"CHARACTERS:\n{char_block}\nKeep exactly this cast. VOICE is off-screen only when written. "
        "Never add, remove, duplicate, replace, or transform a character.\n\n"
        f"SCENE:\n{scene['purpose'][:620]} The action stays inside {ZONES[number]}. {safety} {continuity_note}\n\n"
        f"DIALOGUE ORDER:\n{dialogue_order}\n\n"
        + "\n\nHARD CUT.\n\n".join(shot_sections)
        + "\n\nPERFORMANCE:\nNaturalistic drama: subtle eyes and listening. "
          "No theatrical gestures. Preserve height, depth, props, and screen direction. Mouths close during pauses.\n\n"
        + "LIP SYNC:\nOnly the current speaker moves their lips. No overlap. "
          "Speak every quote once, verbatim, in order. During pauses, mouths remain closed and still.\n"
        + "\n".join(listeners)
        + "\n\nAUDIO:\nDialogue ONLY, in clear natural American English. No ambience, music, narrator, sound effects, subtitles, captions, or on-screen text.\n\n"
        + f"EDITING:\nExactly {'TWO' if dur == 10 else 'THREE'} shots and {'ONE' if dur == 10 else 'TWO'} hard cut{'s' if dur != 10 else ''}. No dissolve, morph, montage, extra insert, or hidden cut.\n"
        + "\n".join(cuts)
        + "\n\nCAMERA SUMMARY:\n" + "\n".join(camera_summaries)
        + "\nStay inside the anchor. Never pull back, orbit, crane, track beyond frame, or reveal new space."
    )
    if len(prompt) < 2600:
        prompt = prompt.replace(
            "PERFORMANCE:\n",
            "PERFORMANCE:\nMaintain exact facial identity, wardrobe color, body scale, and spatial continuity across both cuts. "
            "Keep background extras in the same zones and core standing/seated poses; only tiny natural movements are allowed. "
            "Treat every pause as active listening: eyes respond before the face, shoulders remain quiet, and hands never reset between angles. "
            "Preserve the same eyelines, distance to furniture, prop orientation, and left-right screen geography established by the uploaded image. "
        )
    if len(prompt) > 3400:
        prompt = prompt.replace(scene["purpose"][:620], scene["purpose"][:120])
    if len(prompt) > 3400:
        prompt = prompt.replace(scene["purpose"][:120], "Follow the scripted dramatic beat faithfully.")
    if not 2600 <= len(prompt) <= 3400:
        raise ValueError(f"Video prompt S{number} ngoài biên hợp lý: {len(prompt)}")
    return prompt


def broll_music(scene_no: int, ordinal: int) -> dict:
    if scene_no in {35, 38}:
        role, emo = "Đẩy", "cú trả cảm xúc lớn, lòng biết ơn lan thành cộng đồng"
        bpm, lead = 82, "restrained strings and low toms"
    else:
        cycle = [("Nâng", "chuyển chương có hy vọng", 84, "muted electric guitar"),
                 ("Kìm", "sợ hãi nhưng vẫn giữ phẩm giá", 66, "felt piano"),
                 ("Nghỉ", "khoảng thở đời thường", 54, "warm Rhodes")]
        role, emo, bpm, lead = cycle[ordinal % 3]
    a = (
        f"American soul-folk at {bpm} BPM, steady walking pulse; open with {lead}, pull almost completely back at the midpoint "
        f"to a close-mic warm alto vocal, then end on one unresolved human chord; lyrics in first person about leaving a light on "
        f"for a stranger and choosing decency without expecting repayment, never triumphant; dry intimate vocal, warm analog tape mix, "
        f"soul-folk, {lead}, restrained, humane"
    )
    b = (
        f"Instrumental cinematic Americana at {bpm} BPM; begin with {lead} and soft upright bass, remove the pulse at the midpoint "
        f"for two bars of near-silence, then return with a small open-ended harmony; no vocals, no choir, no bombast; warm analog mix, "
        f"instrumental, Americana, {lead}, intimate, restrained"
    )
    return {"role": role, "emo": emo, "a": a, "a_kind": "có lời", "b": b, "b_kind": "không lời"}


def broll_video_prompt(scene: dict, subject: str) -> str:
    number = scene["number"]
    safety = "The child is not present in this transition unless shown in the reference; all visible behavior is safe and calm. " if number == 19 else ""
    return (
        "Use the uploaded reference image as the visual anchor for character appearance, wardrobe, layout, lighting, props, and spatial relationships.\n\n"
        "15-SECOND VIDEO. EXACTLY THREE SHOTS. EXACTLY TWO HARD CUTS.\n\n"
        f"CHARACTERS:\n{character_line(subject, number, 'held in the exact anchored position')}\n"
        "Keep exactly this visible character. Do not add, remove, replace, duplicate, or transform anyone.\n\n"
        f"SCENE:\nA wordless transition at {ZONES[number]} that lets the previous dramatic beat settle and establishes the new time or place. "
        f"{safety}The emotion is internal and restrained; suggest the character processing what just happened without prescribing a theatrical gesture. "
        "KHÔNG CÓ LỜI THOẠI TRONG CLIP NÀY. Tuyệt đối không ai mở miệng như đang nói.\n\n"
        "SHOT 1 — MEDIUM WIDE — STATIC LOCKED-OFF CAMERA ON A FIXED TRIPOD\n"
        f"Hold {subject} inside the already visible environment. Small natural breathing only; the mouth remains closed.\n\n"
        "HARD CUT.\n\nSHOT 2 — MEDIUM SHOT — VERY SLOW PUSH-IN\n"
        "A slow, controlled push-in reads the emotional state. Hands and props remain continuous; no new area enters frame.\n\n"
        "HARD CUT.\n\nSHOT 3 — MEDIUM CLOSE-UP — RACK FOCUS THEN STATIC\n"
        f"Rack focus gently onto {subject}, then hold. End before the first spoken action of the next dramatic beat.\n\n"
        "PERFORMANCE:\nUse a quiet lived-in state rather than a list of gestures. The character has just crossed an emotional threshold and is gathering "
        "enough steadiness to continue. No default sigh, no symbolic pantomime, no random walking, and no completed state-change action. "
        "Background extras, if visible in the uploaded frame, make only tiny natural movements and never look at camera. "
        "Keep exact facial identity, wardrobe, body scale, hand state, prop orientation, eyeline, screen direction, and distance to furniture "
        "through both cuts. The final frame must remain a believable continuation of the uploaded Start Frame, ready for the next spoken beat.\n\n"
        "LIP SYNC:\nNo character speaks. No character moves their lips as if talking. During the entire clip every mouth remains closed with lips still.\n\n"
        "AUDIO:\nNO DIALOGUE. NO MUSIC IN THE GENERATED CLIP. Allow only very light location-appropriate ambient sound and one restrained practical SFX; "
        "no narrator, no subtitles, no captions, and no on-screen text.\n\n"
        "EDITING:\nExactly THREE shots total. Exactly TWO hard cuts. No extra cuts, montage, dissolve, morph, or time-lapse.\n"
        "CUT 1: At exactly five seconds, after the establishing hold.\nCUT 2: At exactly ten seconds, after the push-in settles.\n\n"
        "CAMERA SUMMARY:\nSHOT 1 = medium wide, static locked-off.\nSHOT 2 = medium shot, very slow push-in.\n"
        "SHOT 3 = medium close-up, one rack focus then static.\nNever pull back, orbit, crane, track outside the frame, or reveal space absent from the uploaded image."
    )


def creditor_master() -> dict:
    prompt = (
        "ẢNH THAM CHIẾU: dùng đúng nhân dạng CREDITOR và phòng người chủ nợ đã đính.\n\n"
        "Tạo MỘT ẢNH TĨNH photorealistic 16:9, cinematic wide shot ngang tầm mắt, bao quát phòng làm việc. "
        "CREDITOR ngồi một mình sau bàn, điện thoại áp tai, thân người ổn định, miệng khép ở trạng thái chờ trước câu nói. "
        "Điện thoại và tay cầm thấy rõ; giữ nguyên 100% kiến trúc, đồ đạc và ánh sáng của thẻ địa điểm. "
        "Không thêm người, không nhân bản bàn hoặc điện thoại.\n\nKHUNG NGANG 16:9"
    )
    return sf_object(
        "SF-S28-M2-MASTER", "S28-M2 · MASTER — NGUỒN GIỌNG CHỦ NỢ",
        "Bản sao có người thật nói để lấy chuẩn Voice cho các câu O.S. qua điện thoại.",
        prompt, ["REF_CREDITOR_ANCHOR_FULL"], "REF_BG_CREDITOR_ROOM_NIGHT",
        "Cinematic Wide Shot, CREDITOR RÕ MẶT, ngồi sau bàn với điện thoại",
        {"zone": "phòng làm việc của chủ nợ", "who": {"CREDITOR": "ngồi sau bàn, rõ mặt"},
         "dist": "camera trong phòng, không khám phá ngoài ảnh neo", "hands": {"CREDITOR": "một tay áp điện thoại, tay kia đặt trên bàn"}},
    )


def creditor_voice_prompt(lines: list[dict]) -> str:
    groups = split_two(lines)
    dialogue_1 = "\n".join(f'CREDITOR — controlled and cold: "{x["text"]}"' for x in groups[0])
    dialogue_2 = "\n".join(f'CREDITOR — controlled and cold: "{x["text"]}"' for x in groups[1]) or "No added dialogue; mouth closed."
    cut_anchor = groups[0][-1]["text"]
    prompt = (
        "Use the uploaded image as the anchor for the creditor's exact face, wardrobe, office layout, lighting, desk, telephone, and hand position.\n\n"
        "10-SECOND VIDEO. EXACTLY TWO SHOTS. EXACTLY ONE HARD CUT.\n\n"
        "CHARACTERS:\nCREDITOR — 48-year-old American man, wearing dark maroon, seated behind the desk with a telephone at his ear.\n"
        "Keep exactly this one visible character. Never add, remove, duplicate, replace, or transform anyone.\n\n"
        "SCENE:\nThis is the visible voice-source copy for the creditor heard off-screen in Cross's phone call. He is practical and controlled, "
        "not theatrical or menacing. The phone remains at his ear and the office stays exactly as anchored.\n\n"
        "DIALOGUE ORDER:\nCREDITOR\n\n"
        "SHOT 1 — MEDIUM SHOT — STATIC LOCKED-OFF CAMERA ON A FIXED TRIPOD\n"
        "Hold the seated posture. He speaks the first part with economical mouth movement and a steady eyeline toward the desk.\n"
        f"{dialogue_1}\n\nHARD CUT.\n\n"
        "SHOT 2 — MEDIUM CLOSE-UP ON CREDITOR — VERY SLOW PUSH-IN\n"
        "Very slow push-in toward his face, staying inside the room already visible. He finishes the assigned lines once, then closes his mouth. "
        f"Do not invent additional words, threats, gestures, or movement.\n{dialogue_2}\n\n"
        "PERFORMANCE:\nNaturalistic American drama. The pressure comes from quiet certainty, not volume. Preserve face, body scale, phone orientation, "
        "handedness, seated height, desk distance, and screen direction across the cut. Eyes react before the face; shoulders and free hand stay restrained. "
        "No pacing, standing, pointing, smiling, shouting, or touching any prop besides the telephone. The final frame remains stable and usable for editing.\n\n"
        "LIP SYNC:\nOnly CREDITOR moves his lips, and only while speaking the quoted words. Speak every quote once, verbatim, in its written order. "
        "No overlap, paraphrase, repetition, or improvised line. During pauses his mouth stays closed with lips completely still.\n\n"
        "AUDIO:\nCREDITOR dialogue ONLY, clear natural American English recorded close and dry. No audible Cross voice, ambience, music, narrator, "
        "sound effects, subtitles, captions, or on-screen text.\n\n"
        "EDITING:\nExactly TWO shots and ONE hard cut. No dissolve, morph, montage, insert, reaction cut, or hidden edit.\n"
        f"CUT 1: Immediately after \"{cut_anchor}\".\n\n"
        "CAMERA SUMMARY:\nSHOT 1 = medium shot, static locked-off.\nSHOT 2 = medium close-up, very slow push-in.\n"
        "Never pull back, orbit, crane, pan outside the office, reveal new space, or change the room layout."
    )
    if len(prompt) < 2600:
        prompt = prompt.replace(
            "PERFORMANCE:\n",
            "PERFORMANCE:\nMaintain exact continuity in the telephone cord, desk objects, chair, shirt color, facial identity, and background geometry. "
            "The hard cut changes framing only; it does not advance time or reset the actor. "
        )
    if not 2600 <= len(prompt) <= 3400:
        raise ValueError(f"Prompt nguồn giọng ngoài biên: {len(prompt)}")
    return prompt


def add_creditor_ref(ref_scene: dict) -> None:
    if not any(x["id"] == "REF_CREDITOR_ANCHOR_FULL" for x in ref_scene["sfs"]):
        prompt = (
            "Ảnh tham chiếu NHÂN VẬT PHỤ + TRANG PHỤC, photorealistic, KHUNG DỌC 9:16, toàn thân từ đầu đến chân. "
            "Một người đàn ông Mỹ 48 tuổi, khuôn mặt khỏe mạnh nhưng lạnh và thực dụng, tóc ngắn gọn, vóc dáng trung bình; "
            "áo màu đỏ mận đậm và quần tối màu phẳng phiu. Đứng thẳng chính diện trong studio nền trơn, ánh sáng dịu đều, "
            "miệng khép, hai tay thả tự nhiên, không cầm vật, không thêm sẹo, hình xăm hay phụ kiện."
        )
        ref_scene["sfs"].insert(-12, {
            "id": "REF_CREDITOR_ANCHOR_FULL", "label": "CREDITOR — NGƯỜI GỌI ĐIỆN",
            "desc": "Vai phụ · khoảng 48 tuổi · người đòi khoản nợ cờ bạc của Cross qua điện thoại. THẺ NEO NHÂN DẠNG.\nDùng: S28",
            "prompt": prompt, "status": "proposed", "notes": "", "usedBy": [],
            "refs": {"chars": [], "bg": None}, "picked": "",
        })
    if not any(x["id"] == "REF_BG_CREDITOR_ROOM_NIGHT" for x in ref_scene["sfs"]):
        location_prompt = (
            "Bối cảnh ở Mỹ: một phòng làm việc kín đang được dùng cho cuộc gọi đòi nợ ban đêm. Photorealistic, điện ảnh nhưng hiện thực, "
            "cinematic wide shot, ống kính 28mm, camera ngang tầm mắt. Phòng nhỏ, sáng sủa và đang hoạt động bình thường. Bên trái là tủ hồ sơ "
            "kim loại xám và một ghế gỗ; bên phải là cửa sổ có rèm mành khép, dưới cửa sổ đặt máy sưởi thấp. Đối diện camera là bàn gỗ tối màu "
            "với điện thoại bàn không nhãn, sổ ghi chép đóng và đèn bàn chụp kem. Sau lưng camera là cửa ra hành lang mở hé, để lộ một dải tường "
            "sơn trắng ngà. Mặt bàn gọn, vật dụng thực dụng, nhãn thiết bị là thương hiệu hư cấu. Không có người trong khung hình. Đèn LED trắng "
            "trung tính từ trần chiếu đều; đèn bàn chỉ tạo một lớp vàng nhạt trên mặt gỗ, bóng đổ mềm, độ tương phản trung bình. Tường xám nhạt, "
            "gỗ nâu sẫm và kim loại lạnh tạo vẻ kín đáo, khác hẳn ánh đèn đường xanh đỏ trong xe tuần tra. Tổng thể rõ nét, tỉnh táo, không u tối, "
            "không moody, không cháy trắng.\n\nKHUNG NGANG 16:9"
        )
        ref_scene["sfs"].append({
            "id": "REF_BG_CREDITOR_ROOM_NIGHT", "label": "PHÒNG NGƯỜI CHỦ NỢ — ĐÊM",
            "desc": "Phòng nguồn giọng O.S. để tạo bản sao có người thật nói qua điện thoại.\nDùng: S28",
            "prompt": location_prompt, "status": "proposed", "notes": "", "usedBy": [],
            "refs": {"chars": [], "bg": None}, "picked": "",
        })


def make_shot(shot_id: str, sf_id: str, text: str, prompt: str, dur: int = 15, music: dict | None = None,
              notes: str = "") -> dict:
    result = {
        "id": shot_id, "sf": sf_id, "dur": dur, "text": text, "prompt": prompt,
        "prompt_text": text, "status": "todo", "notes": notes,
    }
    if music is not None:
        result["music"] = music
    return result


def rebuild_used_by(board: dict) -> None:
    by_id = {}
    for scene in board["scenes"]:
        for sf in scene.get("sfs", []):
            sf["usedBy"] = []
            by_id[sf["id"]] = sf
    for scene in board["scenes"]:
        for sf in scene.get("sfs", []):
            refs = list(sf.get("refs", {}).get("chars", []))
            bg = sf.get("refs", {}).get("bg")
            if bg:
                refs.append(bg)
            for ref in refs:
                if ref in by_id and sf["id"] not in by_id[ref]["usedBy"]:
                    by_id[ref]["usedBy"].append(sf["id"])
        for shot in scene.get("shots", []):
            if shot["sf"] in by_id and shot["id"] not in by_id[shot["sf"]]["usedBy"]:
                by_id[shot["sf"]]["usedBy"].append(shot["id"])


def build() -> dict:
    board = json.loads(BOARD_PATH.read_text(encoding="utf-8"))
    ref_scene = board["scenes"][0]
    if ref_scene["id"] != "REF":
        raise ValueError("Scene đầu tiên không phải REF")
    add_creditor_ref(ref_scene)
    scenes = parse_script()
    if [x["number"] for x in scenes] != list(range(1, 39)):
        raise ValueError("Kịch bản không đủ S1–S38")
    output_scenes = [ref_scene]
    global_angle_index = 0
    music_ordinal = 0
    for scene in scenes:
        number = scene["number"]
        chunks = partition_scene(scene)
        chunk_clusters = cluster_numbers(scene, chunks)
        first_master_cast = cluster_cast(scene, 1)
        if not first_master_cast:
            raise ValueError(f"S{number} không có cast")
        def create_master(cluster: int) -> dict:
            cast = cluster_cast(scene, cluster)
            master_id = f"SF-S{number}-M{cluster}-MASTER"
            master_goc = f"Cinematic Wide Shot, {', '.join(cast)} RÕ MẶT, đúng trục không gian"
            master_refs = refs_for_cast(cast, number) + MASTER_PROPS.get((number, cluster), [])
            return sf_object(
                master_id, f"S{number}-M{cluster} · MASTER — {scene['title']}",
                f"Master khóa cụm {cluster} tại {ZONES[number]} và vị trí cast trước beat đầu.",
                master_prompt(scene, cast), master_refs, BG[number],
                master_goc, pose_for(cast, number),
            )
        master = create_master(1)
        master_id = master["id"]
        sfs, shots = [], []
        next_number = 1
        if number in BROLL_SCENES:
            subject = first_master_cast[0]
            b_angle = "Medium Wide Shot" if number in {4, 35} else f"Medium Close-Up (MCU) on {subject}"
            b_id = f"SF-S{number}-{next_number:02d}-B1"
            v_id = f"V-S{number}-{next_number:02d}-B1"
            b_sf = sf_object(
                b_id, f"[NHỊP] S{number}-{next_number:02d} · cầu nối vào {scene['title']}",
                "Nhịp không thoại bắt buộc/chuyển thời gian; dừng trước hành động thoại đầu.",
                broll_sf_prompt(scene, subject, master_id, b_angle), refs_for_cast([subject], number), master_id,
                f"{b_angle}, {subject} rõ mặt trong nhịp chuyển", pose_for([subject], number, subject),
            )
            sfs.append(b_sf)
            shots.append(make_shot(
                v_id, b_id, "[NHỊP KHÔNG THOẠI] Chuyển địa điểm/thời gian và giữ nhịp cảm xúc trước câu thoại đầu.",
                broll_video_prompt(scene, subject), 15, broll_music(number, music_ordinal),
            ))
            music_ordinal += 1
            next_number += 1
        sfs.append(master)
        seen_clusters: set[int] = set()
        prior_candidates: list[tuple[str, tuple[str, ...], str, int, str]] = []
        sf_use_count: dict[str, int] = {}
        shot_no = next_number
        creditor_master_added = False
        for chunk_idx, chunk in enumerate(chunks):
            cluster = chunk_clusters[chunk_idx]
            current_master_id = f"SF-S{number}-M{cluster}-MASTER"
            current_master_cast = cluster_cast(scene, cluster)
            current_master_goc = f"Cinematic Wide Shot, {', '.join(current_master_cast)} RÕ MẶT, đúng trục không gian"
            if cluster not in seen_clusters and cluster != 1:
                sfs.append(create_master(cluster))
            v_id = f"V-S{number}-{shot_no:02d}"
            text = "\n".join(f"{x['speaker']}: {x['text']}" for x in chunk)
            dur = 10 if sum(word_count(x["text"]) for x in chunk) < 24 else 15
            focus = next((x["speaker"] for x in chunk if x["speaker"] != "VOICE"), current_master_cast[0])
            cast = visible_cast(scene, chunk, focus)
            if number in {6, 26, 35, 36, 37}:
                actual = []
                for entry in chunk:
                    if entry["speaker"] != "VOICE" and entry["speaker"] not in actual:
                        actual.append(entry["speaker"])
                for name in current_master_cast:
                    if name not in actual:
                        actual.append(name)
                    if len(actual) == 4:
                        break
                cast = actual[:4]
            cast_sig = tuple(sorted(cast))
            prop_refs = props_for(number, chunk)
            if cluster not in seen_clusters:
                sf_id = current_master_id
                angle = current_master_goc
                seen_clusters.add(cluster)
            else:
                reuse = None
                if chunk_idx >= 2:
                    # Ưu tiên dùng lại góc chung, nhưng mỗi SF chỉ phục vụ tối đa hai clip.
                    reuse = next((x for x in reversed(prior_candidates)
                                  if x[3] == cluster and x[1] == cast_sig and "Two-Shot" in x[2]
                                  and sf_use_count.get(x[0], 0) < 2), None)
                    allow_single = ((chunk_idx == 2 and number % 4 == 0)
                                    or chunk_idx % 3 == 0 or chunk_idx % 4 == 0)
                    if reuse is None and allow_single:
                        reuse = next((x for x in reversed(prior_candidates)
                                      if x[3] == cluster and x[1] == cast_sig and x[4] == focus and "ECU" not in x[2]
                                      and sf_use_count.get(x[0], 0) < 2), None)
                if reuse:
                    sf_id, _, angle, _, _ = reuse
                else:
                    sf_id = f"SF-S{number}-{shot_no:02d}"
                    angle = angle_for(global_angle_index, number, focus, cast, prop_refs)
                    refs_chars = refs_for_cast(cast, number) + [x for x in prop_refs if x not in refs_for_cast(cast, number)]
                    sf = sf_object(
                        sf_id, f"S{number}-{shot_no:02d} · {focus} — beat thoại",
                        f"Start Frame trước beat: {chunk[0]['text'][:140]}",
                        normal_sf_prompt(scene, cast, focus, angle, chunk, current_master_id), refs_chars,
                        current_master_id, f"{angle}, {', '.join(cast)}", pose_for(cast, number, focus),
                    )
                    sfs.append(sf)
                    prior_candidates.append((sf_id, cast_sig, angle, cluster, focus))
                    global_angle_index += 1
            sf_use_count[sf_id] = sf_use_count.get(sf_id, 0) + 1
            continuation_notes = []
            if chunk[0].get("word_pos", 0) > 0:
                continuation_notes.append("Tiếp liền câu thoại từ clip trước; không lấy lại nhịp từ đầu.")
            if chunk[-1].get("word_end", chunk[-1].get("word_pos", 0)) < chunk[-1].get("word_total", 1) - 1:
                continuation_notes.append("Câu thoại còn tiếp ở clip sau; không hạ giọng kết câu.")
            shots.append(make_shot(
                v_id, sf_id, text, clip_prompt(scene, chunk, cast, angle, dur), dur=dur,
                notes=" ".join(continuation_notes),
            ))
            shot_no += 1
            if number == 28:
                voice_lines = [x for x in chunk if x["speaker"] == "VOICE"]
                if voice_lines:
                    if not creditor_master_added:
                        sfs.append(creditor_master())
                        creditor_master_added = True
                    copy_id = f"V-S28-{shot_no:02d}"
                    copy_text = "\n".join(f"CREDITOR: {x['text']}" for x in voice_lines)
                    shots.append(make_shot(
                        copy_id, "SF-S28-M2-MASTER", copy_text, creditor_voice_prompt(voice_lines), dur=10,
                        notes="Bản sao nguồn giọng cho các câu VOICE O.S.; giữ nguyên lời thoại theo luật điện thoại.",
                    ))
                    shot_no += 1
        output_scenes.append({
            "id": f"S{number}", "name": f"S{number} — {scene['title']}",
            "script": scene["body"], "sfs": sfs, "shots": shots,
        })
    board["scenes"] = output_scenes
    board["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rebuild_used_by(board)
    return board


if __name__ == "__main__":
    result = build()
    BOARD_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã ghi {BOARD_PATH}")
