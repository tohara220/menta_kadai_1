import os
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

SOURCE_CSV_PATH = "source.csv"

# 検索ソース
DEFAULT_CHARACTERS = ["ぜんいつ","たんじろう","ねずこ","いのすけ"]

"""
処理は細かく関数化する
関数化のポイント:関数内には具体的な内容を記述せずに引数を持たせる
この処理でしか使えなくなってしまうような記述は極力避けて、
別のプロジェクトに使い回す前提で記述する。
"""

def read_source(csv_path: str):
    """
    sourceをCSVから読み込む
    関数の基本は、引数（今回はcsv_path）→処理（関数の中身）→戻り値（return）
    """
    # ファイルが存在しない場合は、初期値で新規作成
    if not os.path.exists(csv_path):
        print(f"csv_path:{csv_path}が存在しません。新規作成します。")
        write_source(csv_path, DEFAULT_CHARACTERS)
    # ファイルを読み込み
    with open(csv_path, mode="r", encoding="utf-8_sig")as f:
        return f.read().splitlines() # readでファイル読み込み、splitlinesで1行ずつに分解してlistとして返す
    
def write_source(csv_path: str, source: list):
    """
    sourceをcsvに書き込む
    """
    with open(csv_path, mode="w", encoding="utf-8_sig") as f:
        f.write("\n".join(source)) # listを改行（\n）で連結してファイルに書き込む
    
### 検索ツール
def search():
    """
    mainとなる検索処理
    """
    # sourceをcsvから読み込む
    source = read_source(SOURCE_CSV_PATH)
    # while Trueにすると無限に繰り返す
    while True:
        # ユーザー入力
        word =input("鬼滅の登場人物の名前を入力してください >>> ")
        # 検索
        if word in source:
            print(f"「{word}」は登録されています。")
        else:
            print(f"「{word}」は未登録です。")
            # 追加
            is_add = input(f"{word}を追加登録しますか？ y:する n:しない>>")
            if is_add == "y":
                source.append(word)
                
        # sourceをcsvに書き込む
        write_source(SOURCE_CSV_PATH, source=source)

"""
実行時に呼び出したい関数を記述。
if __name__等の記述は提携文として覚える。
"""
if __name__ == "__main__":
    search()