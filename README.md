# URL-shortener
URL shortener with simple UI.

Поле для ввода ссылки проверяет адрес на корректность , выдавая предупреждение, если формат не подходит. 

Также предусмотрена ситуация при добавлении одной и той же ссылки : заново она добавляться в БД не будет, возвращая уже существующий адрес.

При попытке перейти на сокращенную ссылку, которой не создавалось - будет осуществлен переход на домашнюю страницу. 


Алгоритм, используемый в этом проекте, заключается в следующем : получаемый URl добавляется в БД, а его id в БД используется для создания сокращенного URL. При помощи системы счисления с основанием 62, т.к. это позволяет создать большее количество таких ссылок. Логику можно увидеть в файле shortener/views.py . Также реализован алгоритм декодирования при переходе на сокращенную ссылку, что позволяет хранить в БД только оригинальный URL , а сокращенный получать при запросе. 
