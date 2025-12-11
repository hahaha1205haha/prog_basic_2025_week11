# 第10週 課題解答と第11週の演習のための 共有リポジトリ

● main_report.py （第10週の課題模範プログラム （Atsumi2025_airtemp_7days.csv  → data_day1.pyへ変換して動かす:方法2） 
● make_data_day1_from_csv.py 
2025年温海カブ圃場の環境データ（Atsumi2025_airtemp_7days.csv）から1日分の温度データを取り出し、data_day1.pyへ変換するスクリプト。

Atsumi2025_airtemp_7days.csv
から （2025-08-24 の行だけ読む）          
temps = [24.3, 23.8, 22.9, ...]   ← 24時間分
          　↓ 
data_day1.py を自動生成

● Atsumi2025_airtemp_7days.csv （前回と同じ）

● main_starter.py (第10週の課題模範解答（CSVファイルを直接読み出す：方法3））
● main_advanced_solution.py （第9週で説明した課題が早く終わった学生向けの機能追加をしたバージョンの模範解答）
「連続してしきい値以上になった時間数（連続アラート）」 を数える関数を追加。
しきい値が 0〜60 の範囲外だった場合に警告を出す処理を追加。
