السلام عليكم و رحمة الله و بركاته 

ال programs اللي احنا بنعمل عليها test ال Scope بتاعها بيكون واحد من تلاته 
- large scope , medium scope , small scope 

Large Scope 
دا بيكون للمواقع الكبيره طب تعمل معاه ايه ؟ او تعرفه ازاي ؟ 
اولا : بتعرفه لما تشوف ال Scope بتاع الموقع زي كدا 

All <company> apps and assets not listed under the Out of Scope list 

و دا معناه ان الشركه دي بتقول اي موقع تابع لينا تقدر تعمل test عليه 
طب و انا هعرف المواقع دي ازاي ؟ 

هتروح الاول علي الموقع دا https://www.crunchbase.com 

و هتديله اسم الشركه اللي انت عاوز تشتغل عليها و ليكن مثلا sony 
 وهناك النتايج اللي بتطلع بتكون دي الشركات التابعه ليها تقدر تاخد المواقع دي و تشتغل عليها و اي ثغره تطلع معاك تبلغها عادي 
طايب هل لحد هنا ال Scope خلص ؟ 

لا دي الخطوة الاولي بس 
تاني خطوة بتروح ع الموقع دا bgp.he.net

و هنا بتديله اسم الموقع بتاعك و هو بيطلع ال ASN و CIDR بتاعها 
يعني اي الكلام دا تقدر تفهمه من هنا 
https://en.wikipedia.org/wiki/Autonomous_system_(Internet)
https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing

بعد ما بتطلع ال ASN و ال CIDR  
تقدر تطلع منهم ال domains و ال Subdomains اللي موجودين فيهم 
و دا عن طريق amass tool ودا اللينك بتاعها https://github.com/OWASP/Amass

و دي ال Commands اللي هتشغلها 

amass intel -asn ***** ---------> for asn 
amass intel -cidr *.*.*.*/* -----> for cidr 

و دي كمان ال user guide عشان لو حبيت تعمل Scan اكتر 
https://github.com/OWASP/Amass/blob/master/doc/user_guide.md

و بعد ما بتخلص العمليه دي بتكون جمعت ال domains كلها الخاصه بالشركه و تنقل بعدها لل medium scope

----------------------------------------------------------------------------------


ال medium scope بيكون عباره عن domains و انت بتجيب ال subdomains بتاعته 
ازاي ؟ 
يعني بيكون الموقع حاطط ال Scope بتاعه كدا 

domain.com.*

و انت كل اللي عليك انك تطلع ال subdomains اللي فيه و تبدا تشتغل عليهم 

هتطلعهم ازاي ؟ 
عندك tools كتيره تقدر تستخدمها 

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


و ممكن كمان تعمل Enumeration بال certificates 

و هنا tools زي دي 
crtsh 
https://github.com/knqyf263/crtsh
certspooter 
https://github.com/SSLMate/certspotter
crtfinder 
https://github.com/eslam3kl/crtfinder

بعدها تقدر تعمل brute force 

عن طريق ال amass  برضو مع wordlist من seclist 
https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS

amass enum -brute -w wordlist.txt -d example.com


بعد ما بتخلص تجميع لل subdomains تقدر هنا تعملهم sort عشان تشيل اي متشابه بينهم 
cat subs.txt | sort -u | tee -a new-subs.txt 

بعد ما بنخلص المرحله دي اول حاجة نعملها اننا بنعمل subdomain takeover test 
عن طريق subzy 
https://github.com/LukaSikic/subzy

هنا المفروض تطلع ال resolved subdomains اللي نقدر تنشتغل عليهم 
و دي هنا هشتغل tool من دول 

- httprobe 
https://github.com/tomnomnom/httprobe
- httpx 
https://github.com/projectdiscovery/httpx
و انا شغال ب httpx افضل بكتير 

هتعمل ال Command دا عشان تطلع ال Resolved 
cat new-subs.txt | httpx -silent | tee -a alive.txt 

و بعد ما تخلصه كدا هيكون معاك ال resolved subs 
تقدر منه تشتغل ف اكتر من حاجة لكن الافضل 
انك تدور علي endpoint و paths لان وارد تلاقي اي حاجة مهمه 

اول حاجة هتشغل ال Wayback عشان تجيب ال endpoints بتاعتها 
cat alive.txt | waybackurls | tee -a waybackurls.txt 

و من هنا تقدر تعمل sort للثغرات عن طريق gf و تحط كل ثغره في ملف خاص بيها تبدأ تعمل عليها test 
https://github.com/tomnomnom/waybackurls
https://github.com/tomnomnom/gf
https://github.com/1ndianl33t/Gf-Patterns

تاني حاجة تقد تطلع ال js files 
و دا عن طريق subjs 
cat alive.txt | subjs | tee -a js.txt 
https://github.com/lc/subjs
ملفات ال js تقدر تطلع منها 
- ال endpoint الخاصه بالموقع و منها تعملها brute force تاني 
و دي بتطلع ب tool اسمها linkfinder 
https://github.com/GerbenJavado/LinkFinder

- secrets و دي بتكون (Google map api , aws urls , sensitive links )
و دي بتطلع ب tool اسمها secret finder 
https://github.com/m4ll0k/SecretFinder

دا لينك بيعرفك ازاي تطلع google map api 
https://ozguralp.medium.com/unauthorized-google-maps-api-key-usage-cases-and-why-you-need-to-care-1ccb28bf21e

و دا لينك تاني بيعرفك ازاي تعمل js enumeration و تستفاد منه 
https://gist.github.com/m4ll0k/31ce0505270e0a022410a50c8b6311ff

بعد ما خلصت العمليتين اللي فوق تقدر تشوف ال subdomains اللي الحاله بتاعتها 200OK,403,301,302
و تعرف انت هتشتغل ازاي فيهم 

تقدر تعمل ال Command دا و تطلع ال subdomains ال 200 عشان تقدر تشتغل علطول 
cat alive.txt | httpx -mc 200 -silent | tee -a 200.txt 

ولو عاوز تجيب ال input parameters اللي موجوده في الموقع كله 
تعمل ال Command دا 
python3 paramspider -d domain.com 
https://github.com/devanshbatham/ParamSpider


كدا خلاص انت عملت recon و خلصت كل حاجة اللي معاك حاليا 
- domains & subdomains   للتارجت كله 
- Endpoint & Paths 
- Input parameters 

تقدر بعد كدا تشتغل علي Google dorks و تجيب 
- login & Register pages
site:*.domain.com inurl:login | inurl:sign 
- Index of pages 
site:*.domain.com inurl:index+of
- Admin panel 
site:*.domain.com inurl:admin | inurl:panel

تقدر تشوف ال tips دي و تاخد ال commands اللي فيها 

- لو عاوز تعمل automate و تجيب subdomains live و endpoint و input parameters
https://twitter.com/0xElkot/status/1288425261030084609

--------------------------------------------------------------------------

Small Scope 

و دا بيكون ال scope كله حوالي عن Subdoamin واحد او اكتر 

دي methodology تقدر تمشي عليها في حاله لو نسيت تعمل test في مكان معين 

- دي بالنسبه لل Scopes و ازاي تتعامل معاهم
https://www.xmind.net/m/hKKexj/

- ودي عشان تعرف ال techniques اللي تمشي عليها في حاله لو حبيت تعمل test علي نوع معين من الثغرات 
https://www.xmind.net/m/bULg/





