# Shift-JIS -> UTF-8 変換

## 概要

- `sjis` フォルダ内の　 Shift-JIS ファイルを UTF-8 に変換して `utf8` フォルダに出力する

## 使い方

- sjis フォルダ内に対象ファイルを置く
- utf8 フォルダを作る
- 実行する

```
py toutf8.py
```

## 注意

- 元ファイルと同じファイル名で出力する
- エラーチェック等してないので下記はエラー終了する
  - sjis フォルダがない
  - sjis フォルダ内にフォルダがある
  - utf8 フォルダがない
