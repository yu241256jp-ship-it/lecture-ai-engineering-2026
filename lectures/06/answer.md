# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：[tool call] glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]： [tool call] fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
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
・MCP公式ドキュメントを fetch MCP を利用して調査した。
・VS Code公式ドキュメントを fetch MCP を利用して調査した。
・command(stdio)方式と url(http)方式の違い、設定場所、有効範囲を比較した。
- 結果：
・MCPサーバーには stdio(command) 方式と http(url) 方式があることを確認した。
・stdio方式はローカルでコマンドを実行して MCPサーバーを起動する方式である。
・http方式は公開されているMCPサーバーへURLで接続する方式である。
・VS Codeでは「MCP: Add Server」や「Chat: Open Customizations」からサーバーを追加できる。
・設定の有効範囲として、ユーザー全体で利用する Global 設定と、プロジェクト単位で利用する Workspace 設定（.mcp.json）があることを確認した。
・今回の演習では glossary と fetch が command方式、AWS MCP が url方式だった。
- 気づき・疑問：
・MCPサーバーの接続方法は異なるが、どちらもLLMへツールを提供するという目的は同じだった。
・VS Codeでは設定画面から簡単にMCPサーバーを追加できることが分かった。
・MCPによって外部サービスやローカルツールを統一的に利用できる仕組みが便利だと感じた。
