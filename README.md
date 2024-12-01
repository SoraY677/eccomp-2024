<div align="center">

# 2024 年 🧭 進化計算コンペティション <br/> セルフリゾルバ

公式サイト: https://opthub.ai/ja/competitions/eccomp2024

</div>

## 🔧 開発環境

### 環境

- [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)

### コマンド

#### 環境変数の設定

```bash
python ./_tool/copy.py .template.env .env
```

<details>

<summary>環境変数の設定項目一覧</summary>

|           変数名           |          概要           |                           関連リンク                            |
| :------------------------: | :---------------------: | :-------------------------------------------------------------: |
|       ECCOMP_API_KEY       |   OPTHUB の API キー    |                                                                 |
| SINGLE_OBJECTIVE_1_API_KEY | 単目的部門１の API キー | https://opthub.ai/ja/competitions/eccomp2024/single-objective-1 |
| SINGLE_OBJECTIVE_2_API_KEY | 単目的部門２の API キー | https://opthub.ai/ja/competitions/eccomp2024/single-objective-2 |
| SINGLE_OBJECTIVE_3_API_KEY | 単目的部門３の API キー | https://opthub.ai/ja/competitions/eccomp2024/single-objective-3 |
| MULTI_OBJECTIVE_1_API_KEY  | 多目的部門１の API キー | https://opthub.ai/ja/competitions/eccomp2024/multi-objective-1  |
| MULTI_OBJECTIVE_2_API_KEY  | 多目的部門２の API キー | https://opthub.ai/ja/competitions/eccomp2024/multi-objective-2  |
| MULTI_OBJECTIVE_3_API_KEY  | 多目的部門３の API キー | https://opthub.ai/ja/competitions/eccomp2024/multi-objective-3  |

</details>

#### メイン実行

```bash
python ./src/main.py
```

#### その他

```bash
# コードフォーマット
yapf -i --recursive .
```

## 📕 ドキュメント一覧

- [問題](https://opthub.ai/ja/problems/number-place)
- [コンペティションページ](https://opthub.ai/ja/competitions/eccomp2024)
- [自作ドキュメント](./doc)

## 🌲 構成・役割

```

eccomp-2024/
  ├ src/ - メインのソースコード類
  ├ analytics/ - データ分析ログ等
  ├ doc/ - ドキュメント一覧
  ├ .template.env - 環境変数テンプレートファイル

```
