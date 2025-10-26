# AtCoder / 競技プログラミング学習用リポジトリ

このリポジトリは、AtCoder を中心とした競技プログラミングの学習・練習用です。問題ごとにディレクトリを分け、入出力に従うシンプルな `main.py` を配置します。実行時間・メモリの計測も行い、実装の改善に活かします。

## 目的
- 問題を解いて解法を蓄積する（WA/RE の学びも残す）
- 実装力（データ構造・アルゴリズム・高速化）を鍛える
- 実行時間・メモリを意識した実装を習慣化する

## 開発環境
- 言語: Python `3.14`
- パッケージ管理: `uv`（`uv.lock` を同梱）
- Dev Container: `.devcontainer` を用意（VS Code 推奨）

## セットアップ
- Dev Container 利用（推奨）
  1. VS Code で「Reopen in Container」
  2. 自動で Python/uv が利用可能になります
- ローカル実行
  1. Python 3.14 を用意
  2. `uv` をインストール（https://docs.astral.sh/uv/）
  3. 必要に応じて仮想環境を作成し有効化
  4. 依存があれば `uv sync`（現状 `dependencies` は空）

## ディレクトリ構成
```
.
├─ tasks/                 # 問題ごとのディレクトリ
│  └─ <problem-id>/
│     ├─ inputs           # 入力例テキストファイル格納
│     ├─ README.md        # 問題文・メモ
│     └─ main.py          # 解答（標準入出力）
├─ .devcontainer/         # Dev Container 設定
├─ .github/               # Dependabot 等
├─ .venv/                 # 任意の仮想環境
├─ pyproject.toml         # プロジェクト設定（requires-python など）
├─ uv.lock                # uv ロックファイル
└─ README.md              # このファイル
```

## 実行方法（例）
- 標準入力を必要とする場合:
  - 手元で入力: `python tasks/dp-example-3/main.py` → 入力を貼り付け
  - ファイルから: `python tasks/dp-example-3/main.py < tasks/dp-example-3/inputs/inputs_1.txt`

## 計測（実行時間・メモリ）
- 簡易: シェルの `/usr/bin/time -v` を使う
  - 例: `/usr/bin/time -v python tasks/dp-example-3/main.py < input.txt`
- Python 内で計測（スニペット）:
  ```python
  # 計測用スニペット（必要に応じて main.py 冒頭/末尾に挿入）
  import time, tracemalloc
  tracemalloc.start()
  t0 = time.perf_counter()

  # ... ここに処理 ...

  elapsed = time.perf_counter() - t0
  current, peak = tracemalloc.get_traced_memory()
  tracemalloc.stop()
  print(f"elapsed: {elapsed*1000:.3f} ms")
  print(f"peak memory: {peak/1024:.1f} KiB")
  ```

## 新しい問題の追加手順
1. `tasks/<problem-name>/` を作成
2. `README.md` に問題文や気づき・解法メモを記載
3. `main.py` に解答実装（標準入出力）
4. 必要なら入力例ファイルや計測スクリプトを配置

## コーディング方針（推奨）
- 入出力: `sys.stdin.readline` を用いて高速化
- 構成: `solve()` を定義し、`if __name__ == "__main__": solve()` の形に統一
- 型: 可能なら型ヒントを付与
- 計測: ボトルネック見直し時のみスニペットを有効化

## CI / メンテナンス
- Dependabot による Dev Container 等の定期更新を有効化
- 追加の CI（lint/format/test）は必要に応じて検討

## 参考リンク
- AtCoder: https://atcoder.jp/
