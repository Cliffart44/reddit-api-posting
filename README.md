# [_Тестовое задание отправки комментария в reddit_][Task]
[<img align="right" width=28% height=28% src="/workpapers/reddit-logo.png"/>][Reddit]

---
## Процедура запуска автотеста

### Окружение
- [x] [**Python 3.9**](https://www.python.org/downloads) или выше
- [x] [**PyCharm**](https://www.jetbrains.com/pycharm/download)

### Запуск
1. Необходимо получить учётные данные [reddit](https://www.reddit.com)
   (инструкция в [текстовом](https://towardsdatascience.com/how-to-use-the-reddit-api-in-python-5e05ddfd1e5c)
   формате или [видео](https://youtu.be/FdjVoOf9HN4)).
2. Для простоты и удобства работы с учётными данными создан отдельный файл
   [*credentials*](src/variables/credentials.py), в котором их в дальнейшем нужно указать.
3. Внутренняя настройка проекта сводится к следующим шагам:
    - Получить код [репозитория](https://github.com/Cliffart44/reddit-api-posting) удобным способом.
    - Установить папку [*src*](/src) как *Sources Root* в контекстном меню.
    - В меню *Select Run/Debug Configuration* выбрать *Add Configuration*.
    - Создать новую конфигурацию: в диалоговом окне нажать кнопку
       *Add New Configuration* → *Python*.
    - Настроить команду запуска: *Module name*: `robot.run`.
    - Параметр *Working Directory* должен указывать на папку [*src*](/src).
    - В поле *Parameters* ввести [аргументы запуска
       тестов](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#executing-test-cases),
       например, `--outputdir output --include reddit tests`.
    - Выполнить в терминале `pip install -r requirements.txt` для установки необходимых пакетов.
    - Указать учётные данные [reddit](https://www.reddit.com) согласно пункту **2**.
    - Нажать [`Ctrl+Shift+F10`][Run] для запуска теста.

#### Отчёты
> При указании параметров из инструкции выше после запуска тестов будут находиться в каталоге [*output*](/src/output).
Также доступен [пример результата запуска](https://reddit-api-posting.netlify.app) автотеста.

### Примечания
Данное исполнение не включает в себя некоторые другие решения, используемые на последних проектах,
над которыми работал, например, *REST-клиент* (предоставляет более развёрнутые отчёты о ходе тестов,
проверяет коды ответов сервера) и декоратор *SchemaValidator* (валидирует ответы по схемам).
Однако, для тестового задания намеренно была выбрана наиболее лаконичная реализация,
поскольку, на мой взгляд, она лучше всего соответствует задаче.
Вместе с этим, вышеупомянутые решения можно подключить и к данному проекту при необходимости.

---
[<img align="right"
src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=yellow"/>][Pre-commit]
[<img align="right" src="https://badges.gitter.im/Cliffart44/community.svg"/>][Gitter]

[Task]: https://github.com/Cliffart44/reddit-api-posting
[Reddit]: https://www.redditinc.com/brand
[Run]: https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html#run
[Pre-commit]: https://github.com/pre-commit/pre-commit
[Gitter]: https://gitter.im/Cliffart44/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
