# Yandex AI Studio — quickstart
# Источник: https://aistudio.yandex.ru/docs/ru/ai-studio/quickstart/index

Платформа Yandex AI Studio объединяет ИИ-сервисы и технологии Yandex Cloud для вашего бизнеса, чтобы вы могли создавать собственные ИИ-решения.

AI Studio предоставляет широкий выбор API и инструментов для решения любой задачи: OpenAI-совместимые API для создания текстовых и голосовых агентов, MCP-серверы и инструменты веб-поиска и поиска по файлам, а также специализированные API, разработанные в Яндексе.

В этом разделе вы создадите и настроите свой аккаунт, а затем отправите свой первый запрос к генеративной текстовой модели, доступной в Model Gallery.

Подготовьте облако к работе
Подготовьте облако к работе

AI Studio использует
ресурсную модель
Yandex Cloud: большинство сервисов хранит ресурсы в каталогах. Каталоги принадлежат облакам, а облака — организациям. Каталог потребуется и для работы с AI Studio.

Войдите в AI Studio
, используя личный аккаунт на Яндексе (Яндекс ID). Подробную инструкцию, как создать такой аккаунт, смотрите в Справке
Яндекс ID
.

Создайте организацию:

Введите название организации.

Укажите название облака — оно будет использоваться для всех ресурсов Yandex Cloud.

Нажмите
Открыть AI Studio
.

В организации будет автоматически создан новый каталог с именем
default
.

Привяжите платежный аккаунт
Привяжите платежный аккаунт

Для работы с AI Studio необходим активный
платежный аккаунт
, привязанный к вашему облаку. При создании первого платежного аккаунта, привязанного к пользовательскому аккаунту, вам будет начислен
стартовый грант
.

После авторизации в AI Studio нажмите кнопку
Привязать платежный аккаунт
в правом верхнем углу интерфейса.

Создайте платежный аккаунт или выберите существующий.

Нажмите кнопку
Добавить карту
.

Укажите данные карты: 16-значный номер, срок действия, код CVV (с обратной стороны карты).

Нажмите кнопку
Привязать
.

Убедитесь, что платежный аккаунт имеет статус
ACTIVE
или
TRIAL_ACTIVE
.

Создайте API-ключ
Создайте API-ключ

Чтобы создать API-ключ:

Интерфейс AI Studio

В
интерфейсе AI Studio
нажмите
Создать API-ключ
в правом верхнем углу.

(Опционально) Измените описание API-ключа, чтобы вы легко могли найти его после.

Выберите срок действия API-ключа.

Нажмите кнопку
Создать
.

Сохраните идентификатор и секретный ключ.

Внимание

Не передавайте никому свой API-ключ. После закрытия диалога значение ключа будет недоступно.

Вместе с API‑ключем будет создан и
сервисный аккаунт
с минимальными ролями, необходимыми для работы в AI Studio.

Получите данные для аутентификации в API, как описано в разделе
Аутентификация в API Yandex AI Studio
.

Настройте окружение
Настройте окружение

Установите необходимые пакеты и библиотеки:

Python

Node.js

cURL

Go

AI SDK

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

            

Примечание

Если вы используете ОС
Windows
, рекомендуем предварительно
установить
оболочку
WSL
и выполнять дальнейшие действия в этой оболочке.

Установите библиотеку OpenAI Python:

pip install --upgrade openai

            

Установите библиотеку OpenAI Node.js:

npm install --save openai

# or

yarn add openai

            

Установите
cURL
.

Установите Go версии
1.23.4
или выше:

Примечание

Для OS Windows cкачайте и запустите установщик с
официального сайта
.

Для macOS и установите пакет с
официального сайта
или используйте Homebrew:

brew install go

            

Скачайте архив с
официального сайта
:

wget https://go.dev/dl/go1.23.4.linux-amd64.tar.gz

            

Распакуйте архив в директорию
/usr/local
:

sudo
tar -C /usr/local -xzf go1.23.4.linux-amd64.tar.gz

            

Откройте файл
~/.bashrc
:

nano ~/.bashrc

            

Добавьте в конец файла следующие строки:

export
GOROOT=/usr/local/go
# где лежит сам Go

export
GOPATH=
$HOME
/go
# рабочая директория (модули, кэш)

export
PATH=
$PATH
:
$GOROOT
/bin
# чтобы работала команда go

export
PATH=
$PATH
:
$GOPATH
/bin
# чтобы работали установленные инструменты

            

Сохраните файл и перезагрузите настройки:

source
~/.bashrc

            

Проверьте работоспособность:

go version 

            

Пример ответа:

go version go1.23.4 linux/amd64

            

Установите библиотеку OpenAI Go:

go get github.com/openai/openai-go

            

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

            

Примечание

Если вы используете ОС
Windows
, рекомендуем предварительно
установить
оболочку
WSL
и выполнять дальнейшие действия в этой оболочке.

Установите библиотеку AI SDK:

pip install yandex-ai-studio-sdk

            

Чтобы использовать
модели
Model Gallery, задайте данные для аутентификации. Для этого вам понадобятся
идентификатор каталога
и секретное значение созданного API-ключа:

Python

Node.js

cURL

Go

AI SDK

import
openai

YANDEX_FOLDER_ID=
''

YANDEX_API_KEY=
''

client = openai.OpenAI(
    api_key=YANDEX_API_KEY,
    project=YANDEX_FOLDER_ID,
    base_url=
"https://ai.api.cloud.yandex.net/v1"

)

            

import
OpenAI
from
"openai"
;

const
YANDEX_FOLDER_ID
=
''
;

const
YANDEX_API_KEY
=
''
;

const
openai =
new
OpenAI
({

apiKey
:
YANDEX_API_KEY
,

project
:
YANDEX_FOLDER_ID
,

baseURL
:
'https://ai.api.cloud.yandex.net/v1'
});

            

export
YANDEX_FOLDER_ID=
''

export
YANDEX_API_KEY=
''

            

package
main

import
(

"context"

"github.com/openai/openai-go"

"github.com/openai/openai-go/option"

)

const
(
    YANDEX_FOLDER_ID =
""

    YANDEX_API_KEY   =
""

)

func
main
()
{
    client := openai.NewClient(
        option.WithAPIKey(YANDEX_API_KEY),
        option.WithBaseURL(
"https://ai.api.cloud.yandex.net/v1"
),
    )
}

            

export
YANDEX_FOLDER_ID=
''

export
YANDEX_API_KEY=
''

            

Отправьте запрос к модели
Отправьте запрос к модели

Отправьте запрос к модели. Для примера обратитесь к модели Alice AI LLM:

Python

Node.js

cURL

Go

AI SDK

YANDEX_MODEL =
"aliceai-llm"

response = client.responses.create(
    model=
f"gpt://
{YANDEX_CLOUD_FOLDER}
/
{YANDEX_MODEL}
"
,

input
=
"Придумай 3 необычные идеи для стартапа в сфере путешествий."
,
    temperature=
0.8
,
    max_output_tokens=
1500

)

print
(response.output[
0
].content[
0
].text)

            

const
response =
await
openai.
responses
.
create
({

model
:
`gpt://
${YANDEX_FOLDER_ID}
/aliceai-llm`
,

input
:
'Придумай 3 необычные идеи для стартапа в сфере путешествий.'

});

console
.
log
(response.
output_text
);

            

curl \\
  --request POST https://ai.api.cloud.yandex.net/v1/responses \\
  --header
"Authorization: Api-Key
${YANDEX_API_KEY}
"
\\
  --header
"Content-Type: application/json"
\\
  --data
'{
    "modelUri": "gpt://'
"
${YANDEX_FOLDER_ID}
"
'/aliceai-llm",
    "temperature": 0.8,
    "max_output_tokens": 1500,
    "input": "Придумай 3 необычные идеи для стартапа в сфере путешествий."
  }'

            

package
main

import
(

"context"

"fmt"

"log"

"github.com/openai/openai-go"

"github.com/openai/openai-go/option"

)

const
(
  YANDEX_FOLDER_ID =
""

  YANDEX_API_KEY   =
""

)

func
main
()
{
  client := openai.NewClient(
    option.WithAPIKey(YANDEX_API_KEY),
    option.WithBaseURL(
"https://ai.api.cloud.yandex.net/v1"
),
  )

  ctx := context.Background()

  resp, err := client.Chat.Completions.New(ctx, openai.ChatCompletionNewParams{
    Model: fmt.Sprintf(
"gpt://%s/aliceai-llm"
, YANDEX_FOLDER_ID),
    Messages: []openai.ChatCompletionMessageParamUnion{
      openai.UserMessage(
"Придумай 3 необычные идеи для стартапа в сфере путешествий."
),
    },
    Temperature: openai.Float(
0.8
),
    MaxTokens:   openai.Int(
1500
),
  })

if
err !=
nil
{
    log.Fatalf(
"Ошибка при запросе: %v"
, err)
  }

  fmt.Println(resp.Choices[
0
].Message.Content)
}

            

import
os

from
yandex_ai_studio_sdk
import
AIStudio

YANDEX_API_KEY = os.environ[
"YANDEX_API_KEY"
]
YANDEX_FOLDER_ID = os.environ[
"YANDEX_FOLDER_ID"
]

sdk = AIStudio(
    folder_id=YANDEX_FOLDER_ID,
    auth=YANDEX_API_KEY,
)

model = sdk.models.completions(
"aliceai-llm"
)
model = model.configure(temperature=
0.8
, max_tokens=
1500
)
result = model.run(
"Придумай 3 необычные идеи для стартапа в сфере путешествий."
)

for
alternative
in
result:

print
(alternative.text)

            

Что дальше
Что дальше

Узнайте подробнее о сервисе

