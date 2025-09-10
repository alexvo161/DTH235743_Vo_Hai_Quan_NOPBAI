'''
Giá trị các biến:

i1 = 2

i2 = 5

i3 = -3

d1 = 2.0

d2 = 5.0

d3 = -0.5

(a) i1 + (i2 * i3)

Tính trong ngoặc trước: i2 * i3 = 5 * (-3) = -15

Cộng i1: 2 + (-15) = -13

Kết quả: -13

(b) i1 * (i2 + i3)

Trong ngoặc: i2 + i3 = 5 + (-3) = 2

Nhân i1: 2 * 2 = 4

Kết quả: 4

(c) i1 / (i2 + i3)

Trong ngoặc: 5 + (-3) = 2

Phép chia nguyên số: 2 / 2 = 1.0 (phép chia / trong Python 3 trả về float)

Kết quả: 1.0

(d) i1 // (i2 + i3)

Trong ngoặc: 2

Phép chia lấy phần nguyên (floor division): 2 // 2 = 1

Kết quả: 1

(e) i1 / i2 + i3

Phép chia trước: 2 / 5 = 0.4 (float)

Cộng i3: 0.4 + (-3) = -2.6

Kết quả: -2.6

(f) i1 // i2 + i3

Phép chia lấy phần nguyên: 2 // 5 = 0 (2 chia 5 là 0 dư 2)

Cộng i3: 0 + (-3) = -3

Kết quả: -3

(g) 3 + 4 + 5 / 3

Phép chia trước: 5 / 3 ≈ 1.6667

Cộng 3 + 4 = 7

Tổng: 7 + 1.6667 = 8.6667

Kết quả: ~8.6667

(h) 3 + 4 + 5 // 3

Phép chia lấy phần nguyên: 5 // 3 = 1

Cộng 3 + 4 = 7

Tổng: 7 + 1 = 8

Kết quả: 8

(i) (3 + 4 + 5) / 3

Trong ngoặc: 3 + 4 + 5 = 12

Chia cho 3: 12 / 3 = 4.0

Kết quả: 4.0

(j) (3 + 4 + 5) // 3

Trong ngoặc: 12

Chia lấy phần nguyên: 12 // 3 = 4

Kết quả: 4

(k) d1 + (d2 * d3)

Trong ngoặc: 5.0 * (-0.5) = -2.5

Cộng: 2.0 + (-2.5) = -0.5

Kết quả: -0.5

(l) d1 + d2 * d3

Theo ưu tiên nhân trước: 5.0 * (-0.5) = -2.5

Cộng 2.0 + (-2.5) = -0.5

Kết quả: -0.5

(m) d1 / d2 - d3

Chia trước: 2.0 / 5.0 = 0.4

Trừ d3: 0.4 - (-0.5) = 0.4 + 0.5 = 0.9

Kết quả: 0.9

(n) d1 / (d2 - d3)

Trong ngoặc: 5.0 - (-0.5) = 5.5

Chia: 2.0 / 5.5 ≈ 0.3636

Kết quả: ~0.3636

(o) d1 + d2 + d3 / 3

Phép chia trước: -0.5 / 3 ≈ -0.1667

Cộng: 2.0 + 5.0 = 7.0

Tổng: 7.0 + (-0.1667) = 6.8333

Kết quả: ~6.8333

(p) (d1 + d2 + d3) / 3

Trong ngoặc: 2.0 + 5.0 + (-0.5) = 6.5

Chia: 6.5 / 3 ≈ 2.1667

Kết quả: ~2.1667

(q) d1 + d2 + (d3 / 3)

Trong ngoặc: -0.5 / 3 ≈ -0.1667

Cộng: 2.0 + 5.0 = 7.0

Tổng: 7.0 + (-0.1667) = 6.8333

Kết quả: ~6.8333

(r) 3 * (d1 + d2) * (d1 - d3)

Trong ngoặc đầu: 2.0 + 5.0 = 7.0

Trong ngoặc sau: 2.0 - (-0.5) = 2.5

Tính: 3 * 7.0 * 2.5 = 3 * 17.5 = 52.5

Kết quả: 52.5
'''