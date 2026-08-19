#!/usr/bin/env python3
import json
import sys
import os

VALID_SF_KEYS = {
    'id', 'label', 'goc', 'pose', 'prompt', 'refs', 'status', 'notes',
    'desc', 'luatchung', 'ai_request', 'ai_done', 'picked', 'image', 'chat'
}

# Khoá định danh của shot trong sf-board.json là 'id', KHÔNG phải 'sh'. Bản cũ
# chỉ nhận 'sh' nên `if 'sh' not in p_sh: continue` bỏ qua SẠCH mọi shot rồi vẫn
# in "patch thành công" — hỏng hoàn toàn im lặng. 'sh' giữ lại làm bí danh.
VALID_SHOT_KEYS = {
    'id', 'sh', 'sf', 'dur', 'text', 'goc', 'prompt', 'notes', 'video',
    'vstatus', 'vpicked', 'vversions', 'ai_request', 'ai_done',
    'music'
}

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def cmd_xem(board_path, scene_id):
    data = load_json(board_path)
    for sc in data.get('scenes', []):
        if sc.get('id') == scene_id:
            print(json.dumps(sc, ensure_ascii=False, indent=2))
            return
    print(f"Không tìm thấy scene {scene_id}", file=sys.stderr)
    sys.exit(1)

def filter_keys(obj, valid_keys):
    return {k: v for k, v in obj.items() if k in valid_keys}

def cmd_patch(board_path, scene_id, patch_file):
    patch_data = load_json(patch_file)
    data = load_json(board_path)
    
    scene = None
    for sc in data.get('scenes', []):
        if sc.get('id') == scene_id:
            scene = sc
            break
            
    if not scene:
        print(f"Chưa có scene {scene_id}, tạo mới...")
        scene = {'id': scene_id, 'sfs': [], 'shots': []}
        if 'scenes' not in data:
            data['scenes'] = []
        data['scenes'].append(scene)
        
    # Xử lý các trường của scene
    if 'name' in patch_data:
        scene['name'] = patch_data['name']
    if 'script' in patch_data:
        scene['script'] = patch_data['script']
        
    # Xử lý SFS
    if 'sfs' in patch_data:
        if 'sfs' not in scene:
            scene['sfs'] = []
        for p_sf in patch_data['sfs']:
            p_sf = filter_keys(p_sf, VALID_SF_KEYS)
            if 'id' not in p_sf:
                continue
            
            # Update or append
            found = False
            for i, sf in enumerate(scene['sfs']):
                if sf.get('id') == p_sf['id']:
                    scene['sfs'][i].update(p_sf)
                    found = True
                    break
            if not found:
                scene['sfs'].append(p_sf)
                
    # Xử lý SHOTS
    if 'shots' in patch_data:
        if 'shots' not in scene:
            scene['shots'] = []
        for p_sh in patch_data['shots']:
            p_sh = filter_keys(p_sh, VALID_SHOT_KEYS)
            sid = p_sh.get('id') or p_sh.get('sh')
            if not sid:
                continue
            p_sh.pop('sh', None)
            p_sh['id'] = sid

            # Ép kiểu dur
            if 'dur' in p_sh:
                try:
                    p_sh['dur'] = int(p_sh['dur'])
                except (ValueError, TypeError):
                    pass

            # Update or append
            found = False
            for i, sh in enumerate(scene['shots']):
                if (sh.get('id') or sh.get('sh')) == sid:
                    scene['shots'][i].update(p_sh)
                    found = True
                    break
            if not found:
                scene['shots'].append(p_sh)

    # XOÁ có kiểm soát. Viết lại một scene thì phải bỏ được SF/shot cũ, nếu không
    # `shots[].sf` sẽ còn trỏ vào SF đã chết và hỏng dữ liệu sau này.
    for khoa, kho in (('xoa_sfs', 'sfs'), ('xoa_shots', 'shots')):
        ids = set(patch_data.get(khoa) or [])
        if ids:
            scene[kho] = [x for x in scene.get(kho, [])
                          if (x.get('id') or x.get('sh')) not in ids]
            print(f"  · xoá {len(ids)} mục khỏi {kho}")

    # Thứ tự shot quyết định thứ tự dựng phim — patch xong phải xếp lại theo
    # danh sách user khai, không để shot mới rơi hết xuống cuối.
    if patch_data.get('thu_tu_shots'):
        thu_tu = {v: k for k, v in enumerate(patch_data['thu_tu_shots'])}
        scene['shots'].sort(key=lambda x: thu_tu.get(x.get('id') or x.get('sh'), 10**6))

    save_json(board_path, data)
    print(f"Đã patch scene {scene_id} thành công.")

def main():
    if len(sys.argv) < 4:
        print("Cách dùng:")
        print("  python3 sua-board.py xem <project_dir> <scene_id>")
        print("  python3 sua-board.py patch <project_dir> <scene_id> <patch.json>")
        sys.exit(2)
        
    cmd = sys.argv[1]
    proj_dir = sys.argv[2]
    scene_id = sys.argv[3]
    board_path = os.path.join(proj_dir, 'sf-board.json')
    
    if not os.path.exists(board_path):
        print(f"Lỗi: Không tìm thấy file {board_path}", file=sys.stderr)
        sys.exit(1)
        
    if cmd == 'xem':
        cmd_xem(board_path, scene_id)
    elif cmd == 'patch':
        if len(sys.argv) < 5:
            print("Lỗi: Thiếu file patch.json", file=sys.stderr)
            sys.exit(2)
        cmd_patch(board_path, scene_id, sys.argv[4])
    else:
        print(f"Lệnh không hợp lệ: {cmd}", file=sys.stderr)
        sys.exit(2)

if __name__ == '__main__':
    main()
