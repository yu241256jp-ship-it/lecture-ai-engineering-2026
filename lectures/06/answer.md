# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：[tool call] glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：[tool call] fetch_fetch({'url': 'https://modelcontextprotocol.io/'}
- STEP 4 の [tool call]：[tool call] aws_aws___search_documentation({'search_phrase': 'Amazon S3 バージョニング 概要'})
- 気づき・疑問：
・glossary MCP を追加すると、講座独自の用語を検索できるようになった。
・fetch MCP を使うことで Web サイトの内容を取得して要約できることが分かった。
・AWS MCP を使うことで AWS 公式ドキュメントを検索できた。
・MCP サーバーを追加するだけで利用できるツールが増える仕組みが興味深かった。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：発展
- やったこと：
・VS Code における MCP サーバーの設定方法を調査した。
・command を利用するローカル MCP サーバーと、url を利用するリモート MCP サーバーの違いを調べた。
・今回の演習で利用した glossary、fetch、AWS の設定方法と比較した。
- 結果：
・command を利用する場合はローカルで MCP サーバーのプロセスを起動する。
・url を利用する場合は公開されている MCP サーバーへ接続する。
・VS Code ではユーザー単位またはワークスペース単位で MCP サーバーを設定できる。
・今回の演習で利用した app/mcp_servers.json も同じ考え方で MCP サーバーを管理していた
- 気づき・疑問：
・MCP によって LLM が外部ツールを利用できる仕組みを実際に体験できた。
・同じ MCP でもローカル実行とリモート接続の両方に対応していることが分かった。
・AWS MCP では公式ドキュメント検索が利用でき、用途に応じてさまざまなサーバーを組み合わせられると感じた。
