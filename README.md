# correios.postmon.com.br

Interface para comunicação com os sistemas de rastreamento dos Correios.

## Webservice

O webservice dos Correios é um serviço SOAP, com uma complexidade alta para a comunicação que deveria ser simples.

Com o Postmon, é possível acessar todas as funcionalidades do serviço dos Correios de uma forma simplificada e respostas em JSON.

https://correios.postmon.com.br/webservice/buscaEventos/?objetos=PL657535905BR

Para buscar mais de um objeto, os objetos devem ser concatenados sem caractere separador.

https://correios.postmon.com.br/webservice/buscaEventos/?objetos=PL657535905BRDV430359393BR

## Acompanhamento pelo usuário

Você pode enviar diretamente o link de acompanhamento por email, funcionalidade que não existe mais no site dos Correios.

http://correios.postmon.com.br/rastreamento/?objeto=PL657535905BR

## Status

O projeto está em início do desenvolvimento, para se adaptar às alterações recentes dos Correios.
