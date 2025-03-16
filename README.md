# Müşteri İlişkileri Yönetimi
Bu proje, müşteri destek yönlendirmesi ve pazarlama kampanyası seçimi için dinamik programlama yöntemini kullanmaktadır. Proje iki ana bileşenden oluşmaktadır:

1.Müşteri Destek Yönlendirme

Müşteri destek yönlendirme fonksiyonunun amacı her müşteriyi o müşterinin bulunduğu şehirde hizmet verebilecek ve kapasitesi yeterli olan bir temsilciye yönlendirmektir. Müşteri destek yönlendirmesi fonksiyonunda dinamik programlama kullanılmıştır. Dinamik programlama burada daha büyük ve karmaşık bir problemi çözmek için alt problemleri çözerek çözümün adım adım ilerlemesini sağlar. Yani her müşteri için yapılan temsilci seçiminde önceki müşteri seçimlerinin çözüm sonuçları kullanılarak en uygun temsilci atanır. Bu her adımda birikimli bilgi kullanarak daha verimli bir çözüm elde edilmesini sağlar.

2.Pazarlama Kampanya Seçimi

Pazarlama kampanya seçim fonksiyonu belirli bir bütçeyle hangi pazarlama kampanyalarının seçileceğine karar verirken dinamik programlama yöntemini kullanır. Burada dinamik programlama yaklaşımıyla her bütçe seviyesi için en yüksek getiri hesaplanır. Bu hesaplama önceki çözümlerden faydalanılarak yapılır. Bu daha doğru ve uzun vadede daha verimli sonuçlar elde edilmesini sağlar.

# Dinamik Programlama
Dinamik programlama karmaşık problemleri daha küçük alt problemlere bölerek çözmeyi amaçlayan bir optimizasyon tekniğidir. Alt problemler bir kez çözüldükten sonra bu çözümler bir tablo içinde saklanır ve tekrar gerektiğinde doğrudan kullanılır. Bu sayede aynı alt problemin tekrar tekrar çözülmesinden kaçınılır ve hesaplama maliyeti azalır. Dinamik programlamanın temelinde alt problem tekrarı ve optimal alt yapı prensipleri yatar. Yani bir problemin çözümü daha küçük alt problemlerin en iyi çözümlerine dayanır. Dinamik programlamanın diğer yöntemlerden farkı, çözümün her aşamasında önceki adımlardan edinilen bilgilerin kullanılmasını sağlayarak, daha hızlı ve daha verimli bir çözüm sunmasıdır. Dinamik programlama, karmaşık optimizasyon problemlerinde tercih edilen etkili bir yöntemdir. 

Dinamik programlamanın avantajları karmaşık ve büyük problemleri etkili bir şekilde çözme yeteneğinden gelir. Dinamik programlama alt problemleri çözüp sonuçlarını sakladığı için aynı alt problemin tekrar çözülmesini önler ve bu sayede zaman karmaşıklığını büyük ölçüde azaltır. Ayrıca dinamik programlama optimal alt yapı prensibine dayandığı için genellikle global olarak en iyi sonucu bulur. Tekrarlanan hesaplamaların önüne geçilmesi sayesinde daha az işlem gücü kullanılır ve algoritmanın performansı artar. Bu sayede karmaşık optimizasyon problemleri daha kolay ve verimli bir şekilde çözülebilir. 

Dinamik programlamanın dezavantajları ise genellikle bellek tüketimi ve gereksiz hesaplamalarla ilgilidir. Alt problemleri ve çözümlerini saklamak için bir tablo veya dizi kullanıldığı için bellek tüketimi yüksek olabilir. Bu durum özellikle büyük problemlerde belleğin yetersiz kalmasına veya sistem performansının düşmesine yol açabilir. Ayrıca bazı durumlarda problemin tamamını çözmeden de sonuca ulaşmak mümkünken dinamik programlama tüm alt problemleri çözdüğü için gereksiz hesaplamalara neden olabilir. Bu da kaynakların verimsiz kullanılmasına yol açabilir.

# Kullanım Adımları
1.Projeyi bilgisayarınıza indirin veya GitHub'dan klonlayın.

2.Python yüklü olduğundan emin olun.

3.Terminal veya komut istemcisinde CRM.py komutunu çalıştırarak projeyi çalıştırın.

4.Çalıştırdıktan sonra her müşterinin yönlendirildiği temsilcileri ve pazarlama kampanyaları içinde bütçeye en uygun olan pazarlama kampanyaları ile en yüksek getiriyi elde edeceksiniz.

# Kod Yapısı
1.Müşteri Destek Yönlendirme

Temsilci-Şehir Eşlemesi: Temsilcilerin hangi şehirlerde hizmet verdikleri rep_şehir_map adlı bir sözlükte saklanır. 

Müşteri Yönlendirme: Her müşteri için uygun temsilci seçilir. Eğer kapasite müsaitse ve şehir uyumluysa müşteri o temsilciye atanır. 

Dinamik Programlama: dp tablosu müşteri atamaları için en iyi sonucu verir ve kapasite durumlarına göre bir temsilci seçilir. 

Sonuç Yazdırma: Müşterilere atanan temsilciler ekranda listelenir. Eğer uygun temsilci bulunmazsa bu durum da bildirilir.

2.Pazarlama Kampanya Seçimi

Dinamik Programlama: Kampanyaların maliyetleri ve getirileri bütçeye göre değerlendirilir. dp[b] tablosu hangi bütçeyle hangi kampanyaların yapılabileceğini ve bunlardan ne kadar getiri elde edilebileceğini hesaplar. 

Kampanya Seçimi: Bütçenin uygun olduğu her kampanya için en yüksek getiriyi sağlayanlar seçilir. Kampanyaların maliyeti ve getiri değerlerine göre sıralama yapılır. 

Sonuç Yazdırma: Seçilen kampanyalar ve toplam ROI hesaplanır ve ekrana yazdırılır.

# Programın İşleyişi
1.Müşteri Destek Yönlendirme

1.1.Müşterilerin şehirlerine göre, temsilcilerin kapasiteleri ve hangi şehirlerde hizmet verdiklerine göre müşteri atamaları yapılır.

1.2.Dinamik programlama matrisi oluşturulur. Her müşteri ve temsilci için en uygun atama yapılır.

1.3.Temsilci şehir haritası kullanılarak her temsilcinin hangi şehirlerde hizmet verdiği belirlenir.

1.4.Kapasite kontrolü yapılır. Temsilci kapasitesini aşmayacak şekilde en uygun temsilci atanır.

1.5.Son olarak her müşteri için atanan temsilci yazdırılır. Eğer uygun temsilci bulunamazsa bu durum belirtilir.

2.Pazarlama Kampanya Seçimi

2.1.Verilen bütçe ile en yüksek getiriyi sağlayacak kampanyalar dinamik programlama kullanılarak seçilir.

2.2.Dinamik programlama matrisi oluşturulur ve her bütçe değeri için maksimum getiri hesaplanır.

2.3.Seçilen kampanyalar belirli bir bütçe sınırına göre seçilir ve kalan bütçe ile yeni kampanyalar seçilmeye devam edilir.

2.4.Seçilen kampanyalar ve toplam ROI hesaplanarak yazdırılır.

# Kullanılan Teknolojiler
Programlama Dili: Proje Python dilinde yazılmıştır.

Dinamik Programlama: Bu projede dinamik programlama alt problemlerin çözümlerini saklayarak tekrar hesaplama yapılmadan en optimal sonuca ulaşmak için kullanılmıştır.

# Ekran Çıktısı
![image](https://github.com/user-attachments/assets/ae3ce8e2-c6d5-453c-9464-9827ec1b0f45)
