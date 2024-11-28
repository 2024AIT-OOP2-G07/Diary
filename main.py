from diaries.DiarySample import DiarySample
from diaries.k23070_Diary import DiarySekiya

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), DiarySekiya()] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
