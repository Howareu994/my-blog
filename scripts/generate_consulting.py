import json
import os
from datetime import datetime, timedelta

# ==========================================
# ⚙️ 心理辅导 (Consulting) 释放规则引擎
# ==========================================

# 1. 视界范围：开放未来 2 个月的排期
MONTHS_AHEAD = 2

# 2. 每日切割规则：10点到16点，直接写明时间区间！
# 你可以在这里随意修改具体时长，比如 1小时 或 1.5小时
SLOT_RANGES = [
    "10:00 - 11:00",
    "11:30 - 12:30",
    "14:00 - 15:00",
    "15:30 - 16:30"
]

# 3. 绝对黑名单：你确定要休息/外出的日期 (格式: YYYY-MM-DD)
BLOCKED_DATES = [
    "2026-05-14",
    "2026-05-25"
]

# 4. 周期性休息日：0=周一, 6=周日 (默认屏蔽周末)
BLOCKED_WEEKDAYS = [5, 6]

def generate_slots():
    print(f"⚙️ 正在启动时间引擎，计算未来 {MONTHS_AHEAD} 个月的心理咨询频段...")

    slots = []
    # 从明天开始算起
    current_date = datetime.now() + timedelta(days=1)
    end_date = current_date + timedelta(days=MONTHS_AHEAD * 30)

    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        weekday = current_date.weekday()

        if weekday not in BLOCKED_WEEKDAYS and date_str not in BLOCKED_DATES:
            # 直接灌入完整的时间区间
            for time_range in SLOT_RANGES:
                slots.append(f"{date_str} {time_range}") # 生成格式: 2026-05-10 10:00 - 11:00

        current_date += timedelta(days=1)

    os.makedirs('data', exist_ok=True)

    # ⚠️ 写入 consulting 专属的 json 文件
    with open('data/consulting_slots.json', 'w', encoding='utf-8') as f:
        json.dump(slots, f, ensure_ascii=False, indent=2)

    print(f"✅ 心理预约模块化完成！共释放了 {len(slots)} 个区间。")
    print(f"📁 数据已同步至 data/consulting_slots.json")

if __name__ == "__main__":
    generate_slots()