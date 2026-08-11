const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuBtn.addEventListener('click', () => {
  mobileMenu.classList.toggle('hidden');
  mobileMenu.classList.toggle('flex');
});

mobileMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.add('hidden');
    mobileMenu.classList.remove('flex');
  });
});

function toggleTheme() {
  const htmlEl = document.documentElement;
  const isDark = htmlEl.classList.contains('dark');
  
  if (isDark) {
    htmlEl.classList.remove('dark');
    localStorage.theme = 'light';
    updateThemeIcons('☀️'); 
  } else {
    htmlEl.classList.add('dark');
    localStorage.theme = 'dark';
    updateThemeIcons('🌙'); 
  }
}

function updateThemeIcons(icon) {
  document.getElementById('theme-btn-mobile').innerText = icon;
  document.getElementById('theme-btn-desktop').innerText = icon;
}

if (localStorage.theme === 'light' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: light)').matches)) {
  document.documentElement.classList.remove('dark');
  updateThemeIcons('☀️');
} else {
  document.documentElement.classList.add('dark');
  updateThemeIcons('🌙');
}

function openModal(id) { 
    document.getElementById(id).classList.remove('hidden'); 
    document.body.style.overflow = 'hidden'; 
}
function closeModal(id) { 
    document.getElementById(id).classList.add('hidden'); 
    document.body.style.overflow = 'auto'; 
}

// كائن الترجمات المحدث مع المسميات والخبرات الجديدة
const translations = {
  de: {
    page_title: "Mahmoud | Premium Software Development",
    nav_home: "Home", nav_about: "Über Mich", nav_work: "Meine Arbeit", nav_contact: "Kontakt",
    hero_title: "MAHMOUD", hero_subtitle: "Premium Software Development",
    about_pretitle: "Exzellente Software braucht klare Architektur",
    about_title: 'Ein hochwertiger Code ist mehr als nur Syntax, er automatisiert Prozesse und <span class="text-slate-400 dark:text-gray-500">integriert KI...</span>',
    about_desc: "Als Software Developer verwandle ich komplexe Probleme in elegante Lösungen. Meine Leidenschaft liegt darin, durch sauberen Code und innovative Technologien echten Mehrwert zu schaffen.",
    work_title: "Meine Arbeit", 
    project_ufo_desc: "Interaktives Web-Spiel mit flüssigen Animationen und komplexer JavaScript-Logik.",
    btn_view_project: 'PROJEKT ANSEHEN <span class="group-hover:translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    project_mo_desc: "Architektur-Demonstration von UI/UX Design und starken Backend-Automatisierungen.",
    project_hw_title: "HW-Automatisierung", 
    project_hw_desc: "Systemdiagnose-Tool mit Jenkins-CI/CD. Automatisiertes Testing und terminierte Kundenreports.",
    btn_view_doc: 'DOKUMENTATION <span class="group-hover:translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    project_git_desc: "Mein öffentliches Repository. Entdecken Sie saubere Code-Strukturen und weitere Projekte.",
    btn_view_github: 'GITHUB BESUCHEN <span class="group-hover:translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    exp_title: "Erfahrung", 
    exp_focus: "Aktueller Fokus", 
    exp_job1_title: "Software Developer",
    exp_task1_1: "▹ Konzeption und Umsetzung von Web-Anwendungen unter Einsatz von KI-Tools", 
    exp_task1_2: "▹ Entwicklung skalierbarer Software-Projekte", 
    exp_task1_3: "▹ Entwicklung von Python-Skripten zur Automatisierung Von Datenprozessen",
    exp_job2_title: "Ausbildung zum Fachinformatiker für Anwendungsentwicklung",
    exp_task2_1: "▹ Automatisierung vom Prozessen, Datenanalyse",
    exp_task2_2: "▹ Webentwicklung",
    exp_task2_3: "▹ Projektverwaltung mit Git",
    tech_langs: "Programmiersprachen", tech_tools: "Tools", tech_frameworks: "Frameworks",
    contact_title: "Lass uns reden.", contact_email: "E-Mail", contact_github: "Codes ansehen ↗",
    footer_rights: "© 2026 MAHMOUD. ALLE RECHTE VORBEHALTEN.", footer_impressum: "Impressum", footer_privacy: "Datenschutz",
    impressum_text: "Mahmoud<br>Software Developer<br>Regensburg, Deutschland<br><br>Kontakt: Benachrichtigung.Mahmoud@hotmail.com<br>Tel: +49 1525 2690273",
    privacy_text: "<p>Wir nehmen den Schutz Ihrer Daten ernst. Auf dieser Website werden keine Cookies zur Nachverfolgung (Tracking) verwendet.</p><p>Der Provider der Seiten (Host) erhebt und speichert automatisch Informationen in sogenannten Server-Log-Dateien...</p>"
  },
  en: {
    page_title: "Mahmoud | Premium Software Development",
    nav_home: "Home", nav_about: "About Me", nav_work: "My Work", nav_contact: "Contact",
    hero_title: "MAHMOUD", hero_subtitle: "Premium Software Development",
    about_pretitle: "Excellent software needs clear architecture",
    about_title: 'High-quality code is more than just syntax, it automates processes and <span class="text-slate-400 dark:text-gray-500">integrates AI...</span>',
    about_desc: "As a Software Developer, I transform complex problems into elegant solutions. My passion lies in creating real value through clean code and innovative technologies.",
    work_title: "My Work", 
    project_ufo_desc: "Interactive web game with smooth animations and complex JavaScript logic.",
    btn_view_project: 'VIEW PROJECT <span class="group-hover:translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    project_mo_desc: "Architecture demonstration of UI/UX design and strong backend automations.",
    project_hw_title: "HW Automation", 
    project_hw_desc: "System diagnostics tool with Jenkins CI/CD. Automated testing and scheduled client reports.",
    btn_view_doc: 'DOCUMENTATION <span class="group-hover:translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    project_git_desc: "My public repository. Discover clean code structures and more projects.",
    btn_view_github: 'VISIT GITHUB <span class="group-hover:translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    exp_title: "Experience", 
    exp_focus: "Current Focus", 
    exp_job1_title: "Software Developer",
    exp_task1_1: "▹ Design and implementation of web applications using AI tools", 
    exp_task1_2: "▹ Development of scalable software projects", 
    exp_task1_3: "▹ Development of Python scripts for automating data processes",
    exp_job2_title: "Apprenticeship as IT Specialist for Application Development",
    exp_task2_1: "▹ Process automation, Data analysis",
    exp_task2_2: "▹ Web development",
    exp_task2_3: "▹ Project management with Git",
    tech_langs: "Programming Languages", tech_tools: "Tools", tech_frameworks: "Frameworks",
    contact_title: "Let's talk.", contact_email: "Email", contact_github: "View Codes ↗",
    footer_rights: "© 2026 MAHMOUD. ALL RIGHTS RESERVED.", footer_impressum: "Imprint", footer_privacy: "Privacy Policy",
    impressum_text: "Mahmoud<br>Software Developer<br>Regensburg, Germany<br><br>Contact: Benachrichtigung.Mahmoud@hotmail.com<br>Phone: +49 1525 2690273",
    privacy_text: "<p>We take the protection of your data seriously. No tracking cookies are used on this website.</p>"
  },
  ar: {
    page_title: "محمود | تطوير برمجيات متقدمة",
    nav_home: "الرئيسية", nav_about: "من أنا", nav_work: "أعمالي", nav_contact: "تواصل معي",
    hero_title: "محمود", hero_subtitle: "تطوير برمجيات متقدمة",
    about_pretitle: "البرمجيات الممتازة تتطلب هيكلية واضحة",
    about_title: 'الكود عالي الجودة هو أكثر من مجرد صيغة، إنه يؤتمت العمليات و<span class="text-slate-400 dark:text-gray-500">يدمج الذكاء الاصطناعي...</span>',
    about_desc: "بصفتي مطور برمجيات، أقوم بتحويل المشاكل المعقدة إلى حلول أنيقة. شغفي يكمن في خلق قيمة حقيقية من خلال الكود النظيف والتقنيات المبتكرة.",
    work_title: "أعمالي", 
    project_ufo_desc: "لعبة ويب تفاعلية برسومات متحركة سلسة ومنطق جافا سكريبت معقد.",
    btn_view_project: 'عرض المشروع <span class="group-hover:-translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    project_mo_desc: "عرض معماري لتصميم واجهة وتجربة المستخدم وأتمتة خلفية قوية.",
    project_hw_title: "أتمتة الأجهزة (HW)", 
    project_hw_desc: "أداة تشخيص النظام باستخدام Jenkins-CI/CD. اختبار آلي وتقارير مجدولة للعملاء.",
    btn_view_doc: 'قراءة التوثيق <span class="group-hover:-translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    project_git_desc: "مستودعي العام. اكتشف هياكل الأكواد النظيفة والمزيد من المشاريع.",
    btn_view_github: 'زيارة جيت هاب <span class="group-hover:-translate-x-2 transition-transform rtl:rotate-180 inline-block">➔</span>',
    exp_title: "الخبرة", 
    exp_focus: "التركيز الحالي", 
    exp_job1_title: "مطور برمجيات",
    exp_task1_1: "▹ تصميم وتنفيذ تطبيقات الويب باستخدام أدوات الذكاء الاصطناعي", 
    exp_task1_2: "▹ تطوير مشاريع برمجية قابلة للتوسع", 
    exp_task1_3: "▹ تطوير سكربتات بايثون لأتمتة عمليات البيانات",
    exp_job2_title: "تدريب مهني كمتخصص تقنية معلومات لتطوير التطبيقات",
    exp_task2_1: "▹ أتمتة العمليات وتحليل البيانات",
    exp_task2_2: "▹ تطوير الويب",
    exp_task2_3: "▹ إدارة المشاريع باستخدام Git",
    tech_langs: "لغات البرمجة", tech_tools: "الأدوات", tech_frameworks: "أطر العمل",
    contact_title: "لنتحدث.", contact_email: "البريد الإلكتروني", contact_github: "عرض الأكواد ↗",
    footer_rights: "© 2026 محمود. جميع الحقوق محفوظة.", footer_impressum: "بيانات النشر", footer_privacy: "سياسة الخصوصية",
    impressum_text: "محمود<br>مطور برمجيات<br>ريغنسبورغ، ألمانيا<br><br>للتواصل: Benachrichtigung.Mahmoud@hotmail.com<br>هاتف: +49 1525 2690273",
    privacy_text: "<p>نحن نأخذ حماية بياناتك على محمل الجد. لا يتم استخدام أي ملفات تعريف ارتباط (Cookies) للتتبع على هذا الموقع.</p>"
  }
};

function changeLanguage(lang) {
  document.documentElement.lang = lang;
  if (lang === 'ar') { 
      document.documentElement.setAttribute('dir', 'rtl'); 
  } else { 
      document.documentElement.setAttribute('dir', 'ltr'); 
  }

  // تحديث ألوان أزرار اللغة العادية
  document.querySelectorAll('[id^="btn-"]:not([id$="-mob"])').forEach(btn => btn.classList.remove('text-gold', 'dark:text-gold', 'font-bold'));
  if(document.getElementById('btn-' + lang)) document.getElementById('btn-' + lang).classList.add('text-gold', 'dark:text-gold', 'font-bold');

  // تحديث ألوان أزرار اللغة في الهاتف
  document.querySelectorAll('[id$="-mob"]').forEach(btn => btn.classList.remove('text-gold', 'dark:text-gold', 'font-bold'));
  if(document.getElementById('btn-' + lang + '-mob')) document.getElementById('btn-' + lang + '-mob').classList.add('text-gold', 'dark:text-gold', 'font-bold');

  const elements = document.querySelectorAll('[data-i18n]');
  elements.forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (translations[lang] && translations[lang][key]) { 
        el.innerHTML = translations[lang][key]; 
    }
  });
}

window.onload = () => { changeLanguage('de'); };
