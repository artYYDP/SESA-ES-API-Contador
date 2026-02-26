# SESA-ES-API-Contador

Uma API simples e leve destinada a contabilizar cliques em links dos painéis
disponibilizados na página dos painéis da **SESA-ES**.

O serviço foi pensado para coletar informações estratégicas que auxiliem o
marketing e o próprio controle da secretaria, permitindo entender quais são os
painéis mais visitados e quando o fazem. Os dados são enviados em tempo real
quando o usuário clica, e também podem ser obtidos em um formato consolidado para
análises diárias.

---

## Funcionalidades principais

- **Registrar origem do clique**: cada clique em link dos painéis é enviado para
	a API, informando a origem (qual painel) e outros metadados mínimos.
- **Coletar histórico de cliques**: um endpoint permite subir um lote de dados
	que representa todos os cliques de um dia anterior (`D-1`), possibilitando
	relatórios e atualizações em massa.

Essa divisão simplifica a integração com o front-end (envio a cada clique) e
garante que a base de dados possa ser atualizada por meio de um fluxo diário de
dados já tratados.

## Endpoints

> A aplicação roda a partir de `app.py` (Flask/FastAPI dependendo da implementação). Abaixo estão os
> caminhos esperados, mas confira o código-fonte para detalhes de parâmetros e
> formato de dados.

1. `POST /click` – contabiliza um clique individual.
	 - **Body**: JSON contendo pelo menos `origin` (painel) e `timestamp`.
	 - Exemplo:

		 ```json
		 {
			  "origin": "painel_home",
			  "clicked_at": "2026-02-25T14:32:00Z"
		 }
		 ```

2. `POST /bulk` – recebe informações de todos os cliques de um dia anterior.
	 - **Body**: array de objetos com informações de cada clique.
	 - Usado para atualização diária de `D-1`.

Outros endpoints podem ser adicionados conforme a evolução do projeto.

## Como contribuir / executar localmente

1. Clone o repositório:

	```bash
	 git clone https://github.com/artYYDP/SESA-ES-API-Contador.git
	 cd SESA-ES-API-Contador
	 ```

2. Crie e ative um ambiente virtual Python (recomendado):

	 ```bash
	 python -m venv venv
	 source venv/Scripts/activate   # Windows
	 ```

3. Instale as dependências:

	 ```bash
	 pip install -r requirements.txt
	 ```

4. Execute a aplicação:

	 ```bash
	 python app.py
	 ```

> ⚠️ Ajuste as variáveis de ambiente/configuração de banco conforme sua
> implementação.

## Exemplos de uso

```bash
# Envia um clique único
curl -X POST http://localhost:5000/click \
	-H 'Content-Type: application/json' \
	-d '{"origin":"painel_geral","clicked_at":"2026-02-25T14:32:00Z"}'

# Atualiza com lote diário
curl -X POST http://localhost:5000/bulk \
	-H 'Content-Type: application/json' \
	-d '[{"origin":"painel_geral","clicked_at":"2026-02-25T14:32:00Z"}, ...]'
```

## Objetivo e visão

O propósito desta API é fornecer métricas simples e confiáveis que apoiem a
tomada de decisões sobre quais painéis são mais relevantes para o público da
SESA-ES. Com registros granulares e a capacidade de consolidar dados por dia, as
informações podem ser integradas a dashboards e relatórios de marketing.

O projeto está aberto para melhorias, como autenticação, front-end de
visualização, exportação de relatórios e análise de tendências.

## Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
<!-- Fim do README -->