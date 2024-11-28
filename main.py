from diaries.DiarySample import DiarySample
from diaries.TadaSample import DiaryTada

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), DiaryTada()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
