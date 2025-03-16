def müşteri_destek_yönlendirme(müşteriler, temsilciler, kapasite, sehirler):
    n = len(müşteriler)
    m = len(temsilciler)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    rep_şehir_map = {i: set() for i in range(m)}
    for i, (rep_id, rep_şehir) in enumerate(temsilciler):
        rep_şehir_map[i] = set(rep_şehir)

    allocation = [-1] * n
    for i in range(1, n + 1):
        müşteri_id, müşteri_şehir = müşteriler[i - 1]

        en_iyi_rep = -1
        for j in range(1, m + 1):
            if kapasite[j - 1] > 0 and müşteri_şehir in rep_şehir_map[j - 1]:
                if dp[i][j] < dp[i - 1][j - 1] + 1:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    en_iyi_rep = j - 1
                    kapasite[j - 1] -= 1
                    allocation[i - 1] = en_iyi_rep
                    break

    for i in range(n):
        müşteri_id, müşteri_şehir = müşteriler[i]
        atanmış_rep = f"Temsilci {allocation[i] + 1}" if allocation[i] != -1 else None
        if atanmış_rep:
            print(f"Müşteri {müşteri_id} ({müşteri_şehir}) -> {atanmış_rep}")
        else:
            print(f"Müşteri {müşteri_id} ({müşteri_şehir}) için uygun temsilci bulunamadı.")

def pazarlama_kampanya_seçimi(kampanyalar, bütçe):
    n = len(kampanyalar)
    dp = [0] * (bütçe + 1)
    seçilen_kampanyalar = []

    for i in range(n):
        maliyet, getiri = kampanyalar[i]
        for b in range(bütçe, maliyet - 1, -1):
            if dp[b] < dp[b - maliyet] + getiri:
                dp[b] = dp[b - maliyet] + getiri

    kalan_bütçe = bütçe
    while kalan_bütçe > 0:
        for i in range(n):
            maliyet, getiri = kampanyalar[i]
            if kalan_bütçe >= maliyet and dp[kalan_bütçe] == dp[kalan_bütçe - maliyet] + getiri:
                seçilen_kampanyalar.append(kampanyalar[i])
                kalan_bütçe -= maliyet
                break

    print("\nSeçilen Pazarlama Kampanyaları:")
    for kampanya in seçilen_kampanyalar:
        print(f"Kampanya Maliyeti: {kampanya[0]}, Getiri: {kampanya[1]}")

    toplam_roi = dp[bütçe]
    print(f"\nToplam ROI: {toplam_roi}")

    return toplam_roi

müşteriler = [(1, 'Istanbul'), (2, 'Ankara'), (3, 'Istanbul'), (4, 'Izmir'),
              (5, 'Istanbul')]  # Müşteri talebi
temsilciler = [('Temsilci 1', ['Istanbul', 'Ankara']), ('Temsilci 2', ['Izmir']),
               ('Temsilci 3', ['Ankara', 'Istanbul'])]  # Temsilciler
kapasite = [2, 1, 3]  # Temsilcilerin kapasiteleri

kampanyalar = [(100, 200), (200, 350), (150, 250), (80, 180), (120, 220), (300, 500)]
bütçe = 400

print("Müşteri Yönlendirmeleri:")
müşteri_destek_yönlendirme(müşteriler, temsilciler, kapasite, ['Istanbul', 'Ankara', 'Izmir'])

pazarlama_kampanya_seçimi(kampanyalar, bütçe)