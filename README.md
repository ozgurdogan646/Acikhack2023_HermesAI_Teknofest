![assets](https://user-images.githubusercontent.com/93613110/229923174-18cd6148-76bf-485b-9146-c123b15553ce.png)
## <div align=center>Yarışma Bilgileri</div>
<div><b>Yarışma Konusu:</b> Aşağılayıcı Söylemlerin Doğal Dil İşleme İle Tespiti <br><br></div>
<div><b>Yarışmanın Alt Başlıkları:</b> Cinsiyetçi, ırkçı, küfür ve hakaret söylemleri gibi aşağılayıcı söylemler içeren cümlelerin doğal dil işleme yöntemleri ile tespit edilmesi ve ortaya çıkan teknik yetkinliğin sektörel kullanım alanları üzerine öneriler iletilmesi. <br><br></div>
<div><b>Yarışma Etiketleri:</b> SEXIST, RACIST, PROFANITY, INSULT, OTHER <br></div>

# <div align=center>Dokümantasyon</div>
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
<p>Veri seti içerisinde ofansif ve ofansif olmayan veriler arasında bir fark olduğu gözlemlendi. Target etiketleri arasında inceleme yapıldığında ise dağılımın eşit olduğu gözlemlendi.

### <div align=center>Verilerin Token Uzunluğuna Göre İncelenmesi</div>

### <div align=center>İşlenmemiş Veri Üzerindeki Stopwords'lerin Analizi</div>
