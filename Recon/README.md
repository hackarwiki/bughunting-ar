
### <h3 dir="rtl" align="right"> السلام عليكم و رحمة الله و بركاته </h3>

<p dir="rtl" align="right">
ال programs اللي احنا بنعمل عليها test ال Scope بتاعها بيكون واحد من تلاته<br>
- large scope , medium scope , small scope<br>
</p>


## <h2 dir="rtl" align="right"> Large Scope </h2>
<p dir="rtl" align="right">
دا بيكون للمواقع الكبيره طب تعمل معاه ايه ؟ او تعرفه ازاي ؟ <br>
اولا : بتعرفه لما تشوف ال Scope بتاع الموقع زي كدا <br>
</p>

<p dir="rtl" align="right">
All <company> apps and assets not listed under the Out of Scope list <br>
و دا معناه ان الشركه دي بتقول اي موقع تابع لينا تقدر تعمل test عليه <br>
طب و انا هعرف المواقع دي ازاي ؟ <br>
هتروح الاول علي الموقع دا https://www.crunchbase.com <br>
</p>

<p dir="rtl" align="right">
و هتديله اسم الشركه اللي انت عاوز تشتغل عليها و ليكن مثلا sony<br>
 وهناك النتايج اللي بتطلع بتكون دي الشركات التابعه ليها تقدر تاخد المواقع دي و تشتغل عليها و اي ثغره تطلع معاك تبلغها <br>
طايب هل لحد هنا ال Scope خلص ؟<br>
</p>

<p dir="rtl" align="right">
لا دي الخطوة الاولي بس<br>
تاني خطوة بتروح ع الموقع دا bgp.he.net
</p>

<p dir="rtl" align="right">
و هنا بتديله اسم الموقع بتاعك و هو بيطلع ال ASN و CIDR بتاعها<br>
يعني اي الكلام دا تقدر تفهمه من هنا
</p>

```url
https://en.wikipedia.org/wiki/Autonomous_system_(Internet)
https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing
```

<p dir="rtl" align="right">
بعد ما بتطلع ال ASN و ال CIDR  <br>
تقدر تطلع منهم ال domains و ال Subdomains اللي موجودين فيهم<br>
و دا عن طريق amass tool ودا اللينك بتاعها https://github.com/OWASP/Amass<br>
و دي ال Commands اللي هتشغلها
</p>

```bash
amass intel -asn ***** ---------> for asn
amass intel -cidr *.*.*.*/* -----> for cidr
```

<p dir="rtl" align="right">
و دي كمان ال user guide عشان لو حبيت تعمل Scan اكتر<br>
https://github.com/OWASP/Amass/blob/master/doc/user_guide.md
</p>

<p dir="rtl" align="right">
و بعد ما بتخلص العمليه دي بتكون جمعت ال domains كلها الخاصه بالشركه و تنقل بعدها لل medium scope
</p>
----------------------------------------------------------------------------------

<p dir="rtl" align="right">
ال medium scope بيكون عباره عن domains و انت بتجيب ال subdomains بتاعته<br>
ازاي ؟<br>
يعني بيكون الموقع حاطط ال Scope بتاعه كدا<br>
</p>

```url
domain.com.*
```

<p dir="rtl" align="right">
و انت كل اللي عليك انك تطلع ال subdomains اللي فيه و تبدا تشتغل عليهم<br>
هتطلعهم ازاي ؟<br>
عندك tools كتيره تقدر تستخدمها<br>
</p>

- subfinder
https://github.com/projectdiscovery/subfinder
Command
subfinder -d domain.com

- assestfinder
https://github.com/tomnomnom/assetfinder
Command
assestfinder -subs-only domain.com

- amass
amass enum --passive -d domain.com

<p dir="rtl" align="right">
و ممكن كمان تعمل Enumeration بال certificates<br>
و هنا tools زي دي<br>
</p>

crtsh
https://github.com/knqyf263/crtsh
certspooter
https://github.com/SSLMate/certspotter
crtfinder
https://github.com/eslam3kl/crtfinder

<p dir="rtl" align="right">
بعدها تقدر تعمل brute force
عن طريق ال amass  برضو مع wordlist من seclist
https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS
</p>

```bash
amass enum -brute -w wordlist.txt -d example.com
```

<p dir="rtl" align="right">
بعد ما بتخلص تجميع لل subdomains تقدر هنا تعملهم sort عشان تشيل اي متشابه بينهم<br>
</p>

```bash
cat subs.txt | sort -u | tee -a new-subs.txt
```

<p dir="rtl" align="right">
بعد ما بنخلص المرحله دي اول حاجة نعملها اننا بنعمل subdomain takeover test<br>
عن طريق subzy<br>
https://github.com/LukaSikic/subzy
</p>

<p dir="rtl" align="right">
هنا المفروض تطلع ال resolved subdomains اللي نقدر تنشتغل عليهم<br>
و دي هنا هشتغل tool من دول<br>
</p>

- httprobe
https://github.com/tomnomnom/httprobe
- httpx
https://github.com/projectdiscovery/httpx

<p dir="rtl" align="right">
و انا شغال ب httpx افضل بكتير
</p>

<p dir="rtl" align="right">
هتعمل ال Command دا عشان تطلع ال Resolved
</p>

```bash
cat new-subs.txt | httpx -silent | tee -a alive.txt
```

<p dir="rtl" align="right">
و بعد ما تخلصه كدا هيكون معاك ال resolved subs<br>
تقدر منه تشتغل ف اكتر من حاجة لكن الافضل<br>
انك تدور علي endpoint و paths لان وارد تلاقي اي حاجة مهمه<br>
<br>
<br>
اول حاجة هتشغل ال Wayback عشان تجيب ال endpoints بتاعتها<br>
</p>

```bash
cat alive.txt | waybackurls | tee -a waybackurls.txt
```

<p dir="rtl" align="right">
و من هنا تقدر تعمل sort للثغرات عن طريق gf و تحط كل ثغره في ملف خاص بيها تبدأ تعمل عليها test<br>
</p>

```urls
https://github.com/tomnomnom/waybackurls
https://github.com/tomnomnom/gf
https://github.com/1ndianl33t/Gf-Patterns
```

<p dir="rtl" align="right">
تاني حاجة تقد تطلع ال js files<br>
و دا عن طريق subjs<br>
</p>

```bash
cat alive.txt | subjs | tee -a js.txt
https://github.com/lc/subjs
```

<p dir="rtl" align="right">
ملفات ال js تقدر تطلع منها<br>
- ال endpoint الخاصه بالموقع و منها تعملها brute force تاني<br>
و دي بتطلع ب tool اسمها linkfinder<br>
https://github.com/GerbenJavado/LinkFinder<br>
</p>

<p dir="rtl" align="right">
- secrets و دي بتكون (Google map api , aws urls , sensitive links )<br>
و دي بتطلع ب tool اسمها secret finder<br>
https://github.com/m4ll0k/SecretFinder
</p>

<p dir="rtl" align="right">
دا لينك بيعرفك ازاي تطلع google map api<br>
https://ozguralp.medium.com/unauthorized-google-maps-api-key-usage-cases-and-why-you-need-to-care-1ccb28bf21e<br>
</p>


<p dir="rtl" align="right">
و دا لينك تاني بيعرفك ازاي تعمل js enumeration و تستفاد منه
https://gist.github.com/m4ll0k/31ce0505270e0a022410a50c8b6311ff
</p>

<p dir="rtl" align="right">
بعد ما خلصت العمليتين اللي فوق تقدر تشوف ال subdomains اللي الحاله بتاعتها 200OK,403,301,302<br>
و تعرف انت هتشتغل ازاي فيهم<br>
</p>

<p dir="rtl" align="right">
تقدر تعمل ال Command دا و تطلع ال subdomains ال 200 عشان تقدر تشتغل علطول<br>
</p>

```bash
cat alive.txt | httpx -mc 200 -silent | tee -a 200.txt
```

<p dir="rtl" align="right">
ولو عاوز تجيب ال input parameters اللي موجوده في الموقع كله<br>
تعمل ال Command دا<br>
</p>

```bash
python3 paramspider -d domain.com
https://github.com/devanshbatham/ParamSpider
```

<p dir="rtl" align="right">
كدا خلاص انت عملت recon و خلصت كل حاجة اللي معاك حاليا
- domains & subdomains   للتارجت كله
- Endpoint & Paths
- Input parameters
</p>

<p dir="rtl" align="right">
تقدر بعد كدا تشتغل علي Google dorks و تجيب
</p>

```bash
- login & Register pages
site:*.domain.com inurl:login | inurl:sign
- Index of pages
site:*.domain.com inurl:index+of
- Admin panel
site:*.domain.com inurl:admin | inurl:panel
```

<p dir="rtl" align="right">
تقدر تشوف ال tips دي و تاخد ال commands اللي فيها
<br>
<br>
- لو عاوز تعمل automate و تجيب subdomains live و endpoint و input parameters
https://twitter.com/0xElkot/status/1288425261030084609
</p>

--------------------------------------------------------------------------------

## <h2 dir="rtl" align="right"> Small Scope </h2>

<p dir="rtl" align="right">
و دا بيكون ال scope كله حوالي عن Subdoamin واحد او اكتر<br>
<br>
دي methodology تقدر تمشي عليها في حاله لو نسيت تعمل test في مكان معين<br>
</p>

<p dir="rtl" align="right">
- دي بالنسبه لل Scopes و ازاي تتعامل معاهم<br>
https://www.xmind.net/m/hKKexj/<br>
<br>
- ودي عشان تعرف ال techniques اللي تمشي عليها في حاله لو حبيت تعمل test علي نوع معين من الثغرات<br>
https://www.xmind.net/m/bULg/<br>
<p dir="rtl" align="right">
