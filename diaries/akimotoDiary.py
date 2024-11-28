from diaries.AbstractDiary import AbstractDiary

class DiaryAkimoto(AbstractDiary):

    def get_date(self):
        return "2021-11-28"

    def get_summary(self):
        return "こんなのがリーダーでいいんですかね？"

    def get_author(self):
        return "Akimoto"
