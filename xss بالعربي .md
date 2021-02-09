# <h1 dir='rtl' align='right'> XSS بالعربي </h1>

## <h2 dir='rtl' align='right'> ** المقدمة ** </h2>

<h2 dir='rtl' align='right'>
  Cross-Site Scripting (XSS) هو نوع من هجمات الحقن, حيث يتم حقن البرامج النصية الضارة في مواقع الويب. هناك ثلاثة أنواع من هجوم XSS
</h2>

<h3 dir='rtl' align='right'> Reflected XSS - النوع المنعكس </h3>

   <p dir='rtl' align='right'>هو عبارة عن تشغل كود ضار من مصدر اخر عن طريق برامتر في رابط الموقع كمثال </p>

<h3 dir='rtl' align='right'> Stored XSS - المخزن </h3>

  <p dir='rtl' align='right'>
  هو ببساطة النوع الذي يكون موجود في مكان مثل ادراج كومنت او صورة في مكان يراه الكثير ويكون مخزن علي الموقع دائما .
  </p>

<h3 dir='rtl' align='right'> DOM-Based XSS - من داخل كود جافا سكربت </h3>

  <p dir='rtl' align='right'> نوع من XSS يحتوي على حمولات موجودة في DOM بدلاً من كود HTML. </p>

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
