![assets](https://user-images.githubusercontent.com/93613110/229923174-18cd6148-76bf-485b-9146-c123b15553ce.png)
## <div align=center>Yarışma Bilgileri</div>
<div><b>Yarışma Konusu:</b> Aşağılayıcı Söylemlerin Doğal Dil İşleme İle Tespiti <br><br></div>
<div><b>Yarışmanın Alt Başlıkları:</b> Cinsiyetçi, ırkçı, küfür ve hakaret söylemleri gibi aşağılayıcı söylemler içeren cümlelerin doğal dil işleme yöntemleri ile tespit edilmesi ve ortaya çıkan teknik yetkinliğin sektörel kullanım alanları üzerine öneriler iletilmesi. <br><br></div>
<div><b>Yarışma Etiketleri:</b> SEXIST, RACIST, PROFANITY, INSULT, OTHER <br></div>

# <div align=center>Dokümantasyon</div>
### <div>İçerik</div>
- Yarışma Verisi
- Keşifsel Veri Analizi (EDA)
  - Veri Seti İçerisindeki Sınıf Dağılımı
  - Temizlenmiş Verilerin Token, Kelime ve Karakter Uzunluğuna Göre İncelenmesi
  - İşlenmemiş Veri Üzerindeki Stop Word lerin Analizi
  - Veri Seti İçerisindeki En Çok Geçen Kelimelerin İncelenmesi
  - nGram Analizi (n=2)
- Veri Ön İşleme Aşamları
- Model Denemeleri
  - Binary Sınıflandırma Sonuçları
  - Multiclass Sınıflandırma Sonuçları
- En Başarılı Modellerin Karmaşıklık Matrisi (Confusion Matrix)
- Dış Veri İle Modelleme
- Ensemble Model
- Final

## <div align=center>Yarışma Verisi</div>
<p>Yarışma için paylaşılan veri seti içerisinde 12620 veri bulunmaktadır.</p>
<p>Veri seti içerisindeki sütunlar; <b>id</b>, <b>text</b>, <b>is_offensive</b>, <b>target</b></p>
<p>
  <b>id:</b> Her bir verinin eşsiz kimliği<br>
  <b>text:</b> Sınıflandırılması gereken string türündeki veriler<br>
  <b>is_offensive:</b> Text içerisindeki string'lerin ofansiflik düzeyine göre etiketleri<br>
  <b>target:</b> Text içerisindeki string'lerin tür etiketleri
</p>

## <div align=center>Keşifsel Veri Analizi (EDA)</div>
### <div align=center>Veri Seti İçerisindeki Sınıf Dağılımı</div>
<div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/229932943-dc899df5-b07b-49ab-9423-dd467847340e.png"></div><br>
<p align=center>Veri seti içerisinde ofansif ve ofansif olmayan verilerin dağılımı arasında bir fark olduğu gözlemlendi.<br>Target etiketleri arasında inceleme yapıldığında ise dağılımın eşit olduğu gözlemlendi.</p>
<p align=center></p>

### <div align=center>Temizlenmiş Verilerin Token, Kelime ve Karakter Uzunluğuna Göre İncelenmesi</div>
<div align=center><img width="45%" src="https://user-images.githubusercontent.com/93613110/229936466-00041f5a-e9e3-4473-aed4-45613563a1e6.png"></div>
<p align=center>Veri seti içerisindeki ortalama metin uzunluğu 40.40. Minimum 5 karakter uzunluğunda veri bulunmaktadır. <br>Maksiumum 275 karakter uzunluğunda veri bulunmaktadır.</p>
<div align=center><img width="55%" src="https://user-images.githubusercontent.com/93613110/229936665-e92cc6e7-4dff-44c7-8066-1bd272d49e7a.png"></div>
<p align=center>Veriler içerisindeki ortalama kelime uzunlukları incelendi. Ofansif etiketlerine ve target etiketlerine göre gruplandırılarak analizler yapıldı. Ortalama kelime uzunluklarının 5 civarı olduğu gözlemlendi.</p>
<div align=center><img width="35%" src="https://user-images.githubusercontent.com/93613110/229938779-ca798003-9f9d-4c9b-ad5c-8dd0f976b775.png"></div>
<p align=center>Veri seti içerisinde 32 tokenden büyük çok az veri bulunmaktadır. 32 tokenden büyük olan verileri %95’i ‘OTHER’ sınıfına aittir. Bu nedenle tokenize etme işleminde parametre olarak maksimum token uzunluğu 32 kabul edilmiştir.</p>

### <div align=center>İşlenmemiş Veri Üzerindeki Stop Word lerin Analizi</div>
<p align=center>Stop word ler model üzerinde etkisiz kelimelerdir. Farklı etiketler içerisinde çok fazla bulundukları için tahmin sonucunu etkilememektedir. <br><br>Stop word ler kullanılarak ve kullanmadan 2 farklı eğitim gerçekleştirildi. Eğitim sonuçları alt taraftaki görsel ile paylaşıldı. Sonuçlara ve incelemelerimize göre de tahmin üzerinde bir etkileri olmadıkları gözlemlendi.</p>

#### <div align=center>Stopword Histogram</div>
<div align=center><img width="60%" src="https://user-images.githubusercontent.com/93613110/229939142-cb97b8ce-9d98-4e4b-ba7b-502b08bba3c5.png"></div>

#### <div align=center>Stop Word ün Başarı Metrikleri Üzerindeki Etkileri</div>
<div align=center><img width="60%" src="https://user-images.githubusercontent.com/93613110/230078861-41c5b92a-b157-4b55-869e-a18d2e4edc2e.png"></div>

### <div align=center>Veri Seti İçerisindeki En Çok Geçen Kelimelerin İncelenmesi</div>
<p align=center>Daha iyi bir model oluşturmak ve veri setini daha iyi anlayabilmek için en çok geçen kelimelerin olduğu grafik ve kelime bulutları(world cloud) oluşturuldu. Bazı etiketler için belirli kelime gruplarının belirleyici ve sıklık ile metinler içerisinde yer aldığı tespit edildi.</p>

#### <div align=center>Veri Seti İçerisindeki Kelimelerin Histogramı</div>
<div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/230078361-b1ef6782-e92c-4f6e-a6c7-9b64d058bdbf.png"></div>

#### <div align=center>Target Etiketlerine Göre Kelime Bulutları</div>
<div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/230077967-d4941e22-0c84-459c-ae4d-5f685f620655.png"></div>

### <div align=center>nGram Analizi (n=2)</div>
<div align=center><img width="50%" src="https://user-images.githubusercontent.com/93613110/230079454-db443f34-b7ea-4e5e-a255-075cb94847d9.png"></div>

## <div align=center>Veri Ön İşleme Aşamları</div>
- Duplicate veriler tespit edildi ve çıkarıldı.
- Karakterler küçük harfe dönüştürüldü.
- Metinler içerisindeki stop word ler çıkarıldı. (nltk kütüphanesi içerisindeki türkçe stop word ler kullanıldı)
- Bozuk veriler tespit edildi ve çıkarıldı (Örneğin sadece tek bir harften oluşan 133 adet  veri tespit edildi).
- Metinler noktalama işareti ve ifadelerden arındırıldı. (Noktalama işaretlerine ek olarak “<”, “>” gibi ifadeler tespit edildi ve çıkartıldı. Yapılan incelemeler ile çok fazla noktalama işaretinin bulunmadığı gözlemlendi).

## <div align=center>Model Denemeleri</div>
<div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/230085141-bf5c921f-ae38-420a-97af-0c1426714101.png"></div>

#### <div align=center>Binary Model Sonuçları</div>
<div align=center><img width="40%" src="https://user-images.githubusercontent.com/93613110/230088439-8d8d2be9-ad73-4847-b140-04c1c31e2f18.png"></div>

#### <div align=center>Multiclass Model Sonuçları</div>
<div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/230086260-b96d0186-693a-4b84-aabc-0e357533e498.png"></div>

## <div align=center>En Başarılı Modellerin Karmaşıklık Matrisi (Confusion Matrix)</div>

<div align=center>
<table>
  <tr>
    <td>&nbsp;</td>
    <td>Model İsmi</td>
    <td>Confusion Matrix</td>
  </tr>
  <tr>
    <td>Model-1</td>
    <td>bert-base-turkish-cased-mean-nli-stsb-tr</td>
    <td><div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/230100599-6a419d53-98ad-4c6f-a87b-4e8dbe9d5e8e.png"></div>
</td>
  </tr>
  <tr>
    <td>Model-2</td>
    <td>electra-base-turkish-cased-discriminator</td>
    <td><div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/230100922-fecee533-82d2-4b87-8fde-d18eb7136cbd.png"></div></td>
  </tr>
  <tr>
    <td>Model-3</td>
    <td>Bert-base-turkish-cased-mean-nli-stsb-tr-corrected-label</td>
    <td><div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/230100968-928bae6f-60d0-4d0c-8f06-4f1b38a5f243.png"></div></td>
  </tr>
</table>
</div>

## <div align=center>Dış Veri İle Modelleme</div>

## <div align=center>Ensemble Model</div>
<div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/230087470-51bab07e-45c2-4f8c-b0d9-be967b868468.png"></div>
<div align=center><img width="40%" src="https://user-images.githubusercontent.com/93613110/230087724-e825dd1a-a3af-4375-a458-855e00f1e4b9.png"></div>


## <div align=center>Final</div>
<div align=center><img width="50%" src="https://user-images.githubusercontent.com/93613110/230090373-343c0674-6cef-45e7-9b2f-817a0521ceff.png"></div>
