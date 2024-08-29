# Guia de utilização de componentes de Interface Reutilizáveis

Este guia aborda a utilização e personalização de componentes de interface reutilizáveis na nossa aplicação, com ênfase na extensão da base de estilos, na estrutura das páginas de registro e login, e na criação e atualização da sidebar. Seguindo essas orientações, garantimos uma experiência de usuário consistente e coerente em toda a aplicação

## Introdução

A base de estilos, definida no arquivo `base.html`, é o alicerce da estrutura de todas as páginas da aplicação. Este arquivo já inclui a importação do arquivo CSS do **Bootstrap**, contém todas as configurações essenciais de estilo e elementos comuns necessários para garantir a consistência visual e funcionalidade ao longo do projeto.

Além das definições próprias, pode-se utilizar os componentes disponibilizados na biblioteca do Bootstrap, o que permite uma construção rápida e eficiente de elementos da interface. Adicionalmente, a aplicação faz uso do **Chart.js**, uma poderosa biblioteca para a ciração de gráficos dinâmicos e interativos, facilitando a visualização de dados.

## Instruções para extensão da base de estilos

Para iniciar o desenvolvimento de qualquer página, utilize a extensão do `base.html` em seu template específico. Este procedimento assegura que todas as definições de estilo e configurações globais sejam herdadas, mantendo a uniformidade do design e o comportamento esperado dos componentes.

### Como utilizar:

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
```django
{% extends 'layouts/base.html' %}
{% load static %}

{% block content %}
<h1>Bem-vindo à Minha Nova Página</h1>
<p>Este é um exemplo de como usar a base de estilos configurada no base.html.</p>
{% endblock %}
```
## Estrutura das Páginas de Registro e Login

No contexto deste projeto, a maioria das páginas se baseia no template `base.html` para manter uma consistência visual e estrutural. No entanto, as páginas de registro e login são **exceções** a essa regra. Elas não utilizam esse template, devido à necessidade de uma interface mais simplificada, limpa e direta, que facilita o foco do usuário na tarefa de autenticação. Além de não precisar das ferramentes disponibilizadas na base de layout. 

### Explicação das configurações de URL e View

As páginas de registro e login já estão prontas e organizadas na pasta `accounts`. Para que essas páginas sejam acessíveis através do navegador, é necessário configurar as rotas e as views que irão processas as requisições HTTP conforme a estrutura do sua pasta de aplicação. Abaixo segue um modelo de configuração.

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

### Estrutura da Sidebar

A sidebar é gerada dinamicamente usando JavaScript com base em uma lista de tópicos. Cada tópico é representado por um objeto que contém informações como o link, ícone e o nome da página. 

### Adicionando Novos Itens

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

## Utilização do Chart.js na aplicação

Para utilizar o Chart.js na aplicação, é necessário importar o script diretamente no arquivo HTML onde será modelado e utilizado os gráficos.

### Como importar

No arquivo HTML da página, adicione o seguinte código:

```django
{% block scripts %}
    <script src="{% static 'js/plugins/chartjs.min.js' %}"></script>
{% endblock scripts %}
```

Ao adicionar este bloco no arquivo HTML, o Chart.js será carregado somente quando necessário, garantindo que os gráficos sejam renderizados corretamente e otimizando o desempenho da aplicação.

## Estrutura de pastas

Essa estrutura foi projetada para armazenar componentes reutilizáveis de maneira que sejam facilmente acessíveis a todos os membros da equipe. Com todos os templates organizados dentro dapasta `design`, a equipe pode rapidamente localizar e utilizar os arquivos necessários para o desenvolvimento de novas funcionalidades ou atualizações de existentes.

```bash
<RAIZ_DA_BIBLIOTECA>                      # Diretório raiz da biblioteca
   |
   |-- design/                            # Diretório principal para recursos de design
   |   |
   |   |-- templates/                     # Diretório raiz dos templates 
   |   |          
   |   |-- accounts/                      # Diretório para páginas de autenticação
   |   |    |-- login.html                # Página de Login (Entrar)
   |   |    |-- register.html             # Página de Registro (Cadastrar-se)
   |   |
   |   |-- includes/                      # Diretório de componentes reutilizáveis
   |   |    |-- sidebar.html              # Componente da Barra Lateral (Sidebar)
   |   |    |-- navigation.html           # Componente da Barra de Navegação
   |   |
   |   |-- layouts/                       # Diretório de layouts de página
   |   |    |-- base.html                 # Template base (Masterpage) para páginas gerais
   |   |
   |   |-- pages/                         # Diretório para páginas específicas
   |        |-- index.html                # Página do Dashboard (Painel de Controle)
   |        |-- *.html                    # Todas as outras páginas adicionais
   |    
   |-- ************************************************************************

```

## Referências
[1] "Bootstrap v5.0 Documentação". Disponível em: https://getbootstrap.com/docs/5.0/getting-started/introduction/

[2] "Chart.js Documentação". Disponível em: https://www.chartjs.org/docs/latest/

[3] "Bootstrap Icons". Disponível em: https://icons.getbootstrap.com/

---

Este guia foi formatado para fornecer uma estrutura calra e coerente para o desenvolvimento e manunteção de componentes reutilizáveis dentro da sua aplicação.