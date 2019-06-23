# FizzBuzz問題

     3の倍数の場合は「Fizz」、5の場合は「Buzz」、3の倍数かつ5の倍数は「FizzBuzz」と出力する。また、いずれでもない場合はその数を出力する。 

## 要件の分解
- 3の倍数の場合は「Fizz」と出力する
- 5の場合は「Buzz」と出力する
- 3の倍数かつ5の倍数は「FizzBuzz」と出力する
- いずれでもない場合はその数を出力する

## 満たす要件のToDo List
ユニットテストでTDD満たしたい要件
- [x] 入力された数字を文字列で出力する
  - [x] 1を入力した時に文字列で1出力する
    - [x] 失敗するテストを作成
    - [x] テストが通るように仮実装する
    - [x] リファクタリングして本実装する
- [x] 3の場合に「Fizz」と出力する
  - [x] 失敗するテストを作成
  - [x] テストが通るように仮実装する
  - [x] リファクタリングして本実装する
- [x] 5の場合に「Buzz」と出力する
  - [x] 失敗するテストを作成
  - [x] テストが通るように仮実装する
  - [x] リファクタリングして本実装する
- [x] refactor duplication and structure
- [x] 3の倍数かつ5の倍数には「FizzBuzz」と出力する
  - [x] 失敗するテストを作成
  - [x] テストが通るように仮実装する
  - [x] リファクタリングして本実装する

実装時に考えなくて良い
- [] 1からxxまで繰り返す
- [] 1から100まで繰り返す

# 実施ログ
- Readmeに要件を記載してToDoを分解
- 失敗するテストを追加
  - テストが正常に失敗してテスト自体は正常に動作することを確認