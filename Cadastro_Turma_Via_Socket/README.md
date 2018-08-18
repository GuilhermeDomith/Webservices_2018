<h1>Cadastro de Turma Via Socket<h1>

A aplicação cliente, desenvolvida em Python, permite inserir as turmas e alunos por meio do terminal. Após 
o término da inserção o programa cliente irá converter os dados fornecidos em um objeto JSON e enviar para o 
programa servidor por meio do socket. 

O programa servidor, desenvolvido em Java, irá receber a mensagem e irá exibir as turmas fornecidas no 
programa cliente.

Para executar as aplicações os seguintes comandos devem ser executados:
<pre>
    $ java -jar ServidorAPP/jar/ServidorAPP.jar
    $ python ClienteAPP/app.py
</pre>