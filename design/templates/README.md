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
## Estrutura das Páginas de Registro e Login

No contexto deste projeto, a maioria das páginas se baseia no template `base.html` para manter uma consistência visual e estrutural. No entanto, as páginas de registro e login são exceções a essa regra. Elas não utilizam esse template, devido à necessidade de uma interface mais simplificada, limpa e direta, que facilita o foco do usuário na tarefa de autenticação. Além de não precisar das ferramentes disponibilizadas na base de layout. 

#### Explicação das configurações de URL e View

As páginas de registro e login já estão prontas e organizadas na pasta `accounts`. Para que essas páginas sejam acessíveis através do navegador, é necessário configurar as rotas e as views que irão processas as requisições HTTP. Abaixo segue um modelo de configuração.

1. **Configurações das URLs (`urls.py`):**
```django
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
```
2. **Definição das Views (`views.py`):**
```django
from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')
```

## Criação e Atualização da Sidebar

A sidebar (barra lateral) é um componente essencial para a navegação do usuário na aplicação. Ela fornece uma visão geral das principais seções e páginas, além de atuar como uma rota de fuga, caso queira retornar a página principal.

#### Estrutura da Sidebar

A sidebar é gerada dinamicamente usando JavaScript com base em uma lista de tópicos. Cada tópico é representado por um objeto que contém informações como o link, ícone e o nome da página. 

#### Adicionando Novos Itens

Para adicionar novos itens à siderbar, siga estas etapas:

1. **Atualize o Array `topics`:**

Adicione um novo objeto ao array `topics` com as informações do novo item. **Certifique-se de preencher todos os campos:** o `link` para link da página, o `iconClass` para o ícone desejado, e o `page` para o nome da página que aparecerá na sidebar. Exemplo: 

```javascript
const topics = [
  { href: "nova-pagina.html", iconClass: "bi bi-newspaper", link: "#", page: "Nova pagina" } 
];
```

2. **Verifique a Biblioteca de Ícones:** 

Está sendo utilizado ícones da [Bootstrap Icons](https://icons.getbootstrap.com/), assegure-se que a classe do ícone (`iconClass`) esteja correta. 
