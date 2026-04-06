# Yandex AI Studio — manage_index
# Источник: https://aistudio.yandex.ru/docs/ru/ai-studio/operations/agents/manage-searchindex

AI-агенты
в своей работе могут использовать гибридный поиск по контексту, получаемому из файлов внешних баз знаний. Такой дополнительный контекст хранится в
поисковых индексах
Vector Store — специальных векторных хранилищах Yandex AI Studio, которые создаются с помощью Vector stores API и в которых документы представлены в виде векторов (
эмбеддингов
).

Перед началом работы
Перед началом работы

Чтобы воспользоваться примерами:

Python

Создайте
сервисный аккаунт и
назначьте
ему
роли
ai.assistants.editor
и
ai.languageModels.user
.

Получите
и сохраните
API-ключ
сервисного аккаунта, указав для него
область действия
yc.ai.foundationModels.execute
.

Примечание

Если вы используете ОС
Windows
, рекомендуем предварительно
установить
оболочку
WSL
и выполнять дальнейшие действия в этой оболочке.

Установите Python версии
3.10
или выше.

(Опционально) Установите библиотеку Python
venv
для создания изолированных виртуальных окружений в Python.

(Опционально) Создайте и войдите в новое виртуальное окружение Python:

python3 -m venv new-env

source
new-env/bin/activate

            

Установите
библиотеку
OpenAI для Python:

pip install openai

            

Загрузить файлы
Загрузить файлы

Прежде чем создавать поисковый индекс, загрузите в Vector Store файлы, которые требуется проиндексировать:

Python

Скачайте и распакуйте
архив
с примерами файлов, которые будут использоваться как дополнительный источник информации. В файлах содержатся рекламные тексты для туров на Бали и в Казахстан, сгенерированные YandexGPT Pro.

Создайте файл
upload.py
и добавьте в него следующий код:

import
pathlib

from
openai
import
OpenAI

YANDEX_API_KEY =
""

YANDEX_FOLDER_ID =
""

# Локальный файл для индексации

def
local_path
(
path:
str
) -> pathlib.Path:

return
pathlib.Path(__file__).parent / path

def
main
():
    client = OpenAI(
        api_key=YANDEX_API_KEY,
        base_url=
"https://ai.api.cloud.yandex.net/v1"
,
        project=YANDEX_FOLDER_ID,
    )

# Загружаем несколько файлов

    file_names = [
"bali.md"
,
"kazakhstan.md"
]
    file_ids = []

print
(
"Загружаем файлы..."
)

for
fname
in
file_names:
        f = client.files.create(
            file=
open
(local_path(fname),
"rb"
),

# Значение assistants используется для всех файлов, которые должны подключаться

# к Vector stores API

            purpose=
"assistants"
,
        )

print
(
f"Файл
{fname}
загружен:"
, f.
id
)
        file_ids.append(f.
id
)

if
__name__ ==
"__main__"
:
    main()

            

Где:

YANDEX_API_KEY
— полученный перед началом работы
API-ключ
сервисного аккаунта.

YANDEX_FOLDER_ID
—
идентификатор каталога
, в котором выполняются операции с Vector stores API.

Выполните созданный файл:

python3 upload.py

            

Результат:

Загружаем файлы...
Файл bali.md загружен: fvt5ajp8l83v********
Файл kazakhstan.md загружен: fvtbq10jv46r********

            

Сохраните полученные идентификаторы загруженных файлов — они понадобятся при создании поискового индекса.

Создать поисковый индекс Vector Store
Создать поисковый индекс Vector Store

Создайте поисковый индекс из предварительно загруженных файлов:

Python

Создайте файл
index.py
и добавьте в него следующий код:

import
time

from
openai
import
OpenAI

YANDEX_API_KEY =
""

YANDEX_FOLDER_ID =
""

def
main
():
    client = OpenAI(
        api_key=YANDEX_API_KEY,
        base_url=
"https://ai.api.cloud.yandex.net/v1"
,
        project=YANDEX_FOLDER_ID,
    )

    input_file_ids = [
""
,
""
]

# Создаем поисковый индекс с несколькими файлами

print
(
"Создаем поисковый индекс..."
)
    vector_store = client.vector_stores.create(

# Говорящее название индекса

        name=
"База знаний поддержки"
,

# Ваши метки для файлов

        metadata={
"key"
:
"value"
},

# Время жизни индекса

# last_active_at — после последней активности

# или created_at — после создания

        expires_after={
"anchor"
:
"last_active_at"
,
"days"
:
1
},

# Стратегия разбиения документов на фрагменты (чанки)

# `max_chunk_size_tokens` — максимальный размер фрагмента в токенах

# `chunk_overlap_tokens` — размер перекрытия между соседними фрагментами, помогает избежать потери информации на границах фрагментов

        chunking_strategy={

'type'
:
'static'
,

'static'
: {

'max_chunk_size_tokens'
:
1408
,

'chunk_overlap_tokens'
:
148

          }
        },  

        file_ids=input_file_ids,
# "

YANDEX_FOLDER_ID =
""

def
main
():
    client = OpenAI(
        api_key=YANDEX_API_KEY,
        base_url=
"https://ai.api.cloud.yandex.net/v1"
,
        project=YANDEX_FOLDER_ID,
    )

    index_id =
""

# Поиск по индексу

    query =
"Стоимость поездки на Бали"

print
(
f"Ищем по запросу:
{query}
"
)
    results = client.vector_stores.search(index_id, query=query)

for
r
in
results:

print
(
"Результат:"
, r)

if
__name__ ==
"__main__"
:
    main()

            

Где
index_id
— идентификатор поискового индекса Vector Store, полученный на предыдущем шаге.

Выполните созданный файл:

python3 query.py

            

Результат:

Ищем по запросу: Стоимость поездки на Бали
Результат: VectorStoreSearchResponse(attributes={}, content=[Content(text='**Бали — райский уголок, где 
вас ждут незабываемые впечатления!**\
\
Приглашаем вас провести незабываемый отпуск на Бали! Этот 
волшебный остров в Индонезии славится своими прекрасными пляжами, уникальной культурой и гостеприимными 
жителями. Здесь вы сможете насладиться красотой природы, попробовать местную кухню и познакомиться с 
новыми людьми. **Что нужно для поездки?** Для въезда на территорию Индонезии вам потребуется виза. Вот 
список документов, которые необходимы для её оформления:\
* Загранпаспорт, срок действия которого 
составляет не менее 6 месяцев на момент въезда в страну. * Две фотографии, соответствующие требованиям 
консульства. * Подтверждение бронирования отеля или письмо другого жилья. * Бронь или билеты туда и 
обратно. * Анкета, заполненная на английском языке. Обратите внимание, что требования могут меняться, 
поэтому перед поездкой рекомендуется проверить актуальную информацию на сайте консульства или визового 
центра. Стоимость визы 300 рублей. Не упустите возможность посетить этот прекрасный остров и получить 
массу положительных эмоций! Бронируйте свой отдых на Бали уже сегодня! **Мы ждём вас!**', type='text', 
valid=True)], file_id='fvt5ajp8l83v********', filename='bali.md', score=0.9999999979850982, valid=True)

Результат: VectorStoreSearchResponse(attributes={}, content=[Content(text='**Казахстан: путешествие в 
сердце Евразии**\
\
Откройте для себя Казахстан — удивительную страну, где встречаются Восток и Запад. 
Здесь вы сможете насладиться бескрайними степями, величественными горами, историческими памятниками и 
гостеприимством местных жителей. **Что нужно для поездки?** Чтобы попасть в Казахстан из России, вам 
потребуются следующие документы:\
* Загранпаспорт, срок действия которого составляет не менее 3 месяцев 
на момент окончания поездки. * Миграционная карта (выдаётся в самолете или на границе). * Медицинская 
страховка (не обязательна, но рекомендуется). Не упустите возможность посетить эту прекрасную страну и 
получить массу положительных эмоций! Бронируйте свой отдых в Казахстане уже сегодня! **Мы ждём вас!**', 
type='text', valid=True)], file_id='fvtbq10jv46r********', filename='kazakhstan.md', score=0.0, 
valid=True)

            

В результате Vector stores API вернет текстовые фрагменты с указанием имени и идентификатора файла, а также оценку релевантности поисковому запросу для каждого фрагмента.

Удалить из индекса один из файлов-источников
Удалить из индекса один из файлов-источников

Чтобы удалить файл-источник из поискового индекса, передайте в Vector stores API идентификаторы индекса и этого файла:

Python

Создайте файл
remove_file.py
и добавьте в него следующий код:

import
os

import
pathlib

import
time

from
openai
import
OpenAI

YANDEX_API_KEY =
""

YANDEX_FOLDER_ID =
""

def
main
():
    client = OpenAI(
        api_key=YANDEX_API_KEY,
        base_url=
"https://ai.api.cloud.yandex.net/v1"
,
        project=YANDEX_FOLDER_ID,
    )

    index_id =
""

    file_to_delete =
""

# Удаление одного файла из индекса

print
(
"Удаляем один файл из поискового индекса..."
)
    deleted_file = client.vector_stores.files.delete(
        file_to_delete, vector_store_id=index_id
    )

print
(
f"Файл
{file_to_delete}
удален из индекса:"
, deleted_file)

if
__name__ ==
"__main__"
:
    main()

            

Где:

index_id
— идентификатор поискового индекса Vector Store, полученный ранее.

file_to_delete
— идентификатор файла, который требуется удалить. Идентификаторы были получены ранее при загрузке файлов и при выполнении поискового запроса.

Выполните созданный файл:

python3 remove_file.py

            

Результат:

Удаляем один файл из поискового индекса...
Файл fvt5ajp8l83v******** удален из индекса: VectorStoreFileDeleted(id='fvt5ajp8l83v********', deleted=True, object='vector_store.file.deleted', valid=True)

            

Удалить поисковый индекс Vector Store
Удалить поисковый индекс Vector Store

Чтобы удалить весь поисковый индекс, передайте в Vector stores API его идентификатор:

Python

Создайте файл
delete_index.py
и добавьте в него следующий код:

import
os

import
pathlib

import
time

from
openai
import
OpenAI

YANDEX_API_KEY =
""

YANDEX_FOLDER_ID =
""

def
main
():
    client = OpenAI(
        api_key=YANDEX_API_KEY,
        base_url=
"https://ai.api.cloud.yandex.net/v1"
,
        project=YANDEX_FOLDER_ID,
    )

    index_id =
""

# Удаляем весь Vector Store

    deleted_store = client.vector_stores.delete(index_id)

print
(
"Vector Store удален:"
, deleted_store)

if
__name__ ==
"__main__"
:
    main()

            

Где
index_id
— идентификатор поискового индекса Vector Store, полученный ранее.

Выполните созданный файл:

python3 delete_index.py

            

Результат:

Vector Store удален: VectorStoreDeleted(id='fvt9ef7q28n5********', deleted=True, object='vector_store.deleted', valid=True)

            

См. также
См. также

Поисковые индексы Vector Store

Создать текстового агента с поиском по файлам

