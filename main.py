from diaries.DiarySample import DiarySample
from diaries.akimotoDiary import DiaryAkimoto
from diaries.k23070_Diary import DiarySekiya
from diaries.ShibataDiary import ShibataDiary
from diaries.NagaoDiary import NagaoDiary
from diaries.TadaSample import DiaryTada
from diaries.SakaiDiary import SakaiDiary

diaries = [
    DiarySample(), 
    SakaiDiary(),
    DiaryTada(),
    NagaoDiary(),
    ShibataDiary(),
    DiaryAkimoto(),
    DiarySekiya()
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
