*** Settings ***
Library    Collections
Library    jsonschema
Library    OperatingSystem
Library    libraries.Main    WITH NAME    Local

*** Keywords ***
Validate json
    [Documentation]    Валидация ответа сервера по json-схеме
    [Arguments]        ${response}    ${schema_name}

    ${schema}    Get Binary File    .${/}schemas${/}${schema_name}.json
    ${schema}    Evaluate           json.loads('''${schema}''')    json

    Validate    instance=${response}    schema=${schema}
