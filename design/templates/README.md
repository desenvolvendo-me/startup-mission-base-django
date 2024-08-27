# Guia de utilização de componentes de Interface Reutilizáveis

A base de estilos, definida no arquivo `base.html`, é o alicerce da estrutura de todas as páginas da aplicação. Este arquivo contém todas as configurações essenciais de estilo e elementos comuns necessários para garantir a consistência visual e funcionalidade ao longo do projeto.

#### Instruções para extensão da base de estilos

Para iniciar o desenvolvimento de qualquer página, utilize a extensão do `base.html` em seu template específico. Este procedimento assegura que todas as definições de estilo e configurações globais sejam herdadas, mantendo a uniformidade do deseign e o comportamento esperado dos componentes.

#### Como utilizar:

1. **Extensão da Base:** Comece o arquivo de template declarando que ele estende o `base.html`. Isso é feito com a seguinte linha no topo do arquivo.
```django
{% extends 'layouts/base.html' %}
```
2. **Carregamento de Arquivos Estáticos:** Em seguida, carregue as tags de arquivo estático que permitem a inclusão de recursos como CSS e JavaScript:
```django
{% load static %}
```
3. **Definição do Bloco de Conteúdo:** Utilize o bloco de conteúdo (`block content`) para inserir o conteúdo específico da página que está sendo desenvolvida. Todo o conteúdo personalizado deve estar dentro deste bloco:
```django
{% block content %}
<!-- Seu conteúdo HTML específico aqui -->
{% endblock %}
```
 
#### Exemplo de uso

Aqui está um exemplo básico de como iniciar uma nova página que utiliza o `base.html` como base:
```html
{% extends 'layouts/base.html' %}
{% load static %}

{% block content %}
<h1>Bem-vindo à Minha Nova Página</h1>
<p>Este é um exemplo de como usar a base de estilos configurada no base.html.</p>
{% endblock %}
```
