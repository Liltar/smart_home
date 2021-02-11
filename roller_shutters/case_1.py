# ставим на сигнализ:
# если светло и разрешен упр ролетами - роллеты закрываются - даём импульс 4 сек на закрытие
# если темно - ничего не делаем

# получаем время захода солнца
from astral import LocationInfo, sun
import datetime
location = LocationInfo('Kiev')
sunset_time = sun.sunset(location.observer, date=datetime.date.today(), tzinfo=location.timezone)
current_time = datetime.datetime.now()
