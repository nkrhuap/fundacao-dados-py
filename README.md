Abaixo estão cinco desafios concebidos sob a perspectiva de problemas reais de infraestrutura e engenharia de dados que preenchem esse repo. Eles exigem apenas os conceitos fundamentais (tipos, modo interativo, variáveis/constantes, conversão e I/O), mas forçam a mentalidade de resiliência e controle de fluxo.

---

#### Desafio 1: Inspeção de Estado e Tipagem no Modo Interativo (REPL)
* **Contexto de Mercado:** Durante a depuração de incidentes em nós de processamento ou contêineres, o engenheiro muitas vezes não tem acesso a uma IDE gráfica. O diagnóstico rápido de payloads corrompidos é feito diretamente no REPL do Python via terminal.
* **Objetivo:** Explorar os mecanismos de introspecção nativos do CPython para dissecar a anatomia de variáveis de diferentes tipos.
* **Requisitos:**
  * Inicie uma sessão interativa no terminal (`python`).
  * Crie variáveis simulando registros de uma tabela: um identificador textual, uma contagem inteira, um valor monetário e um indicador booleano.
  * Utilize as funções nativas de introspecção (`type()`, `id()`, `dir()`) para inspecionar cada elemento.
  * Compare a identidade de memória (`id()`) entre dois inteiros pequenos iguais e, em seguida, entre dois números inteiros muito grandes (acima de $10^6$).
* **Critério de Conclusão:** Explicar conceitualmente por que inteiros pequenos compartilham referências de memória no CPython (mecanismo de *interning*) e por que a verificação de igualdade de valor (`==`) difere da identidade de objeto (`is`).

---

#### Desafio 2: Ingestão de Telemetria e *Cast* Explícito de Sensores
* **Contexto de Mercado:** Sensores de IoT e agentes de monitoramento emitem métricas em formatos brutos de texto. Um coletor de métricas precisa normalizar essas informações para os tipos primitivos corretos antes de alimentar um banco de dados analítico.
* **Objetivo:** Construir um script de parsing básico que receba entradas manuais via `input()` e faça a conversão controlada para os tipos adequados.
* **Requisitos:**
  * O script deve solicitar via terminal: `id_dispositivo` (texto), `temperatura_lida` (número com casas decimais), `ciclos_executados` (número inteiro) e `sensor_ativo` (texto representando booleano, ex: `"true"` ou `"false"`).
  * Realize a conversão explícita de cada variável para o seu tipo canônico (`str`, `float`, `int`, `bool`).
  * A conversão booleana deve tratar explicitamente a entrada de texto, garantindo que `"false"` ou `"False"` resulte no booleano `False` e `"true"` ou `"True"` resulte em `True`.
* **Critério de Conclusão:** O programa deve imprimir na tela o tipo primitivo de cada variável após a conversão, provando que nenhum tipo foi preservado como `str` por omissão.

---

#### Desafio 3: Contrato de Configuração e Constantes de Pipeline
* **Contexto de Mercado:** Pipelines de dados não toleram "números mágicos" ou reatribuições acidentais de estado. Parâmetros como limites de lote (batch size), tempo limite de conexão e prefixos de ambiente devem seguir contratos rígidos de nomenclatura para evitar efeitos colaterais em execução concorrente.
* **Objetivo:** Estruturar um cabeçalho de script definindo configurações operacionais imutáveis em contraste com variáveis de estado mutável.
* **Requisitos:**
  * Defina as constantes de configuração do pipeline de acordo com a convenção da PEP 8 (caixa alta com underscores): limite de registros por lote, versão do esquema e diretório de destino.
  * Inicialize variáveis de rastreamento de execução: total de registros processados, tempo acumulado e flag de encerramento.
  * Simule a progressão de três "lotes" de dados apenas alterando as variáveis de estado (acumulando valores) e mantendo as constantes estritamente intocadas.
* **Critério de Conclusão:** O código deve demonstrar clareza semântica: qualquer desenvolvedor que ler o arquivo deve distinguir imediatamente o que é configuração de infraestrutura (estática) e o que é estado transitório de memória (dinâmico).

---

#### Desafio 4: Formatação de Logs Estruturados para Agentes de Coleta
* **Contexto de Mercado:** Em produção, a saída padrão (`stdout`) de um script não é lida por humanos em tempo real, mas ingerida por agentes de log (como Fluentbit, Logstash ou coletores de cloud) que exigem formatos padronizados com delimitadores claros para indexação.
* **Objetivo:** Utilizar funções de saída (`print()`) e interpolação de strings (*f-strings*) para produzir saídas padronizadas sem bibliotecas externas.
* **Requisitos:**
  * Capture entradas de execução via `input()`: nível de severidade (ex: `INFO`, `WARNING`), nome da tabela e quantidade de linhas rejeitadas.
  * Formate a saída de log utilizando `f-strings` com alinhamento de texto fixo e formatação numérica explícita (ex: zeros à esquerda para contadores ou casas decimais controladas).
  * Utilize os argumentos nativos da função `print()` (especificamente `sep` e `end`) para criar registros no padrão delimitado por tubos (`|`) ou em formato chave-valor.
* **Critério de Conclusão:** A saída no terminal deve seguir uma estrutura tabular consistente, mesmo que os valores inseridos variem em comprimento de caracteres.

---

#### Desafio 5: Aritmética Escalar e o Dilema da Precisão Monetária
* **Contexto de Mercado:** Cálculos de agregação em pipelines contábeis não podem sofrer com dispersão de dízimas flutuantes. Uma falha de precisão de frações de centavo acumulada em milhões de linhas gera passivos de auditoria e relatórios financeiros inconsistentes.
* **Objetivo:** Resolver o problema da imprecisão de tipos de ponto flutuante utilizando exclusivamente aritmética de inteiros (técnica de escala).
* **Requisitos:**
  * Receba via `input()` um valor monetário expresso como número decimal (ex: `"125.75"`).
  * Converta a entrada sem utilizar `float` diretamente no armazenamento principal da métrica, transformando o valor para sua representação em centavos inteiros (`int`).
  * Realize uma operação de acréscimo de taxa fixa (ex: aplicar 150 centavos de taxa) e calcule uma partição inteira e o resto da divisão para reverter a saída para o formato legível `reais,centavos`.
  * Imprima o resultado final formatado, comparando-o conceitualmente com o que aconteceria se a mesma operação acumulasse divisões sucessivas em `float`.
* **Critério de Conclusão:** Demonstrar como manipular grandezas decimais discretas mantendo determinismo matemático absoluto usando apenas os tipos primitivos `int` e `str`.

