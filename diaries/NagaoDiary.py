from diaries.AbstractDiary import AbstractDiary

class NagaoDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return "説明早くて追いつかぬ"
    
    def get_author(self):
        return "Nagao"