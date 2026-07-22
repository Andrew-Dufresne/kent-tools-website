#!/usr/bin/env python3
import json
from pathlib import Path
SRC = Path(r"C:\Users\AMD\WorkBuddy\Kent Tools")
T = json.load(open(SRC / "_translations.json", encoding="utf-8"))

PATCH = {
"Kent Tools — Professional Crimping Tools Manufacturer & Supplier": {
 "ar": "كينت تولز — مصنع ومورد احترافي لأدوات الضغط",
 "de": "Kent Tools — Professioneller Hersteller und Lieferant von Quetschwerkzeugen",
 "es": "Kent Tools — Fabricante y proveedor profesional de herramientas de engaste",
 "fr": "Kent Tools — Fabricant et fournisseur professionnel d'outils de sertissage",
 "ja": "Kent Tools — プロの圧着工具メーカー兼サプライヤー",
 "pt": "Kent Tools — Fabricante e fornecedor profissional de ferramentas de compressão",
 "ru": "Kent Tools — профессиональный производитель и поставщик обжимных инструментов"},
"Kent Tools is a leading manufacturer of crimping tools — pro press copper crimpers, battery cable crimpers, manual hydraulic crimpers. OEM/ODM welcome. Factory direct pricing.": {
 "ar": "كينت تولز شركة رائدة في تصنيع أدوات الضغط — مكابس النحاس برو برس، ومكابس كابلات البطارية، والمكابس الهيدروليكية اليدوية. نرحب بخدمات OEM/ODM. أسعار مباشرة من المصنع.",
 "de": "Kent Tools ist ein führender Hersteller von Quetschwerkzeugen — Pro-Press-Kupfercrimpzangen, batteriebetriebene Kabelcrimpzangen, manuelle hydraulische Crimpzangen. OEM/ODM willkommen. Preise direkt ab Werk.",
 "es": "Kent Tools es un fabricante líder de herramientas de engaste — crimpadoras de cobre pro press, crimpadoras de cable a batería, crimpadoras hidráulicas manuales. OEM/ODM bienvenido. Precios directos de fábrica.",
 "fr": "Kent Tools est un fabricant leader d'outils de sertissage — pinceuses cuivre pro press, pinceuses câble batterie, pinceuses hydrauliques manuelles. OEM/ODM les bienvenus. Prix direct usine.",
 "ja": "Kent Toolsは圧着工具の大手メーカーです — プロプレス銅管圧着機、バッテリーケーブル圧着機、手动油圧圧着機。OEM/ODM歓迎。工場直販価格。",
 "pt": "Kent Tools é um fabricante líder de ferramentas de compressão — crimpadores de cobre pro press, crimpadores de cabo a bateria, crimpadores hidráulicos manuais. OEM/ODM bem-vindo. Preços diretos de fábrica.",
 "ru": "Kent Tools — ведущий производитель обжимных инструментов — про-пресс медные обжимные клещи, аккумуляторные кабельные обжимные клещи, ручные гидравлические обжимные клещи. OEM/ODM приветствуются. Цены напрямую от завода."},
"Professional <span>Crimping</span><br>Tools for Every Job": {
 "ar": "أدوات ضغط <span>احترافية</span><br>لكل مهمة",
 "de": "Professionelle <span>Quetschwerkzeuge</span><br>für jeden Job",
 "es": "Herramientas de engaste <span>profesionales</span><br>para cada trabajo",
 "fr": "Outils de sertissage <span>professionnels</span><br>pour chaque travail",
 "ja": "プロの<span>圧着工具</span><br>あらゆる作業に",
 "pt": "Ferramentas de compressão <span>profissionais</span><br>para cada trabalho",
 "ru": "Профессиональные <span>обжимные инструменты</span><br>для любой задачи"},
"Kent Tools — your reliable partner in crimping equipment. From copper pipe pressing to battery cable crimping and hydraulic solutions — we deliver tools that electricians and plumbers trust. OEM / ODM / wholesale — factory direct pricing, global shipping.": {
 "ar": "كينت تولز — شريكك الموثوق في معدات الضغط. من كبس أنابيب النحاس إلى كبس كابلات البطارية والحلول الهيدروليكية — نقدم أدوات يثق بها الكهربائيون والسباكون. OEM / ODM / الجملة — أسعار مباشرة من المصنع، شحن عالمي.",
 "de": "Kent Tools — Ihr verlässlicher Partner für Crimpausrüstung. Vom Kupferrohr-Pressen über das batteriebetriebene Kabelcrimpen bis zu hydraulischen Lösungen — wir liefern Werkzeuge, die Elektriker und Klempner vertrauen. OEM / ODM / Großhandel — Preise direkt ab Werk, weltweiter Versand.",
 "es": "Kent Tools — su socio confiable en equipos de engaste. Desde el prensado de tubos de cobre hasta el crimpado de cables a batería y soluciones hidráulicas — entregamos herramientas en las que confían electricistas y fontaneros. OEM / ODM / mayorista — precios directos de fábrica, envío global.",
 "fr": "Kent Tools — votre partenaire fiable en matériel de sertissage. Du pressage de tubes de cuivre au sertissage de câbles batterie et aux solutions hydrauliques — nous livrons des outils que les électriciens et plombiers recommandent. OEM / ODM / grossiste — prix direct usine, expédition mondiale.",
 "ja": "Kent Tools — 圧着機器の信頼できるパートナー。銅管のプレスからバッテリーケーブル圧着、油圧ソリューションまで — 電気技師や配管工が信頼する工具をお届けします。OEM / ODM / 卸売 — 工場直販価格、世界配送。",
 "pt": "Kent Tools — seu parceiro confiável em equipamentos de compressão. Do prensamento de tubos de cobre ao crimpagem de cabos a bateria e soluções hidráulicas — entregamos ferramentas em que eletricistas e encanadores confiam. OEM / ODM / atacado — preços diretos de fábrica, envio global.",
 "ru": "Kent Tools — ваш надёжный партнёр в обжимном оборудовании. От опрессовки медных труб до аккумуляторного кабельного обжима и гидравлических решений — мы поставляем инструменты, которым доверяют электрики и сантехники. OEM / ODM / опт — цены напрямую от завода, доставка по всему миру."},
"Products — Kent Tools | Crimping Tools &amp; Rebar Solutions": {
 "ar": "منتجات — كينت تولز | أدوات الضغط وحديد التسليح",
 "de": "Produkte — Kent Tools | Quetschwerkzeuge &amp; Bewehrungslösungen",
 "es": "Productos — Kent Tools | Herramientas de engaste y soluciones para armadura",
 "fr": "Produits — Kent Tools | Outils de sertissage et solutions d'armature",
 "ja": "製品 — Kent Tools | 圧着工具と鉄筋ソリューション",
 "pt": "Produtos — Kent Tools | Ferramentas de compressão e soluções para armadura",
 "ru": "Продукция — Kent Tools | Обжимные инструменты и решения для арматуры"},
"Browse Kent Tools full product range: pro press copper crimpers, battery cable crimpers, manual hydraulic crimpers, rebar tying tools, rebar benders, rebar cutters and more. Full specifications. OEM/ODM available.": {
 "ar": "تصفح المجموعة الكاملة لمنتجات كينت تولز: مكابس النحاس برو برس، ومكابس كابلات البطارية، والمكابس الهيدروليكية اليدوية، وأدوات ربط حديد التسليح، وماكينات الثني، والقطع والمزيد. مواصفات كاملة. يتوفر OEM/ODM.",
 "de": "Entdecken Sie das vollständige Produktsortiment von Kent Tools: Pro-Press-Kupfercrimpzangen, batteriebetriebene Kabelcrimpzangen, manuelle hydraulische Crimpzangen, Rebar-Bindemaschinen, Rebar-Bieger, Rebar-Schneider und mehr. Volle Spezifikationen. OEM/ODM verfügbar.",
 "es": "Explore la gama completa de productos de Kent Tools: crimpadoras de cobre pro press, crimpadoras de cable a batería, crimpadoras hidráulicas manuales, herramientas de amarre de armadura, dobladoras de armadura, cortadoras de armadura y más. Especificaciones completas. OEM/ODM disponible.",
 "fr": "Découvrez la gamme complète de produits Kent Tools : pinceuses cuivre pro press, pinceuses câble batterie, pinceuses hydrauliques manuelles, machines de ligature d'armature, coudeuses d'armature, coupeuses d'armature et plus. Spécifications complètes. OEM/ODM disponible.",
 "ja": "Kent Toolsの全製品ラインナップをご覧ください：プロプレス銅管圧着機、バッテリーケーブル圧着機、手动油圧圧着機、鉄筋結束機、鉄筋曲げ機、鉄筋切断機など。完全な仕様。OEM/ODM対応。",
 "pt": "Explore a linha completa de produtos Kent Tools: crimpadores de cobre pro press, crimpadores de cabo a bateria, crimpadores hidráulicos manuais, ferramentas de amarração de armadura, dobradorias de armadura, cortadoras de armadura e mais. Especificações completas. OEM/ODM disponível.",
 "ru": "Ознакомьтесь с полным ассортиментом продукции Kent Tools: про-пресс медные обжимные клещи, аккумуляторные кабельные обжимные клещи, ручные гидравлические обжимные клещи, машины для вязки арматуры, арматурные гибщики, арматурные резаки и другое. Полные спецификации. Доступен OEM/ODM."},
"About Us — Kent Tools | Crimping Tools Manufacturer": {
 "ar": "من نحن — كينت تولز | مصنع أدوات الضغط",
 "de": "Über uns — Kent Tools | Hersteller von Quetschwerkzeugen",
 "es": "Sobre nosotros — Kent Tools | Fabricante de herramientas de engaste",
 "fr": "À propos de nous — Kent Tools | Fabricant d'outils de sertissage",
 "ja": "私たちについて — Kent Tools | 圧着工具メーカー",
 "pt": "Sobre nós — Kent Tools | Fabricante de ferramentas de compressão",
 "ru": "О нас — Kent Tools | Производитель обжимных инструментов"},
"Learn about Kent Tools — a professional crimping tools manufacturer with 24+ years of experience. ISO-certified factory, OEM/ODM, global shipping.": {
 "ar": "تعرف على كينت تولز — مصنع احترافي لأدوات الضغط بخبرة تزيد عن 24 عاماً. مصنع معتمد ISO، OEM/ODM، شحن عالمي.",
 "de": "Lernen Sie Kent Tools kennen — ein professioneller Hersteller von Quetschwerkzeugen mit über 24 Jahren Erfahrung. ISO-zertifiziertes Werk, OEM/ODM, weltweiter Versand.",
 "es": "Conozca Kent Tools — un fabricante profesional de herramientas de engaste con más de 24 años de experiencia. Fábrica certificada ISO, OEM/ODM, envío global.",
 "fr": "Découvrez Kent Tools — un fabricant professionnel d'outils de sertissage avec plus de 24 ans d'expérience. Usine certifiée ISO, OEM/ODM, expédition mondiale.",
 "ja": "Kent Toolsについて — 24年以上の実績を持つプロの圧着工具メーカー。ISO認証工場、OEM/ODM、世界配送。",
 "pt": "Conheça a Kent Tools — fabricante profissional de ferramentas de compressão com mais de 24 anos de experiência. Fábrica certificada ISO, OEM/ODM, envio global.",
 "ru": "Узнайте о Kent Tools — профессиональном производителе обжимных инструментов с опытом более 24 лет. Сертифицированный по ISO завод, OEM/ODM, доставка по всему миру."},
"About Kent Tools": {
 "ar": "كينت تولز — من نحن",
 "de": "Über Kent Tools",
 "es": "Sobre Kent Tools",
 "fr": "À propos de Kent Tools",
 "ja": "Kent Toolsについて",
 "pt": "Sobre a Kent Tools",
 "ru": "О Kent Tools"},
"CE Certified": {
 "ar": "معتمد CE", "de": "CE-zertifiziert", "es": "Certificado CE", "fr": "Certifié CE", "ja": "CE認証", "pt": "Certificado CE", "ru": "Сертификат CE"},
"RoHS Compliant": {
 "ar": "متوافق مع RoHS", "de": "RoHS-konform", "es": "Conforme a RoHS", "fr": "Conforme RoHS", "ja": "RoHS準拠", "pt": "Conforme RoHS", "ru": "Соответствие RoHS"},
"GS Safety": {
 "ar": "سلامة GS", "de": "GS-Sicherheit", "es": "Seguridad GS", "fr": "Sécurité GS", "ja": "GS安全", "pt": "Segurança GS", "ru": "Безопасность GS"},
"Delivering reliable crimping solutions to the world.": {
 "ar": "نقدم حلول ضغط موثوقة للعالم.",
 "de": "Wir liefern verlässliche Crimplösungen in die ganze Welt.",
 "es": "Entregamos soluciones de engaste confiables al mundo.",
 "fr": "Nous livrons des solutions de sertissage fiables dans le monde entier.",
 "ja": "世界中に信頼できる圧着ソリューションをお届けします。",
 "pt": "Entregamos soluções de compressão confiáveis para o mundo.",
 "ru": "Мы поставляем надёжные обжимные решения по всему миру."},
"Contact — Kent Tools | Get a Quote for Rebar Tools": {
 "ar": "اتصل بنا — كينت تولز | احصل على عرض سعر لأدوات حديد التسليح",
 "de": "Kontakt — Kent Tools | Angebot für Bewehrungswerkzeuge anfordern",
 "es": "Contacto — Kent Tools | Solicite cotización para herramientas de armadura",
 "fr": "Contact — Kent Tools | Demandez un devis pour outils d'armature",
 "ja": "お問い合わせ — Kent Tools | 鉄筋工具の見積もりを取得",
 "pt": "Contato — Kent Tools | Solicite orçamento para ferramentas de armadura",
 "ru": "Контакты — Kent Tools | Запросите расчёт для арматурных инструментов"},
"Contact Kent Tools for rebar tool inquiries. OEM/ODM, wholesale orders. WhatsApp: +995 593 583 830. Email: kent@gezhi.group": {
 "ar": "تواصلوا مع كينت تولز للاستفسار عن أدوات حديد التسليح. OEM/ODM، طلبات الجملة. واتساب: +995 593 583 830. البريد: kent@gezhi.group",
 "de": "Kontaktieren Sie Kent Tools für Anfragen zu Bewehrungswerkzeugen. OEM/ODM, Großbestellungen. WhatsApp: +995 593 583 830. E-Mail: kent@gezhi.group",
 "es": "Contacte con Kent Tools para consultas sobre herramientas de armadura. OEM/ODM, pedidos al por mayor. WhatsApp: +995 593 583 830. Correo: kent@gezhi.group",
 "fr": "Contactez Kent Tools pour vos demandes d'outils d'armature. OEM/ODM, commandes de gros. WhatsApp : +995 593 583 830. E-mail : kent@gezhi.group",
 "ja": "鉄筋工具についてはKent Toolsまでお問い合わせください。OEM/ODM、卸注文対応。WhatsApp: +995 593 583 830。メール: kent@gezhi.group",
 "pt": "Contate a Kent Tools para dúvidas sobre ferramentas de armadura. OEM/ODM, pedidos atacadistas. WhatsApp: +995 593 583 830. E-mail: kent@gezhi.group",
 "ru": "Свяжитесь с Kent Tools по вопросам арматурных инструментов. OEM/ODM, оптовые заказы. WhatsApp: +995 593 583 830. E-mail: kent@gezhi.group"},
"Get in Touch": {
 "ar": "تواصل معنا", "de": "Kontakt aufnehmen", "es": "Póngase en contacto", "fr": "Entrez en contact", "ja": "お問い合わせ", "pt": "Entre em contato", "ru": "Свяжитесь с нами"},
"Let&rsquo;s Talk Business": {
 "ar": "لنتحدث عن العمل", "de": "Sprechen wir über Geschäfte", "es": "Hablemos de negocios", "fr": "Parlons affaires", "ja": "仕事の話をしましょう", "pt": "Vamos falar de negócios", "ru": "Давайте поговорим о бизнесе"},
"Frequently Asked Questions": {
 "ar": "الأسئلة الشائعة", "de": "Häufig gestellte Fragen", "es": "Preguntas frecuentes", "fr": "Questions fréquentes", "ja": "よくある質問", "pt": "Perguntas frequentes", "ru": "Часто задаваемые вопросы"},
"<strong>Prefer to message directly?</strong><br>Click the WhatsApp button below to start a chat instantly — we respond within minutes during business hours.": {
 "ar": "<strong>تفضل المراسلة المباشرة؟</strong><br>انقر زر واتساب أدناه لبدء محادثة فورية — نرد خلال دقائق أثناء ساعات العمل.",
 "de": "<strong>Lieber direkt Nachricht senden?</strong><br>Klicken Sie unten auf den WhatsApp-Button, um sofort zu chatten — wir antworten innerhalb von Minuten während der Geschäftszeiten.",
 "es": "<strong>¿Prefiere enviar un mensaje directo?</strong><br>Haga clic en el botón de WhatsApp abajo para iniciar un chat al instante — respondemos en minutos durante el horario laboral.",
 "fr": "<strong>Préférez-vous envoyer un message directement ?</strong><br>Cliquez sur le bouton WhatsApp ci-dessous pour démarrer une discussion instantanée — nous répondons en quelques minutes pendant les heures ouvrables.",
 "ja": "<strong>直接メッセージをご希望ですか？</strong><br>下のWhatsAppボタンをクリックするとすぐにチャットが始まります — 営業時間内なら数分で返信します。",
 "pt": "<strong>Prefere enviar mensagem diretamente?</strong><br>Clique no botão do WhatsApp abaixo para iniciar um chat instantâneo — respondemos em minutos durante o horário comercial.",
 "ru": "<strong>Предпочитаете написать напрямую?</strong><br>Нажмите кнопку WhatsApp ниже, чтобы начать чат мгновенно — отвечаем в течение нескольких минут в рабочее время."}
}

for k, v in PATCH.items():
    T[k] = v
json.dump(T, open(SRC / "_translations.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("patched A:", len(PATCH))
