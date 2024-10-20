# 📚 Orquestrador BotCity - README

## ✨ Visão Geral

O **Orquestrador BotCity** é uma ferramenta poderosa que facilita a automação de bots, permitindo o gerenciamento centralizado de suas execuções, erros e alertas. Ele oferece uma interface amigável para monitorar e controlar as automações, proporcionando visibilidade total sobre o status das tarefas.

---

## 🔔 Seção de Alertas

Na seção de **Alertas**, é possível visualizar todos os eventos que merecem atenção durante a execução das automações. Cada alerta contém informações importantes como:

- **Automação**: Nome do bot que gerou o alerta (exemplo: Bot Fakturama).
- **Mensagem**: Descrição do alerta, que pode indicar o início de uma tarefa ou qualquer evento relevante.
- **ID da Tarefa**: Um número identificador exclusivo da tarefa relacionada.
- **Repositório**: O repositório no qual o bot está sendo executado (exemplo: equipe_linus).

![Exemplo de alerta](https://i.imgur.com/NhQ0EKX.png)

---

## ⚠️ Erros de Execução

Em caso de falha, a seção de erros fornece um relatório detalhado do problema, facilitando a análise e correção. Para cada erro registrado, o Orquestrador apresenta:

- **Linguagem**: A linguagem utilizada na automação (exemplo: Python).
- **Bot**: Nome do bot que gerou o erro.
- **Mensagem de erro**: Uma descrição detalhada do erro encontrado (exemplo: `Element not available. Cannot invoke click_relative`).
- **StackTrace**: Exibe a trilha completa do erro para facilitar o diagnóstico.

![Exemplo de erro](https://i.imgur.com/XGkCqhP.png)

---

## 📝 Fila de Tarefas

A seção **Fila de Tarefas** mostra o estado atual de execução de cada tarefa automatizada. Aqui você pode verificar informações como:

- **State**: Estado da tarefa (exemplo: Finalizado).
- **Itens Processados e Falhas**: Número de itens que foram processados com sucesso e aqueles que falharam.
- **Tempo de Execução**: A duração total da execução da tarefa.
- **Runner**: O nome do ambiente ou máquina que está executando o bot (exemplo: runner-vespertino-01).

Essa visualização proporciona uma visão geral da eficiência e da completude de cada execução automatizada.

![Exemplo de fila de tarefa](https://i.imgur.com/sbUmK5Q.png)

---

## 🧾 **Logs de Execução**

A seção **Logs de Execução** permite acompanhar o histórico detalhado das atividades realizadas por cada bot durante a automação. Essa funcionalidade é essencial para rastrear o desempenho e identificar possíveis gargalos ou erros. Nos logs de execução, você pode verificar informações como:

- **Data e Hora**: O registro exato de quando a execução ocorreu.
- **Ação Executada**: Descrição da atividade realizada pelo bot em cada etapa (exemplo: 'Clique no botão "Enviar"').
- **Status da Ação**: O resultado de cada ação (exemplo: Sucesso ou Falha).
- **Mensagem de Retorno**: Informações adicionais ou mensagens de erro geradas durante a execução (exemplo: `Elemento não encontrado`).
- **Duração da Ação**: O tempo gasto para completar cada etapa individualmente.

Essa visualização oferece uma visão detalhada do comportamento do bot durante a execução e facilita o diagnóstico de problemas ou a otimização de tarefas.

![Exemplo de logs de execução](https://i.imgur.com/q7qVN0X.png)

---

## 🚀 Funcionalidades Principais

1. **Gestão de Alertas**: Acompanhe eventos importantes, como início e término de tarefas ou erros críticos.
2. **Monitoramento de Erros**: Tenha uma visão detalhada dos erros ocorridos durante a execução dos bots, incluindo o log completo do erro.
3. **Fila de Tarefas**: Monitore o progresso de cada automação e visualize o estado de finalização.
4. **Automação Escalável**: Facilita a orquestração de múltiplos bots e execuções simultâneas, garantindo uma operação fluida e eficiente.

---

## 🎯 Conclusão

O **Orquestrador BotCity** é uma ferramenta essencial para quem busca eficiência e controle em suas automações. Ele fornece uma interface clara e organizada, permitindo que os desenvolvedores acompanhem, identifiquem e corrijam problemas rapidamente, além de garantir que as execuções sejam realizadas conforme o esperado.
