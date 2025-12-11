# Week10/11: Temperature Monitor — Advanced Model Answer
# 早く終わった学生向け：連続アラート時間 + しきい値バリデーション付き
#
# 実行方法:
#   python main_advanced_solution.py

from data_day1 import temperatures


def mean(nums):
    """リストの平均値を返す。空リストのときは None。"""
    if len(nums) == 0:
        return None
    total = 0.0
    for n in nums:
        total += n
    return total / len(nums)


def hottest_hour(nums):
    """
    最大値とそのインデックス(時間=0..23)をタプルで返す。
    空リストなら (None, None)。
    """
    if len(nums) == 0:
        return (None, None)

    max_val = nums[0]
    max_idx = 0
    for idx in range(1, len(nums)):
        if nums[idx] > max_val:
            max_val = nums[idx]
            max_idx = idx
    return (max_val, max_idx)


def count_alerts(nums, threshold):
    """threshold（しきい値）以上の時間数を数える。"""
    count = 0
    for t in nums:
        if t >= threshold:
            count += 1
    return count


def longest_alert_streak(nums, threshold):
    """
    しきい値以上が『連続』した最長時間数（個数）を求める。

    例:
        nums = [27, 28, 29, 27, 30, 31, 32, 26], threshold=28 のとき、
        28以上の部分は [28, 29], [30, 31, 32] → 最長ストリークは 3。
    """
    current = 0  # 現在連続中の長さ
    best = 0     # これまでで一番長かった長さ

    for t in nums:
        if t >= threshold:
            current += 1
            if current > best:
                best = current
        else:
            # 連続が切れるのでリセット
            current = 0

    return best


def validate_threshold(threshold):
    """
    しきい値が 0〜60℃ の範囲にあるかチェックする。
    正常なら True、異常なら False を返す。
    """
    if threshold < 0 or threshold > 60:
        print("エラー: しきい値は 0〜60℃ の範囲にしてください。")
        print(f"現在のしきい値: {threshold}")
        return False
    return True


def make_report_line(day_label, nums, threshold):
    """
    1行のレポート文字列を作成する。
    例:
      "Day1 | avg=23.5°C | max=30.2°C at h=14 | alerts(>=28)=5"
    """
    avg = mean(nums)
    mx, h = hottest_hour(nums)
    alerts = count_alerts(nums, threshold)
    # 平均と最大値は小数1桁で表示
    return (
        f"{day_label} | avg={avg:.1f}°C | "
        f"max={mx:.1f}°C at h={h} | alerts(>={threshold})={alerts}"
    )


if __name__ == "__main__":
    # しきい値は自由に変えてよい（発展で学生にいじらせる）
    THRESHOLD = 28.0

    # ① まずはしきい値のバリデーション
    if not validate_threshold(THRESHOLD):
        # 異常値の場合はここで終了（本格的には再入力処理なども可）
        raise SystemExit("プログラムを終了します。")

    print("== Advanced Temperature Monitor ==")
    print("データ件数:", len(temperatures))

    avg = mean(temperatures)
    mx, h = hottest_hour(temperatures)
    alerts = count_alerts(temperatures, THRESHOLD)
    streak = longest_alert_streak(temperatures, THRESHOLD)

    print("平均:", avg)
    print("最大(値, 時間):", (mx, h))
    print(f"しきい値以上の時間数(>= {THRESHOLD}°C):", alerts)
    print(f"しきい値以上が連続した最長時間数:", streak)

    print()
    print("レポート行:")
    print(make_report_line("Day1", temperatures, THRESHOLD))
