*** Settings ***
Documentation    Работа с Reddit через API
Resource         common.resource
Force Tags       reddit

*** Variables ***
${comment_text}    Hello, world!

*** Test Cases ***
Comment posting
    [Documentation]    Публикация комментария
    [Tags]             positive
    [Setup]            Set comment fullname in "pythonsandlot"
    [Teardown]         Delete Comment    ${comment}[name]

    ${comment}    Post Comment    ${comment_text}    ${fullname}

    Validate json                      ${comment}    comment
    Dictionary Should Contain Value    ${comment}    ${comment_text}    Комментарий не добавлен

*** Keywords ***
Set comment fullname in "${subreddit}"
    [Documentation]    Получение полного имени сообщения для отправки комментария

    ${comments}    Get Subreddit Comments    ${subreddit}

    Dictionary Should Contain Key    ${comments}                        data    Ошибка получения комментариев
    Dictionary Should Contain Key    ${comments}[data][children][-1]    data    Комментарии не найдены

    Set Test Variable    $fullname    ${comments}[data][children][-1][data][name]
