import json
import os
from datetime import datetime, timedelta

# ==========================================
# ⚙️ 幸存者的 Termin 释放规则引擎
# ==========================================

# 1. 视界范围：生成未来几个月的排期？
MONTHS_AHEAD = 3

# 2. 每日切割规则：7点到20点，按3小时切割
# (19:00-22:00 超出了20点，所以最后一班是 16:00-19:00)
SLOT_HOURS = ["07:00", "10:00", "13:00", "16:00"]

# 3. 绝对黑名单：你确定要休息/外出的日期 (格式: YYYY-MM-DD)
BLOCKED_DATES = [
    "2026-05-14", # 比如：老子这天要去看展
    "2026-05-25"  # 比如：这天要处理私人事务
]

# 4. 周期性休息日：0=周一, 6=周日
# 默认屏蔽周六(5)和周日(6)
BLOCKED_WEEKDAYS = [5, 6]

def generate_slots():
    print("⚙️ 正在启动时间引擎，计算未来 3 个月的可用频段...")

    slots = []
    # 从明天开始算起（避免释放今天已经过去的时间）
    current_date = datetime.now() + timedelta(days=1)
    end_date = current_date + timedelta(days=MONTHS_AHEAD * 30)

    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        weekday = current_date.weekday()

        # 检查是否触碰黑名单或周末
        if weekday not in BLOCKED_WEEKDAYS and date_str not in BLOCKED_DATES:
            # 灌入每日的时间模块
            for hour in SLOT_HOURS:
                slots.append(f"{date_str} {hour}")

        current_date += timedelta(days=1)

    # 确保 data 文件夹存在
    os.makedirs('data', exist_ok=True)

    # 将计算好的所有槽位写入 JSON
    with open('data/slots.json', 'w', encoding='utf-8') as f:
        json.dump(slots, f, ensure_ascii=False, indent=2)

    print(f"✅ 时间模块化完成！共向外释放了 {len(slots)} 个 Termin 槽位。")
    print(f"📁 数据已同步至 data/slots.json")

if __name__ == "__main__":
    generate_slots()