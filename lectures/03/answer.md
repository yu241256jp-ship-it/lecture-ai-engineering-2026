# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
   第1回の素のLLMと比べて、エージェントは用語集を検索してから回答していた。
  「3レベル」についても講座の内容に基づいて説明できていた。
- `--trace` で見えたツール呼び出し（ツール名と引数）：
   [tool call] search_glossary({'query': 'LoRA'})
   [tool call] search_glossary({'query': 'QLoRA'}) 

- 1つの質問での LLM 呼び出し回数（`requests`）：
   requests=2
- 追加したツールと、docstring に書いた説明：

## 宿題

- 取り組んだレベル：発展
- やったこと：
発展(a)に取り組んだ。
演習で使用した INSTRUCTIONS と既存ツールを利用し、Google ADK でエージェントを作成した。
adk_agent/glossary_agent/agent.py を作成し、search_glossary と get_lecture_summary を ADK の Agent に登録した。
adk run でエージェントを起動し、演習と同じ質問を実行した。
- 結果：
「LoRAとQLoRAの違いは？」という質問に対して、Pydantic AI版とほぼ同じ内容を回答できた。
「AIE2026の講座の宿題にある3レベルとは何ですか？」という質問にも正しく回答できた。
INSTRUCTIONS の内容が反映され、回答の最後に理解度確認クイズが出力された。
ADK版は Agent の定義がシンプルで、少ないコード量で同様のエージェントを構築できた。
一方で、Pydantic AI の --trace のようにツール呼び出しを簡単に確認する機能は確認できなかった。
- 気づき・疑問：
同じツールと指示を利用すれば、フレームワークが変わっても似た振る舞いのエージェントを作れることが分かった。
Pydantic AI はツール呼び出しや実行過程の確認がしやすいと感じた。
ADK はエージェント定義が簡潔で分かりやすかった。
フレームワークによる違いよりも、指示（INSTRUCTIONS）やツール設計の影響が大きいと感じた。