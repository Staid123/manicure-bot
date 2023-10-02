##admin
admin-hello = Здравствуйте! Давайте сделаем вам график работы?
              Список всех команд - /help
admin-no = Жаль, если передумаете - введите команду /start

           Список всех команд - /help
admin-yes = Введите имя клиента
admin-phone-number = Введите его номер телефона
                     (например 380682445335)
admin-bad-phone = Вы ввели номер телефона в неправильном формате!
                  Попробуйте еще раз!
                  Правильный ввод номера телефона: 380682445335
admin-year = Выберите с какого года вы планируете принимать записи
admin-month = Выберите месяц
admin-day = Выберите день
admin-time = Выберите время
admin-service = Выберите вид услуги
admin-service-more = Ещё что-то?
admin-send-anketa = Вы записали {$client_name} на { $date }, услуги: {$type_of_service}
admin-end = Отлично!
            Чтобы посмотреть список всех команд введите /help
admin-records = { $name } { $date } { $time } на { $service }
                номер телефона клиента: { $phone }
admin-delete-record = Нажмите на запись которую хотите удалить
rec = { $name } { $date } {$time}


##help
help-command = /add_record - добавить запись
               /check_records - посмотреть записи
               /delete_record - удалить запись

##utils
delimiter = ----------------------------------------------------------------------


##dates
months = Январь, Февраль, Март, Апрель, Май, Июнь, Июль, Август, Сентябрь, Октябрь, Ноябрь, Декабрь
week-days = Понедельник, Вторник, Среда, Четверг, Пятница, Суббота, Воскресенье
datetime={$year}-{$month}-{$day}


###keyboard
##inline
command-help = /help
command-help-description = Список всех команд

##services
services = Маникюр, Снятие гель лак, Покрытие гель лак, Педикюр полный, Педикюр пальцы, Брови, Укрепление

##time
start-working-time = 8:00


##user
user-start = Здравствуйте { $name }! 
             Отправьте ваш номер телефона, чтобы я смог проверить записаны ли вы!
user-records = { $date } { $time } { $service }
user-commands = /see_my_records - посмотреть свои записи
request-contact = Отправить свой номер телефона
see-records = Мне нужен ваш номер телефона, чтобы посмотреть записаны ли вы!
no-records = Вы еще не записаны к Татьяне! 
             Если вы считаете, что возникла ошибка - позвоните ей!

##reminder
send-reminder = Здравствуйте, напоминание! 
                Вы записаны к Татьяне на { $service } { $date }