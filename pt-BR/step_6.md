## Criptografando mensagens inteiras

Em vez de apenas criptografar e descriptografar mensagens um caractere de cada vez, vamos mudar o programa para criptografar mensagens inteiras!

+ Em primeiro lugar, verifique se o seu código está assim:
    
    ![captura de tela](images/messages-character-finished.png)

+ Crie uma variável para armazenar a nova mensagem criptografada.
    
    ![captura de tela](images/messages-newmessage.png)

+ Altere seu código para armazenar a mensagem do usuário e não apenas um caractere.
    
    ![captura de tela](images/messages-message.png)

+ Adicione um laço `for` ao seu código e recue o restante do código para que ele seja repetido para cada caractere na mensagem.
    
    ![captura de tela](images/messages-loop.png)

+ Teste seu código. Você deve ver que cada caractere na mensagem é criptografado e impresso um de cada vez.
    
    ![captura de tela](images/messages-loop-test.png)

+ Vamos adicionar cada caractere criptografado à sua variável `novaMensagem`.
    
    ![captura de tela](images/messges-message-add-character.png)

+ Você pode imprimir a `novaMensagem` com o comando `print` quando ela for criptografada.
    
    ![captura de tela](images/messages-print-message-characters.png)

+ Se você excluir os espaços antes da instrução `print`, a mensagem criptografada será exibida apenas uma vez no final. Você também pode excluir o código para imprimir as posições dos caracteres.
    
    ![captura de tela](images/messages-print-message-comment.png)