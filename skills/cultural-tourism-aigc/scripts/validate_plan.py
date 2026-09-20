#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ALLOWED_ROUTES = {"auto", "economy", "continuity", "hero"}
ALLOWED_CAMERAS = ("固定", "缓推", "缓拉", "左移", "右移")

def validate(data):
    errors = []
    shots = data.get("shots") or []
    if len(shots) < 2:
        errors.append("至少需要两个镜头")
    for index, shot in enumerate(shots, 1):
        if shot.get("shot_id") != index:
            errors.append(f"第{index}项 shot_id 不连续")
        if not 2 <= float(shot.get("duration_s", 0)) <= 15:
            errors.append(f"第{index}镜时长应为2到15秒")
        if not str(shot.get("camera", "")).startswith(ALLOWED_CAMERAS):
            errors.append(f"第{index}镜运镜不稳定或未指定")
        if shot.get("generation_route", "auto") not in ALLOWED_ROUTES:
            errors.append(f"第{index}镜 generation_route 无效")
        if index == 1 and shot.get("start_from_previous"):
            errors.append("首镜不能延续上一镜")
        if shot.get("start_from_previous") and not shot.get("continuity"):
            errors.append(f"第{index}镜延续动作但缺少 continuity")
        for key in ("scene_desc", "action", "end_state", "transition", "soundscape"):
            if not str(shot.get(key, "")).strip():
                errors.append(f"第{index}镜缺少 {key}")
    if shots and not str(shots[-1].get("screen_location", "")).strip():
        errors.append("末镜缺少城市落款 screen_location")
    declared = data.get("duration_s")
    if declared is not None:
        total = sum(float(s.get("duration_s", 0)) for s in shots)
        if abs(total - float(declared)) > 0.1:
            errors.append(f"镜头总时长 {total:g} 与声明 {declared:g} 不一致")
    return errors

def main():
    path = Path(sys.argv[1])
    errors = validate(json.loads(path.read_text(encoding="utf-8")))
    if errors:
        print("FAIL")
        print("\n".join(f"- {item}" for item in errors))
        raise SystemExit(1)
    print("PASS")

if __name__ == "__main__":
    main()
