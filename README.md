![assets](https://user-images.githubusercontent.com/93613110/229923174-18cd6148-76bf-485b-9146-c123b15553ce.png)
## <div align=center>Yarışma Bilgileri</div>
<div><b>Yarışma Konusu:</b> Aşağılayıcı Söylemlerin Doğal Dil İşleme İle Tespiti <br><br></div>
<div><b>Yarışmanın Alt Başlıkları:</b> Cinsiyetçi, ırkçı, küfür ve hakaret söylemleri gibi aşağılayıcı söylemler içeren cümlelerin doğal dil işleme yöntemleri ile tespit edilmesi ve ortaya çıkan teknik yetkinliğin sektörel kullanım alanları üzerine öneriler iletilmesi. <br><br></div>
<div><b>Yarışma Etiketleri:</b> SEXIST, RACIST, PROFANITY, INSULT, OTHER <br></div>

# <div align=center>Dokümantasyon</div>
## <div align=center>Kontent</div>
- Yarışma Verisi
- Keşifsel Veri Analizi (EDA)
  - Veri Seti İçerisindeki Sınıf Dağılımı
  - Verilerin Token, Kelime ve Karakter Uzunluğuna Göre İncelenmesi
  - İşlenmemiş Veri Üzerindeki Stopwords'lerin Analizi
  - Veri Seti İçerisindeki En Çok Geçen Kelimelerin İncelenmesi
  - nGram Analizi (n=2)
- Veri Ön İşleme Aşamları
- Model Denemeleri
- Çok Sınıflı Mimari (MultiClass Architecture)
- Topluluk Öğrenmesi (Ensemble Learning)
- Final

## <div align=center>Yarışma Verisi</div>


<p>Yarışma için paylaşılan veri seti içerisinde 12461 veri bulunmaktadır.</p>
<p>Veri seti içerisindeki sütunlar; <b>id</b>, <b>text</b>, <b>is_offensive</b>, <b>target</b></p>
<p>
  <b>id:</b> Her bir verinin eşsiz kimliği<br>
  <b>text:</b> Sınıflandırılması gereken string türündeki veriler<br>
  <b>is_offensive:</b> Text içerisindeki string'lerin ofansiflik düzeyine göre etiketleri<br>
  <b>target:</b> Text içerisindeki string'lerin tür etiketleri
</p>

## <div align=center>Keşifsel Veri Analizi (EDA)</div>
### <div align=center>Veri Seti İçerisindeki Sınıf Dağılımı</div>
<img width="100%" src="https://user-images.githubusercontent.com/93613110/229932943-dc899df5-b07b-49ab-9423-dd467847340e.png">
<p>Veri seti içerisinde ofansif ve ofansif olmayan verilerin dağılımı arasında bir fark olduğu gözlemlendi. Target etiketleri arasında inceleme yapıldığında ise dağılımın eşit olduğu gözlemlendi.

### <div align=center>Verilerin Token, Kelime ve Karakter Uzunluğuna Göre İncelenmesi</div>
<div align=center><img width="60%" src="https://user-images.githubusercontent.com/93613110/229936466-00041f5a-e9e3-4473-aed4-45613563a1e6.png"></div>
<p>Veri seti içerisindeki ortalama metin uzunluğu 40.40. Minimum 5 karakter uzunluğunda veri bulunmaktadır. Maksiumum 275 karakter uzunluğunda veri bulunmaktadır.</p>
<div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/229936665-e92cc6e7-4dff-44c7-8066-1bd272d49e7a.png"></div>
<p>Veri seti içerisindeki ortalama metin uzunluğu 40.40. Minimum 5 karakter uzunluğunda veri bulunmaktadır. Maksiumum 275 karakter uzunluğunda veri bulunmaktadır.</p>
<div align=center><img width="50%" src="https://user-images.githubusercontent.com/93613110/229938779-ca798003-9f9d-4c9b-ad5c-8dd0f976b775.png"></div>
<p>Veri seti içerisindeki ortalama metin uzunluğu 40.40. Minimum 5 karakter uzunluğunda veri bulunmaktadır. Maksiumum 275 karakter uzunluğunda veri bulunmaktadır.</p>

### <div align=center>İşlenmemiş Veri Üzerindeki Stopwords'lerin Analizi</div>
<div align=center><img width="80%" src="https://user-images.githubusercontent.com/93613110/229939142-cb97b8ce-9d98-4e4b-ba7b-502b08bba3c5.png"></div>
<div style="display: inline-block; width: 20%"><img width="20%" src="https://user-images.githubusercontent.com/93613110/229939756-2faec58a-2fef-493c-805c-a1917ff5d527.png"></div>
<div style="display: inline-block;"><img width="20%" src="https://user-images.githubusercontent.com/93613110/229939756-2faec58a-2fef-493c-805c-a1917ff5d527.png"></div>
<div style="display: inline-block;"><img width="20%" src="https://user-images.githubusercontent.com/93613110/229939756-2faec58a-2fef-493c-805c-a1917ff5d527.png"></div>
<div style="display: inline-block;"><img width="20%" src="https://user-images.githubusercontent.com/93613110/229939756-2faec58a-2fef-493c-805c-a1917ff5d527.png"></div>

### <div align=center>Veri Seti İçerisindeki En Çok Geçen Kelimelerin İncelenmesi</div>

### <div align=center>nGram Analizi (n=2)</div>

## <div align=center>Veri Ön İşleme Aşamları</div>

## <div align=center>Model Denemeleri</div>

## <div align=center>Çok Sınıflı Mimari (MultiClass Architecture)</div>

## <div align=center>Topluluk Öğrenmesi (Ensemble Learning)</div>

## <div align=center>Final</div>
