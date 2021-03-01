# ставим на сигнализ:
# если светло и разрешен упр ролетами - роллеты закрываются - даём импульс 4 сек на закрытие
# если темно - ничего не делаем
# что управляет ролетами - то, что дает импульс на электромотор
# что управляет сигнализацией - хранит её статус

# получаем время захода солнца
from astral import LocationInfo, sun
import datetime
from pytz import timezone
location = LocationInfo()
sunset_time = sun.sunset(location.observer, date=datetime.datetime.now(), tzinfo=location.timezone)
london = timezone('Europe/London')
current_time = london.localize(datetime.datetime.now())
dark = current_time >= sunset_time
while True:
    if dark:

        break
    else:
        break
