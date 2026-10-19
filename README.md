# Veri Bilimi Pratik Projeleri

Bu depo, farklı makine öğrenmesi / veri bilimi konularında (sınıflandırma, regresyon, kümeleme, zaman serisi,
öneri sistemleri, görüntü sınıflandırma, NLP) **uygulamalı olarak çalıştığım pratik projelerin** bir koleksiyonudur.

## Önemli not — kaynak ve özgünlük

Aşağıdaki projelerin büyük bölümü **[thecleverprogrammer.com](https://thecleverprogrammer.com) (Aman Kharwal)**
kaynaklı eğitim materyallerini adım adım takip ederek uyguladığım çalışmalardır. Bunları kendi özgün
araştırmam/ürünüm olarak sunmuyorum — amaç, farklı ML teknikleri üzerinde pratik yapmak, kodu anlayarak
çalıştırmak ve bir kısmını Streamlit ile uçtan uca deploy etmekti. Her alt klasörün kendi README'sinde
kaynak belirtilmiştir.

## Projeler

| Proje | Açıklama |
|---|---|
| [Deprem Risk Tahmini](./earthquake-prediction) | ABD Jeoloji Araştırmaları Kurumu (USGS) geçmiş deprem verileriyle, enlem/boylam ve derinlik bilgisinden büyüklük ve derinlik tahmini yapan bir yapay sinir ağı (Keras) modeli. |
| [Mobil Telefon Fiyat Segmenti Tahmini](./mobile-price-classification) | Telefon donanım özelliklerinden (RAM, batarya, kamera vb.) yararlanarak istatistiksel modelleme ve doğrusal regresyon ile fiyat segmenti tahmini. |
| [Reklam Harcamasına Göre Satış Tahmini](./sales-prediction) | TV, radyo ve gazete reklam harcamalarına bağlı olarak ürün satış miktarını öngören doğrusal regresyon modeli. |
| [Iris Çiçeği Türü Sınıflandırması](./iris-flower-classification) | Klasik Iris veri setinde taç/çanak yaprak ölçülerinden çiçek türünü öngören KNN ve Keras tabanlı sınıflandırma modelleri; Streamlit arayüzüyle canlı tahmin. |
| [Yapay Sinir Ağları (ANN) ile Görüntü Sınıflandırma](./image-classification-ann) | Fashion MNIST veri setindeki 28x28 piksel gri tonlamalı kıyafet görsellerini yapay sinir ağı (ANN) ile sınıflandırma. |
| [Hava Durumu Tahmini (Delhi)](./weather-forecasting) | Delhi şehrine ait günlük iklim verileriyle Facebook Prophet kütüphanesi kullanılarak gelecek günlerin sıcaklık tahmini. |
| [Web Sitesi Trafik Tahmini](./website-traffic-forecasting) | Günlük web sitesi ziyaret verileriyle zaman serisi (ARIMA/SARIMA) kullanılarak gelecekteki trafik hacmini öngören model. (Not: eğitilmiş model dosyası 400MB+ olduğu için depoya eklenmedi.) |
| [Dogecoin Fiyat Tahmini](./dogecoin-price-prediction) | Geçmiş Dogecoin fiyat verileriyle AutoTS kütüphanesi kullanılarak kripto para fiyat tahmini (zaman serisi regresyonu). |
| [Makine Öğrenmesi Algoritmasının Görselleştirilmesi](./visualize-ml-algorithm) | Doğrusal regresyon modelinin tahmin ettiği eğilim çizgisinin Plotly ile interaktif olarak görselleştirilmesi. |
| [Güneş Sisteminin 3B Görselleştirilmesi](./visualize-solar-system) | Plotly ile gezegenlerin konum ve yörüngelerini temsil eden interaktif 3 boyutlu bir güneş sistemi görselleştirmesi. |
| [Sosyal Medya Reklamı Hedef Kitle Sınıflandırması](./social-media-ads-classification) | Yaş, tahmini maaş gibi özelliklere göre bir kullanıcının sosyal medya reklamındaki ürünü satın alıp almayacağını öngören Karar Ağacı (Decision Tree) sınıflandırma modeli. |
| [Kredi Kartı Müşteri Segmentasyonu](./credit-card-clustering) | Bakiye, alışveriş tutarı ve kredi limiti gibi finansal davranışlara göre kredi kartı müşterilerini K-Means ile kümelere ayıran bir segmentasyon çalışması. |
| [Kitap Öneri Sistemi](./book-recommendation-system) | Kullanıcı derecelendirmelerinden yararlanarak k-En Yakın Komşu (k-NN) tabanlı işbirlikçi filtreleme ile kitap öneri sistemi. (Not: BX-Books/Users/Ratings veri setleri boyut kısıtı nedeniyle depoya eklenmedi.) |
| [Film Öneri Sistemi](./movie-recommendation-system) | Film özetlerinin TF-IDF temsiliyle içerik tabanlı (content-based) benzerlik hesaplanarak film öneren bir sistem. (Not: TMDB veri setleri boyut kısıtı nedeniyle depoya eklenmedi.) |
| [İşaret Dili Harf Sınıflandırması](./sign-language-classification) | El işareti görsellerinden Amerikan İşaret Dili (ASL) harflerini tanıyan, TensorFlow/Keras ile eğitilmiş bir görüntü sınıflandırma modeli. |
| [ARIMA ile Hisse/Zaman Serisi Tahmini](./arima-zaman-serisi-tahmini) | Yahoo Finance verileriyle Mevsimsel ARIMA (SARIMA) modeli kullanılarak zaman serisi tahmini örneği. |
| [İngilizce-Hintçe Makine Çevirisi](./language-translation-marianmt) | HuggingFace Transformers kütüphanesindeki MarianMT mimarisinin İngilizce-Hintçe çeviri verisiyle fine-tune edilmesi ve Streamlit üzerinden gösterimi. |
| [Hızlı Çeviri Aracı](./translate-quick-tool) | googletrans / deep-translator paketleriyle metinleri istenen dile çeviren basit bir araç; ek olarak çeviri verisiyle lojistik regresyon tabanlı bir dil sınıflandırma denemesi. |


## Canlı Demolar (HuggingFace Spaces)

Bu projelerin bir kısmı kendi HuggingFace hesabımda (**sifaaral**) Streamlit uygulaması olarak deploy edilmiştir:
https://huggingface.co/sifaaral

(Not: bazı Space'lerde bağımlılık/sürüm uyumsuzluğu nedeniyle build hatası olabilir, yeniden deploy gerekebilir.)
