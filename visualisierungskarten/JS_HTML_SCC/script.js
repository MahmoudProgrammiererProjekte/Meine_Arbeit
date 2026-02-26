document.addEventListener("DOMContentLoaded", () => {
    "use strict";

    // --- 1. إدارة التحية الديناميكية ---
    const initGreeting = () => {
        const container = document.getElementById("greeting-container");
        if (!container) return;

        const hours = new Date().getHours();
        let greetingText = "";

        if (hours < 12) {
            greetingText = "Guten Morgen";
        } else if (hours < 18) {
            greetingText = "Guten Tag";
        } else {
            greetingText = "Guten Abend";
        }

        container.innerHTML = `${greetingText}, ich bin <br>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">Mahmoud</span>`;
    };

    // --- 2. إدارة الوضع الليلي (Dark Mode) ---
    const initThemeToggle = () => {
        const toggleBtn = document.getElementById("dark-mode-toggle");
        const themeIcon = document.getElementById("theme-icon");
        const html = document.documentElement;
        
        // الأيقونات بصيغة SVG
        const sunIcon = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>';
        const moonIcon = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>';

        const applyTheme = (theme) => {
            if (theme === "dark") {
                html.classList.add("dark");
                themeIcon.innerHTML = sunIcon;
                localStorage.setItem("theme", "dark");
            } else {
                html.classList.remove("dark");
                themeIcon.innerHTML = moonIcon;
                localStorage.setItem("theme", "light");
            }
        };

        // التحقق من الإعدادات المحفوظة أو إعدادات النظام
        const savedTheme = localStorage.getItem("theme");
        const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        
        if (savedTheme === "dark" || (!savedTheme && systemPrefersDark)) {
            applyTheme("dark");
        } else {
            applyTheme("light");
        }

        // حدث الضغط على الزر
        toggleBtn?.addEventListener("click", () => {
            const isDark = html.classList.contains("dark");
            applyTheme(isDark ? "light" : "dark");
            
            // تأثير حركي للزر
            toggleBtn.style.transform = "rotate(15deg) scale(0.9)";
            setTimeout(() => toggleBtn.style.transform = "rotate(0deg) scale(1)", 150);
        });
    };

    // --- 3. الأنيميشن عند السكرول (Intersection Observer) ---
    const initScrollAnimations = () => {
        const elements = document.querySelectorAll(".animate-on-scroll");
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    // إيقاف المراقبة بعد الظهور الأول لتحسين الأداء
                    observer.unobserve(entry.target); 
                }
            });
        }, { threshold: 0.15, rootMargin: "0px 0px -50px 0px" });

        elements.forEach(el => observer.observe(el));
    };

    // --- 4. تفاعل المهارات ومحاكاة الأتمتة ---
    const initSkillInteractions = () => {
        const skills = document.querySelectorAll(".skill-tag");
        
        skills.forEach(skill => {
            skill.addEventListener("click", function() {
                // محاكاة تسجيل حدث (Analytics/AI Automation)
                console.log(`[System]: User interested in skill -> ${this.innerText}`);
                
                // تأثير بصري للضغطة
                this.classList.toggle("ring-2");
                this.classList.toggle("ring-primary");
                this.classList.toggle("ring-offset-2");
                if(document.documentElement.classList.contains('dark')) {
                    this.classList.toggle("ring-offset-gray-900");
                }
            });
        });
        
        // رسالة ترحيبية في الكونسول للمطورين (Easter Egg)
        console.log("%c Mahmoud AI Portfolio Engine Ready! ", "background: #8b5cf6; color: white; font-weight: bold; border-radius: 4px; padding: 4px;");
    };

    // تشغيل جميع الوظائف
    initGreeting();
    initThemeToggle();
    initScrollAnimations();
    initSkillInteractions();
});
