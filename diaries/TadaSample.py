from diaries.AbstractDiary import AbstractDiary

class DiaryTada(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "今日は朝起きるのが辛かった.昨夜は労働後にどうしても原神がしたくなって寝るのが遅くなってしまったからだと思う.今日こそは早く寝たい"

    def get_author(self):
        return "Tada"
